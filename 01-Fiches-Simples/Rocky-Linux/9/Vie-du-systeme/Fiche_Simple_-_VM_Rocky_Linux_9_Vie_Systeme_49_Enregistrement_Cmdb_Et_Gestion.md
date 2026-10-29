# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Inventorier la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter les informations d'inventaire :
   ```bash
   hostnamectl
   cat /etc/os-release
   ip -br a
   sudo dmidecode -s system-serial-number
   ```
   👉 Explication : identité, version, adresses et numéro de série.

2. Créer la fiche CMDB avec propriétaire et criticité.
   👉 Explication : assure le suivi du cycle de vie.

3. Lister les comptes autorisés :
   ```bash
   getent group wheel
   sudo -l -U ADMIN1
   ```
   👉 Explication : rapproche les accès de la CMDB.

## 2. Production — Contrôles

Mettre à jour la CMDB à chaque changement.

## 3. Production — Sécurité

Revoir les accès tous les trimestres.

## Validation et retour arrière

- **Validation** : La fiche CMDB est complète.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
