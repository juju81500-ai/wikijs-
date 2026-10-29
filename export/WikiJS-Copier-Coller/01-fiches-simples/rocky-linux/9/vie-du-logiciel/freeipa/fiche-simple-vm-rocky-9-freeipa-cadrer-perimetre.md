# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Cadrer_Perimetre.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / cadrage

---

## Problème précis à résoudre

Savoir si FreeIPA est le bon outil et s'il est supporté sur Rocky Linux 9 avant d'installer.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le système et les services déjà actifs :
   ```bash
   cat /etc/os-release
   systemctl list-units --type=service --state=running | grep -Ei "named|slapd|dirsrv|httpd|nginx|krb5"
   ```
   👉 Explication : Contrôle la version de Rocky Linux et l'absence d'un annuaire, DNS, serveur web ou CA déjà présents sur la VM.

2. Lire dans le guide le statut de support : Rocky Linux 9 est compatible RHEL mais la procédure n'a pas été testée sur Rocky.
   👉 Explication : le projet FreeIPA supporte officiellement Fedora et RHEL; la compatibilité Rocky est une hypothèse à valider sur une VM pilote.

3. Noter par écrit ce qui n'est pas couvert : réplicas, confiance AD, CA externe, migration OpenLDAP/NIS.
   👉 Explication : ces cas demandent une procédure dédiée; ne pas les improviser.

## 2. Production — Contrôles

Décider si le besoin est un annuaire complet (LDAP + Kerberos + CA) ou un simple LDAP; valider avec le responsable sécurité; prévoir une VM dédiée.

## 3. Production — Sécurité

- Ne jamais installer FreeIPA sur un serveur qui héberge déjà annuaire, DNS, serveur web ou CA.
- Conserver les statuts « À revoir » et « À tester » tant que la VM pilote n'est pas validée.

## Validation et retour arrière

- **Validation** : périmètre et statut de support documentés, aucun service concurrent sur la VM.
- **Retour arrière** : aucun changement n'a été fait : rien à annuler.

## Si le problème n'est pas résolu

- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 1](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9#1-perimetre-et-statut-de-support)