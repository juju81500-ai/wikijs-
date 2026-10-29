# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Figer l'état de référence.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter l'identité et les versions :
   ```bash
   cat /etc/os-release
   uname -r
   hostnamectl
   ```
   👉 Explication : preuves de version et de nom.

2. Collecter services, ports et espace :
   ```bash
   systemctl --failed
   ss -tulpn
   df -hT
   rpm -qa | sort > ~/baseline-paquets.txt
   ```
   👉 Explication : état à comparer lors des audits.

3. Archiver le résultat avec la date.
   👉 Explication : base de comparaison pour les dérives.

## 2. Production — Contrôles

Stocker la baseline dans la CMDB ou le dépôt de documentation.

## 3. Production — Sécurité

Ne pas y mettre de secret.

## Validation et retour arrière

- **Validation** : Aucun service en échec et baseline archivée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)