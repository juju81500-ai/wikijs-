# Fiche_Simple_-_VM_pfSense_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Pare-feu pfSense CE ([[Glossary:VM]] ou matériel)
- **OS / Version** : pfSense CE; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Désactiver les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services actifs dans Status > Services et désactiver [[Glossary:DHCP]], [[Glossary:DNS]] Resolver ou [[Glossary:SSH]] s'ils ne servent pas.
   👉 Explication : moins de services signifie moins de vulnérabilités.

2. Lister les ports en écoute :
   ```sh
   sockstat -4 -6 -l
   service -e
   ```
   👉 Explication : montre les services à l'écoute et les services démarrés au boot.

3. Retirer les paquets inutiles dans System > Package Manager > Installed Packages.
   👉 Explication : supprime des composants inutiles.

## 2. Production — Contrôles

Comparer la liste à la baseline à chaque revue.

## 3. Production — Sécurité

Aucun service d'administration ne doit écouter sur le [[Glossary:WAN]].

## Validation et retour arrière

- **Validation** : Seuls les ports prévus sont à l'écoute.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md)
- [Sommaire pfSense CE](./sommaire-vie-du-systeme-pfsense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
