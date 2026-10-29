# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Installer le service attendu.

## 1. Hors-Production (Lab / Test / POC)

1. Installer par paquet (exemple Nginx) puis activer et ouvrir le port :
   ```bash
   sudo apt install nginx
   sudo systemctl enable --now nginx
   sudo ufw allow from 192.0.2.0/24 to any port 80,443 proto tcp
   systemctl status nginx --no-pager
   ```
   👉 Explication : installe et démarre le service; la règle UFW limite l'accès aux clients prévus.

2. Pour un logiciel livré en snap, privilégier le canal stable :
   ```bash
   snap info NOM_SNAP | head
   sudo snap install NOM_SNAP
   ```
   👉 Explication : remplacer `NOM_SNAP`; `snap list` montre l'état et les mises à jour automatiques.

3. Pour les autres logiciels, ouvrir la fiche du dossier **Vie du logiciel**.
   👉 Explication : chaque logiciel a son guide en étapes.

## 2. Production — Contrôles

Un rôle par machine quand c'est possible.

## 3. Production — Sécurité

Ouvrir le port au pare-feu uniquement pour les clients prévus.

## Validation et retour arrière

- **Validation** : Le service répond depuis un client autorisé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
