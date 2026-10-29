# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Appliquer tous les correctifs.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour :
   ```bash
   sudo apt update
   sudo apt full-upgrade -y
   sudo apt autoremove -y
   sudo snap refresh
   ```
   👉 Explication : installe les mises à jour APT, y compris celles qui changent des dépendances, puis celles des snaps.

2. Redémarrer si le noyau a changé :
   ```bash
   [ -f /var/run/reboot-required ] && cat /var/run/reboot-required
   sudo needrestart -r l
   sudo reboot
   ```
   👉 Explication : indique si un redémarrage est requis; `needrestart` liste les services à relancer.

## 2. Production — Contrôles

En production, planifier dans une fenêtre de maintenance avec snapshot.

## 3. Production — Sécurité

Relire la liste des paquets avant `-y` en production.

## Validation et retour arrière

- **Validation** : `apt list --upgradable` est vide.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)