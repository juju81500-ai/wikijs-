# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bloquer les tentatives répétées de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Système > Paramètres > Administration, vérifier que la protection contre le force brute (verrouillage après échecs) est active pour le GUI et SSH.
   👉 Explication : les adresses fautives sont ajoutées à une table de blocage.

2. Lister les adresses bloquées et en débloquer une :
   ```sh
   pfctl -t sshlockout -T show
   pfctl -t sshlockout -T delete IP_BLOQUEE
   ```
   👉 Explication : `IP_BLOQUEE` est l'adresse à débloquer après vérification.

3. Compléter par Services > Détection d'intrusion (Suricata) si le débit le permet.
   👉 Explication : détecte les attaques connues en plus du blocage.

## 2. Production — Contrôles

Surveiller les adresses bloquées dans les journaux d'authentification.

## 3. Production — Sécurité

Ne pas bloquer son propre poste d'administration : l'inscrire dans une liste de confiance.

## Validation et retour arrière

- **Validation** : Une série d'échecs de test aboutit à un blocage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
