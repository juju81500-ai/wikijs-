# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Configurer le clavier de la console.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les dispositions françaises :
   ```bash
   localectl list-keymaps | grep -i '^fr'
   ```
   👉 Explication : repère `fr` ou `fr-latin9`.

2. Appliquer la disposition :
   ```bash
   sudo localectl set-keymap fr
   ```
   👉 Explication : écrit `/etc/vconsole.conf` (KEYMAP=fr).

3. Contrôler :
   ```bash
   localectl status
   ```
   👉 Explication : affiche `VC Keymap: fr`.

## 2. Production — Contrôles

Documenter la disposition utilisée en salle serveur.

## 3. Production — Sécurité

Un mauvais clavier fausse la saisie des mots de passe; tester avant de valider.

## Validation et retour arrière

- **Validation** : Les caractères saisis en console correspondent aux touches.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
