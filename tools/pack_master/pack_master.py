#!/usr/bin/env python3
"""Pack Master : CLI tout-en-un (bibliotheque standard uniquement).

Sous-commandes : check, refresh, sources, all.
Les scripts de 00-Administration sont invoques tels quels (subprocess).
"""
from __future__ import annotations

import argparse
import json
import socket
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional, Sequence

HERE = Path(__file__).resolve().parent
DEFAULT_MANIFEST = HERE / "sources.json"
ADMIN = "00-Administration"
MARKER = Path(ADMIN) / "verify_wiki.py"
MAX_BYTES = 1_048_576
TIMEOUT = 10.0
USER_AGENT = "pack-master-sources-check/1.0"


def find_root(start: Optional[Path] = None) -> Path:
    """Remonte depuis `start` jusqu'a la racine du pack."""
    start = (start or HERE).resolve()
    for candidate in (start, *start.parents):
        if (candidate / MARKER).is_file():
            return candidate
    raise FileNotFoundError(f"racine du pack introuvable (absence de {MARKER})")


def run_script(root: Path, script: str, *args: str) -> int:
    cmd = [sys.executable, str(root / ADMIN / script), *args]
    print(f"$ {' '.join([Path(cmd[0]).name, script, *args])}", flush=True)
    return subprocess.run(cmd, cwd=root).returncode


def cmd_check(root: Path) -> int:
    steps = [
        ("verify_wiki.py", []),
        ("03-Qualite-Tests/check_links.py", []),
    ]
    return _run_steps(root, steps)


def cmd_refresh(root: Path) -> int:
    steps = [
        ("verify_wiki.py", []),
        ("prepare_wikijs_import.py", ["--refresh"]),
        ("prepare_wikijs_import.py", ["--manual", "--refresh"]),
        ("prepare_wikijs_import.py", ["--check"]),
        ("prepare_wikijs_import.py", ["--check", "--manual"]),
    ]
    return _run_steps(root, steps)


def _run_steps(root: Path, steps) -> int:
    for script, args in steps:
        code = run_script(root, script, *args)
        if code != 0:
            print(f"ECHEC ({code}) : {script} {' '.join(args)}", file=sys.stderr)
            return code
    return 0


# --- sources -----------------------------------------------------------------

