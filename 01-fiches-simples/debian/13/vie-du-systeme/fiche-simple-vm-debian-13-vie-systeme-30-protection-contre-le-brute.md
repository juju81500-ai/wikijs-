# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : [[Glossary:VM]] Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

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
   👉 Explication : active la prison [[Glossary:SSH]].

2. Activer et contrôler :
   ```bash
   sudo systemctl enable --now fail2ban
   sudo fail2ban-client status sshd
   ```
   👉 Explication : affiche les [[Glossary:IP]] bannies.

## 2. Production — Contrôles

Ajouter le réseau d'administration à `ignoreip`.

## 3. Production — Sécurité

Surveiller les faux positifs.

## Validation et retour arrière

- **Validation** : `fail2ban-client status sshd` répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Debian 13 Securite Fail2ban](../vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban.md)
- [Vie du système : les 50 étapes, tous OS](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md)
- [Sommaire Debian 13](./sommaire-vie-du-systeme-debian-13.md)
- [Documentation officielle](https://www.debian.org/doc/)
