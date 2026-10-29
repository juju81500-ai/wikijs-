# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-18`

---

## Problème précis à résoudre

Garantir la résolution des noms critiques sans DNS.

## 1. Hors-Production (Lab / Test / POC)

1. ESXi n'a pas d'interface pour `/etc/hosts` : éditer le fichier en SSH :
   ```sh
   vi /etc/hosts
   cat /etc/hosts
   ```
   👉 Explication : ajouter `IP_VCENTER vcenter.domaine.local` si le DNS est incertain.

2. Rendre la modification persistante : `/etc/hosts` est conservé par `/sbin/auto-backup.sh`.
   ```sh
   /sbin/auto-backup.sh
   ```
   👉 Explication : sinon la modification est perdue au redémarrage.

3. Limiter l'usage au strict nécessaire.
   👉 Explication : le DNS reste la source de référence.

## 2. Production — Contrôles

Documenter les entrées ajoutées.

## 3. Production — Sécurité

Contrôler le fichier après chaque modification.

## Validation et retour arrière

- **Validation** : Le nom se résout sans DNS.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
