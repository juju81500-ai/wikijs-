---
title: "FreeIPA"
description: "Installer un serveur FreeIPA sur Rocky Linux 9 avec son DNS intégré, créer un utilisateur de test, vérifier l'authentification Kerberos, puis le durcir (politique de mots de passe, sauvegarde, pare-feu restreint) avant de l'utiliser comme annuaire de l'entreprise. Le nom d'hôte doit être un FQDN rés"
published: true
date: 2026-10-29T12:25:12Z
tags: ["[rocky-linux-9]", "[freeipa]", "[ipa]", "[kerberos]", "[ldap]", "[dns]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:25:12Z
dateModified: 2026-10-29T12:25:12Z
---

# 📄 FreeIPA

- **Environnement** : VM (Rocky Linux 9)
- **OS / Version** : Rocky Linux 9.x
- **Version** : FreeIPA 4.10.x (paquets `ipa-server` des dépôts Rocky 9, à vérifier sur la version déployée)
- **Catégorie** : Systèmes, annuaires et services
- **Tags** : `[rocky-linux-9]`, `[freeipa]`, `[ipa]`, `[kerberos]`, `[ldap]`, `[dns]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer un serveur FreeIPA sur Rocky Linux 9 avec son DNS intégré, créer un utilisateur de test, vérifier l'authentification Kerberos, puis le durcir (politique de mots de passe, sauvegarde, pare-feu restreint) avant de l'utiliser comme annuaire de l'entreprise. Le nom d'hôte doit être un FQDN résolu correctement. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification du nom d'hôte et de la résolution :
```bash
sudo hostnamectl set-hostname ipa01.lab.local
hostnamectl status
getent hosts ipa01.lab.local
```
👉 Explication : FreeIPA exige un FQDN. `ipa01.lab.local` doit résoudre vers l'adresse IP du serveur (fichier `/etc/hosts` ou DNS). Sans cela, l'installation échoue.

2. Installation des paquets serveur et DNS :
```bash
sudo dnf install -y ipa-server ipa-server-dns
rpm -q ipa-server ipa-server-dns
```
👉 Explication : Installe le serveur FreeIPA et le module DNS intégré. Les paquets viennent des dépôts Rocky Linux 9 et supposent une VM déjà installée et à jour (`sudo dnf update -y`).

3. Installation et configuration du serveur :
```bash
sudo ipa-server-install --realm=LAB.LOCAL --domain=lab.local --setup-dns --no-forwarders
```
Les mots de passe `admin` et de l'annuaire (Directory Manager) sont saisis à l'invite, ne pas les écrire dans la commande.
👉 Explication : `--realm` est le domaine Kerberos (en majuscules), `--domain` le domaine DNS. `--setup-dns` installe un DNS intégré, `--no-forwarders` évite les redirecteurs externes, adaptés à un lab isolé. Confirmer la configuration proposée puis attendre la fin (plusieurs minutes).

4. Ouverture des services dans firewalld et contrôle de SELinux :
```bash
sudo firewall-cmd --permanent --add-service=freeipa-ldap --add-service=freeipa-ldaps --add-service=dns --add-service=kerberos --add-service=kpasswd --add-service=http --add-service=https
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
getenforce
```
👉 Explication : Ces services firewalld couvrent LDAP, LDAPS, DNS, Kerberos, le changement de mot de passe et l'interface web. `getenforce` doit répondre `Enforcing`. Ne pas désactiver SELinux pour contourner un problème : le corriger avec `ausearch -m AVC -ts recent`.

5. Contrôle des services FreeIPA et création d'un utilisateur de test :
```bash
sudo ipactl status
kinit admin
ipa user-add jdupont --first=Jean --last=Dupont
ipa passwd jdupont
```
👉 Explication : `ipactl status` doit afficher tous les services en `RUNNING`. `kinit admin` obtient un ticket Kerberos administrateur (saisie du mot de passe admin). `ipa user-add` crée `jdupont`, `ipa passwd` définit son mot de passe.

6. Test d'authentification Kerberos :
```bash
kdestroy
kinit jdupont
klist
```
👉 Explication : `kinit jdupont` doit demander le mot de passe et réussir. `klist` affiche le ticket obtenu pour `jdupont@LAB.LOCAL`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarde complète avant toute modification :
```bash
sudo ipa-backup
sudo ls -lh /var/lib/ipa/backup/
```
👉 Explication : `ipa-backup` crée une archive de la configuration et de la base FreeIPA dans `/var/lib/ipa/backup/`. À faire avant chaque changement et à copier hors du serveur.

2. Enrôlement d'un poste client Rocky Linux 9 :
```bash
sudo dnf install -y ipa-client
sudo ipa-client-install --mkhomedir --domain=lab.local --server=ipa01.lab.local --realm=LAB.LOCAL
```
👉 Explication : Installe le client et rattache le poste à FreeIPA (le mot de passe `admin` est demandé). `--mkhomedir` crée le répertoire personnel à la première connexion. Exécuter sur le poste client, pas sur le serveur.

3. Création d'un groupe d'accès et ajout de l'utilisateur :
```bash
ipa group-add grp-comptabilite --desc="Comptabilité"
ipa group-add-member grp-comptabilite --users=jdupont
ipa group-show grp-comptabilite
```
👉 Explication : Les accès sont accordés à des groupes plutôt qu'à des utilisateurs isolés. `group-show` vérifie que `jdupont` est bien membre.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Politique de mots de passe renforcée :
```bash
ipa pwpolicy-show
sudo ipa pwpolicy-mod --minlength=14 --maxfail=5 --lockouttime=900
ipa pwpolicy-show
```
👉 Explication : Impose 14 caractères minimum, verrouille après 5 échecs pendant 900 secondes. Les options exactes sont à vérifier avec `ipa help pwpolicy-mod` sur la version déployée.

2. Restriction du pare-feu à l'administration et au réseau interne :
```bash
sudo firewall-cmd --permanent --new-zone=ipa-interne
sudo firewall-cmd --permanent --zone=ipa-interne --add-source=192.168.10.0/24
sudo firewall-cmd --permanent --zone=ipa-interne --add-service=freeipa-ldap --add-service=freeipa-ldaps --add-service=kerberos --add-service=dns
sudo firewall-cmd --reload
sudo firewall-cmd --zone=ipa-interne --list-all
```
👉 Explication : Crée une zone dédiée n'acceptant que le réseau `192.168.10.0/24` (adapter au réseau réel). Les services sont retirés de la zone par défaut pour éviter une exposition large. Avant d'appliquer, s'assurer que l'accès SSH d'administration reste autorisé (`--add-service=ssh` dans la même zone).

3. Journaux et état de santé de l'annuaire :
```bash
sudo ipa-healthcheck --failures-only
sudo journalctl -u ipa-dnskeysyncd -n 50 --no-pager
```
👉 Explication : `ipa-healthcheck` vérifie la configuration et renvoie les anomalies. Les échecs doivent être remontés à l'administrateur de l'annuaire. Le nom de l'outil est à vérifier sur la version déployée.

4. Sauvegarde planifiée hors serveur :
```bash
sudo ipa-backup --data --online
sudo ls -lh /var/lib/ipa/backup/
```
👉 Explication : `--data` sauvegarde uniquement les données, `--online` évite d'arrêter les services. Copier ensuite l'archive vers un stockage distant, avec la procédure de sauvegarde du pack. La restauration se fait par `ipa-restore`, à tester régulièrement.

5. Point à vérifier : les réplicas (`ipa-replica-install`) et la migration de versions doivent faire l'objet d'une procédure dédiée, car leurs commandes varient fortement selon la version FreeIPA déployée.

---