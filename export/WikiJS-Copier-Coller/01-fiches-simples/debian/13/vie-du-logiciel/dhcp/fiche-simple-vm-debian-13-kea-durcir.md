# Fiche_Simple_-_VM_Debian_13_Kea_Durcir.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP

---

## Problème précis à résoudre

Réduire la surface d'exposition de Kea et cadrer son exploitation.

## 1. Hors-Production (Lab / Test / POC)

1. Limiter les interfaces d'écoute dans `/etc/kea/kea-dhcp4.conf` (clé `interfaces-config`).
   👉 Explication : Kea ne répond que sur l'interface prévue.

2. Restreindre les droits des fichiers de configuration et des sauvegardes :
   ```bash
   sudo ls -l /etc/kea/
   ```
   👉 Explication : les secrets SQL éventuels sont en clair dans la configuration; vérifier qu'ils ne sont pas lisibles par tous.

3. Ne pas exposer l'API de contrôle HTTP; si elle est activée, utiliser HTTPS, authentification et filtrage réseau.
   👉 Explication : le socket de contrôle UNIX est désactivé par défaut.

4. Tenir le système et le canal stable à jour :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i kea
   ```
   👉 Explication : toute mise à niveau se teste d'abord sur un serveur pilote.

## 2. Production — Contrôles

Supervision du service, revue des journaux, plan de mise à jour; HA et base SQL uniquement selon les procédures ISC.

## 3. Production — Sécurité

- N'activer aucun hook ni composant inutile.
- Ne pas exposer l'API de contrôle à un réseau non maîtrisé.

## Validation et retour arrière

- **Validation** : Interfaces limitées, droits restreints, aucun composant superflu actif.
- **Retour arrière** : Restaurer la configuration précédente et redémarrer le service.

## Si le problème n'est pas résolu

- [ISC Kea — Sécurité](https://kea.readthedocs.io/en/latest/arm/security.html)
- [Guide complet Kea DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13#7-durcissement-et-exploitation)