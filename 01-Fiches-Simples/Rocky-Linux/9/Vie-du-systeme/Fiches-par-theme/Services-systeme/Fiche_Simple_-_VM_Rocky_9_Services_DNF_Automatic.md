# 📄 Fiche_Simple_-_VM_Rocky_9_Services_DNF_Automatic.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 (dnf-automatic fourni par BaseOS)
- **Catégorie** : Services / Correctifs de sécurité automatiques
- **Tags** : `[rocky9]`, `[rhel9]`, `[dnf]`, `[dnf-automatic]`, `[systemd]`, `[hardening]`

## 🎯 Problème précis à résoudre
Appliquer automatiquement les correctifs de sécurité sur Rocky Linux 9 via `dnf-automatic`, sans redémarrage non maîtrisé du serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer l'outil :
   ```bash
   sudo dnf install -y dnf-automatic
   ```
   👉 Explication : Installe le binaire `dnf-automatic` et ses deux timers systemd.

2. Lire la configuration par défaut :
   ```bash
   sudo grep -E '^(upgrade_type|apply_updates|reboot|emit_via)' /etc/dnf/automatic.conf
   ```
   👉 Explication : Par défaut, `upgrade_type` vaut `default` et `apply_updates` vaut `no` : les paquets sont vérifiés mais non installés.

---

## ⚡ 2. Production — Façon Simplifiée
1. Limiter les mises à jour aux correctifs de sécurité et autoriser leur application :
   ```bash
   sudo sed -i 's/^upgrade_type = .*/upgrade_type = security/' /etc/dnf/automatic.conf
   sudo sed -i 's/^apply_updates = .*/apply_updates = yes/' /etc/dnf/automatic.conf
   ```
   👉 Explication : `upgrade_type = security` ne traite que les avis de sécurité. Vérifier ensuite le fichier avec la commande de la section 1, car `sed` ne modifie que les lignes déjà présentes.

2. Activer le timer qui installe les correctifs :
   ```bash
   sudo systemctl enable --now dnf-automatic-install.timer
   systemctl list-timers dnf-automatic-install.timer --no-pager
   ```
   👉 Explication : `dnf-automatic-install.timer` télécharge et applique les mises à jour. Le timer `dnf-automatic.timer` se contente de télécharger et d'annoncer.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Garder le redémarrage manuel et contrôler le besoin de redémarrer :
   ```bash
   sudo dnf install -y dnf-utils
   sudo needs-restarting -r
   ```
   👉 Explication : La commande `needs-restarting` provient de `dnf-utils` sur Rocky Linux 9. Son code retour vaut `1` si un redémarrage est nécessaire (noyau ou service mis à jour). Ne pas utiliser `reboot = when-needed` sans fenêtre de maintenance.

2. Consulter les correctifs de sécurité en attente et les traces d'exécution :
   ```bash
   sudo dnf updateinfo list --security
   sudo journalctl -u dnf-automatic-install.service --no-pager -n 50
   ```
   👉 Explication : La première commande liste les avis de sécurité non appliqués. La seconde affiche le journal du dernier passage du timer.

---

## ✅ Contrôle
```bash
systemctl is-active dnf-automatic-install.timer
```
👉 Explication : Doit retourner `active`. Le prochain déclenchement est visible avec `systemctl list-timers`.
