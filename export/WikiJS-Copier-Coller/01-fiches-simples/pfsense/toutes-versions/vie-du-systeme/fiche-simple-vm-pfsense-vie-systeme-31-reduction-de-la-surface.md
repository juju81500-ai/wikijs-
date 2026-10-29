# Fiche_Simple_-_VM_pfSense_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Désactiver les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services actifs dans Status > Services et désactiver DHCP, DNS Resolver ou SSH s'ils ne servent pas.
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

Aucun service d'administration ne doit écouter sur le WAN.

## Validation et retour arrière

- **Validation** : Seuls les ports prévus sont à l'écoute.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)