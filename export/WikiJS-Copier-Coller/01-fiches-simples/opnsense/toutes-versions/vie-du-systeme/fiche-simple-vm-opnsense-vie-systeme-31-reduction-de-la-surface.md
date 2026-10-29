# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Désactiver les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services actifs dans Lobby > Tableau de bord (widget Services) et dans chaque menu Services; désactiver DHCP, Unbound ou SSH s'ils ne servent pas.
   👉 Explication : moins de services signifie moins de vulnérabilités.

2. Lister les ports en écoute :
   ```sh
   sockstat -4 -6 -l
   configctl service list 2>/dev/null | head -30
   ```
   👉 Explication : montre les services à l'écoute et les services gérés par OPNsense.

3. Retirer les plugins non utilisés dans Système > Micrologiciel > Plugins > Désinstaller.
   👉 Explication : supprime des composants inutiles.

## 2. Production — Contrôles

Comparer la liste à la baseline à chaque revue.

## 3. Production — Sécurité

Aucun service d'administration ne doit écouter sur le WAN.

## Validation et retour arrière

- **Validation** : Seuls les ports prévus sont à l'écoute.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)