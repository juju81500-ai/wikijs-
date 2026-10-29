# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Garder l'heure exacte avec chrony.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'installation :
   ```bash
   sudo dnf install -y chrony
   sudo systemctl enable --now chronyd
   ```
   👉 Explication : chrony est le client NTP standard de Rocky.

2. Déclarer le serveur NTP interne (`ntp.exemple.lan` à adapter) :
   ```bash
   echo 'server ntp.exemple.lan iburst' | sudo tee /etc/chrony.d/interne.conf
   sudo systemctl restart chronyd
   ```
   👉 Explication : `iburst` accélère la synchronisation initiale.

3. Contrôler :
   ```bash
   chronyc sources -v
   chronyc tracking
   ```
   👉 Explication : `^*` marque la source choisie; l'écart doit être faible.

## 2. Production — Contrôles

Utiliser deux à quatre sources NTP internes.

## 3. Production — Sécurité

Restreindre `allow` si la machine sert de serveur NTP.

## Validation et retour arrière

- **Validation** : `chronyc tracking` montre `Leap status: Normal`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)