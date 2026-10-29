# Fiche_Simple_-_Appliance_OPNsense_Installation_Recette.md

- **Environnement** : Appliance physique ou VM dédiée avec interfaces réseau identifiées
- **OS / Version** : OPNsense Community ou Business Edition, release maintenue compatible avec la plateforme
- **Catégorie** : pare-feu / validation

---

## Problème précis à résoudre

Valider interfaces, filtrage, administration, journaux et sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. **Interfaces > Overview** et **System > Gateways > Configuration** : vérifier interfaces, passerelles et route par défaut.
   👉 Explication : confirme le routage.

2. Contrôler route et heure :
   ```sh
   netstat -rn
   date
   ```
   👉 Explication : Dans le shell de la console, affiche la table de routage et l'heure.

3. Depuis des clients de test, vérifier les flux autorisés et les refus attendus.
   👉 Explication : valide le filtrage.

4. Confirmer que l'administration n'est joignable que depuis le réseau prévu; consulter **Firewall > Log Files > Live View**.
   👉 Explication : valide l'isolation de l'administration et les journaux.

5. Tester la sauvegarde de configuration, un redémarrage contrôlé (**Power > Reboot**) et la restauration en lab.
   👉 Explication : prouve la reprise.

6. Consigner version, empreinte du média, interfaces, adresses, règles, responsable et résultat.
   👉 Explication : trace de recette.

## 2. Production — Contrôles

Conserver le compte rendu de recette.

## 3. Production — Sécurité

- Tester la restauration en lab, pas en production.

## Validation et retour arrière

- **Validation** : tous les points de la recette sont validés et consignés.
- **Retour arrière** : corriger puis rejouer la recette; en dernier recours restaurer la configuration exportée.

## Si le problème n'est pas résolu

- [OPNsense — Installation](https://docs.opnsense.org/manual/install.html)
- [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html)
- [Guide complet — étape 5](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production#5-recette)