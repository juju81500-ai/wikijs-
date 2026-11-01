#!/usr/bin/env python3
"""Genere le referentiel des sites TSSR (titres, categories et liens uniquement).

Sources publiques : sitemaps (robots.txt autorise), balise <title> des pages,
arborescence GitHub. Aucun contenu pedagogique n'est copie ni stocke.
Bibliotheque standard seulement. Usage :
    python3 tools/referentiel/build_referentiel.py [--cache FICHIER] [--no-fetch]
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import OrderedDict, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

UA = "pack-master-referentiel/1.0 (titres publics, debit limite)"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "01-Fiches-Simples" / "Transverses" / "Tout-en-un" / "00-Referentiel-Sites"
DATE = time.strftime("%Y-%m-%d")

SR = "https://www.stephane-robert.info"
JS = "https://www.jousseaume.online"
GH_REPO = "kipit/nivvlem-TSSR"

_lock = threading.Lock()
_last = [0.0]
MIN_INTERVAL = 0.15  # secondes entre deux requetes (tous threads confondus)


def http_get(url: str, timeout: float = 25.0, retries: int = 2) -> str | None:
    for attempt in range(retries + 1):
        with _lock:
            wait = _last[0] + MIN_INTERVAL - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            _last[0] = time.monotonic()
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read(400_000).decode("utf-8", "replace")
        except urllib.error.HTTPError as err:
            if err.code in (404, 410, 403):
                return None
        except (urllib.error.URLError, TimeoutError, OSError):
            pass
        time.sleep(1.5 * (attempt + 1))
    return None


def sitemap_urls(url: str) -> list[str]:
    text = http_get(url) or ""
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", text)


def clean_title(raw: str, site_suffixes: tuple[str, ...]) -> str:
    title = html.unescape(re.sub(r"\s+", " ", raw)).strip()
    for suffix in site_suffixes:
        if title.endswith(suffix):
            title = title[: -len(suffix)].strip(" -|—–")
    return title.replace("|", "/")


def page_title(url: str, suffixes: tuple[str, ...]) -> str | None:
    text = http_get(url)
    if not text:
        return None
    match = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
    if not match:
        return None
    title = clean_title(match.group(1), suffixes)
    if not title or re.match(r"^\d{3} ", title):
        return None
    return title


def slug_title(slug: str) -> str:
    words = slug.strip("/").split("/")[-1].replace("_", "-").split("-")
    text = " ".join(w for w in words if w)
    return text[:1].upper() + text[1:] if text else slug


def load_cache(path: Path) -> dict:
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_cache(path: Path, cache: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")


def fetch_titles(urls: list[str], cache: dict, cache_path: Path, suffixes, workers: int, fetch: bool) -> None:
    todo = [u for u in urls if u not in cache]
    if not fetch or not todo:
        return
    done = [0]

    def work(url: str) -> None:
        title = page_title(url, suffixes)
        with _lock:
            cache[url] = title or ""
            done[0] += 1
            if done[0] % 100 == 0:
                print(f"  titres recuperes : {done[0]}/{len(todo)}", flush=True)
                save_cache(cache_path, cache)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(work, todo))
    save_cache(cache_path, cache)


def title_for(url: str, cache: dict) -> str:
    cached = cache.get(url)
    if cached:
        return cached
    return slug_title(urllib.parse.urlsplit(url).path)


# --- Rendu -------------------------------------------------------------------

def md_head(title: str, tags: list[str], intro: str) -> list[str]:
    tag_text = ", ".join(f"`{t}`" for t in tags)
    return [f"# {title}", "", f"- **Tags** : {tag_text}", "", intro, ""]


def write(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def link(title: str, url: str) -> str:
    return f"[{title}]({url})"


LEGAL = (
    "Ce référentiel ne reproduit **aucun contenu pédagogique** : il liste uniquement les titres publics, "
    "les catégories et les liens, à des fins de navigation. Les droits sur les cours restent à leurs auteurs ; "
    "pour les lire, utiliser le lien vers le site d'origine. Les titres sont relevés le " + DATE + " ; "
    "ils peuvent évoluer côté éditeur."
)


def sr_urls() -> list[str]:
    urls = sitemap_urls(f"{SR}/sitemap-content.xml")
    return [u for u in urls if "/en/" not in u and "/pagefind/" not in u and "/api/" not in u]


def render_stephane_robert(urls: list[str], cache: dict) -> dict:
    base = OUT / "Stephane-Robert"
    docs: dict[str, list[str]] = defaultdict(list)
    competences, articles, parcours = [], [], []
    for url in urls:
        parts = [p for p in urllib.parse.urlsplit(url).path.split("/") if p]
        if not parts:
            continue
        head = parts[0]
        if head == "docs" and len(parts) >= 2:
            docs[parts[1]].append(url)
        elif head == "competences" and len(parts) >= 2:
            competences.append(url)
        elif head == "post" and len(parts) >= 2 and parts[1] != "page":
            articles.append(url)
        elif head in {"metiers", "labs", "certifications", "formations", "examens", "outils", "glossaire"}:
            parcours.append(url)
    counts: dict[str, int] = OrderedDict()

    small = {cat: items for cat, items in docs.items() if len(items) < 3}
    for cat, items in sorted(docs.items()):
        if cat in small:
            continue
        title_cat = title_for(f"{SR}/docs/{cat}/", cache)
        lines = md_head(
            f"Référentiel — Stéphane Robert : {cat}",
            ["transverse", "tout-en-un", "referentiel", "stephane-robert", cat],
            f"Catégorie **{cat}** du site stephane-robert.info ({len(items)} pages). "
            f"Page d'entrée : {link(title_cat, f'{SR}/docs/{cat}/')}.\n\n" + LEGAL,
        )
        by_sub: dict[str, list[str]] = OrderedDict()
        for url in sorted(items):
            parts = [p for p in urllib.parse.urlsplit(url).path.split("/") if p]
            if len(parts) == 2:
                continue
            by_sub.setdefault(parts[2], []).append(url)
        for sub, sub_urls in by_sub.items():
            sub_url = f"{SR}/docs/{cat}/{sub}/"
            heading = title_for(sub_url, cache) if sub_url in sub_urls else slug_title(sub)
            lines += [f"## {heading}", ""]
            for url in sub_urls:
                depth = len([p for p in urllib.parse.urlsplit(url).path.split("/") if p]) - 3
                if sub_url not in sub_urls:
                    depth -= 1
                lines.append(f"{'  ' * max(depth, 0)}- {link(title_for(url, cache), url)}")
            lines.append("")
        write(base / f"Docs_{cat}.md", lines)
        counts[f"docs/{cat}"] = len(items)

    if small:
        lines = md_head(
            "Référentiel — Stéphane Robert : pages de documentation diverses",
            ["transverse", "tout-en-un", "referentiel", "stephane-robert"],
            "Petites catégories et pages isolées de la section `/docs/`.\n\n" + LEGAL,
        )
        for cat, items in sorted(small.items()):
            lines += [f"## {slug_title(cat)}", ""]
            lines += [f"- {link(title_for(u, cache), u)}" for u in sorted(items)]
            lines.append("")
        write(base / "Docs_Pages_Diverses.md", lines)
        counts["docs/divers"] = sum(len(i) for i in small.values())

    groups: dict[str, list[str]] = OrderedDict()
    for url in sorted(competences):
        slug = urllib.parse.urlsplit(url).path.strip("/").split("/")[1]
        groups.setdefault(slug.split("-")[0], []).append(url)
    lines = md_head(
        "Référentiel — Stéphane Robert : parcours par compétences",
        ["transverse", "tout-en-un", "referentiel", "stephane-robert", "competences"],
        f"{len(competences)} fiches de compétences regroupées par préfixe de thème.\n\n" + LEGAL,
    )
    for prefix, items in groups.items():
        lines += [f"## Thème « {prefix} » ({len(items)})", ""]
        lines += [f"- {link(title_for(u, cache), u)}" for u in items]
        lines.append("")
    write(base / "Competences.md", lines)
    counts["competences"] = len(competences)

    lines = md_head(
        "Référentiel — Stéphane Robert : métiers, labs, certifications et outils",
        ["transverse", "tout-en-un", "referentiel", "stephane-robert", "certifications"],
        "Parcours métiers, labs, certifications, formations, examens, outils et glossaire.\n\n" + LEGAL,
    )
    sections: dict[str, list[str]] = OrderedDict()
    for url in sorted(parcours):
        sections.setdefault(urllib.parse.urlsplit(url).path.strip("/").split("/")[0], []).append(url)
    for name, items in sections.items():
        lines += [f"## {slug_title(name)}", ""]
        lines += [f"- {link(title_for(u, cache), u)}" for u in items]
        lines.append("")
    write(base / "Metiers_Labs_Certifications.md", lines)
    counts["parcours"] = len(parcours)

    lines = md_head(
        "Référentiel — Stéphane Robert : articles de blog",
        ["transverse", "tout-en-un", "referentiel", "stephane-robert", "veille"],
        f"{len(articles)} articles (actualité, veille, retours d'expérience).\n\n" + LEGAL,
    )
    lines += [f"- {link(title_for(u, cache), u)}" for u in sorted(articles)]
    write(base / "Articles_Blog.md", lines)
    counts["articles"] = len(articles)

    index = md_head(
        "Référentiel — Stéphane Robert",
        ["transverse", "tout-en-un", "referentiel", "stephane-robert"],
        f"Site : {SR}/. Cartographie des catégories de formation, compétences, labs et articles "
        "(versions anglaises `/en/` non listées : doublons des pages françaises).\n\n" + LEGAL,
    )
    index += ["| Page du référentiel | Pages listées |", "|---|---|"]
    for name in sorted(base.glob("*.md")):
        if name.name == "README.md":
            continue
        n = sum(1 for line in name.read_text(encoding="utf-8").splitlines() if line.lstrip().startswith("- ["))
        index.append(f"| [{name.stem.replace('_', ' ')}]({name.name}) | {n} |")
    write(base / "README.md", index)
    return counts


def build_jousseaume(cache: dict, fetch: bool, workers: int, cache_path: Path) -> dict:
    urls = sitemap_urls(f"{JS}/sitemap.xml")
    suffixes = (" | Root & Code", " - Root & Code", " | Root _&_ Code", " | Root &amp; Code")
    fetch_titles(urls, cache, cache_path, suffixes, workers, fetch)
    categories = [u for u in urls if "/categorie/" in u and u.rstrip("/").count("/") >= 4]
    course_category: dict[str, str] = {}
    for cat_url in categories:
        text = http_get(cat_url) if fetch else None
        if not text:
            continue
        for match in re.findall(r'href="(?:https://www\.jousseaume\.online)?(/cours/[^"#?]+)"', text):
            course_category.setdefault((JS + match).rstrip("/"), cat_url)
    courses = sorted(u for u in urls if "/cours/" in u)
    others = [u for u in urls if "/cours/" not in u and "/categorie/" not in u]
    lines = md_head(
        "Référentiel — Root & Code (jousseaume.online)",
        ["transverse", "tout-en-un", "referentiel", "jousseaume", "bts-sio"],
        f"Site : {JS}/ — tutoriels, TP et QCM. {len(courses)} cours en {len(categories)} catégories.\n\n" + LEGAL,
    )
    by_cat: dict[str, list[str]] = defaultdict(list)
    for course in courses:
        by_cat[course_category.get(course.rstrip("/"), "autre")].append(course)
    for cat_url in sorted(categories):
        items = by_cat.get(cat_url, [])
        lines += [f"## {link(title_for(cat_url, cache), cat_url)} ({len(items)})", ""]
        lines += [f"- {link(title_for(u, cache), u)}" for u in items]
        lines.append("")
    if by_cat.get("autre"):
        lines += [f"## Cours non rattachés à une catégorie ({len(by_cat['autre'])})", ""]
        lines += [f"- {link(title_for(u, cache), u)}" for u in by_cat["autre"]]
        lines.append("")
    if others:
        lines += ["## Autres pages", ""]
        lines += [f"- {link(title_for(u, cache), u)}" for u in others]
    write(OUT / "Jousseaume" / "Referentiel_Root_and_Code.md", lines)
    return {"cours": len(courses), "categories": len(categories)}


def build_nivvlem(cache: dict, fetch: bool, workers: int, cache_path: Path) -> dict:
    text = http_get(f"https://api.github.com/repos/{GH_REPO}/git/trees/main?recursive=1")
    tree = json.loads(text)["tree"] if text else []
    paths = sorted(item["path"] for item in tree if item["path"].endswith(".md") and not item["path"].startswith("_"))
    raw = {p: "https://raw.githubusercontent.com/%s/main/%s" % (GH_REPO, urllib.parse.quote(p)) for p in paths}
    todo = [u for u in raw.values() if u not in cache]
    if fetch and todo:
        def work(url: str) -> None:
            body = http_get(url)
            heading = ""
            if body:
                match = re.search(r"(?m)^#\s+(.+)$", body)
                heading = re.sub(r"^[^\w(]+", "", match.group(1)).strip() if match else ""
            with _lock:
                cache[url] = heading

        with ThreadPoolExecutor(max_workers=workers) as pool:
            list(pool.map(work, todo))
        save_cache(cache_path, cache)
    modules: dict[str, list[str]] = OrderedDict()
    for path in paths:
        top = path.split("/")[0]
        if top in {"README.md", "modules.md"}:
            continue
        modules.setdefault(top, []).append(path)
    lines = md_head(
        "Référentiel — nivvlem-TSSR (GitHub)",
        ["transverse", "tout-en-un", "referentiel", "nivvlem", "tssr"],
        f"Dépôt : https://github.com/{GH_REPO} — notes de cours et fiches de référence TSSR "
        f"({sum(len(v) for v in modules.values())} documents Markdown). Le dépôt ne déclare pas de licence : "
        "seuls les titres et liens sont repris, aucun texte n'est recopié.\n\n" + LEGAL,
    )
    for module, files in modules.items():
        lines += [f"## {slug_title(module)}", ""]
        for path in files:
            url = f"https://github.com/{GH_REPO}/blob/main/" + urllib.parse.quote(path)
            heading = cache.get(raw[path]) or slug_title(Path(path).stem)
            if path.endswith("/README.md"):
                lines.append(f"- **{link(heading + ' (sommaire du module)', url)}**")
            else:
                lines.append(f"- {link(heading, url)}")
        lines.append("")
    write(OUT / "Nivvlem" / "Referentiel_nivvlem-TSSR.md", lines)
    return {"modules": len(modules), "documents": sum(len(v) for v in modules.values())}


def build_index(stats: dict) -> None:
    lines = md_head(
        "Référentiel des sites TSSR — cours et catégories",
        ["transverse", "tout-en-un", "referentiel", "tssr"],
        "Carte des quatre sources publiques suivies par le pack : catégories, cours et liens vers les sites d'origine.\n\n" + LEGAL,
    )
    lines += [
        "| Source | Pages du référentiel | Volume relevé |",
        "|---|---|---|",
        f"| Stéphane Robert — documentation, compétences, labs, articles | [Index](Stephane-Robert/README.md) | {sum(stats['sr'].values())} pages |",
        f"| Root & Code (jousseaume.online) | [Référentiel](Jousseaume/Referentiel_Root_and_Code.md) | {stats['js']['cours']} cours, {stats['js']['categories']} catégories |",
        f"| nivvlem-TSSR (GitHub) | [Référentiel](Nivvlem/Referentiel_nivvlem-TSSR.md) | {stats['nv']['modules']} modules, {stats['nv']['documents']} documents |",
        "| ZenTSSR | [Référentiel](ZenTSSR/Referentiel_ZenTSSR.md) | voir la page |",
        "",
        "## Comment s'en servir",
        "",
        "1. Choisir la catégorie dans l'index de la source.",
        "2. Ouvrir le cours sur le site d'origine, pour lire son contenu à jour.",
        "3. Suivre les leçons originales du pack dans les huit catégories « tout-en-un » pour une version illustrée et structurée.",
        "",
        "## Régénérer le référentiel",
        "",
        "```bash",
        "python3 tools/referentiel/build_referentiel.py --cache /tmp/referentiel-cache.json",
        "```",
        "👉 Explication : relit les sitemaps publics à débit limité, récupère uniquement les titres de page et réécrit ces fichiers.",
    ]
    write(OUT / "README.md", lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path("/tmp/referentiel-cache.json"))
    parser.add_argument("--no-fetch", action="store_true", help="n'interroge pas les pages (titres issus du cache ou des URL)")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    cache = load_cache(args.cache)
    fetch = not args.no_fetch

    print("Stéphane Robert : lecture du sitemap", flush=True)
    urls = sr_urls()
    suffixes = (" | Stéphane Robert", " - Stéphane Robert", " | Stephane Robert")
    fetch_titles(urls, cache, args.cache, suffixes, args.workers, fetch)
    sr_counts = render_stephane_robert(urls, cache)
    print("Jousseaume", flush=True)
    js_counts = build_jousseaume(cache, fetch, args.workers, args.cache)
    print("nivvlem-TSSR", flush=True)
    nv_counts = build_nivvlem(cache, fetch, args.workers, args.cache)
    build_index({"sr": sr_counts, "js": js_counts, "nv": nv_counts})
    save_cache(args.cache, cache)
    print("Terminé :", sr_counts, js_counts, nv_counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
