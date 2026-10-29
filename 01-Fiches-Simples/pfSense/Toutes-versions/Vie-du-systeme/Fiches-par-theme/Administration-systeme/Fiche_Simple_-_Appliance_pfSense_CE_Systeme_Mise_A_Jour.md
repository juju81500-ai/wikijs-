# 📄 Fiche_Simple_-_Appliance_pfSense_CE_Systeme_Mise_A_Jour.md

- **Environnement** : pfSense CE sur VM Proxmox VE ou appliance dédiée, fenêtre de maintenance planifiée
- **OS / Version** : pfSense CE 2.x (base FreeBSD) - Toutes-versions
- **Catégorie** : Système / Mises à jour
- **Tags** : `pfsense`, `ce`, `freebsd`, `update`, `pkg`, `maintenance`

---

## 🎯 Problème précis à résoudre
Mettre à jour pfSense CE (système de base et paquets) sans rupture de filtrage, avec un point de retour arrière et une vérification après redémarrage.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever la version installée depuis le shell (option 8) :
   `cat /etc/version`
   👉 Explication : Donne la version courante à comparer avec les notes de version Netgate.
2. Vérifier la branche de mise à jour configurée :
   `System > Update > Update Settings` : Branch = version stable (à vérifier sur la version déployée)
   👉 Explication : Une branche de développement ne doit jamais être utilisée en production.
3. Rechercher les mises à jour disponibles :
   `System > Update > System Update` : lancer la vérification (libellé du bouton à vérifier sur la version déployée)
   👉 Explication : Interroge le dépôt Netgate et indique la version cible.
4. Créer un point de retour arrière côté hyperviseur, après export de configuration :
   `qm snapshot <vmid_pfsense> avant-maj-pfsense` (sur l'hôte Proxmox)
   👉 Explication : Permet un retour arrière complet de la VM si la mise à jour échoue.
5. Lancer la mise à jour depuis la console :
   `Console > option 13 Update from console` (à vérifier sur la version déployée)
   👉 Explication : Met à jour le système via l'outil intégré, puis propose le redémarrage.
6. Vérifier après redémarrage :
   `pkg info pfSense-base`
   👉 Explication : Confirme la version du paquet de base installée et la réussite de la mise à jour.

---

## ⚡ 2. Production — Façon Simplifiée
1. Mettre à jour les paquets installés :
   `System > Package Manager > Installed Packages` : vérifier les mises à jour disponibles et appliquer
   👉 Explication : Les paquets tiers (ex. Suricata, pfBlockerNG) évoluent séparément du système de base.
2. Prévoir la mise à jour dans une fenêtre de maintenance :
   `System > Update` : à planifier manuellement (pfSense CE n'applique pas les mises à jour automatiquement)
   👉 Explication : L'appliance redémarre et coupe le trafic pendant quelques minutes.
3. Contrôler les paquets obsolètes depuis le shell :
   `pkg upgrade -n`
   👉 Explication : Mode simulation (-n) : affiche ce qui serait mis à jour sans rien modifier.

---

## 🔒 3. Production — Façon Sécurisée
1. Tester la version cible sur un clone de lab avant la production :
   `qm clone <vmid_pfsense> <vmid_test> --name pfsense-test-maj --full 1`
   👉 Explication : Valide la mise à jour et les règles sur une copie isolée avant d'intervenir sur la production.
2. Exporter la configuration chiffrée avant intervention (voir la fiche Sauvegarde_Configuration) :
   `Diagnostics > Backup & Restore` : Encrypt this configuration file
   👉 Explication : La configuration reste récupérable si la mise à jour modifie le comportement des règles.
3. Revenir en arrière si la vérification échoue :
   `qm rollback <vmid_pfsense> avant-maj-pfsense` (sur l'hôte Proxmox)
   👉 Explication : Restaure la VM à l'état du snapshot pris avant la mise à jour.
4. Ne pas lancer de mise à jour non contrôlée depuis le shell :
   `pkg upgrade -y` est interdit en production
   👉 Explication : Met à jour sans vérification ni fenêtre de maintenance, et peut désynchroniser l'interface web.
