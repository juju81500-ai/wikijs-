#!/usr/bin/env python3
"""Build and validate a Wiki.js 2.x Git-storage import tree."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRECTORIES = (
    "00-Administration",
    "01-Fiches-Simples",
    "02-Fiches-Completes",
    "03-Templates-Machines",
    "04-Questions-Reponses",
    "05-Hardening-AIS-Cyber",
    "06-Documentation-ext",
)
CATEGORY_TITLES = {
    "00-Administration": "Administration",
    "01-Fiches-Simples": "Fiches simples",
    "02-Fiches-Completes": "Fiches completes",
    "03-Templates-Machines": "Templates machines",
    "04-Questions-Reponses": "Questions et reponses",
    "05-Hardening-AIS-Cyber": "Hardening AIS Cyber",
    "06-Documentation-ext": "Documentation externe",
}
TAG_LINE = re.compile(r"(?im)^\s*[-*]?\s*\*\*Tags\*\*\s*:\s*(.*?)\s*$")
HEADING = re.compile(r"^#\s+(.+?)\s*#*\s*$")
FRONT_MATTER = re.compile(r"\A---\r?\n.*?\r?\n---(?:\r?\n|\Z)", re.DOTALL)
ROUTE_SEGMENT = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")


@dataclass(frozen=True)
class Page:
    route: str
    title: str
    description: str
    tags: tuple[str, ...]
    content: str
    source: str
    timestamp: str


def slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value)).strip("-") or "page"


def is_markdown(path: Path, text: str) -> bool:
    if path.name.lower().endswith(".md"):
        return True
    if path.name.startswith("."):
        return False
    sample = "\n".join(text.splitlines()[:60])
    return bool(re.search(r"(?m)^#\s+\S", sample) or TAG_LINE.search(sample))


def tags_from(text: str) -> tuple[str, ...]:
    match = TAG_LINE.search(text)
    if not match:
        return ()
    raw_tags = match.group(1)
    values = re.findall(r"`([^`]+)`", raw_tags)
    if not values:
        values = [part.strip() for part in raw_tags.split(",") if part.strip()]
    return tuple(dict.fromkeys(value.strip() for value in values if value.strip()))


def title_from(path: Path, text: str) -> str:
    for line in text.splitlines()[:60]:
        match = HEADING.match(line.strip())
        if match:
            title = match.group(1).replace("📄", "").strip()
            title = re.sub(r"(?i)\.md$", "", title)
            if re.match(r"(?i)^fiche(?:_|\s)", title):
                title = title.replace("_", " ")
            return re.sub(r"\s+", " ", title).strip() or path.stem
    return re.sub(r"\s+", " ", path.stem.replace("_", " ")).strip()


def description_from(text: str) -> str:
    for line in text.splitlines()[:80]:
        candidate = line.strip()
        if not candidate or candidate.startswith(("#", "- **", "---", "```", ">", "|")):
            continue
        candidate = re.sub(r"[*_`]+", "", candidate)
        return candidate[:300]
    return ""


def rewrite_markdown_links(content: str, source: Path, routes: dict[Path, str]) -> tuple[str, int]:
    rewritten = 0
    in_code = False
    output_lines = []
    for line in content.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            in_code = not in_code
            output_lines.append(line)
            continue
        if in_code:
            output_lines.append(line)
            continue

        def replace_link(match: re.Match[str]) -> str:
            nonlocal rewritten
            target_text = match.group(2).strip()
            if target_text.startswith("<") and ">" in target_text:
                target = target_text[1 : target_text.index(">")]
                suffix = target_text[target_text.index(">") + 1 :]
                use_angle_brackets = True
            else:
                pieces = target_text.split(maxsplit=1)
                target = pieces[0]
                suffix = f" {pieces[1]}" if len(pieces) > 1 else ""
                use_angle_brackets = False

            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith("/") or not parsed.path:
                return match.group(0)

            candidate = (source.parent / unquote(parsed.path)).resolve()
            variants = [candidate]
            if candidate.suffix.lower() == ".md":
                variants.append(candidate.with_suffix(""))
            else:
                variants.append(Path(f"{candidate}.md"))
            route = next((routes[item] for item in variants if item in routes), None)
            if route is None:
                return match.group(0)

            rewritten += 1
            destination = urlunsplit(("", "", f"/{route}", parsed.query, parsed.fragment))
            if use_angle_brackets:
                destination = f"<{destination}>"
            return f"[{match.group(1)}]({destination}{suffix})"

        output_lines.append(MARKDOWN_LINK.sub(replace_link, line))
    return "\n".join(output_lines), rewritten


def rewrite_internal_links(pages: list[Page]) -> tuple[list[Page], int]:
    routes = {
        (ROOT / page.source).resolve(): page.route
        for page in pages
        if not page.source.startswith("[")
    }
    result = []
    total_rewritten = 0
    for page in pages:
        if page.source.startswith("["):
            result.append(page)
            continue
        content, rewritten = rewrite_markdown_links(page.content, ROOT / page.source, routes)
        result.append(replace(page, content=content))
        total_rewritten += rewritten
    return result, total_rewritten


def source_pages() -> tuple[list[Page], list[str]]:
    pages: list[Page] = []
    skipped: list[str] = []
    for directory in SOURCE_DIRECTORIES:
        source_root = ROOT / directory
        if not source_root.is_dir():
            raise FileNotFoundError(f"Dossier source absent : {source_root}")

        for path in sorted(source_root.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(source_root)
            if ".git" in relative.parts or any(part.startswith(".") for part in relative.parts):
                skipped.append(str(path.relative_to(ROOT)))
                continue
            if path.name.lower() in {"_sidebar.md", "_navbar.md"}:
                skipped.append(str(path.relative_to(ROOT)))
                continue

            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                raise ValueError(f"Fichier illisible : {path.relative_to(ROOT)} ({error})") from error
            if not is_markdown(path, text):
                skipped.append(str(path.relative_to(ROOT)))
                continue
            if FRONT_MATTER.match(text):
                raise ValueError(
                    f"Front matter deja present dans {path.relative_to(ROOT)}; "
                    "conversion interrompue pour eviter un double en-tete."
                )

            stem = path.name[:-3] if path.name.lower().endswith(".md") else path.name
            route_parts = [slug(directory)] + [slug(part) for part in relative.parts[:-1]] + [slug(stem)]
            route = "/".join(route_parts)
            pages.append(
                Page(
                    route=route,
                    title=title_from(path, text),
                    description=description_from(text),
                    tags=tags_from(text),
                    content=text.rstrip() + "\n",
                    source=str(path.relative_to(ROOT)),
                    timestamp=datetime.fromtimestamp(
                        path.stat().st_mtime, timezone.utc
                    ).isoformat(timespec="seconds").replace("+00:00", "Z"),
                )
            )
    return pages, skipped


def metadata(title: str, description: str, tags: tuple[str, ...], timestamp: str) -> str:
    return (
        "---\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"description: {json.dumps(description, ensure_ascii=False)}\n"
        "published: true\n"
        f"date: {timestamp}\n"
        f"tags: {json.dumps(list(tags), ensure_ascii=False)}\n"
        "editor: markdown\n"
        f"dateCreated: {timestamp}\n"
        f"dateModified: {timestamp}\n"
        "---\n\n"
    )


def generated_pages(pages: list[Page]) -> list[Page]:
    timestamp = max(
        (page.timestamp for page in pages),
        default=datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    )
    result = list(pages)
    category_links = []
    for directory, title in CATEGORY_TITLES.items():
        category_route = slug(directory)
        category_links.append(f"- [{title}](/{category_route}/00-index)")
        result.append(
            Page(
                route=f"{category_route}/00-index",
                title=title,
                description=f"Index des pages : {title}.",
                tags=("tssr", "index"),
                content=f"# {title}\n\nPages et sous-dossiers de cette rubrique.\n",
                source="[index genere]",
                timestamp=timestamp,
            )
        )

    result.append(
        Page(
            route="readme",
            title="Wiki TSSR AIS Cyber",
            description="Documentation technique TSSR, AIS et cyber.",
            tags=("tssr", "ais", "cyber"),
            content="# Wiki TSSR AIS Cyber\n\n" + "\n".join(category_links) + "\n",
            source="[accueil genere]",
            timestamp=timestamp,
        )
    )
    return result


def validate_pages(pages: list[Page]) -> list[str]:
    errors: list[str] = []
    routes: dict[str, str] = {}
    for page in pages:
        if page.route in routes:
            errors.append(f"Route en doublon : {page.route} ({routes[page.route]} et {page.source})")
        else:
            routes[page.route] = page.source
        if not all(ROUTE_SEGMENT.fullmatch(part) for part in page.route.split("/")):
            errors.append(f"Route invalide : {page.route} ({page.source})")
        if not page.title.strip():
            errors.append(f"Titre absent : {page.source}")
    return errors


def output_path_for(output: Path, route: str) -> Path:
    return output.joinpath(*route.split("/")).with_suffix(".md")


def remove_stale_markdown(output: Path, pages: list[Page]) -> None:
    expected = {output_path_for(output, page.route) for page in pages}
    for path in output.rglob("*.md"):
        if path not in expected:
            path.unlink()


def write_tree(output: Path, pages: list[Page], refresh: bool) -> None:
    if output.exists() and any(output.iterdir()) and not refresh:
        raise FileExistsError(f"La sortie existe et n'est pas vide : {output}")
    output.mkdir(parents=True, exist_ok=True)
    if refresh:
        remove_stale_markdown(output, pages)
    for page in pages:
        destination = output_path_for(output, page.route)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            metadata(page.title, page.description, page.tags, page.timestamp) + page.content,
            encoding="utf-8",
            newline="\n",
        )


def write_manual_tree(output: Path, pages: list[Page], refresh: bool) -> None:
    if output.exists() and any(output.iterdir()) and not refresh:
        raise FileExistsError(f"La sortie existe et n'est pas vide : {output}")
    output.mkdir(parents=True, exist_ok=True)
    if refresh:
        remove_stale_markdown(output, pages)
    for page in pages:
        destination = output_path_for(output, page.route)
        destination.parent.mkdir(parents=True, exist_ok=True)
        content = TAG_LINE.sub("", page.content, count=1)
        content = re.sub(r"\n{3,}", "\n\n", content).lstrip()
        destination.write_text(content, encoding="utf-8", newline="\n")

    manifest_path = output / "IMPORT-MANIFEST.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as manifest_file:
        writer = csv.writer(manifest_file)
        writer.writerow(("route", "titre", "tags"))
        for page in pages:
            writer.writerow((f"/{page.route}", page.title, ", ".join(page.tags)))


def validate_tree(output: Path) -> int:
    files = sorted(output.rglob("*.md")) if output.is_dir() else []
    errors: list[str] = []
    seen_routes: set[str] = set()
    required = ("title:", "description:", "published: true", "date:", "tags:", "editor: markdown", "dateCreated:", "dateModified:")
    for path in files:
        route = "/".join(path.relative_to(output).with_suffix("").parts)
        if route in seen_routes:
            errors.append(f"Route en doublon : {route}")
        seen_routes.add(route)
        if not all(ROUTE_SEGMENT.fullmatch(part) for part in route.split("/")):
            errors.append(f"Route invalide : {route}")
        text = path.read_text(encoding="utf-8")
        match = FRONT_MATTER.match(text)
        if not match:
            errors.append(f"Front matter absent ou non ferme : {path.relative_to(output)}")
            continue
        front_matter = match.group(0)
        for key in required:
            if not re.search(rf"(?m)^{re.escape(key)}", front_matter):
                errors.append(f"Metadonnee absente ({key}) : {path.relative_to(output)}")

    if errors:
        print(f"ERREURS : {len(errors)}")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK : {len(files)} pages Markdown, routes uniques et front matter complet.")
    return 0


def validate_manual_tree(output: Path) -> int:
    files = sorted(output.rglob("*.md")) if output.is_dir() else []
    manifest = output / "IMPORT-MANIFEST.csv"
    errors: list[str] = []
    routes: set[str] = set()
    for path in files:
        route = "/".join(path.relative_to(output).with_suffix("").parts)
        if route in routes:
            errors.append(f"Route en doublon : {route}")
        routes.add(route)
        if not all(ROUTE_SEGMENT.fullmatch(part) for part in route.split("/")):
            errors.append(f"Route invalide : {route}")
        if FRONT_MATTER.match(path.read_text(encoding="utf-8")):
            errors.append(f"Front matter a retirer avant collage : {path.relative_to(output)}")

    if not manifest.is_file():
        errors.append("Manifeste absent : IMPORT-MANIFEST.csv")
    else:
        try:
            with manifest.open(encoding="utf-8", newline="") as manifest_file:
                rows = list(csv.DictReader(manifest_file))
            if len(rows) != len(files):
                errors.append(f"Manifeste : {len(rows)} lignes pour {len(files)} pages.")
            if any(not row.get("route") or not row.get("titre") for row in rows):
                errors.append("Manifeste : route ou titre absent.")
        except (OSError, UnicodeError, csv.Error) as error:
            errors.append(f"Manifeste illisible : {error}")

    if errors:
        print(f"ERREURS : {len(errors)}")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK : {len(files)} fichiers Markdown sans front matter et manifeste complet.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="dossier de sortie (defaut selon le mode choisi)",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="simuler la conversion sans ecrire")
    mode.add_argument("--check", action="store_true", help="valider un arbre d'import deja genere")
    parser.add_argument(
        "--manual",
        action="store_true",
        help="generer des pages Markdown sans front matter pour le copier-coller dans l'editeur",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="actualiser les pages generees dans un dossier de sortie existant",
    )
    args = parser.parse_args()
    default_output = "export/WikiJS-Copier-Coller" if args.manual else "export/WikiJS-Import-v2"
    output = (args.output or ROOT / default_output).resolve()

    if args.check:
        return validate_manual_tree(output) if args.manual else validate_tree(output)
    for directory in SOURCE_DIRECTORIES:
        source = (ROOT / directory).resolve()
        if output == source or source in output.parents:
            print("ERREUR : le dossier de sortie ne peut pas etre place dans une source.")
            return 1

    try:
        source, skipped = source_pages()
        source, links_rewritten = rewrite_internal_links(source)
        pages = generated_pages(source)
    except (OSError, ValueError) as error:
        print(f"ERREUR : {error}")
        return 1

    errors = validate_pages(pages)
    if errors:
        print(f"ERREURS de routes : {len(errors)}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Pages source : {len(source)}; index et accueil : {len(pages) - len(source)}")
    print(f"Fichiers ignores (dépôts Git, scripts, exports non Markdown) : {len(skipped)}")
    print(f"Liens locaux convertis vers Wiki.js : {links_rewritten}")
    if args.dry_run:
        mode_label = "copier-coller" if args.manual else "import avec front matter"
        print(f"Simulation OK ({mode_label}) : aucune modification ecrite.")
        return 0

    try:
        if args.manual:
            write_manual_tree(output, pages, args.refresh)
        else:
            write_tree(output, pages, args.refresh)
    except (OSError, FileExistsError) as error:
        print(f"ERREUR de sortie : {error}")
        return 1
    print(f"Arbre Wiki.js genere : {output}")
    return validate_manual_tree(output) if args.manual else validate_tree(output)


if __name__ == "__main__":
    sys.exit(main())