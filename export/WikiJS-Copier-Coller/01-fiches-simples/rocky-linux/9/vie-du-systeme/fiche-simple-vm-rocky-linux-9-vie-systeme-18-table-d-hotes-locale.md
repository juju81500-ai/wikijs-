# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Gérer le fichier `/etc/hosts`.

## 1. Hors-Production (Lab / Test / POC)

1. Visualiser le fichier :
   ```bash
   cat /etc/hosts
   ```
   👉 Explication : contient `localhost` par défaut.

2. Ajouter le nom de la machine (adresse et nom à adapter) :
   ```bash
   echo '192.0.2.10 SRV01.EXEMPLE.LAN SRV01' | sudo tee -a /etc/hosts
   ```
   👉 Explication : permet la résolution sans DNS; ajout en fin de fichier.

3. Vérifier l'ordre de résolution :
   ```bash
   grep '^hosts' /etc/nsswitch.conf
   getent hosts SRV01
   ```
   👉 Explication : `files` avant `dns` donne priorité au fichier local.

## 2. Production — Contrôles

Limiter `/etc/hosts` au strict nécessaire; le DNS reste la source de vérité.

## 3. Production — Sécurité

Une entrée erronée peut détourner un service; relire avant de valider.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie l'adresse attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)