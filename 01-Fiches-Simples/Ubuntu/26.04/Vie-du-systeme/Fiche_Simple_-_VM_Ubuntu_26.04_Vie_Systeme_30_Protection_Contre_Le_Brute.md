# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bloquer les tentatives répétées.

## 1. Hors-Production (Lab / Test / POC)

1. Installer fail2ban (lecture du journal systemd) :
   ```bash
   sudo apt install fail2ban
   sudo tee /etc/fail2ban/jail.local >/dev/null <<'EOT'
   [sshd]
   enabled = true
   backend = systemd
   maxretry = 5
   bantime = 1h
   EOT
   ```
   👉 Explication : active la prison SSH; `backend = systemd` évite de dépendre de `/var/log/auth.log`.

2. Activer et contrôler :
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

- [Fiche détaillée : VM Ubuntu 26.04 Securite Fail2ban](<../Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Ubuntu_26.04_Securite_Fail2ban.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
