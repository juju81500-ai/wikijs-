# Fiche_Simple_-_VM_Debian_12_Zabbix_Concevoir_Preparer.md

- **Environnement** : VM dédiée Zabbix Server, base locale et agents/proxies autorisés
- **OS / Version** : Debian 12 Bookworm; Zabbix 7.0 LTS depuis le dépôt officiel compatible
- **Catégorie** : supervision / conception Zabbix

---

## Problème précis à résoudre

Préparer la supervision Zabbix en déterminant capacité, versions, flux réseau et stratégie de sauvegarde avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Relever ressources et réseau :
   ```bash
   nproc; free -h; df -h /var/lib/mysql 2>/dev/null || df -h /
   ip -br a
   ```
   👉 Explication : dimensionner la base selon hôtes, items et durée de conservation; réserver DNS/IP.

2. Contrôler les versions proposées par le dépôt Zabbix officiel (déjà ajouté selon la documentation Zabbix pour Debian 12) :
   ```bash
   sudo apt update
   apt-cache policy zabbix-server-mysql zabbix-frontend-php
   ```
   👉 Explication : le candidat doit provenir du dépôt Zabbix 7.0 LTS et non des dépôts Debian.

3. Consigner : TLS, sauvegarde de la base, flux réseau des agents (10050/10051).
   👉 Explication : ces flux sont ouverts uniquement entre agents/proxies et serveur.

## 2. Production — Contrôles

Faire approuver capacité, version, réseau, stockage, TLS, rétention, sauvegarde base/configuration et responsabilités d'exploitation.

## 3. Production — Sécurité

- Ne pas ouvrir le port serveur à Internet ou à tout le réseau.
- Ne pas mélanger paquets Debian avec ceux d'un dépôt Zabbix d'une autre distribution.
- Ne pas commencer avant d'avoir défini la reprise de la base et de la configuration.
- Ne pas conserver les secrets dans la documentation ou le dépôt.

## Validation et retour arrière

- **Validation** : candidats APT, dimensions, flux, TLS et procédure de restauration confirmés.
- **Arrêt** : reporter si le dépôt ne correspond pas à Debian 12 ou à la branche LTS choisie.

## Si le problème n'est pas résolu

- [Zabbix — documentation 7.0](https://www.zabbix.com/documentation/7.0/en/manual)
- [Zabbix — téléchargement officiel](https://www.zabbix.com/download)
- [Guide complet Zabbix Debian 12](/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12)