# Fiche_Simple_-_VM_Debian_13_Centreon_Preparer.md

- **Environnement** : VM Debian 13 dédiée, serveur Centreon Central avec MariaDB locale
- **OS / Version** : Debian 13 Trixie; Centreon 26.10
- **Catégorie** : supervision / prérequis
- **Tags** : `debian13`, `centreon`, `supervision`, `prerequis`

---

## Problème précis à résoudre

Vérifier que la VM Debian 13 est prête (nom, heure, réseau, espace disque) avant d'installer Centreon Central.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   hostnamectl
   timedatectl status
   ip -br address
   ```
   👉 Explication : affiche le nom d'hôte, l'heure et l'adresse IP; l'IP doit être fixe et le nom conforme au DNS.

2. Exécuter :
   ```bash
   df -h
   free -h
   ```
   👉 Explication : contrôle l'espace disque et la mémoire; Centreon stocke les métriques, prévoir large selon hôtes, services et rétention.

3. Exécuter :
   ```bash
   getent hosts $(hostname -f)
   ```
   👉 Explication : vérifie que le nom complet de la VM se résout (DNS prêt).

4. Faire un instantané ou une sauvegarde de la VM avant toute installation.
   👉 Explication : donne un point de retour si l'installation échoue.

## 2. Production — Contrôles

Prévoir DNS, IP fixe, fuseau horaire, serveur SMTP, certificat TLS, espace pour les métriques et une sauvegarde testable; dimensionner selon le nombre d'hôtes, de services, les intervalles et la rétention.

## 3. Production — Sécurité

- Ne pas commencer sans sauvegarde de la VM.
- Réserver la VM au réseau de gestion.
- Vérifier que Debian 13 est bien la version supportée par Centreon 26.10.

## Validation et retour arrière

- **Validation** : nom, heure et IP corrects, espace suffisant, sauvegarde réalisée.
- **Retour arrière** : aucune modification n'est faite à cette étape; restaurer l'instantané si besoin.

## Si le problème n'est pas résolu

- [Centreon — installation unattended](https://docs.centreon.com/docs/installation/installation-of-a-central-server/unattended-install-central/)
- [Centreon — installation par paquets](https://docs.centreon.com/docs/installation/installation-of-a-central-server/using-packages/)
- [Guide complet Déployer Centreon 26.10 sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/48_Deploiement_Centreon_26.10_Debian_13.md#1-preparer-le-serveur)
