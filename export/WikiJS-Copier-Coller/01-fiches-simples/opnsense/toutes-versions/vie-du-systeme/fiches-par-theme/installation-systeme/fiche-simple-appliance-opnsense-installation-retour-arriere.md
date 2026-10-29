# Fiche_Simple_-_Appliance_OPNsense_Installation_Retour_Arriere.md

- **Environnement** : Appliance physique ou VM dédiée avec interfaces réseau identifiées
- **OS / Version** : OPNsense Community ou Business Edition, release maintenue compatible avec la plateforme
- **Catégorie** : pare-feu / retour arrière

---

## Problème précis à résoudre

Retrouver un accès ou revenir à une configuration valide.

## 1. Hors-Production (Lab / Test / POC)

1. En cas de perte d'accès, utiliser la console locale : **1) Assign interfaces** ou **2) Set interface IP address** pour corriger l'affectation.
   👉 Explication : la console reste accessible même sans réseau.

2. Restaurer une configuration valide : menu console (entrée de restauration de configuration, selon la version) ou **System > Configuration > Backups > Restore**.
   👉 Explication : revient à un état connu.

3. Voir les sauvegardes locales :
   ```sh
   ls -l /conf/backup/
   ```
   👉 Explication : Dans le shell de la console, liste les sauvegardes automatiques de configuration.

4. Si une mise à jour empêche le démarrage, suivre la procédure officielle de restauration propre à la version et au type de stockage.
   👉 Explication : ne pas effacer l'installation ni réinitialiser sans sauvegarde vérifiée.

## 2. Production — Contrôles

Ne jamais réinitialiser aux valeurs d'usine sans sauvegarde vérifiée.

## 3. Production — Sécurité

- Protéger les configurations exportées.

## Validation et retour arrière

- **Validation** : accès rétabli et configuration valide chargée.
- **Retour arrière** : sans objet : cette étape est elle-même le retour arrière.

## Si le problème n'est pas résolu

- [OPNsense — Installation](https://docs.opnsense.org/manual/install.html)
- [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html)
- [Guide complet — étape 6](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production#6-retour-arriere)