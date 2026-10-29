# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier ce qu'un poste distant voit.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis un autre poste :
   ```sh
   nmap -sS -p- -T4 ADRESSE_NAS
   ```
   👉 Explication : ports vus de l'extérieur ; périmètre autorisé uniquement.

2. Tester les partages :
   ```sh
   smbclient -L //ADRESSE_NAS -U ADMIN1
   showmount -e ADRESSE_NAS
   ```
   👉 Explication : partages SMB et exports NFS.

## 2. Production — Contrôles

Refaire après chaque changement.

## 3. Production — Sécurité

Aucun port de stockage sur Internet.

## Validation et retour arrière

- **Validation** : Résultats conformes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)