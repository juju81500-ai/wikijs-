# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Protéger la configuration et les points de restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les droits du fichier de configuration :
   ```sh
   ls -l /conf/config.xml
   ls -ld /conf /conf/backup
   ```
   👉 Explication : `config.xml` doit appartenir à `root` et ne pas être lisible par les autres.

2. Créer un point de restauration ZFS : Système > Snapshots > Ajouter, puis vérifier :
   ```sh
   bectl list
   zfs list -t snapshot | head
   ```
   👉 Explication : chaque environnement de démarrage permet de revenir en arrière après une mise à jour.

## 2. Production — Contrôles

Limiter le nombre de snapshots conservés pour ne pas saturer le disque.

## 3. Production — Sécurité

Le fichier de configuration contient des secrets : droits stricts et sauvegardes chiffrées.

## Validation et retour arrière

- **Validation** : `config.xml` n'est accessible qu'à root.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
