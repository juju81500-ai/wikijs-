# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Sécuriser le compte `root`, créé à l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Changer immédiatement le mot de passe par défaut (`opnsense`) dans Système > Accès > Utilisateurs > root > Modifier > Mot de passe.
   👉 Explication : un mot de passe par défaut connu de tous est la première cause de compromission.

2. Ou en console (option 3 « Reset the root password »), saisir le nouveau mot de passe deux fois.
   👉 Explication : méthode de secours si l'accès web est perdu.

3. Contrôler les comptes à privilèges en shell :
   ```sh
   pw usershow root
   awk -F: '$3==0{print $1}' /etc/passwd
   ```
   👉 Explication : liste les comptes d'UID 0; seul `root` doit apparaître.

## 2. Production — Contrôles

Stocker le mot de passe root dans un coffre-fort et le réserver aux urgences.

## 3. Production — Sécurité

Mot de passe long et unique; activer l'authentification à deux facteurs pour les comptes web (Système > Accès > Utilisateurs > Authentification à deux facteurs).

## Validation et retour arrière

- **Validation** : Seul `root` a l'UID 0 et le mot de passe par défaut est refusé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
