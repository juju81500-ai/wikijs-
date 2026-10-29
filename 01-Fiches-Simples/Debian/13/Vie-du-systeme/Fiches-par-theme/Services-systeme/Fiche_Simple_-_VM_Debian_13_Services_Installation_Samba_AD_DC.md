# Fiche simple — Debian 13 : préparer un lab Samba AD DC

- **OS / Version** : VM Debian 13 Trixie, Samba des dépôts Debian
- **Catégorie** : Services réseau / Annuaire Active Directory
- **Tags** : `[debian13]`, `[samba]`, `[ad-dc]`, `[dns]`, `[lab]`

## Objectif

Créer un domaine Samba AD DC neuf dans un environnement de laboratoire isolé. Cette fiche ne décrit pas une migration ou une reprise de forêt existante.

## 1. Préparer avant le provisionnement

Fixer l'adresse IP et le nom du serveur, vérifier NTP, choisir le nom DNS/NetBIOS du domaine et confirmer que le réseau est isolé. Ne jamais utiliser un suffixe `.local` ni un domaine que l'organisation ne contrôle pas.

```bash
hostnamectl
timedatectl status
ip -br address
```
   👉 Explication : relève nom, heure et IP du futur contrôleur de domaine.

## 2. Installer et provisionner

```bash
sudo apt update
sudo apt install samba-ad-dc samba-common-bin krb5-user dnsutils smbclient acl attr
```
   👉 Explication : installe Samba AD DC et les outils Kerberos/DNS.

Pour un domaine de test neuf seulement, lancer une fois le provisionnement interactif et saisir le mot de passe à l'invite :

```bash
sudo samba-tool domain provision --server-role=dc --use-rfc2307 --realm=AD.LAB.TEST --domain=ADLAB --dns-backend=SAMBA_INTERNAL
```
   👉 Explication : provisionne le domaine; remplacer realm et nom NetBIOS; le mot de passe Administrator est demandé à l'écran, ne pas le passer en argument.

Ne pas relancer cette commande sur un contrôleur déjà provisionné.

## 3. Vérifier le service et DNS

```bash
sudo testparm -s
sudo systemctl enable --now samba-ad-dc.service
sudo systemctl --no-pager status samba-ad-dc.service
sudo journalctl -u samba-ad-dc.service -n 40 --no-pager
host -t SRV _ldap._tcp.ad.lab.test 192.0.2.10
```
   👉 Explication : contrôle la configuration, démarre le service, lit l'état et les journaux, puis interroge l'enregistrement SRV LDAP.

Remplacer le nom et l'adresse de l'exemple. Le système et les clients du lab doivent utiliser le DNS du DC. Tester Kerberos avec `kinit Administrator@AD.LAB.TEST` et une saisie interactive du mot de passe.

## Sécurité et retour arrière

Ne pas exposer les ports AD sur Internet. Sauvegarder le domaine avec `samba-tool domain backup online --help` en suivant l'aide de la version installée; tester toute restauration dans un réseau isolé. Pour un lab défectueux, recréer la VM est préférable à la suppression manuelle des bases Samba.

## Source

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- Guide complet : `02-Fiches-Completes/Debian-13/Installation-Deploiement/65_Deploiement_Samba_AD_DC_Debian_13.md`