# Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Cadrer_Prerequis.md

- **Environnement** : Ubuntu Server 24.04: nœud Graylog + MongoDB et Data Node (laboratoire)
- **OS / Version** : Ubuntu Server 24.04 LTS; Graylog 7.2; MongoDB 8.0
- **Catégorie** : journaux / cadrage

---

## Problème précis à résoudre

Vérifier l'hôte avant d'installer Graylog.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et les ressources :
   ```bash
   cat /etc/os-release | grep -E '^(PRETTY_NAME|VERSION_ID)'
   free -h
   nproc
   ```
   👉 Explication : confirme Ubuntu 24.04, mémoire et CPU disponibles.

2. Contrôler l'espace du stockage des données :
   ```bash
   df -hT /var/lib
   lsblk -f
   ```
   👉 Explication : le Data Node demande une zone dédiée, idéalement XFS.

3. Contrôler l'heure et la résolution DNS du nœud :
   ```bash
   timedatectl
   hostname -f
   ```
   👉 Explication : NTP et DNS cohérents sont exigés.

## 2. Production — Contrôles

Dimensionner selon le débit EPS, la taille des événements, la rétention, les index et la charge de recherche; vérifier la matrice de compatibilité Graylog 7.2.

## 3. Production — Sécurité

- Une installation mono-nœud n'est pas une architecture HA.

## Validation et retour arrière

- **Validation** : prérequis relevés et matrice de compatibilité vérifiée.
- **Retour arrière** : lecture seule: rien à annuler.

## Si le problème n'est pas résolu

- [Graylog 7.2 — installation Ubuntu](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm)
- [Graylog — sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)
- [Graylog — matrice de compatibilité](https://go2docs.graylog.org/current/downloading_and_installing_graylog/compatibility_matrix.htm)
- [Guide complet Graylog Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04#1-cadrage-et-prerequis)