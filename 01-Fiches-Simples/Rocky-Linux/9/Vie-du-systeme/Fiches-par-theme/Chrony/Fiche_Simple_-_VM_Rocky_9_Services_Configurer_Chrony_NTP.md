# 📄 Fiche_Simple_-_VM_Rocky_9_Services_Configurer_Chrony_NTP.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd
- **Catégorie** : Services / Synchronisation horaire
- **Tags** : `[rocky9]`, `[rhel9]`, `[chrony]`, `[ntp]`, `[systemd]`, `[time]`

## 🎯 Problème précis à résoudre
Configurer Chrony comme client NTP sur Rocky Linux 9, vérifier la synchronisation avec `chronyc` et n'ouvrir UDP/123 que si le serveur doit répondre à des clients.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer Chrony, activer le service systemd et vérifier son état :
   ```bash
   sudo dnf install chrony
   sudo systemctl enable --now chronyd
   systemctl status chronyd --no-pager
   ```
2. Vérifier la sélection des sources et la dérive :
   ```bash
   chronyc sources -v
   chronyc tracking
   ```
   👉 *Explication : la synchronisation peut prendre du temps après le démarrage; confirmer la connectivité vers les sources autorisées.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder `/etc/chrony.conf`, puis définir les sources NTP internes validées :
   ```text
   server <ntp-interne> iburst
   ```
2. Redémarrer Chrony et vérifier à nouveau :
   ```bash
   sudo systemctl restart chronyd
   chronyc sources -v
   chronyc tracking
   ```
3. Vérifier la configuration appliquée :
   ```bash
   sudo grep -E '^(server|pool|makestep|allow)' /etc/chrony.conf
   ```
   👉 *Explication : Rocky utilise généralement `/etc/chrony.conf`; ne pas remplacer les sources existantes avant d'avoir validé le serveur interne.*

## 🔒 3. Production — Façon Sécurisée
1. Garder Chrony en client si aucun autre équipement ne doit utiliser ce serveur comme source.
2. Ne pas ajouter de directive `allow` ni ouvrir UDP/123 dans firewalld pour un client NTP seul.
3. Ne pas exécuter `chronyc makestep` sans fenêtre de maintenance : un saut d'horloge peut perturber applications, certificats et journaux.

## ✅ Validation et retour arrière
- Confirmer une source sélectionnée, `Leap status: Normal` et une dérive conforme à la politique locale.
- En cas d'échec, restaurer `/etc/chrony.conf`, redémarrer `chronyd` et vérifier `journalctl -u chronyd`.
- Tester l'heure système avec `timedatectl status`.