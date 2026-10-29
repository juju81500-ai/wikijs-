# 📄 VM_Debian_13_Services_Installation-Chronyc-NTP.md

- **Environnement** : VM / Serveur (Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Services Réseau / Synchronisation Horaire NTP

## 🎯 Problème précis à résoudre
Installer et configurer le démon chrony sur Debian 13 pour assurer la synchronisation horaire précise et sécuriser le service NTP.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet Chrony :
   `apt-get update && apt-get install -y chrony`
   👉 Explication : Télécharge et installe le démon de synchronisation horaire Chrony.

2. Consultation de l'état de suivi de l'horloge système :
   `chronyc tracking`
   👉 Explication : Affiche les statistiques courantes de dérive et de synchronisation.

3. Affichage des sources NTP amont :
   `chronyc sources -v`
   👉 Explication : Liste les serveurs de temps interrogés.

---

## ⚡ 2. Production — Façon Simplifiée
1. Configurer les sources NTP internes en éditant `/etc/chrony/chrony.conf` après sauvegarde. Remplacer les pools existants seulement après validation de la source d'entreprise.
   👉 Explication : Ne pas utiliser un `sed` qui peut supprimer toutes les lignes `pool` ou ajouter des sources en doublon.

2. N'ajouter `allow 192.0.2.0/24` que si cette machine doit fournir le temps aux clients de ce réseau. Remplacer le réseau d'exemple par la plage réellement autorisée.
   👉 Explication : Sans `allow`, chrony fonctionne comme client ; cette directive ouvre le rôle serveur aux clients correspondants.

3. Appliquer et vérifier avant tout saut d'horloge :
   ```bash
   sudo systemctl restart chrony
   chronyc tracking
   chronyc sources -v
   ```
   👉 Explication : N'utiliser `chronyc makestep` qu'en fenêtre de maintenance, car un saut temporel peut affecter les applications et journaux.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. NTP classique ne chiffre pas les échanges. Si l'architecture impose un transport authentifié, configurer NTS avec des serveurs compatibles selon la documentation chrony et vérifier l'état NTS ; ne pas présenter une directive `server` comme du chiffrement.

2. Restriction d'accès au port de contrôle local :
   `echo "bindcmdaddress 127.0.0.1" >> /etc/chrony/chrony.conf && systemctl restart chrony`
   👉 Explication : Restreint les commandes de gestion à l'interface de bouclage local.

3. Pour un client NTP, autoriser le trafic sortant requis vers les sources approuvées ; ne pas ouvrir UDP/123 en entrée. Pour un serveur de temps, autoriser UDP/123 uniquement depuis ses clients dans le pare-feu persistant géré par l'hôte.