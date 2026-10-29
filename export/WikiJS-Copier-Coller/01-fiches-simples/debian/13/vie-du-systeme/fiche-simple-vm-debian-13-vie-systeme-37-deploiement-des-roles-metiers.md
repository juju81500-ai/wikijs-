# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer le service attendu.

## 1. Hors-Production (Lab / Test / POC)

1. Installer par paquet (exemple Nginx) puis activer :
   ```bash
   sudo apt install nginx
   sudo systemctl enable --now nginx
   systemctl status nginx --no-pager
   ```
   👉 Explication : installe et démarre le service.

2. Pour les autres logiciels, ouvrir la fiche du dossier **Vie du logiciel**.
   👉 Explication : chaque logiciel a son guide en étapes.

## 2. Production — Contrôles

Un rôle par machine quand c'est possible.

## 3. Production — Sécurité

Ouvrir le port au pare-feu uniquement pour les clients prévus.

## Validation et retour arrière

- **Validation** : Le service répond depuis un client autorisé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)