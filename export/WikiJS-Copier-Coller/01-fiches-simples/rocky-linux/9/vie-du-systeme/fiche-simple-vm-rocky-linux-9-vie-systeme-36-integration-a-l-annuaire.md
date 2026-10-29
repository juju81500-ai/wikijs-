# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Joindre le serveur à l'annuaire.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets d'intégration :
   ```bash
   sudo dnf install -y realmd sssd oddjob oddjob-mkhomedir adcli samba-common-tools
   ```
   👉 Explication : outils de jonction à Active Directory.

2. Découvrir le domaine (adapter `EXEMPLE.LAN`) :
   ```bash
   realm discover EXEMPLE.LAN
   ```
   👉 Explication : vérifie DNS et contrôleurs; `EXEMPLE.LAN` est le domaine.

3. Joindre le domaine avec un compte autorisé (`ADMINAD`) :
   ```bash
   sudo realm join -U ADMINAD EXEMPLE.LAN
   ```
   👉 Explication : demande le mot de passe en interactif; ne jamais l'écrire en clair.

## 2. Production — Contrôles

Joindre dans l'unité d'organisation prévue et ajouter le compte machine à la CMDB.

## 3. Production — Sécurité

Limiter l'accès via `realm permit` et sudo par groupe d'annuaire.

## Validation et retour arrière

- **Validation** : `id UTILISATEUR@EXEMPLE.LAN` renvoie l'identité.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)