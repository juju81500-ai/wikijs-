# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garantir une heure fiable sur le pare-feu et le réseau.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Services > Service de temps réseau > Général : ajouter les serveurs (ex. `fr.pool.ntp.org`), activer l'interface LAN pour servir l'heure, Enregistrer.
   👉 Explication : le pare-feu synchronise son horloge et peut la fournir aux clients.

2. Contrôler la synchronisation en shell :
   ```sh
   ntpq -p
   chronyc sources 2>/dev/null
   ```
   👉 Explication : `ntpq -p` (ou `chronyc sources` selon la version) montre un serveur sélectionné (`*`) avec un décalage faible.

## 2. Production — Contrôles

Utiliser au moins trois sources, dont une interne si possible.

## 3. Production — Sécurité

Autoriser le NTP sortant (UDP 123) seulement vers les serveurs choisis.

## Validation et retour arrière

- **Validation** : Une source est sélectionnée et le décalage est inférieur à quelques millisecondes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
