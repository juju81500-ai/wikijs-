---
title: "Déployer un contrôleur de domaine Samba AD DC sur Debian 13"
description: "Fiche simple : [cadrer les limites et prérequis](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Samba-AD-DC/FicheSimple-VMDebian13SambaADDCPrerequis.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "samba", "active-directory", "domain-controller", "dns", "lab"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer un contrôleur de domaine Samba AD DC sur Debian 13

- **OS / Version** : Debian 13 Trixie, Samba 4.22 depuis les dépôts Debian
- **Type de fiche** : Installation/Déploiement
- **Rôle** : Contrôleur de domaine Active Directory Samba, DNS interne SAMBA_INTERNAL
- **Tags** : `debian13`, `samba`, `active-directory`, `domain-controller`, `dns`, `lab`

## 1. Limites et prérequis

Fiche simple : [cadrer les limites et prérequis](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-prerequis).

Cette procédure est un parcours de laboratoire pour un domaine neuf. Elle n'est ni une procédure de migration d'une forêt Microsoft existante, ni une garantie de compatibilité complète avec tous les rôles et GPO Microsoft. Vérifier la matrice de compatibilité Samba et valider les applications avant toute adoption en production.

Pour une mise en service réelle, prévoir au minimum plusieurs DC dans des domaines de panne distincts, sauvegardes testées, supervision, NTP, procédures de reprise, revue de sécurité et validation de chaque fonctionnalité requise. Une seule VM DC ci-dessous sert uniquement à l'apprentissage.

Les noms et adresses `AD.LAB.TEST`, `ADLAB` et `192.0.2.10` sont des exemples réservés à la documentation. Choisir un domaine DNS contrôlé par l'organisation, un nom NetBIOS et une adresse statique avant le provisionnement. Une fois la forêt créée, les renommer n'est pas une opération courante.

## 2. Préparer Debian

Fiche simple : [préparer Debian](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-preparer-debian).

Configurer l'adresse statique, le nom court `dc1`, l'heure et une résolution locale cohérente. Exemple minimal de `/etc/hosts` :

```text
127.0.0.1 localhost
192.0.2.10 dc1.ad.lab.test dc1
```

Ne pas associer le FQDN du DC à `127.0.1.1`. Vérifier que le système utilise une source NTP fiable et que l'adresse statique est celle prévue pour le domaine :

```bash
hostnamectl
timedatectl status
ip -br address
```

Installer le paquet du rôle AD DC et ses outils d'administration :

```bash
sudo apt update
apt-cache policy samba-ad-dc
sudo apt install samba-ad-dc samba-common-bin krb5-user dnsutils smbclient acl attr
```

Vérifier la version Debian installée et suivre le manuel local correspondant; Debian 13 peut recevoir des mises à jour de sécurité dans la série 4.22. Ne pas ajouter de dépôt tiers Samba au hasard.

Si des services Samba autonomes sont déjà installés, ne pas les laisser concurrencer le daemon AD DC. Examiner les unités disponibles et arrêter/désactiver les unités `smbd`, `nmbd` ou `winbind` séparées lorsqu'elles existent; ne pas désactiver le service `samba-ad-dc`.

## 3. Provisionner un domaine de laboratoire

Fiche simple : [provisionner le domaine de laboratoire](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-provisionner).

Le provisionnement crée la base AD, le partage SYSVOL, le domaine Kerberos et la configuration DNS. Il s'agit d'une opération d'initialisation, pas d'une commande à relancer sur un DC déjà provisionné.

```bash
sudo samba-tool domain provision \
  --server-role=dc \
  --use-rfc2307 \
  --realm=AD.LAB.TEST \
  --domain=ADLAB \
  --dns-backend=SAMBA_INTERNAL
```

Saisir un mot de passe Administrateur fort et unique à l'invite. Ne pas fournir le secret en argument, dans un script, dans l'historique du shell ou dans Wiki.js.

Conserver le `smb.conf` généré par Samba; ne pas le remplacer par une configuration de serveur de fichiers classique. Vérifier sa cohérence :

```bash
sudo testparm -s
sudo test -s /var/lib/samba/private/krb5.conf
```

Examiner `/var/lib/samba/private/krb5.conf` et s'assurer que le client Kerberos système utilise la configuration du domaine avant les tests `kinit`. Si `/etc/krb5.conf` contient déjà une configuration locale, la sauvegarder et fusionner prudemment les paramètres au lieu de l'écraser sans examen.

## 4. Configurer le résolveur et démarrer

Fiche simple : [configurer le résolveur et démarrer](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-resolveur-demarrage).

Le contrôleur de domaine doit résoudre le domaine via son propre DNS AD. Configurer la pile réseau Debian pour utiliser `192.0.2.10` comme DNS primaire sur le DC et sur les clients du lab. Ne pas configurer un DNS public comme résolveur primaire du DC; les requêtes externes doivent être relayées par le service DNS Samba vers un résolveur amont approuvé.

