# Fiche_Simple_-_VM_Debian_12_Bacula_Cadrer_Perimetre.md

- **Environnement** : VM Debian 12 dédiée à Bacula (Director, Storage Daemon, File Daemon, catalogue PostgreSQL)
- **OS / Version** : Debian 12 Bookworm; Bacula Community 15.0.3 (backports)
- **Catégorie** : sauvegarde / cadrage

---

## Problème précis à résoudre

Vérifier que le serveur de laboratoire Debian 12 convient avant de déployer Bacula.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version du système :
   ```bash
   cat /etc/os-release | grep -E '^(PRETTY_NAME|VERSION_ID)'
   ```
   👉 Explication : Bacula 15.0.3 n'est visé que pour Debian 12 Bookworm avec backports.

2. Contrôler mémoire et espace disque disponibles :
   ```bash
   free -h
   df -h /var /tmp
   ```
   👉 Explication : le Storage Daemon a besoin d'un répertoire disque avec assez de place pour les volumes.

3. Lister les ports déjà utilisés :
   ```bash
   sudo ss -tlnp | grep -E ':(9101|9102|9103)\b' || echo 'ports libres'
   ```
   👉 Explication : les ports Bacula par défaut sont 9101 (console), 9102 (File Daemon) et 9103 (Storage Daemon); ils ne doivent pas être occupés.

## 2. Production — Contrôles

Définir RPO/RTO, séparer les rôles Director/Storage/File Daemon selon les besoins, prévoir une copie hors site et des tests de restauration planifiés.

## 3. Production — Sécurité

- Ne pas viser Debian 13 ni les paquets upstream nécessitant une clé d'accès avec ce guide.
- Un stockage sur le même serveur n'est pas une stratégie de reprise.
- Protéger le stockage contre l'effacement ou le chiffrement depuis le serveur sauvegardé.

## Validation et retour arrière

- **Validation** : système Debian 12 confirmé, espace suffisant, ports Bacula libres.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [Bacula — manuels 15.0.x](https://www.bacula.org/15.0.x-manuals/en/main/)
- [Guide complet Bacula Debian 12](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports#1-perimetre-et-architecture)