# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-32`

---

## Problème précis à résoudre

Appliquer les correctifs de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier ou activer `unattended-upgrades` (installé par défaut sur Ubuntu Server) :
   ```bash
   sudo apt install unattended-upgrades
   sudo dpkg-reconfigure -plow unattended-upgrades
   apt-config dump | grep -i 'Periodic::Unattended'
   ```
   👉 Explication : active les mises à jour de sécurité automatiques (configuration dans `/etc/apt/apt.conf.d/50unattended-upgrades`).

2. Tester :
   ```bash
   sudo unattended-upgrade --dry-run --debug
   ```
   👉 Explication : simule sans rien installer.

3. Contrôler l'abonnement Ubuntu Pro (gratuit jusqu'à 5 machines pour un usage personnel ou de test; ESM = correctifs étendus pour `universe`) :
   ```bash
   pro status
   # rattachement : sudo pro attach JETON_PRO
   ```
   👉 Explication : `JETON_PRO` provient du portail ubuntu.com/pro : le saisir sans l'inscrire dans un script ni un ticket. `sudo pro enable livepatch` active les correctifs noyau à chaud.

## 2. Production — Contrôles

Redémarrage automatique seulement dans une fenêtre définie.

## 3. Production — Sécurité

Limiter l'automatisation aux dépôts de sécurité; protéger le jeton Pro comme un secret.

## Validation et retour arrière

- **Validation** : `/var/log/unattended-upgrades/` consultable et `pro status` cohérent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 24.04](./Sommaire_-_Vie_du_systeme_Ubuntu_24.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
