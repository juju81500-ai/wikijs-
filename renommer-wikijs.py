#!/usr/bin/env python3
"""Renomme fichiers et dossiers en slugs compatibles URL Wiki.js. Simulation par défaut ; --apply pour exécuter."""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAX_BYTES = 240
SKIP_DIRS = {".git"}
SKIP_FILES = {Path(__file__).name, "renommage-map.json"}


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c)).lower()
    text = re.sub(r"[_\s.]+", "-", text)
    text = re.sub(r"[^a-z0-9-]", "", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def new_name(name: str, is_dir: bool, parent_rel: str, budget_taken: set) -> str:
    stem, ext = (name, "") if is_dir else (Path(name).stem, Path(name).suffix)
    stem = slug(stem) or "sans-nom"
    ext = "." + slug(ext.lstrip(".")) if slug(ext.lstrip(".")) else ""
    prefix = len(parent_rel.encode()) + (1 if parent_rel else 0)
    limit = MAX_BYTES - prefix - len(ext.encode())
    # Marge de 4 octets pour un suffixe anti-collision "-NN"
    limit -= 4
    if len(stem.encode()) > limit:
        cut = stem.encode()[:limit].decode(errors="ignore")
        if "-" in cut:
            cut = cut.rsplit("-", 1)[0]
        stem = cut.strip("-") or stem[:limit]
    candidate, i = stem + ext, 2
    while candidate in budget_taken:
        candidate = f"{stem}-{i}{ext}"
        i += 1
    return candidate


def process(directory: Path, rel: str, apply: bool, log: dict) -> None:
    entries = sorted(p for p in directory.iterdir()
                     if not p.name.startswith(".")
                     and not (directory == ROOT and p.name in SKIP_FILES))
    # Noms déjà pris par les entrées qui ne changent pas
    taken = set()
    plan = []
    for p in entries:
        target = new_name(p.name, p.is_dir() and not p.is_symlink(), rel, taken)
        taken.add(target)
        plan.append((p, target))
    for p, target in plan:
        is_dir = p.is_dir() and not p.is_symlink()
        dest = p if target == p.name else p.with_name(target)
        if dest != p:
            if dest.exists() and dest.resolve() != p.resolve():
                print(f"CONFLIT, ignoré : {p} -> {dest}", file=sys.stderr)
                dest = p
            else:
                log[str(p.relative_to(ROOT))] = str(dest.relative_to(ROOT))
                print(f"{p.relative_to(ROOT)}  ->  {target}")
                if apply:
                    p.rename(dest)
        if is_dir:
            sub = dest if apply else p
            process(sub, (rel + "/" if rel else "") + dest.name, apply, log)


def main() -> None:
    apply = "--apply" in sys.argv
    log: dict = {}
    process(ROOT, "", apply, log)
    print(f"\n{len(log)} renommage(s) {'effectué(s)' if apply else 'prévu(s) (simulation, ajouter --apply)'}")
    if apply and log:
        (ROOT / "renommage-map.json").write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
