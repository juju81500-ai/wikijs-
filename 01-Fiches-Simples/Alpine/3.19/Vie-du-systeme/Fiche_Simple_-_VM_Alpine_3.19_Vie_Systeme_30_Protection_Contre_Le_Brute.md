# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bannir les sources qui échouent à s'authentifier.

## 1. Hors-Production (Lab / Test / POC)

1. Installer fail2ban :
   ```sh
   doas apk add fail2ban
   ```
   👉 Explication : ajoute le service et les filtres usuels.

2. Configurer la prison SSH (journal BusyBox dans `/var/log/messages`) :
   ```sh
   doas sh -c 'cat > /etc/fail2ban/jail.d/sshd-local.conf <<EOF
   [sshd]
   enabled = true
   logpath = /var/log/messages
   maxretry = 5
   findtime = 10m
   bantime = 1h
   banaction = nftables
   EOF'
   ```
   👉 Explication : 5 échecs en 10 minutes bannissent la source pendant 1 h; `banaction` doit correspondre au pare-feu.

3. Activer et vérifier :
   ```sh
   doas rc-update add fail2ban default
   doas rc-service fail2ban start
   doas fail2ban-client status sshd
   ```
   👉 Explication : la prison `sshd` doit être listée.

## 2. Production — Contrôles

Ajouter le réseau d'administration à `ignoreip`.

## 3. Production — Sécurité

Surveiller les bannissements dans la supervision.

## Validation et retour arrière

- **Validation** : `fail2ban-client status sshd` fonctionne.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite Fail2ban](<../Vie-du-logiciel/Fail2ban/Fiche_Simple_-_LXC_Alpine_3.19_Securite_Fail2ban.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
