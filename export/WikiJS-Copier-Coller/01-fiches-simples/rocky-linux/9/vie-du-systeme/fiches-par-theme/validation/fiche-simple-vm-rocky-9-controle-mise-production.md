# 📄 Fiche_Simple_-_VM_Rocky_9_Controle_Mise_Production.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9
- **Catégorie** : Production / Validation / Exploitation

## 🎯 Problème précis à résoudre
Effectuer la réception technique d'un serveur Rocky Linux avant ouverture en production : réseau, mises à jour, accès, SELinux/firewalld, stockage, sauvegarde et supervision.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever versions, paquets et services en échec :
   ```bash
   cat /etc/rocky-release
   sudo dnf check-update
   systemctl --failed
   ```
   👉 Explication : aucun service ne doit être en échec; les mises à jour en attente sont documentées.

2. Vérifier SELinux et firewalld :
   ```bash
   getenforce
   sudo firewall-cmd --get-active-zones
   sudo firewall-cmd --list-all
   ```
   👉 Explication : `Enforcing` attendu; seuls les services nécessaires sont ouverts dans la zone de l'interface.

3. Tester le service depuis un client autorisé :
   ```bash
   nc -zv IP_SERVEUR PORT
   ```
   👉 Explication : remplacer IP et port; puis restaurer une sauvegarde dans une VM isolée.

## ⚡ 2. Production — Façon Simplifiée
1. Système et heure :
   ```bash
   hostnamectl; ip -br a
   dnf repolist
   chronyc tracking | head -3
   ```
   👉 Explication : hostname/IP documentés, dépôts corrects, heure synchronisée.

2. Accès : `getent group wheel` et `sudo grep -E '^(PermitRootLogin|PasswordAuthentication)' /etc/ssh/sshd_config`
   👉 Explication : compte nominatif dans `wheel`, SSH validé; vérifier aussi la console hyperviseur.

3. Sécurité et rôle :
   ```bash
   getenforce
   sudo firewall-cmd --list-all
   systemctl is-enabled SERVICE
   df -h
   ```
   👉 Explication : SELinux `Enforcing`; règles persistantes (`--permanent`); services activés au boot.

4. Continuité : confirmer sauvegarde récente, restauration testée, responsables et retour arrière consignés.
   👉 Explication : sauvegarde sur une cible distincte du serveur.

## 🔒 3. Production — Façon Sécurisée
- Refuser l'ouverture si un refus SELinux est masqué par un passage en permissif ou si le pare-feu est désactivé.
- Vérifier les alertes stockage, capacité, sauvegarde et correctifs après redémarrage.
- Consigner les exceptions et leur échéance; ne pas laisser de règles temporaires ou comptes de test.

## ✅ Validation et retour arrière
- Tester depuis une seconde machine l'accès métier et l'administration; confirmer journaux et supervision.
- Effectuer une restauration complète d'un échantillon ou d'une VM avant la bascule.
- Si un contrôle échoue, arrêter la bascule et revenir à la version/configuration précédente documentée.