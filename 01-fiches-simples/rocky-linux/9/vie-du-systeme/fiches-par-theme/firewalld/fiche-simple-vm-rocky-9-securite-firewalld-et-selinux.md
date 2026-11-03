# 📄 VM_Rocky_9_Securite_Configuration-Firewalld-Et-SELinux.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Rocky Linux 9 / RHEL 9 - Famille RedHat
- **Catégorie** : Sécurité & Hardening OS
- **Tags** : `[rocky9]`, `[rhel-family]`, `[firewalld]`, `[selinux]`, `[hardening]`

## 🎯 Problème précis à résoudre
Configurer et verrouiller le pare-feu local `firewalld` et ajuster les politiques SELinux en mode applicatif strict sans désactiver le contrôle d'accès obligatoire.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever l'état SELinux et les zones/firewall actifs :
   ```bash
   getenforce
   sudo ausearch -m AVC -ts recent
   sudo firewall-cmd --get-active-zones
   sudo firewall-cmd --get-default-zone
   ```
   👉 Explication : Chercher d'abord les refus AVC et la zone de l'interface concernée. Ne pas désactiver SELinux pour masquer un problème de contexte.
2. Tester un port ponctuellement uniquement en lab et depuis une console accessible :
   `sudo firewall-cmd --zone=public --add-port=8080/tcp`
   👉 Explication : Cette règle est temporaire ; remplacer `public` par la zone réelle et supprimer le test après validation.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier la configuration SELinux et appliquer les contextes attendus :
   ```bash
   getenforce
   sudo restorecon -Rv /var/www/html
   ```
   👉 Explication : Garder SELinux en `Enforcing`. Adapter le chemin au service et examiner les refus AVC avant de modifier une politique.
2. Identifier la zone de l'interface d'administration et les services réellement nécessaires :
   ```bash
   sudo firewall-cmd --get-active-zones
   sudo firewall-cmd --zone=public --list-all
   ```
3. Ouvrir uniquement les services validés, dans la zone réelle, puis vérifier avant/après rechargement :
   ```bash
   sudo firewall-cmd --permanent --zone=public --add-service=ssh
   sudo firewall-cmd --permanent --zone=public --add-service=https
   sudo firewall-cmd --check-config
   sudo firewall-cmd --reload
   sudo firewall-cmd --zone=public --list-all
   ```
   👉 Explication : Remplacer `public` selon l'interface. Ne pas ouvrir HTTP si le service n'en a pas besoin.

---

## 🔒 3. Production — Façon Sécurisée
1. Avant de restreindre l'administration, conserver un accès console. Utiliser une règle de source limitée dans la zone réellement attachée à l'interface, pas `trusted` :
   ```bash
   sudo firewall-cmd --permanent --zone=public --add-rich-rule='rule family="ipv4" source address="192.0.2.0/24" service name="ssh" accept'
   sudo firewall-cmd --check-config
   sudo firewall-cmd --reload
   sudo firewall-cmd --permanent --zone=public --remove-service=ssh
   sudo firewall-cmd --reload
   ```
   `192.0.2.0/24` est un exemple documentaire. Vérifier une seconde connexion via la source autorisée avant de retirer l'ouverture SSH générale ; remplacer `public` par la zone réelle.
2. Ne pas définir la zone par défaut à `drop` sans cartographier toutes les interfaces, services et règles runtime. Les services non explicitement prévus peuvent être coupés.
3. Pour un chemin Web personnalisé, déclarer le type SELinux persistant puis restaurer le contexte :
   ```bash
   sudo semanage fcontext -a -t httpd_sys_content_t '/custom/web(/.*)?'
   sudo restorecon -Rv /custom/web
   ```
   Vérifier d'abord `semanage fcontext -l` pour éviter les doublons. Ne pas utiliser `chcon` comme solution permanente.
4. Si un refus subsiste, examiner `ausearch -m AVC -ts recent` et corriger le contexte ou la règle minimale nécessaire. Ne pas laisser SELinux en mode permissif en production.