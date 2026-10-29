# 📄 LXC_Alpine_3.19_Services_Installation-Et-Configuration-Nginx.md

- **Environnement** : LXC (Proxmox PXC)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine
- **Catégorie** : Web & Micro-services

## 🎯 Problème précis à résoudre
Installer le serveur HTTP ultraléger Nginx sur un conteneur LXC Alpine Linux, configurer le démarrage OpenRC et sécuriser la configuration Web.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Mise à jour de l'index des paquets et installation rapide :
   `apk update && apk add nginx`
   👉 Explication : Télécharge et installe le binaire Nginx depuis les dépôts Alpine.
2. Lancement du service en mémoire :
   `rc-service nginx start`
   👉 Explication : Démarre le processus Nginx sous le contrôle d'OpenRC.
3. Test de réponse HTTP local :
   `wget -qO- 127.0.0.1`
   👉 Explication : Interroge la réponse HTTP du serveur Web local.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajout de Nginx au niveau d'exécution OpenRC au démarrage :
   `rc-update add nginx default`
   👉 Explication : Configure OpenRC pour démarrer le service Nginx automatiquement au boot du conteneur.
2. Démarrage du service via OpenRC :
   `rc-service nginx restart`
   👉 Explication : Redémarre proprement le démon Nginx.
3. Modification de la page d'accueil par défaut :
   `echo "Welcome to Wiki.js Alpine Lab" > /var/www/localhost/htdocs/index.html`
   👉 Explication : Remplace le fichier HTML d'origine par le contenu applicatif.

---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & En-têtes HTTP)
1. Désactivation de l'en-tête de version Nginx :
   `nginx -V`
   👉 Explication : Vérifie la version installée et configure les directives de masquage dans le fichier de configuration principal.
2. Verrouillage des autorisations sur la racine Web :
   `chown -R nginx:www-data /var/www/localhost/htdocs && chmod -R 750 /var/www/localhost/htdocs`
   👉 Explication : Empêche le compte Nginx d'écrire dans les répertoires Web pour contrer les injections de fichiers malveillants.
3. Activation du pare-feu awall local :
   `awall activate`
   👉 Explication : Active les règles de filtrage réseau d'Alpine pour fermer les flux inutilisés.