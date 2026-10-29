# 🏗️ Architecture & READMEs Officiels (Mis à jour - Familles d OS) - Wiki.js Lab & TSSR

## 1. Arborescence Globale du Wiki.js

```text
/ (Racine de Wiki.js)
│
├── 📁 00-Administration/
│   ├── 📁 SSH/
│   │   ├── 📁 PilotSSH/
│   │   └── 📁 Cles-Privees/
│   ├── 📁 Logiciels/
│   │   ├── 📁 Windows/
│   │   ├── 📁 Linux/
│   │   └── 📁 Docker/
│   ├── 📁 Templates/
│   │   ├── 📁 Vierge/
│   │   └── 📁 Texte-IA/
│   └── 📁 Checklists/
│       ├── 📁 LXC/
│       │   ├── 📁 Alpine/
│       │   ├── 📁 Debian-Family/
│       │   └── 📁 RedHat-Family/
│       ├── 📁 VM/
│       │   ├── 📁 Debian-Family/
│       │   ├── 📁 RedHat-Family/
│       │   └── 📁 Windows/
│       └── 📁 Reseau/
│
├── 📁 01-Fiches-Simples/
│   ├── 📁 Debian-Family/            <-- Debian & Dérivés (Debian, Ubuntu, Kali, Mint, Proxmox VE)
│   │   ├── 📁 LXC/
│   │   └── 📁 VM/
│   ├── 📁 RedHat-Family/            <-- RedHat (RHEL) & Dérivés (RHEL, Rocky Linux, AlmaLinux, CentOS, Fedora)
│   │   ├── 📁 LXC/
│   │   └── 📁 VM/
│   ├── 📁 Alpine/                   <-- Alpine Linux (Conteneurs LXC & VM légers)
│   │   ├── 📁 LXC/
│   │   └── 📁 VM/
│   ├── 📁 Windows/                  <-- Windows Server / Windows 10-11
│   │   └── 📁 VM/
│   └── 📁 Docker/
│       ├── 📁 Conteneurs/
│       └── 📁 Hote-Docker/
│
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
│
├── 📁 03-Documentation-Machine/
│   └── 📄 MachinePhysique_Env_Type_NomMachine_OS_Statut.md
│
└── 📁 06-Documentation-ext/
    ├── 📄 README.md
    ├── 📄 Fiches-Aide-Informatique.md
    ├── 📄 Liens-Docs-Logicielles.md
    ├── 📄 Sites-Web.md
    ├── 📄 Hub-CVE.md
    └── 📁 Github/
        └── 📄 Github-TSSR.md
```

## 2. Découpage détaillé par OS et type de fiche

Chaque OS dispose des mêmes sous-dossiers : `Installation-Deploiement`, `Diagnostic` et `Autres`. Les procédures transverses à plusieurs OS sont classées sous `Multi-OS`.

### 🐧 Famille Debian & Dérivés (`Debian-Family/`)
- **Debian** (Version 11 Bullseye, 12 Bookworm, etc.)
- **Ubuntu / Ubuntu Server** (LTS 22.04, 24.04, etc.)
- **Kali Linux** (Outils de sécurité / Pentest)
- **Linux Mint** (Postes de travail)
- **Proxmox VE (PVE)** (Hyperviseur basé sur Debian)

### 🎩 Famille RedHat / RHEL & Dérivés (`RedHat-Family/`)
- **RedHat Enterprise Linux (RHEL)** (RHEL 8, 9, etc.)
- **Rocky Linux** (Alternative RHEL entreprise)
- **AlmaLinux** (Alternative RHEL entreprise)
- **CentOS / CentOS Stream**
- **Fedora** (Distribution communautaire / cutting-edge)

### 🏔️ Famille Alpine Linux (`Alpine/`)
- **Alpine Linux** (Conteneurs LXC et VM légers, APK package manager, OpenRC)

### 🪟 Famille Windows (`Windows/`)
- **Windows Server** (2019, 2022, 2025)
- **Windows Client** (Windows 10, Windows 11)

### 🐳 Famille Docker (`Docker/`)
- **Hôtes Docker** & **Conteneurs / Compose**