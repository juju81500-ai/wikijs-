# Fiche_Simple_-_Appliance_OPNsense_Installation_Preparer_Architecture.md

- **Environnement** : Appliance physique ou VM dédiée avec interfaces réseau identifiées
- **OS / Version** : OPNsense Community ou Business Edition, release maintenue compatible avec la plateforme
- **Catégorie** : pare-feu / préparation

---

## Problème précis à résoudre

Définir l'architecture et préparer un média d'installation vérifié avant toute connexion réseau.

## 1. Hors-Production (Lab / Test / POC)

1. Définir par écrit WAN, LAN, VLAN, réseau de gestion, adresses, passerelle, DNS, règles, NAT, VPN, journaux et accès de secours.
   👉 Explication : sans plan, les règles et l'adressage seront improvisés.

2. Prévoir une console locale ou série; pour une VM, affecter des cartes réseau dédiées et noter leur correspondance avec les interfaces virtuelles.
   👉 Explication : la console est le seul accès fiable en cas de perte d'administration.

3. Télécharger l'image sur **opnsense.org > Download** (site officiel) ainsi que le fichier de sommes de contrôle.
   👉 Explication : évite les images modifiées.

4. Vérifier l'empreinte sous Linux :
   ```bash
   sha256sum OPNsense-REMPLACER-PAR-LE-NOM-DE-L-IMAGE.img.bz2
   ```
   👉 Explication : Calcule l'empreinte SHA-256 de l'image (nom de fichier à remplacer) à comparer à celle publiée par le projet.

5. Vérifier l'empreinte sous Windows :
   ```powershell
   Get-FileHash .\OPNsense-REMPLACER-PAR-LE-NOM-DE-L-IMAGE.img.bz2 -Algorithm SHA256
   ```
   👉 Explication : Équivalent sous Windows (nom de fichier à remplacer).

## 2. Production — Contrôles

Préparer le média d'installation seulement après vérification de l'empreinte.

## 3. Production — Sécurité

- Ne pas connecter l'appliance au réseau de production avant d'avoir défini interfaces et règles.

## Validation et retour arrière

- **Validation** : plan écrit, console disponible, empreinte du média conforme.
- **Retour arrière** : supprimer le média et l'image téléchargée si l'empreinte ne correspond pas.

## Si le problème n'est pas résolu

- [OPNsense — Installation](https://docs.opnsense.org/manual/install.html)
- [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html)
- [Guide complet — étape 1](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production#1-preparer-larchitecture)