---
title: "Postfix"
description: "Installer le serveur SMTP Postfix sur Debian 12, vérifier sur ce même serveur qu'il accepte et remet un message de test, puis le durcir (chiffrement TLS obligatoire, relais restreint aux réseaux autorisés) avant de l'exposer à l'entreprise. Les tests ne se font que sur votre propre serveur."
published: true
date: 2026-10-29T12:24:28Z
tags: ["[debian-12]", "[postfix]", "[smtp]", "[messagerie]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:24:28Z
dateModified: 2026-10-29T12:24:28Z
---

# 📄 Postfix

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Postfix 3.7.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Messagerie et collaboratif
- **Tags** : `[debian-12]`, `[postfix]`, `[smtp]`, `[messagerie]`, `[hardening]`

## 🎯 Objectif
Installer le serveur SMTP Postfix sur Debian 12, vérifier sur ce même serveur qu'il accepte et remet un message de test, puis le durcir (chiffrement TLS obligatoire, relais restreint aux réseaux autorisés) avant de l'exposer à l'entreprise. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Postfix et des outils de test :
```bash
sudo apt update
sudo apt install -y postfix mailutils
```
👉 Explication : Installe l'agent de transfert Postfix et la commande `mail`, utilisée pour envoyer un message de test. Lors de l'assistant debconf, choisir « Site Internet » et renseigner le nom de domaine du lab.

2. Vérification de la configuration et de la version :
```bash
postconf mail_version
sudo postfix check
sudo postconf -n
```
👉 Explication : `postconf mail_version` affiche la version. `postfix check` contrôle les fichiers et permissions sans relancer le service. `postconf -n` liste uniquement les paramètres modifiés par rapport aux valeurs par défaut.

3. Démarrage du service et contrôle de son état :
```bash
sudo systemctl enable postfix
sudo systemctl start postfix
systemctl status postfix --no-pager
```
👉 Explication : Active le démarrage automatique, lance le service puis affiche son état. La ligne `Active: active (exited)` ou `active (running)` est attendue.

4. Envoi d'un message de test en local :
```bash
echo "Message de test Postfix" | mail -s "Test Postfix lab" utilisateur_test@localhost
sudo tail -n 20 /var/log/mail.log
```
👉 Explication : Dépose un message dans la file Postfix pour le compte local `utilisateur_test`. Le journal doit montrer `status=sent` ou `status=deferred` avec la raison. La boîte locale se consulte dans `/var/mail/utilisateur_test`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Déclaration du domaine et des réseaux autorisés à relayer :
```bash
sudo postconf -e "myhostname = <nom_serveur_smtp>"
sudo postconf -e "mydomain = <domaine_entreprise>"
sudo postconf -e "mynetworks = 127.0.0.0/8 <reseau_interne_cidr>"
```
👉 Explication : `<nom_serveur_smtp>` est le nom FQDN du serveur, `<domaine_entreprise>` le domaine des adresses mail, `<reseau_interne_cidr>` le réseau interne (par exemple `192.168.10.0/24`) autorisé à envoyer sans authentification. Ne jamais mettre `0.0.0.0/0` dans `mynetworks`.

2. Contrôle de la syntaxe puis rechargement :
```bash
sudo postfix check
sudo systemctl reload postfix
sudo postconf -n | grep -E "myhostname|mydomain|mynetworks"
```
👉 Explication : Vérifie la configuration avant de recharger le service, puis confirme les valeurs appliquées.

3. Ouverture du pare-feu pour SMTP uniquement :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 25/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Ouvre SSH seulement pour `<adresse_ip_admin>` avant d'activer le pare-feu, pour ne pas se couper l'accès. Le port 25 TCP reçoit le courrier entrant entre serveurs. Les ports de soumission (587) et IMAPS (993) relèvent de la fiche Dovecot.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activation du chiffrement TLS pour les échanges entrants :
```bash
sudo postconf -e "smtpd_tls_security_level = may"
sudo postconf -e "smtpd_tls_cert_file = /etc/ssl/certs/<certificat_smtp>.crt"
sudo postconf -e "smtpd_tls_key_file = /etc/ssl/private/<certificat_smtp>.key"
sudo postconf -e "smtp_tls_security_level = may"
sudo postfix check
sudo systemctl reload postfix
```
👉 Explication : `may` active STARTTLS sans l'imposer aux serveurs distants ; pour un relais strictement chiffré, passer `smtpd_tls_security_level` à `encrypt` une fois les clients compatibles. `<certificat_smtp>` est le nom du certificat émis pour le serveur, à vérifier sur la version déployée.

2. Restriction du relais aux clients authentifiés et aux réseaux internes :
```bash
sudo postconf -e "smtpd_relay_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination"
sudo postconf -e "smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination"
sudo postfix check
sudo systemctl reload postfix
```
👉 Explication : Empêche le serveur d'être utilisé comme relais ouvert. Seuls les réseaux de `mynetworks` et les utilisateurs authentifiés peuvent relayer. Le paramètre `reject_unauth_destination` refuse tout relais pour un destinataire externe non autorisé.

3. Contrôle des journaux et des rejets :
```bash
sudo grep -E "reject|warning|fatal" /var/log/mail.log | tail -n 50
sudo postqueue -p
```
👉 Explication : Liste les rejets, avertissements et erreurs fatales récents, puis le contenu de la file d'attente. Une file qui grossit sans raison ou de nombreuses connexions refusées sont à remonter au responsable sécurité.

4. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/postfix-conf-$(date +%F).tgz /etc/postfix
sudo ls -l /root/postfix-conf-*.tgz
```
👉 Explication : Crée une archive datée de toute la configuration Postfix, à stocker hors du serveur et à protéger en lecture.

---