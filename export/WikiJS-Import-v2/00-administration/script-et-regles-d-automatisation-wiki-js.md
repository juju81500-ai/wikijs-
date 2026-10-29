---
title: "🛠️ Script d'Automatisation & Règles de Validation - Wiki.js"
description: "Le vérificateur réellement présent dans le pack est [verifywiki.py](verifywiki.py). Il contrôle en lecture seule les pages .md et sans extension des dossiers 01-Fiches-Simples, 02-Fiches-Completes, 04-Questions-Reponses, 05-Hardening-AIS-Cyber et 06-Documentation-ext."
published: true
date: 2026-10-27T20:20:13Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:20:13Z
dateModified: 2026-10-27T20:20:13Z
---

# 🛠️ Script d'Automatisation & Règles de Validation - Wiki.js

## Script maintenu
Le vérificateur réellement présent dans le pack est [`verify_wiki.py`](verify_wiki.py). Il contrôle en lecture seule les pages `.md` et sans extension des dossiers `01-Fiches-Simples`, `02-Fiches-Completes`, `04-Questions-Reponses`, `05-Hardening-AIS-Cyber` et `06-Documentation-ext`.

La revue et le suivi des 86 fiches complètes et des 11 fiches Questions/Réponses et réparation sont détaillés dans la [matrice complémentaire](/00-administration/matrice-controle-fiches-completes-et-questions-reponses). Les fiches complètes sont classées par OS et par type de procédure. La matrice distingue contrôle structurel, revue technique et essai sur environnement cible.

### 🔍 1. Contrôles effectués
1. Vérifie les dossiers documentaires attendus, les titres Markdown et les métadonnées `Tags`.
2. Repère les placeholders génériques connus.
3. Ne modifie aucun fichier et ne met pas à jour les dates.
4. Ne vérifie ni la syntaxe des commandes, ni l'exactitude technique, ni le comportement en production.

---

## Archive historique (non maintenue)

Le bloc Python ci-dessous est une ancienne proposition et ne correspond pas à la structure du pack. **Ne pas l'exécuter ni le recopier** ; utiliser le fichier `verify_wiki.py` indiqué ci-dessus.

### Ancien exemple

```python
#!/usr/bin/env python3
"""
Script de vérification et d'automatisation pour la documentation Wiki.js Lab & TSSR.
"""

import os
import re
import sys
from datetime import datetime

EXPECTED_DIRECTORIES = [
    "00-Administration",
    "00-Administration/SSH",
    "00-Administration/Logiciels",
    "00-Administration/Templates",
    "00-Administration/Checklists",
    "01-Fiches-Simples",
    "02-Fiches-Completes",
    "03-Documentation-Machine",
    "06-Documentation-ext",
]

MANDATORY_MACHINE_FIELDS = [
    "Rôle", "Besoins", "Logiciels", "Ports", "Firewall Machine", "Firewall Externe"
]

MANDATORY_SIMPLE_SECTIONS = [
    "Hors-Production", "Production — Façon Simplifiée", "Production — Façon Sécurisée"
]

def update_modification_date(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_content = re.sub(
        r'(Dernière modification\s*:\s*).*',
        rf'\1{now_str}',
        content
    )

    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def verify_wiki(base_path):
    errors = []
    warnings = []
    updated_files = []

    print(f"=== Lancement du contrôle Wiki.js dans : {base_path} ===\n")

    for rel_dir in EXPECTED_DIRECTORIES:
        target_dir = os.path.join(base_path, rel_dir)
        if not os.path.exists(target_dir):
            warnings.append(f"[Dossier Manquant] : {rel_dir}")
            continue
        
        readme_path = os.path.join(target_dir, "README.md")
        if not os.path.exists(readme_path):
            errors.append(f"[README Manquant] : Il manque un README.md dans {rel_dir}")

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".md") or file == "README.md":
                continue
            
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_path)

            if update_modification_date(full_path):
                updated_files.append(rel_path)

            with open(full_path, 'r', encoding='utf-8') as f:
                text = f.read()

            if "Tags" not in text and "tags" not in text:
                errors.append(f"[Tags Manquants] : {rel_path} ne contient pas de section/ligne Tags.")

            if "03-Documentation-Machine" in rel_path:
                for field in MANDATORY_MACHINE_FIELDS:
                    if field not in text:
                        errors.append(f"[Champ Machine Manquant] '{field}' dans {rel_path}")

            if "01-Fiches-Simples" in rel_path:
                for sec in MANDATORY_SIMPLE_SECTIONS:
                    if sec not in text:
                        errors.append(f"[Section Méthode Manquante] '{sec}' dans {rel_path}")

    print("--- RAPPORT DE VÉRIFICATION ---")
    if updated_files:
        print(f"\n✅ Dates de modification mises à jour sur {len(updated_files)} fichier(s) :")
        for uf in updated_files:
            print(f"   - {uf}")

    if warnings:
        print("\n⚠️ Avertissements :")
        for w in warnings:
            print(f"   - {w}")

    if errors:
        print(f"\n❌ {len(errors)} ERREUR(S) DÉTECTÉE(S) :")
        for e in errors:
            print(f"   - {e}")
        return False
    else:
        print("\n🎉 Félicitations ! Votre Wiki.js est 100% conforme aux règles.")
        return True

if __name__ == "__main__":
    path_to_check = sys.argv[1] if len(sys.argv) > 1 else "."
    verify_wiki(path_to_check)
```

---

## 🚀 3. Utilisation
```bash
python3 00-Administration/verify_wiki.py .
```