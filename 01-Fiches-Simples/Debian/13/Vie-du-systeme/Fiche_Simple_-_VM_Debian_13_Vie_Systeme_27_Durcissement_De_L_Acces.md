# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Sécuriser sshd.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier de surcharge :
   ```bash
   sudo tee /etc/ssh/sshd_config.d/20-durcissement.conf >/dev/null <<'EOT'
   PermitRootLogin no
   PasswordAuthentication no
   MaxAuthTries 3
   EOT
   ```
   👉 Explication : interdit root et les mots de passe.

2. Tester puis recharger sans fermer la session actuelle :
   ```bash
   sudo sshd -t
   sudo systemctl reload ssh
   sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication'
   ```
   👉 Explication : contrôle la syntaxe et la configuration effective.

## 2. Production — Contrôles

Limiter par `AllowGroups` et par pare-feu au réseau d'administration.

## 3. Production — Sécurité

Garder une session ouverte jusqu'au test réussi d'une seconde connexion.

## Validation et retour arrière

- **Validation** : `sshd -T` montre `no` pour les deux options.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 13](./Sommaire_-_Vie_du_systeme_Debian_13.md)
- [Documentation officielle](https://www.debian.org/doc/)
