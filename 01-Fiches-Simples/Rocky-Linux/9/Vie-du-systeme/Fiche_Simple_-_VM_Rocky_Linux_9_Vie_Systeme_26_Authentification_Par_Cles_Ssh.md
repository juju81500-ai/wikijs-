# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-26`

---

## Problème précis à résoudre

Remplacer les mots de passe par des clés.

## 1. Hors-Production (Lab / Test / POC)

1. Générer une clé sur le poste d'administration :
   ```bash
   ssh-keygen -t ed25519 -C 'ADMIN1@poste'
   ```
   👉 Explication : crée une paire de clés; protéger par une phrase secrète.

2. Copier la clé publique vers le serveur (adapter `ADMIN1`, `SRV01.EXEMPLE.LAN`) :
   ```bash
   ssh-copy-id ADMIN1@SRV01.EXEMPLE.LAN
   ```
   👉 Explication : ajoute la clé dans `~/.ssh/authorized_keys`.

3. Contrôler les permissions et le contexte SELinux :
   ```bash
   chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
   restorecon -Rv ~/.ssh
   ```
   👉 Explication : SELinux refuse les clés au mauvais contexte; `restorecon` le corrige.

## 2. Production — Contrôles

Une clé par administrateur, révoquée au départ.

## 3. Production — Sécurité

Ne jamais copier la clé privée sur le serveur.

## Validation et retour arrière

- **Validation** : Connexion par clé réussie sans mot de passe.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
