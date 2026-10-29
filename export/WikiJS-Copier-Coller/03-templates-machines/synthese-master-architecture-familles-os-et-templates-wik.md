5. **Docker-LXC/**
# 🏗️ Synthèse Master - Architecture, Familles OS et Templates Officiels Wiki.js

## 1. Arborescence du pack présent

```text
/ (Racine de Wiki.js)
│
├── 📁 00-Administration/             Matrices, arborescence et règles d'automatisation
├── 📁 01-Fiches-Simples/
│   ├── 📁 Alpine/
│   ├── 📁 Debian/
│   ├── 📁 Docker-LXC/
│   ├── 📁 RedHat-Rocky/
│   ├── 📁 Ubuntu/
│   └── 📁 Windows/
├── 📁 02-Fiches-Completes/
│   ├── 📁 Alpine-Linux/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Debian-12/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Debian-13/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Ubuntu-Server/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Rocky-Linux-9/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Windows-Client/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Windows-Server-2022/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Windows-Server-2025/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Docker/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 Proxmox-VE/{Installation-Deploiement,Diagnostic,Autres}/
│   ├── 📁 OPNsense/{Installation-Deploiement,Diagnostic,Autres}/
│   └── 📁 Multi-OS/{Installation-Deploiement,Diagnostic,Autres}/
├── 📁 03-Templates-Machines/         Synthèse et templates
├── 📁 04-Questions-Reponses/         Q/R et fiches de réparation
└── 📁 05-Hardening-AIS-Cyber/        Fiches de durcissement
```

Les fiches complètes sont rangées sous `02-Fiches-Completes/<OS>/<Type>/` avec les catégories `Installation-Deploiement`, `Diagnostic` et `Autres`. Les guides transverses sont dans `Multi-OS`. Les fiches simples et Q/R restent majoritairement sans extension `.md`.

---

## 2. Découpage Détaillé des Familles d'OS

1. **Debian/**
   - Debian 12 Bookworm et Debian 13 Trixie
   - Conteneurs LXC Debian sur Proxmox
   - Ubuntu est classé dans son propre dossier

2. **RedHat-Rocky/**
   - Rocky Linux 9

3. **Alpine/**
   - Alpine Linux (LXC et VM légers)

4. **Windows/**
   - Windows Server 2022 et 2025
   - Windows 10 et Windows 11

5. **Docker-LXC/****
   - Conteneurs, Compose et hôte Docker; l'hôte dépend d'une distribution Linux

---

## 3. Rôles et Règles Transversales

- **Indexation** : l'arborescence et les matrices servent d'index; les pages doivent porter un titre, des tags et un périmètre explicite.
- **Méthodes** : les fiches simples utilisent les modes lab/production quand ils sont pertinents; une procédure de réparation ou un guide spécifique à un produit peut adopter une structure diagnostic/correction/retour arrière.
- **Structure des étapes** : commande exacte ou clic GUI + explication simple, claire et précise.
- **Versions** : vérifier les notes de version et les paquets de la distribution. Debian 12/13, Ubuntu 24.04/26.04 et Windows Server 2022/2025 ne sont pas interchangeables.
- **Contrôle automatisé** : lancer `python3 00-Administration/verify_wiki.py .`; ce contrôle est en lecture seule et ne certifie pas l'exécution réelle des procédures.

---

## 4. Templates Officiels Markdown

Les templates complets de fiches simples, fiches complexes et fiches machine sont dans [[Templates_Officiels_Wiki]].

La compatibilité des versions et des paquets de base est suivie dans [[Compatibilite_Versions_OS_Paquets_Base]]. Le parcours par étapes est dans [[Parcours_Installation_Production_Couverture_Fiches_Simples]].