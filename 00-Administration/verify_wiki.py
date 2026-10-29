#!/usr/bin/env python3
"""Read-only structural checks for the Wiki.js TSSR documentation pack."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DOCUMENT_DIRECTORIES = (
    "01-Fiches-Simples",
    "02-Fiches-Completes",
    "04-Questions-Reponses",
    "05-Hardening-AIS-Cyber",
    "06-Documentation-ext",
)
IMPORTED_EXTERNAL_REPOSITORIES = (Path("05-Referentiel-GitHub/nivvlem-TSSR"),)

PLACEHOLDER_PATTERNS = (
    re.compile(r"\[Commande(?:\s|\])", re.IGNORECASE),
    re.compile(r"\bNOM_DU_FICHIER\b"),
    re.compile(r"systemctl\s+enable\s+--now\s+service", re.IGNORECASE),
)


def documentation_files(root: Path):
    for directory_name in DOCUMENT_DIRECTORIES:
        directory = root / directory_name
        if not directory.is_dir():
            yield directory, None
            continue

        for path in sorted(directory.rglob("*")):
            if not path.is_file() or path.name == "README.md":
                continue
            if directory_name == "06-Documentation-ext":
                relative_path = path.relative_to(directory)
                if any(repository in relative_path.parents for repository in IMPORTED_EXTERNAL_REPOSITORIES):
                    continue
            yield path, directory_name


def check_document(path: Path, root: Path) -> list[str]:
    errors = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return [f"{path.relative_to(root)}: lecture impossible ({error})"]

    relative_path = path.relative_to(root)
    if not re.search(r"(?m)^#\s+\S", text):
        errors.append(f"{relative_path}: titre Markdown de premier niveau absent")
    if not re.search(r"(?im)^\s*[-*]\s*\*\*Tags\*\*\s*:", text):
        errors.append(f"{relative_path}: métadonnée Tags absente")

    for pattern in PLACEHOLDER_PATTERNS:
        if pattern.search(text):
            errors.append(f"{relative_path}: placeholder générique détecté ({pattern.pattern})")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="racine du pack (défaut : dossier parent de 00-Administration)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    errors = []
    files_checked = 0
    for path, directory_name in documentation_files(root):
        if directory_name is None:
            errors.append(f"{path.relative_to(root)}: dossier documentaire absent")
            continue
        files_checked += 1
        errors.extend(check_document(path, root))

    print(f"Fiches contrôlées : {files_checked}")
    if errors:
        print(f"Écarts structurels : {len(errors)}")
        for error in errors:
            print(f"- {error}")
        print("Ce contrôle vérifie la structure, pas l'exécution ni la sécurité effective des procédures.")
        return 1

    print("OK : titres, tags et placeholders génériques vérifiés.")
    print("Ce contrôle ne remplace pas une revue technique ni un test en environnement cible.")
    return 0


if __name__ == "__main__":
    sys.exit(main())