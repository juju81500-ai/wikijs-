# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Compléter `/etc/hosts` si besoin.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer prudemment :
   ```bash
   sudoedit /etc/hosts
   getent hosts srv01
   ```
   👉 Explication : ajouter `192.0.2.10 srv01.exemple.lan srv01`; `getent` confirme la résolution.

## 2. Production — Contrôles

Utiliser le DNS plutôt que `/etc/hosts` pour tout hôte partagé.

## 3. Production — Sécurité

Un `/etc/hosts` modifié peut rediriger du trafic : surveiller ce fichier.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie l'entrée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)