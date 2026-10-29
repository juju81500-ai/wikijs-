# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Remplacer le mot de passe par une clé.

## 1. Hors-Production (Lab / Test / POC)

1. Sur le poste d'administration, créer la clé protégée par phrase secrète :
   ```bash
   ssh-keygen -t ed25519 -C "admin01@poste"
   ```
   👉 Explication : la phrase secrète est saisie à l'invite.

2. Déposer la clé publique (remplacer utilisateur et hôte) :
   ```bash
   ssh-copy-id -i ~/.ssh/id_ed25519.pub admin01@srv01.exemple.lan
   ```
   👉 Explication : copie la clé publique dans `authorized_keys`.

3. Tester dans une seconde session :
   ```bash
   ssh -o PasswordAuthentication=no admin01@srv01.exemple.lan hostname
   ```
   👉 Explication : doit répondre sans mot de passe.

## 2. Production — Contrôles

Clé nominative par administrateur, révocable.

## 3. Production — Sécurité

Ne jamais copier de clé privée sur un serveur.

## Validation et retour arrière

- **Validation** : Connexion par clé réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)