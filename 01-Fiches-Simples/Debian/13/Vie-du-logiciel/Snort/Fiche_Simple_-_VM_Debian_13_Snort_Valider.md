# Fiche_Simple_-_VM_Debian_13_Snort_Valider

- **Environnement** : VM Debian 13 dédiée à Snort IDS passif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : Snort IDS passif / valider
- **Tags** : `snort`, `debian13`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Valider configuration et réception d’événements sans trafic hors périmètre.

## 1. Hors-Production (Lab / Test / POC)

1. Répéter le test de configuration :
   ```bash
   SNORT_CONFIG=/etc/snort/snort.conf
   sudo snort -T -c "$SNORT_CONFIG"
   ```
   👉 Explication : Remplacer SNORT_CONFIG par le chemin présent sur l’hôte; poursuivre seulement si le test réussit.

2. Après approbation, observer 60 secondes sur l’interface miroir :
   ```bash
   SNORT_CONFIG=/etc/snort/snort.conf
   INTERFACE_CAPTURE=INTERFACE_CAPTURE
   sudo timeout --signal=INT 60 snort -c "$SNORT_CONFIG" -i "$INTERFACE_CAPTURE"
   ```
   👉 Explication : Remplacer les valeurs en capitales par le chemin et l’interface autorisés; contrôler la sortie avant un service persistant.

3. Examiner les journaux du test et confirmer l’absence d’erreur ou de mode inline.
   👉 Explication : Comparer aux événements d’une source approuvée; ne pas générer de trafic vers des tiers.

## 2. Production — Contrôles

Valider point de capture approuvé, horodatage, taux d’événements, pertes et chemin d’escalade.

## 3. Production — Sécurité

- Ne pas conserver les charges utiles au-delà du besoin; protéger les alertes et ne pas automatiser de blocage.

## Validation et retour arrière

- **Validation** : Test de configuration réussi et visibilité passive confirmée avec trafic approuvé.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [Snort IDS passif — documentation officielle](https://www.snort.org/documents)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_Snort_Sauvegarder_Restaurer.md)
