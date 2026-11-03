# 📄 VM_Debian_13_Services_Installation-DNS-BIND9.md

- **Environnement** : VM (Debian 13 Trixie)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Services Réseau / DNS (BIND9)
- **Tags** : `[debian13]`, `[bind9]`, `[dns]`, `[chroot]`, `[hardening]`, `[secnumcloud]`

## 🎯 Problème précis à résoudre
Installer et sécuriser BIND sur Debian 13 pour une zone DNS autoritaire, contrôler les transferts et n'activer la récursion que dans une architecture séparée pour les clients internes.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide des paquets BIND9 et des utilitaires réseau :
   `apt-get update && apt-get install -y bind9 bind9utils dnsutils`
   👉 Explication : Télécharge le serveur DNS BIND9, les utilitaires de gestion `named-checkconf` et l'outil de requête `dig`.

2. Test de la zone autoritative après l'avoir configurée :
   `dig @127.0.0.1 lab.example.test SOA +norecurse`
   👉 Explication : Vérifie la réponse SOA de la zone locale sans demander de récursion. Une installation autoritative seule ne doit pas servir de résolveur Internet.

3. Vérification de l'état du service nommé :
   `systemctl status bind9`
   👉 Explication : Contrôle le processus BIND9 en cours d'exécution.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'une zone de résolution directe autoritaire dans `/etc/bind/named.conf.local` :
      zone "lab.example.test" {
      type primary;
         file "/etc/bind/db.lab.example.test";
       allow-transfer { none; };
   };
   👉 Explication : Déclare la zone `lab.example.test` comme zone primaire et interdit son transfert vers d'autres serveurs.

2. Fichier de zone de données `/etc/bind/db.lab.example.test` :
   $TTL 86400
   @ IN SOA ns1.lab.example.test. hostmaster.lab.example.test. ( 2026102701 3600 1800 604800 86400 )
   @ IN NS ns1.lab.example.test.
   ns1 IN A 192.0.2.53
   srv1 IN A 192.0.2.20
   👉 Explication : Configure les enregistrements SOA, NS et A d'un exemple réservé à la documentation.

3. Validation de la configuration et de la zone avant rechargement :
   `sudo named-checkconf -z /etc/bind/named.conf && sudo named-checkzone lab.example.test /etc/bind/db.lab.example.test`
   👉 Explication : Valide la configuration et la zone; ne recharger qu'après réussite des deux contrôles.

4. Appliquer le changement et relire le résultat :
   `sudo rndc reload && dig @127.0.0.1 lab.example.test SOA +norecurse`
   👉 Explication : Recharge les zones et confirme que BIND répond pour la zone autoritative.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Utiliser les protections du paquet Debian, notamment l'utilisateur `bind` et le profil AppArmor. Ne pas ajouter un chroot manuel en modifiant `/etc/default/named` sans procédure spécifique au paquet et migration des fichiers nécessaires.
   👉 Explication : Le paquet Debian gère déjà l'isolation prévue ; une option `-t` ajoutée seule peut empêcher le service de démarrer.

2. Hardening du fichier `/etc/bind/named.conf.options` :
   options {
       directory "/var/cache/bind";
       version "Non disponible";
      recursion no;
      allow-query { 127.0.0.1; 192.0.2.0/24; };
       allow-transfer { none; };
       dnssec-validation auto;
   };
   👉 Explication : Cet exemple est autoritatif uniquement. Pour un résolveur récursif, définir un service séparé et limiter récursion/queries aux clients internes ; ne jamais proposer la récursion à Internet.

3. Vérifier les permissions fournies par le paquet au lieu de changer récursivement tout `/etc/bind` :
   `sudo named-checkconf && sudo systemctl reload bind9`
   👉 Explication : Une modification récursive de propriétaire peut rendre les fichiers de configuration modifiables par le service.

4. Autoriser UDP et TCP 53 uniquement depuis les clients prévus dans le pare-feu persistant. Pour les transferts de zone, autoriser uniquement les secondaires déclarés et utiliser TSIG ; ne pas utiliser une règle nftables ajoutée en mémoire.