class _HttpsOnlyRedirect(urllib.request.HTTPRedirectHandler):
    allow_http = False

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        scheme = urllib.parse.urlsplit(newurl).scheme
        if scheme != "https" and not (self.allow_http and scheme == "http"):
            raise urllib.error.URLError(f"redirection non HTTPS refusee : {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def load_manifest(path: Path) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("manifeste : liste 'sources' absente ou vide")
    seen = set()
    for item in sources:
        if not isinstance(item, dict) or not item.get("id") or not item.get("url"):
            raise ValueError("manifeste : chaque source exige 'id' et 'url'")
        if item["id"] in seen:
            raise ValueError(f"manifeste : id duplique {item['id']}")
        seen.add(item["id"])
        parts = urllib.parse.urlsplit(item["url"])
        if parts.scheme != "https" or not parts.hostname:
            raise ValueError(f"manifeste : URL HTTPS exigee ({item['id']})")
        if parts.username or parts.password or parts.query or parts.fragment:
            raise ValueError(f"manifeste : URL sans identifiants/parametres ({item['id']})")
    return sources


def probe_url(
    url: str,
    method: str = "HEAD",
    timeout: float = TIMEOUT,
    max_bytes: int = MAX_BYTES,
    allow_http: bool = False,
) -> dict:
    """Requete GET/HEAD unique ; le corps est lu par blocs, compte puis jete."""
    if method not in ("GET", "HEAD"):
        raise ValueError("methode limitee a GET/HEAD")
    result = {"url": url, "status": None, "final_url": None,
              "content_type": None, "length": None, "truncated": False, "error": None}
    scheme = urllib.parse.urlsplit(url).scheme
    if scheme != "https" and not (allow_http and scheme == "http"):
        result["error"] = "schema non HTTPS refuse"
        return result
    redirect = _HttpsOnlyRedirect()
    redirect.allow_http = allow_http
    # Contexte TLS par defaut : verification certificat + nom d'hote ; pas de cookies.
    opener = urllib.request.build_opener(redirect, urllib.request.HTTPSHandler())
    req = urllib.request.Request(
        url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with opener.open(req, timeout=timeout) as resp:
            _fill(result, resp, method, max_bytes)
    except urllib.error.HTTPError as err:
        _fill(result, err, method, max_bytes)
    except (urllib.error.URLError, socket.timeout, TimeoutError, OSError) as err:
        result["error"] = str(getattr(err, "reason", err))
    return result


def _fill(result: dict, resp, method: str, max_bytes: int) -> None:
    result["status"] = resp.status if hasattr(resp, "status") else resp.getcode()
    result["final_url"] = resp.geturl()
    result["content_type"] = resp.headers.get("Content-Type")
    declared = resp.headers.get("Content-Length")
    if method == "HEAD":
        result["length"] = int(declared) if declared and declared.isdigit() else None
        return
    total = 0
    while total <= max_bytes:
        chunk = resp.read(min(65536, max_bytes + 1 - total))
        if not chunk:
            break
        total += len(chunk)  # blocs jetes immediatement
    if total > max_bytes:
        result["truncated"] = True
        result["length"] = max_bytes
        if declared and declared.isdigit():
            result["length"] = int(declared)
    else:
        result["length"] = total


def cmd_sources(manifest: Path, test: bool, method: str, timeout: float,
                max_bytes: int, only: Optional[Sequence[str]] = None,
                allow_http: bool = False) -> int:
    try:
        sources = load_manifest(manifest)
    except (OSError, ValueError) as err:
        print(f"ERREUR manifeste : {err}", file=sys.stderr)
        return 2
    if only:
        sources = [s for s in sources if s["id"] in only]
        if not sources:
            print("ERREUR : aucune source ne correspond a --only", file=sys.stderr)
            return 2
    failures = 0
    for src in sources:
        label = f"{src['id']} ({src.get('name', '')})".strip()
        if not test:
            print(f"{label}: {src['url']}")
            continue
        r = probe_url(src["url"], method, timeout, max_bytes, allow_http)
        ok = r["error"] is None and r["status"] is not None and r["status"] < 400
        failures += 0 if ok else 1
        if r["error"]:
            print(f"[KO] {label}: {r['url']} erreur={r['error']}")
        else:
            trunc = "+" if r["truncated"] else ""
            print(f"[{'OK' if ok else 'KO'}] {label}: status={r['status']} "
                  f"final={r['final_url']} type={r['content_type']} "
                  f"longueur={r['length']}{trunc}")
    return 1 if failures else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="verifier les fiches et les liens du depot")
    sub.add_parser("refresh", help="generer les exports Wiki.js optionnels")

    def add_src(sp):
        sp.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
        sp.add_argument("--timeout", type=float, default=TIMEOUT)
        sp.add_argument("--max-bytes", type=int, default=MAX_BYTES)
        sp.add_argument("--method", choices=["HEAD", "GET"], default="HEAD")
        sp.add_argument("--only", action="append", help="id de source (repetable)")

    s = sub.add_parser("sources", help="lister (defaut) ou tester les URL publiques")
    add_src(s)
    s.add_argument("--test", action="store_true", help="requete HTTPS reseau")
    a = sub.add_parser("all", help="verifier le depot puis tester les sources publiques")
    add_src(a)
    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "sources":
        return cmd_sources(args.manifest, args.test, args.method,
                           args.timeout, args.max_bytes, args.only)
    try:
        root = find_root()
    except FileNotFoundError as err:
        print(f"ERREUR : {err}", file=sys.stderr)
        return 2
    if args.command == "check":
        return cmd_check(root)
    if args.command == "refresh":
        return cmd_refresh(root)
    code = cmd_check(root)
    if code != 0:
        return code
    return cmd_sources(args.manifest, True, args.method, args.timeout,
                       args.max_bytes, args.only)


if __name__ == "__main__":
    sys.exit(main())
