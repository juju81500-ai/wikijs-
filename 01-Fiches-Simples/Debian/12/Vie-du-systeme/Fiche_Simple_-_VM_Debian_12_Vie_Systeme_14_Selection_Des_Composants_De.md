# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-14`

---

## Problème précis à résoudre

Installer le strict nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. À l'étape « Sélection des logiciels » de l'installateur, cocher seulement **serveur SSH** et **utilitaires usuels du système**. Après installation, contrôler :
   ```bash
   systemctl list-units --type=service --state=running
   apt list --installed 2>/dev/null | wc -l
   ```
   👉 Explication : liste les services actifs et le nombre de paquets installés.

## 2. Production — Contrôles

Ne pas installer d'environnement de bureau sur un serveur.

## 3. Production — Sécurité

Moins de paquets = moins de surface d'attaque.

## Validation et retour arrière

- **Validation** : Seuls SSH et les services de base tournent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
