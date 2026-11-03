# RHEL et AlmaLinux : compléments par rapport à Rocky Linux 9

- **Environnement** : Serveurs RHEL ou AlmaLinux de la famille EL, en complément des fiches Rocky Linux 9 existantes
- **Tags** : `rhel`, `almalinux`, `rocky`, `dnf`, `selinux`, `subscription`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

- Périmètre : différences d'enregistrement, de dépôts, de support, de migration et de cycle de vie entre RHEL, AlmaLinux et Rocky Linux. Les procédures communes (dnf, SELinux, firewalld, systemd) restent celles des fiches [Rocky Linux 9](../../../rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9.md).
- Prérequis : accès root/sudo, accès aux dépôts, horloge synchronisée, sauvegarde ou instantané préalable.

## 2. Exigences de version et licence

- **Version majeure et mineure à figer avant déploiement**, après lecture des notes de version et du calendrier de support de chaque distribution.
- RHEL : exige un abonnement (ou programme développeur/évaluation selon conditions éditeur actuelles) et un enregistrement pour accéder aux dépôts officiels. Vérifier les conditions sur le portail Red Hat.
- AlmaLinux : distribution communautaire gratuite, binaire-compatible ; pas d'abonnement requis.
- Rocky Linux : idem, communautaire. Vérifier la compatibilité des éditeurs tiers (support applicatif) par distribution.

## 3. Procédure

1. Identifier l'OS :
```bash
cat /etc/os-release
uname -r
```
2. RHEL : enregistrer le système puis contrôler les dépôts.
```bash
sudo subscription-manager register
sudo subscription-manager status
sudo subscription-manager repos --list-enabled
```
3. AlmaLinux : vérifier les dépôts `baseos`, `appstream` et la clé GPG.
```bash
dnf repolist
rpm -qa gpg-pubkey*
```
4. Mettre à jour après instantané : `sudo dnf check-update` puis `sudo dnf update`.
5. Contrôler SELinux (`getenforce`, doit rester `Enforcing`) et firewalld (`firewall-cmd --list-all`).
6. Migration entre distributions EL : n'utiliser que l'outil et la procédure documentés par la distribution cible (par exemple outil officiel de conversion), uniquement sur une copie ou une VM clonée d'abord.
7. Documenter le canal de correctifs de sécurité et le rythme de mise à jour (CVE).

## 4. Vérifications

- `os-release` conforme à la cible ; dépôts activés limités aux dépôts officiels.
- `dnf check-update` sans erreur de signature.
- Services applicatifs de la fiche Rocky rejoués : même résultat attendu, écarts notés.

## 5. Rollback et risques

- Conversion d'une distribution vers une autre : peu réversible ; garder un instantané de VM ou une sauvegarde système complète, et une fenêtre de maintenance.
- Mise à jour majeure sur place : non recommandée en production sans test ; préférer un nouveau serveur et migration des données.
- Désenregistrement RHEL (`subscription-manager unregister`) coupe l'accès aux correctifs : ne pas l'exécuter sans raison.
- Ne pas importer de dépôts tiers non vérifiés (risque de rupture de support et de sécurité).

## 6. Documentation officielle

- <https://docs.redhat.com/>
- <https://wiki.almalinux.org/>
- <https://almalinux.org/>
