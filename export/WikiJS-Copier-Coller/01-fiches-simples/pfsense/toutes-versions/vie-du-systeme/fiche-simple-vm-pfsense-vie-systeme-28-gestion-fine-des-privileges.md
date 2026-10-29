# Fiche_Simple_-_VM_pfSense_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Limiter les droits des administrateurs délégués.

## 1. Hors-Production (Lab / Test / POC)

1. Dans System > User Manager > Groups > Assigned Privileges, attribuer des pages précises (ex. `WebCfg - Firewall: Rules`, `WebCfg - Diagnostics: Ping`) au lieu de `All pages`.
   👉 Explication : chaque groupe n'accède qu'aux pages utiles.

2. Si le shell est nécessaire, installer le paquet `sudo` (System > Package Manager) et contrôler :
   ```sh
   sudo -l -U ADMIN01 2>/dev/null
   id ADMIN01
   ```
   👉 Explication : affiche les droits sudo et les groupes du compte.

## 2. Production — Contrôles

Revue des groupes et privilèges à chaque changement d'équipe.

## 3. Production — Sécurité

Aucun compte ne doit avoir `All pages` hors administrateur principal.

## Validation et retour arrière

- **Validation** : Un compte limité ne voit pas les pages non autorisées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)