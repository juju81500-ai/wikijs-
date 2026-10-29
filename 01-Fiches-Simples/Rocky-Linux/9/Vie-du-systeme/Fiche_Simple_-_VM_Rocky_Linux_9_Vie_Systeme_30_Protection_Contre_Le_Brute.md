# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bloquer les tentatives répétées.

## 1. Hors-Production (Lab / Test / POC)

1. Installer fail2ban (dépôt EPEL) :
   ```bash
   sudo dnf install -y epel-release
   sudo dnf install -y fail2ban fail2ban-firewalld
   ```
   👉 Explication : fail2ban vient d'EPEL; le paquet `fail2ban-firewalld` fournit l'action firewalld.

2. Créer la prison SSH :
   ```bash
   sudo tee /etc/fail2ban/jail.d/sshd.local >/dev/null <<'EOT'
   [sshd]
   enabled = true
   maxretry = 5
   bantime = 1h
   EOT
   ```
   👉 Explication : active la prison SSH avec bannissement d'une heure.

3. Activer et contrôler :
   ```bash
   sudo systemctl enable --now fail2ban
   sudo fail2ban-client status sshd
   ```
   👉 Explication : affiche les IP bannies.

## 2. Production — Contrôles

Ajouter le réseau d'administration à `ignoreip`.

## 3. Production — Sécurité

Surveiller les faux positifs.

## Validation et retour arrière

- **Validation** : `fail2ban-client status sshd` répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Securite Fail2ban](<../Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Rocky_9_Securite_Fail2ban.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