Après avoir vérifié l'unité fournie par le paquet :

```bash
systemctl cat samba-ad-dc.service
sudo systemctl enable --now samba-ad-dc.service
sudo systemctl --no-pager status samba-ad-dc.service
sudo journalctl -u samba-ad-dc.service -n 80 --no-pager
```

Une fois le service démarré, configurer au besoin `dns forwarder` dans la section `[global]` du `smb.conf` généré avec l'adresse réelle du résolveur amont autorisé. Puis valider avec `testparm -s` et redémarrer le service dans une fenêtre de maintenance.

## 5. Vérifier AD, Kerberos et DNS

Fiche simple : [vérifier AD, Kerberos et DNS](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-verifier-ad).

Vérifier les enregistrements de découverte de service attendus :

```bash
host -t A dc1.ad.lab.test 192.0.2.10
host -t SRV _ldap._tcp.ad.lab.test 192.0.2.10
host -t SRV _kerberos._udp.ad.lab.test 192.0.2.10
```

Tester l'authentification Kerberos avec une saisie interactive :

```bash
kinit Administrator@AD.LAB.TEST
klist
```

Tester les commandes d'administration et les ACL SYSVOL :

```bash
sudo samba-tool domain info 127.0.0.1
sudo samba-tool user list
sudo samba-tool ntacl sysvolcheck
sudo samba-tool dbcheck
```

`dbcheck` est un contrôle diagnostique; ne pas ajouter d'option de réparation sans sauvegarde, analyse des résultats et procédure Samba appropriée. Pour un domaine multi-DC, vérifier aussi `samba-tool drs showrepl` sur chaque contrôleur. Vérifier ensuite une jonction d'un poste de test, l'application d'une GPO témoin et l'accès aux partages SYSVOL/NETLOGON.

## 6. Réseau et sécurité

Fiche simple : [ouvrir uniquement les flux AD nécessaires](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-reseau-securite).

Autoriser les flux AD uniquement entre les clients/serveurs approuvés et les contrôleurs de domaine. Le besoin comprend notamment DNS TCP/UDP 53, Kerberos TCP/UDP 88, NTP UDP 123, RPC endpoint mapper TCP 135, LDAP TCP/UDP 389, SMB TCP 445, changement de mot de passe Kerberos TCP/UDP 464 et RPC dynamique TCP (plage définie par la politique système). NetBIOS 137-139 et Global Catalog 3268/3269 ne sont à ouvrir que si le scénario les requiert.

Ne jamais publier LDAP, SMB, RPC, Kerberos ou l'interface d'administration sur Internet. Restreindre SSH et l'accès console, activer les mises à jour Debian, protéger les bases et secrets, surveiller les échecs Kerberos et les changements AD. Évaluer les algorithmes hérités et les besoins NTLM à partir des clients réels; ne pas activer de compatibilité faible sans exception approuvée.

## 7. Sauvegarde et reprise

Fiche simple : [sauvegarder et restaurer le DC](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-sauvegarde).

Ne pas copier à chaud `/var/lib/samba` avec un simple `tar` ou `rsync` comme unique sauvegarde d'un contrôleur actif. Utiliser la commande de sauvegarde intégrée à la version installée et examiner son aide locale avant exécution :

```bash
samba-tool domain backup online --help
samba-tool domain backup offline --help
samba-tool domain backup restore --help
```

Lancer la sauvegarde vers un volume protégé, séparé du serveur, avec une authentification interactive ou un fichier de credentials à permissions strictes si la version l'exige. Chiffrer et contrôler l'accès aux archives, car elles contiennent des données d'identité sensibles. Documenter la version Samba, le DC source, l'heure et le résultat.

Tester la restauration dans un réseau isolé sans routage vers la forêt réelle et avec des noms/adresses de laboratoire distincts. Vérifier l'authentification, les enregistrements DNS, les ACL SYSVOL et les stratégies après restauration. Une sauvegarde non restaurée au moins une fois n'est pas une preuve de reprise.

## 8. Retour arrière et limites

Fiche simple : [revenir en arrière et connaître les limites](/01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-retour-arriere).

Avant provisionnement, l'action la plus sûre pour revenir en arrière est de supprimer et recréer la VM de laboratoire depuis son image initiale. Ne pas « déprovisionner » en supprimant arbitrairement la base AD d'un serveur en production. En cas d'échec de démarrage, conserver les journaux, corriger la configuration, valider avec `testparm -s`, puis redémarrer le service.

Les commandes Samba et la version Debian sont sourcées à partir des manpages Debian 13 et de la documentation Samba. Les procédures de restauration et les usages avancés n'ont pas été testés sur un domaine dans ce workspace; ils nécessitent un essai isolé de la version exacte avant usage opérationnel.

## Sources

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Debian 13 — testparm(1)](https://manpages.debian.org/trixie/samba-common-bin/testparm.1.en.html)
- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)