# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Limiter les droits sudo.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une règle (remplacer groupe et commande) :
   ```bash
   sudo visudo -f /etc/sudoers.d/exploitation
   ```
   👉 Explication : exemple : `%exploitation ALL=(root) /usr/bin/systemctl restart nginx`.

2. Contrôler :
   ```bash
   sudo visudo -c
   sudo -l -U admin01
   ```
   👉 Explication : valide la syntaxe et liste les droits.

## 2. Production — Contrôles

Principe du moindre privilège, revue trimestrielle.

## 3. Production — Sécurité

Toujours éditer avec `visudo`.

## Validation et retour arrière

- **Validation** : `visudo -c` : `parsed OK`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 13](./Sommaire_-_Vie_du_systeme_Debian_13.md)
- [Documentation officielle](https://www.debian.org/doc/)
