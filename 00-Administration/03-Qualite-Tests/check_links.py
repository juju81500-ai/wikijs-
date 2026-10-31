#!/usr/bin/env python3
"""Verifie les liens Markdown relatifs du pack (hors export/ et .git)."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
SKIP_DIRS = {".git", "export", "idee-incorporer-en-attente"}
IMPORTED_EXTERNAL = Path("06-Documentation-ext/05-Referentiel-GitHub/nivvlem-TSSR").parts
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|/|#)", re.IGNORECASE)


def markdown_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        parts = path.relative_to(root).parts
        if SKIP_DIRS.intersection(parts) or parts[: len(IMPORTED_EXTERNAL)] == IMPORTED_EXTERNAL:
            continue
        yield path


def broken_links(root: Path):
    for path in markdown_files(root):
        in_code = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith(("```", "~~~")):
                in_code = not in_code
                continue
            if in_code:
                continue
            for match in LINK.finditer(line):
                target = match.group(1).strip("<>")
                if EXTERNAL.match(target):
                    continue
                file_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
                if file_part and not (path.parent / file_part).exists():
                    yield path.relative_to(root), number, target


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
    broken = list(broken_links(root))
    checked = sum(1 for _ in markdown_files(root))
    print(f"Fichiers Markdown contrôlés : {checked}")
    for path, number, target in broken:
        print(f"- {path}:{number}: lien cassé -> {target}")
    print(f"Liens cassés : {len(broken)}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
