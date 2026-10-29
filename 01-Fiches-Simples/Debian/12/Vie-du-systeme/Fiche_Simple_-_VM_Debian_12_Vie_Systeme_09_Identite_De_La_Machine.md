# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

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

2. Aligner `/etc/hosts` :
   ```bash
   grep -n 127.0.1.1 /etc/hosts
   ```
   👉 Explication : la ligne `127.0.1.1 srv01.exemple.lan srv01` doit exister.

## 2. Production — Contrôles

Respecter la convention de nommage de l'organisation et inscrire le nom au DNS.

## 3. Production — Sécurité

Éviter les noms qui révèlent le rôle ou la version.

## Validation et retour arrière

- **Validation** : `hostname -f` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
