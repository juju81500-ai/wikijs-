# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Nommer la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le nom et vérifier (remplacer `srv01.exemple.lan`) :
   ```bash
   sudo hostnamectl set-hostname srv01.exemple.lan
   hostnamectl
   hostname -f
   ```
   👉 Explication : fixe le nom d'hôte; `hostname -f` doit renvoyer le FQDN.

2. Empêcher cloud-init de réécrire le nom à chaque démarrage, puis aligner `/etc/hosts` :
   ```bash
   echo 'preserve_hostname: true' | sudo tee /etc/cloud/cloud.cfg.d/99-hostname.cfg
   grep -n 127.0.1.1 /etc/hosts
   ```
   👉 Explication : sans cette directive, cloud-init peut remettre le nom initial; la ligne `127.0.1.1 srv01.exemple.lan srv01` doit exister.

## 2. Production — Contrôles

Respecter la convention de nommage de l'organisation et inscrire le nom au DNS.

## 3. Production — Sécurité

Éviter les noms qui révèlent le rôle ou la version.

## Validation et retour arrière

- **Validation** : `hostname -f` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)