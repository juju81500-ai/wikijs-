#!/usr/bin/env python3
"""Convertit 00-cours-theoriques/glossaire.md en termes de glossaire Wiki.js (JSON et CSV)."""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "00-cours-theoriques" / "glossaire.md"
OUT_DIR = Path(__file__).resolve().parent
LOCALE = "fr"
DOC_PAGE = f"/{LOCALE}/00-cours-theoriques/glossaire"
LINK_LABEL = "Voir le glossaire complet"
ENTRY = re.compile(r"^- \*\*(.+?)\*\*(?: \(([^)]+)\))?(?: \([^)]*\))? ?: (.+)$")


def parse() -> list[dict]:
    terms, category = [], ""
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^## \d+\. (.+)$", line)
        if heading:
            category = heading.group(1)
            continue
        if not category:
            continue
        match = ENTRY.match(line)
        if not match:
            continue
        name, expansion, definition = match.groups()
        names = [part.strip() for part in name.split(" / ") if part.strip()]
        terms.append(
            {
                "locale": LOCALE,
                "term": names[0],
                "expansion": expansion or "",
                "definition": definition.strip()[:1].upper() + definition.strip()[1:],
                "aliases": names[1:],
                "category": category,
                "documentationPage": DOC_PAGE,
                "linkLabel": LINK_LABEL,
                "externalReferences": [],
                "relatedTerms": [],
                "caseSensitive": names[0].isupper(),
                "autoLink": False,
            }
        )
    link_related_terms(terms)
    return terms


def link_related_terms(terms: list[dict]) -> None:
    known = {t["term"] for t in terms if re.fullmatch(r"[A-Z][A-Z0-9]{1,7}", t["term"])}
    for item in terms:
        text = f"{item['expansion']} {item['definition']}"
        found = dict.fromkeys(
            word for word in re.findall(r"(?<![\w-])[A-Z][A-Z0-9]{1,7}(?![\w-])", text) if word in known
        )
        item["relatedTerms"] = [w for w in found if w != item["term"]][:5]


def main() -> None:
    terms = parse()
    (OUT_DIR / "glossaire-wikijs.json").write_text(
        json.dumps(terms, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    with (OUT_DIR / "glossaire-wikijs.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("term", "expansion", "definition", "aliases", "category", "documentationPage", "linkLabel", "relatedTerms", "caseSensitive", "autoLink"))
        for item in terms:
            writer.writerow(
                (item["term"], item["expansion"], item["definition"], "|".join(item["aliases"]),
                 item["category"], item["documentationPage"], item["linkLabel"], "|".join(item["relatedTerms"]),
                 item["caseSensitive"], item["autoLink"])
            )
    print(f"{len(terms)} termes écrits dans {OUT_DIR}")


if __name__ == "__main__":
    main()
