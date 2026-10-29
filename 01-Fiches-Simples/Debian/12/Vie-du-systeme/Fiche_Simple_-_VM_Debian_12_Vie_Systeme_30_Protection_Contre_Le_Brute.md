# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bloquer les tentatives répétées.

## 1. Hors-Production (Lab / Test / POC)

1. Installer fail2ban :
   ```bash
   sudo apt install fail2ban
   sudo tee /etc/fail2ban/jail.local >/dev/null <<'EOT'
   [sshd]
   enabled = true
   maxretry = 5
   bantime = 1h
   EOT
   ```
   👉 Explication : active la prison SSH.

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

- [Fiche détaillée : VM Debian 12 Securite Configuration Fail2ban SSH](<../Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Debian_12_Securite_Configuration_Fail2ban_SSH.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
