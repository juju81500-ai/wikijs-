# Fiche_Simple_-_VM_pfSense_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

S'assurer que le pare-feu redémarre seul.

## 1. Hors-Production (Lab / Test / POC)

1. Terminer l'installateur, choisir `Reboot`, retirer l'ISO ou la clé.
   👉 Explication : le pare-feu démarre sur le disque et affiche le menu console.

2. Contrôler les environnements de démarrage et l'amorçage :
   ```sh
   bectl list
   sysctl machdep.bootmethod
   ```
   👉 Explication : `bectl list` montre l'environnement actif (`NR`); System > Boot Environments donne la même vue dans l'interface (ZFS).

## 2. Production — Contrôles

Prendre un environnement de démarrage avant chaque mise à jour.

## 3. Production — Sécurité

Retirer le média d'installation après l'installation.

## Validation et retour arrière

- **Validation** : Le pare-feu redémarre sans média et affiche le menu console.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
