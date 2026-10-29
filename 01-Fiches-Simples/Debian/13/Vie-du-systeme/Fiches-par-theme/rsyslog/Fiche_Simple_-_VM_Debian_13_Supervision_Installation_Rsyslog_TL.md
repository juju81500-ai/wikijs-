# 📄 VM_Debian_13_Supervision_Installation-Rsyslog-TLS.md

- **Environnement** : VM (Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Supervision & Logs / Rsyslog TLS
- **Tags** : `[debian13]`, `[rsyslog]`, `[syslog]`, `[logs]`, `[tls]`, `[hardening]`

## 🎯 Problème précis à résoudre
Configurer le démon `rsyslog` sous Debian 13 pour expédier tous les journaux système vers un serveur de logs centralisé en utilisant le chiffrement TLS et le protocole TCP fiable.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet Rsyslog :
   `apt-get update && apt-get install -y rsyslog`
   👉 Explication : Installe le service de gestion de journaux rsyslog de base.

2. Envoi d'un message de log de test manuel :
   `logger -p local0.info "Test d'envoi de log manuel"`
   👉 Explication : Génère un événement personnalisé dans les journaux locaux.

3. Vérification de la présence de l'événement :
   `tail -n 5 /var/log/syslog`
   👉 Explication : Valide la prise en compte du message par le démon local.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation du module d'extension GnuTLS pour Rsyslog :
   `apt-get install -y rsyslog-gnutls`
   👉 Explication : Ajoute le support du chiffrement SSL/TLS à Rsyslog.

2. Configuration de l'expéditeur distant dans `/etc/rsyslog.d/50-remote.conf` :
   `echo '*.* action(type="omfwd" target="syslog.lab.local" port="514" protocol="tcp")' > /etc/rsyslog.d/50-remote.conf`
   👉 Explication : Redirige l'intégralité des flux de logs vers le serveur central en TCP.

3. Rechargement du service :
   `systemctl restart rsyslog`
   👉 Explication : Applique la nouvelle politique d'expédition distante.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Configuration du chiffrement TLS d'envoi dans `/etc/rsyslog.d/50-remote-tls.conf` :
   `echo -e 'global(DefaultNetstreamDriver="gtls" DefaultNetstreamDriverCAFile="/etc/ssl/certs/ca-syslog.crt")\n*.* action(type="omfwd" target="syslog.lab.local" port="6514" protocol="tcp" StreamDriver="gtls" StreamDriverMode="1" StreamDriverAuthMode="x509/name")' > /etc/rsyslog.d/50-remote-tls.conf`
   👉 Explication : Chiffre les transferts de journaux en TLS et valide l'identité du serveur récepteur par certificat X.509.

2. Configuration du stockage mémoire local sur disque en cas de coupure réseau (Spooling) :
   `echo '$ActionQueueFileName queueSpool\n$ActionQueueMaxDiskSpace 1g\n$ActionQueueSaveOnShutdown on\n$ActionQueueType LinkedList\n$ActionResumeRetryCount -1' >> /etc/rsyslog.d/50-remote-tls.conf`
   👉 Explication : Conserve les logs sur le disque local en cas d'interruption du réseau pour éviter toute perte d'événements de sécurité.

3. Verrouillage des autorisations sur les répertoires de journaux :
   `chmod 750 /var/log/ && systemctl restart rsyslog`
   👉 Explication : Interdit la lecture des fichiers de journaux système aux comptes non privilégies.