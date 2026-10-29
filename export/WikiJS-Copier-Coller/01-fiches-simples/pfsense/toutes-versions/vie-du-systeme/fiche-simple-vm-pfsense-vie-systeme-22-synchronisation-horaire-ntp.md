# Fiche_Simple_-_VM_pfSense_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Garantir une heure fiable sur le pare-feu et le réseau.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Services > NTP > Settings : ajouter les serveurs (ex. `fr.pool.ntp.org`), sélectionner l'interface LAN pour servir l'heure, Save.
   👉 Explication : le pare-feu synchronise son horloge et peut la fournir aux clients.

2. Contrôler la synchronisation : Status > NTP, ou en shell :
   ```sh
   ntpq -p
   ```
   👉 Explication : un serveur sélectionné (`*`) avec un décalage faible prouve la synchronisation.

## 2. Production — Contrôles

Utiliser au moins trois sources, dont une interne si possible.

## 3. Production — Sécurité

Autoriser le NTP sortant (UDP 123) seulement vers les serveurs choisis.

## Validation et retour arrière

- **Validation** : Une source est sélectionnée et le décalage est faible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)