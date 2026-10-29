# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Joindre le domaine ou le VPN.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils de jonction AD :
   ```bash
   sudo apt install realmd sssd sssd-ad sssd-tools adcli krb5-user packagekit libnss-sss libpam-sss
   ```
   👉 Explication : paquets nécessaires à `realm` et à SSSD.

2. Découvrir puis joindre (remplacer domaine et compte) :
   ```bash
   realm discover EXEMPLE.LAN
   sudo realm join -U admin-ad EXEMPLE.LAN
   sudo pam-auth-update --enable mkhomedir
   ```
   👉 Explication : `realm` demande le mot de passe à l'écran; `mkhomedir` crée le dossier personnel à la première connexion.

## 2. Production — Contrôles

Compte de jonction dédié à droits limités.

## 3. Production — Sécurité

Vérifier l'heure (Kerberos tolère 5 minutes d'écart).

## Validation et retour arrière

- **Validation** : `id utilisateur@exemple.lan` répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)