#!/usr/bin/env python3
"""Genere l'index des lecons « tout-en-un » et le registre global des credits d'images.

Lit les fichiers `Lecon_*.md` de chaque categorie (dossier `Lecons/`) et ecrit :
  - Tout-en-un/Lecons_Index.md
  - Tout-en-un/Credits_Images.md
Bibliotheque standard uniquement.
Usage : python3 tools/referentiel/build_lecons_index.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "01-Fiches-Simples" / "Transverses" / "Tout-en-un"


def meta(text: str, key: str) -> str:
    match = re.search(rf"(?m)^\s*[-*]\s*\*\*{key}\*\*\s*:\s*(.+)$", text)
    return match.group(1).strip() if match else "—"


def h1_title(path: Path) -> str:
    match = re.search(r"(?m)^#\s+(.+)$", path.read_text(encoding="utf-8"))
    return match.group(1).strip() if match else path.stem


def credit_rows(text: str) -> list[list[str]]:
    match = re.search(r"(?ms)^##\s+Crédits des images\s*$(.*?)(?=^##\s|\Z)", text)
    if not match:
        return []
    rows = []
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|[\s:|-]+\|$", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0].lower().startswith(("fichier", "---")):
            continue
        rows.append(cells)
    return rows


def kind(cells: list[str]) -> str:
    joined = " ".join(cells).lower()
    if "création originale" in joined or "creation originale" in joined:
        return "Création originale (CC0)"
    return "Image libre tierce"


def main() -> int:
    categories = sorted(p for p in BASE.iterdir() if p.is_dir() and re.match(r"\d{2}-", p.name) and p.name != "00-Referentiel-Sites")
    index = [
        "# Leçons tout-en-un — index",
        "",
        "- **Tags** : `transverse`, `tout-en-un`, `lecon`, `index`",
        "",
        "Leçons originales et illustrées, rangées par catégorie. Chaque leçon comprend objectifs, cours, mise en pratique, exercices corrigés, quiz, erreurs fréquentes et récapitulatif. "
        "Le contenu est rédigé pour ce pack ; les cours des sites suivis sont référencés dans le [référentiel des sites](00-Referentiel-Sites/README.md) sans être reproduits. "
        "Les images libres sont créditées dans le [registre des images](Credits_Images.md).",
        "",
    ]
    credits = [
        "# Crédits des images des leçons",
        "",
        "- **Tags** : `transverse`, `tout-en-un`, `lecon`, `credits`, `licences`",
        "",
        "Registre généré à partir des sections « Crédits des images » de chaque leçon. "
        "Les images « Création originale » sont dédiées au domaine public (CC0). "
        "Les images tierces proviennent de Wikimedia Commons sous licence CC0, domaine public, CC BY ou CC BY-SA ; "
        "les images CC BY-SA restent sous cette licence et doivent conserver leur attribution.",
        "",
        "| Leçon | Fichier | Type | Source / auteur | Licence |",
        "|---|---|---|---|---|",
    ]
    total_lessons = total_words = total_images = third_party = 0
    for category in categories:
        lessons = sorted((category / "Lecons").glob("Lecon_*.md"))
        title = category.name.split("-", 1)[1].replace("-", " ")
        index += [f"## {category.name[:2]} — {title}", ""]
        if not lessons:
            index += ["_Aucune leçon publiée._", ""]
            continue
        index += ["| Leçon | Niveau | Durée estimée | Mots | Images |", "|---|---|---|---|---|"]
        for lesson in lessons:
            text = lesson.read_text(encoding="utf-8")
            h1 = re.search(r"(?m)^#\s+(.+)$", text)
            name = h1.group(1).strip() if h1 else lesson.stem
            rows = credit_rows(text)
            section = re.search(r"(?ms)^##\s+Crédits des images\s*$(.*?)(?=^##\s|\Z)", text)
            credited = section.group(1) if section else ""
            for ref in sorted(set(re.findall(r"!\[[^\]]*\]\(images/([^)\s]+)\)", text))):
                if ref not in credited and "création originale" in credited.lower():
                    rows.append([f"`images/{ref}`", "Création originale", "", "CC0", ""])
            words = len(re.findall(r"\S+", text))
            rel = lesson.relative_to(BASE).as_posix()
            index.append(
                f"| [{name}]({rel}) | {meta(text, 'Niveau')} | {meta(text, 'Durée estimée')} | {words} | {len(rows)} |"
            )
            total_lessons += 1
            total_words += words
            total_images += len(rows)
            for cells in rows:
                cells = (cells + [""] * 5)[:5]
                k = kind(cells)
                third_party += k.startswith("Image libre")
                source = cells[1] if k.startswith("Image libre") else "Création du projet Pack Master"
                author = f" — {cells[2]}" if k.startswith("Image libre") and cells[2] else ""
                licence = cells[3] if k.startswith("Image libre") else "CC0 1.0"
                credits.append(
                    f"| [{name}]({rel}) | {cells[0].replace('|', '/')} | {k} | {source.replace('|', '/')}{author.replace('|', '/')} | {licence.replace('|', '/')} |"
                )
        index.append("")
        listing = [
            f"# Leçons — {title}",
            "",
            f"- **Tags** : `transverse`, `tout-en-un`, `lecon`, `index`",
            "",
            "Leçons originales et illustrées de la catégorie. Retour à l'[index général des leçons](../../Lecons_Index.md).",
            "",
        ]
        listing += [f"- [{h1_title(l)}]({l.name})" for l in lessons]
        (category / "Lecons" / "README.md").write_text("\n".join(listing) + "\n", encoding="utf-8")
    index[4:4] = [
        f"**{total_lessons} leçons**, environ {total_words} mots, {total_images} illustrations ({third_party} images libres tierces, {total_images - third_party} créations originales).",
        "",
    ]
    (BASE / "Lecons_Index.md").write_text("\n".join(index).rstrip() + "\n", encoding="utf-8")
    (BASE / "Credits_Images.md").write_text("\n".join(credits).rstrip() + "\n", encoding="utf-8")
    print(f"{total_lessons} leçons, {total_images} images ({third_party} tierces)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
