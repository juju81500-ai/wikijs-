# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Réduire les risques de sshd.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier de durcissement :
   ```bash
   sudo tee /etc/ssh/sshd_config.d/30-durcissement.conf >/dev/null <<'EOT'
   PasswordAuthentication no
   PermitRootLogin no
   MaxAuthTries 3
   LoginGraceTime 30
   AllowGroups wheel
   EOT
   ```
   👉 Explication : interdit les mots de passe, limite les essais et réserve SSH au groupe wheel.

2. Tester puis recharger :
   ```bash
   sudo sshd -t && sudo systemctl reload sshd
   ```
   👉 Explication : garde la session ouverte pendant le test.

3. Contrôler la politique cryptographique système :
   ```bash
   update-crypto-policies --show
   ```
   👉 Explication : `DEFAULT` convient; `FUTURE` est plus strict (`sudo update-crypto-policies --set FUTURE`).

## 2. Production — Contrôles

Ouvrir une deuxième session avant de recharger pour ne pas se bloquer.

## 3. Production — Sécurité

Ne jamais baisser la politique vers `LEGACY` sans justification.

## Validation et retour arrière

- **Validation** : `sshd -T | grep passwordauthentication` renvoie `no`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)