# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Régler le clavier pour saisir correctement les mots de passe.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'assistant du clavier (disposition `fr`, variante `fr`) :
   ```sh
   setup-keymap fr fr
   ```
   👉 Explication : installe la table de touches et la rend permanente; sans arguments, l'assistant propose la liste interactive.

2. Lister les dispositions disponibles :
   ```sh
   ls /usr/share/bkeymaps/ | head -30
   ```
   👉 Explication : chaque sous-dossier est une disposition (`fr`, `be`, `us`, etc.).

3. Contrôler que le service est lancé au démarrage :
   ```sh
   rc-status boot | grep -i key
   ```
   👉 Explication : le service de chargement du clavier doit figurer dans le niveau `boot`.

## 2. Production — Contrôles

Documenter la disposition retenue pour la console et pour SSH (le clavier distant est celui du poste d'administration).

## 3. Production — Sécurité

Choisir un mot de passe qui ne dépend pas d'une disposition particulière avant le changement de clavier.

## Validation et retour arrière

- **Validation** : Les touches AZERTY correspondent aux caractères tapés (tester `a`, `m`, `1`, `;`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
