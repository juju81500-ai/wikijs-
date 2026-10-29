# 📄 VM_Debian_12_Securite_AppArmor.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sécurité & Contrôle d'accès / Contrôle d'accès obligatoire (MAC)
- **Tags** : `[debian12]`, `[debian-family]`, `[apparmor]`, `[mac]`, `[profils]`, `[enforce]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer AppArmor sur Debian 12, charger les profils fournis par la distribution, passer les services exposés en mode `enforce` après une phase d'observation en `complain`, et analyser les refus éventuels.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation d'AppArmor et des profils :
   `sudo apt-get update && sudo apt-get install -y apparmor apparmor-utils apparmor-profiles apparmor-profiles-extra`
   👉 Explication : Installe le service, les outils `aa-*` et les profils officiels Debian.
2. Vérification de l'activation du module noyau :
   `cat /sys/module/apparmor/parameters/enabled`
   👉 Explication : Doit renvoyer `Y` ; une valeur `N` indique qu'AppArmor n'est pas activé au démarrage du noyau.
3. Consultation des profils chargés :
   `sudo aa-status`
   👉 Explication : Affiche le nombre de profils en mode `enforce` et `complain`, ainsi que les processus protégés.

---

## ⚡ 2. Production — Façon Simplifiée
1. Passage d'un profil en mode observation :
   `sudo aa-complain /etc/apparmor.d/<nom_du_profil>`
   👉 Explication : Le profil journalise les accès refusés sans les bloquer. Exemple de nom : `usr.sbin.<service>`.
2. Passage du profil en mode bloquant après validation :
   `sudo aa-enforce /etc/apparmor.d/<nom_du_profil>`
   👉 Explication : Les accès non autorisés par le profil sont désormais refusés et journalisés.

---

## 🔒 3. Production — Façon Sécurisée (Enforcement & Audit)
1. Contrôle du service AppArmor au démarrage :
   `sudo systemctl status apparmor --no-pager`
   👉 Explication : Confirme que le service est chargé et que les profils sont appliqués à chaque boot.
2. Recensement des refus journalisés :
   `sudo journalctl -k | grep -i 'apparmor="DENIED"'`
   👉 Explication : Liste les accès refusés par un profil ; chaque entrée doit être analysée avant d'élargir la règle.
3. Vérification du nombre de profils en enforce :
   `sudo aa-status | head -n 10`
   👉 Explication : Les premières lignes indiquent le nombre de profils en `enforce`, à comparer avec la liste des services critiques de la fiche serveur.
