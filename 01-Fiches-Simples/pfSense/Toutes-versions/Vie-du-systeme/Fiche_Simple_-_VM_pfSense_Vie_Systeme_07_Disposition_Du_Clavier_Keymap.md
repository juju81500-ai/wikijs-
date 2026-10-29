# Fiche_Simple_-_VM_pfSense_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Obtenir le bon clavier à la console.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur, écran « Keymap Selection » : choisir `French` (ou `Continue with default keymap`).
   👉 Explication : le choix s'applique à la console physique et à la console VM.

2. Changer le clavier après installation en shell :
   ```sh
   kbdcontrol -l fr.acc.kbd
   ```
   👉 Explication : applique le clavier français pour la session en cours.

## 2. Production — Contrôles

Valider la saisie d'un mot de passe avec caractères spéciaux avant de le fixer.

## 3. Production — Sécurité

Utiliser des mots de passe saisissables sur tous les claviers utilisés.

## Validation et retour arrière

- **Validation** : Les touches `a`, `z`, `-`, `/` correspondent au clavier physique.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
