#!/usr/bin/env python3
"""Validate command-block import JSON and check stable identifiers."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


COMMAND_ID_PATTERN = re.compile(r"^(?:c|cmd)-[a-z0-9]+(?:-[a-z0-9]+)*$")
FOLDER_ID_PATTERN = re.compile(r"^f-[a-z0-9]+(?:-[a-z0-9]+)*$")
NUMERIC_COMMAND_ID_PATTERN = re.compile(r"^cmd-(\d+)$")


def validate_import(path: Path, show_next_id: bool) -> int:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(
            f"ERREUR JSON dans {path} : ligne {error.lineno}, "
            f"colonne {error.colno} : {error.msg}"
        )
        return 1
    except (OSError, UnicodeError) as error:
        print(f"ERREUR de lecture dans {path} : {error}")
        return 1

    errors: list[str] = []
    if not isinstance(document, dict):
        print("ERREUR : la racine JSON doit être un objet.")
        return 1

    command_blocks = document.get("command_blocks")
    if not isinstance(command_blocks, dict):
        print("ERREUR : la clé 'command_blocks' doit contenir un objet.")
        return 1

    commands = command_blocks.get("commands")
    if not isinstance(commands, list):
        print("ERREUR : 'command_blocks.commands' doit contenir une liste.")
        return 1

    seen_ids: dict[str, int] = {}
    numeric_ids: list[int] = []
    for index, command in enumerate(commands, start=1):
        if not isinstance(command, dict):
            errors.append(f"Entrée {index} : l'objet commande est invalide.")
            continue

        command_id = command.get("id")
        if not isinstance(command_id, str) or not COMMAND_ID_PATTERN.fullmatch(command_id):
            errors.append(f"Entrée {index} : ID absent ou format invalide ({command_id!r}).")
        else:
            if command_id in seen_ids:
                errors.append(
                    f"ID dupliqué {command_id!r} aux entrées "
                    f"{seen_ids[command_id]} et {index}."
                )
            else:
                seen_ids[command_id] = index

            numeric_match = NUMERIC_COMMAND_ID_PATTERN.fullmatch(command_id)
            if numeric_match:
                numeric_ids.append(int(numeric_match.group(1)))

        folder_id: Any = command.get("folder_id")
        if folder_id is not None and (
            not isinstance(folder_id, str) or not FOLDER_ID_PATTERN.fullmatch(folder_id)
        ):
            errors.append(f"Entrée {index} : folder_id invalide ({folder_id!r}).")

    if errors:
        print(f"ÉCARTS détectés dans {path} :")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK : JSON valide, {len(commands)} commandes, {len(seen_ids)} IDs uniques.")
    if show_next_id:
        next_id = max(numeric_ids, default=0) + 1
        print(f"Prochain ID proposé : cmd-{next_id}")
    print("Les références folder_id sont vérifiées par leur format, pas par l'application cible.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "file",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("TXT.txt"),
        help="fichier JSON à contrôler (défaut : TXT.txt dans ce dossier)",
    )
    parser.add_argument(
        "--next-id",
        action="store_true",
        help="afficher le prochain ID numérique cmd-* disponible",
    )
    args = parser.parse_args()
    return validate_import(args.file, args.next_id)


if __name__ == "__main__":
    sys.exit(main())