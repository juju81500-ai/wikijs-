# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Décider du sort du compte root.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler que root est verrouillé (cas par défaut sous Ubuntu : on utilise `sudo`) :
   ```bash
   sudo passwd -S root
   sudo passwd -l root
   ```
   👉 Explication : `L` indique un compte verrouillé; garder un accès console de secours testé.

2. Ne jamais saisir de mot de passe en argument; en cas de définition, laisser `passwd` le demander :
   ```bash
   sudo passwd root
   ```
   👉 Explication : la commande demande le mot de passe sans l'afficher.

## 2. Production — Contrôles

Stocker tout mot de passe root de secours dans le coffre d'entreprise.

## 3. Production — Sécurité

Interdire root en SSH (étape 27).

## Validation et retour arrière

- **Validation** : `passwd -S root` affiche `L`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)