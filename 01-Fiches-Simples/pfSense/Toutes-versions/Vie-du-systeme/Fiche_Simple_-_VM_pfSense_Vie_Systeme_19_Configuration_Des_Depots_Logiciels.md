# Fiche_Simple_-_VM_pfSense_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Choisir la branche des mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans System > Update > Update Settings : choisir la Branch (`Latest Stable Version`) et enregistrer.
   👉 Explication : sélectionne le dépôt de la version stable; la branche de développement est à éviter en production.

2. Contrôler la configuration du dépôt :
   ```sh
   cat /etc/version
   pkg-static -vv | grep -A5 'Repositories'
   ```
   👉 Explication : affiche la version installée et l'URL du dépôt utilisé.

## 2. Production — Contrôles

Utiliser un miroir interne ou un proxy pour les parcs importants.

## 3. Production — Sécurité

Rester en HTTPS; ne pas activer la branche de développement en production.

## Validation et retour arrière

- **Validation** : System > Update indique l'état du dépôt sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
