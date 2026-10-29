# 📄 Fiche_Simple_-_Appliance_OPNsense_Supervision_Syslog.md

- **Environnement** : OPNsense sur VM Proxmox VE ou appliance dédiée, serveur syslog distant sur le réseau de gestion
- **OS / Version** : OPNsense (base FreeBSD) - Toutes-versions (libellés de menu à vérifier sur la version déployée)
- **Catégorie** : Supervision / Journaux

---

## 🎯 Problème précis à résoudre
Envoyer les journaux d'OPNsense vers un serveur syslog distant, vérifier leur réception et protéger le transport, pour conserver les événements hors de l'appliance.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ouvrir la configuration des cibles de journalisation :
   `System > Settings > Logging / targets` : Add
   👉 Explication : Ajoute une destination distante aux journaux locaux d'OPNsense.
2. Définir la cible :
   Enabled = coché, Transport = `UDP(4)`, Hostname = `<adresse_ip_syslog>`, Port = `514`, Level = `Informational`
   👉 Explication : UDP est suffisant pour un test ; le transport chiffré est traité en section 3.
3. Envoyer un message de test depuis le shell d'OPNsense (option 8) :
   `logger -n <adresse_ip_syslog> -P 514 "test syslog OPNsense"`
   👉 Explication : Émet un message de test directement vers le serveur, sans attendre un événement réel.
4. Vérifier la réception sur le serveur syslog :
   `tcpdump -ni any udp port 514 -c 5` (sur `<adresse_ip_syslog>`)
   👉 Explication : Confirme que les paquets arrivent au serveur et que le port est ouvert.
5. Contrôler les journaux locaux :
   `Diagnostics > Log Files > General` (à vérifier sur la version déployée)
   👉 Explication : Vérifie que les événements sont toujours écrits localement.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajouter la cible de journalisation distante avec les mêmes paramètres que le test, en limitant les applications envoyées :
   `System > Settings > Logging / targets` : Applications = `<applications_a_envoyer>`
   👉 Explication : Limite le volume aux services utiles (pare-feu, système, authentification).
2. Vérifier le format des messages reçus sur le serveur :
   `tail -n 20 /var/log/<fichier_syslog_opnsense>.log` (sur `<adresse_ip_syslog>`, nom selon la configuration rsyslog)
   👉 Explication : Confirme que les messages sont lisibles et horodatés.
3. Vérifier l'espace disque du serveur syslog :
   `df -h /var/log` (sur `<adresse_ip_syslog>`)
   👉 Explication : Un serveur syslog plein perd les événements.

---

## 🔒 3. Production — Façon Sécurisée
1. Chiffrer le transport avec TLS :
   `System > Settings > Logging / targets` : Transport = `TLS(6)`, Port = `6514`, certificat de l'autorité interne (à vérifier sur la version déployée)
   👉 Explication : Empêche la lecture ou la modification des journaux en transit.
2. Configurer le serveur syslog en réception TLS :
   `<fichier_config_rsyslog>` sur `<adresse_ip_syslog>` (module imtls, certificat et clé du serveur)
   👉 Explication : Le serveur n'accepte que les flux chiffrés et authentifiés par certificat.
3. Restreindre les flux syslog au seul OPNsense :
   `Firewall > Rules > LAN` ou règle de `<reseau_gestion>` : Source = `<adresse_ip_opnsense>`, Destination = `<adresse_ip_syslog>`, port = `6514`
   👉 Explication : Seule l'appliance peut écrire sur le collecteur.
4. Vérifier la réception chiffrée :
   `ss -tlnp | grep 6514` (sur `<adresse_ip_syslog>`)
   👉 Explication : Confirme que le serveur écoute sur le port TLS attendu.