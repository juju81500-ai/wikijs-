# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Prerequis.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / prérequis

---

## Problème précis à résoudre

Vérifier nom d'hôte, heure, ressources et ports avant de lancer l'installation FreeIPA.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le nom d'hôte :
   ```bash
   hostnamectl status
   hostname -f
   ```
   👉 Explication : Affiche le FQDN statique; il ne doit jamais valoir `localhost`.

2. Vérifier la résolution et la mémoire :
   ```bash
   getent hosts "$(hostname -f)"
   free -h
   ```
   👉 Explication : Le FQDN doit se résoudre vers l'IP du serveur (dans `/etc/hosts`, le FQDN vient en premier); la RAM doit couvrir le minimum du guide (au moins 2 Go en test).

3. Vérifier la synchronisation de l'heure :
   ```bash
   chronyc tracking
   ```
   👉 Explication : Kerberos échoue en cas de dérive d'horloge; l'heure doit être synchronisée.

4. Noter par écrit le domaine, le realm Kerberos et le FQDN, et prendre un snapshot de la VM.
   👉 Explication : ces trois valeurs sont définitives; utiliser un domaine que l'organisation possède, pas `example.com`.

5. Lister les ports à ouvrir : 80/tcp, 443/tcp, 389/tcp, 636/tcp, 88/tcp+udp, 464/tcp+udp, plus 53/tcp+udp avec DNS intégré.
   👉 Explication : le pare-feu sera configuré à l'étape suivante.

## 2. Production — Contrôles

Réserver la RAM (pas de ballooning), enregistrer le FQDN en DNS direct et inverse, valider le domaine et le realm avec l'équipe.

## 3. Production — Sécurité

- Ne pas utiliser un domaine non possédé par l'organisation.
- Limiter les accès à la VM aux administrateurs de l'annuaire.

## Validation et retour arrière

- **Validation** : FQDN résolu dans les deux sens, heure synchronisée, ressources suffisantes, snapshot pris.
- **Retour arrière** : supprimer le snapshot inutile; aucune modification de configuration n'a été faite.

## Si le problème n'est pas résolu

- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 2](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9#2-prerequis-a-valider-avant-linstallation)