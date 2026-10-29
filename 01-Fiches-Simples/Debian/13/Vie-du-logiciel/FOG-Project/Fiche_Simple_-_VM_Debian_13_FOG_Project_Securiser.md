# Fiche_Simple_-_VM_Debian_13_FOG_Project_Securiser

- **Environnement** : VM Debian 13 dédiée FOG Project (clonage/déploiement d'images), réseau de laboratoire isolé
- **OS / Version** : Debian 13 Trixie; FOG Project (version et support Debian 13 à vérifier)
- **Catégorie** : automatisation / déploiement
- **Tags** : `debian13`, `fog-project`, `securite`, `tls`, `durcissement`

---

## Problème précis à résoudre

Durcir l'instance FOG : comptes, TLS, exposition réseau et secrets.

## 1. Hors-Production (Lab / Test / POC)

1. Se connecter à l'interface web et changer immédiatement les identifiants par défaut décrits dans la documentation (compte administrateur d'origine).
   👉 Explication : les identifiants par défaut sont publics ; créer des comptes nominatifs, retirer ou renforcer le compte d'origine, sans noter de mot de passe dans la fiche.

2. Vérifier les ports en écoute :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : identifier HTTP(S), TFTP, NFS, MariaDB et SSH ; chaque port doit être justifié.

3. Restreindre avec le pare-feu au VLAN de déploiement et d'administration (RESEAU_DEPLOIEMENT à remplacer, ex. un CIDR dédié) :
   ```bash
   sudo nft list ruleset
   ```
   👉 Explication : relire d'abord les règles existantes ; adapter avec l'outil de pare-feu retenu par l'organisation sans couper SSH.

4. Activer HTTPS pour l'interface selon la documentation FOG (certificat émis par la PKI interne).
   👉 Explication : éviter que les identifiants d'administration transitent en clair.

5. Vérifier les droits des fichiers de configuration FOG :
   ```bash
   sudo ls -l /opt/fog/.fogsettings
   ```
   👉 Explication : ce fichier contient des secrets d'installation ; il doit être lisible par root seulement.

## 2. Production — Contrôles

Production : revue des comptes, journaux, accès au réseau, TLS valide, correctifs Debian et FOG suivis, séparation des rôles.

## 3. Production — Sécurité

- Ne jamais exposer l'interface FOG sur Internet ni via NAT public.
- Ne pas stocker de mot de passe de base ou de stockage dans les tickets.
- Les images disque peuvent contenir des données sensibles : chiffrer ou protéger l'accès au stockage.
- Ne pas inclure de secrets de domaine (jonction AD) en clair dans les images.

## Validation et retour arrière

- **Validation** : identifiants par défaut inutilisables, ports minimaux, HTTPS actif.
- **Retour arrière** : restaurer l'instantané ou la configuration pare-feu précédente.

## Si le problème n'est pas résolu

- [Documentation officielle FOG Project](https://docs.fogproject.org/)
- [Dépôt officiel FOG Project](https://github.com/FOGProject/fogproject)
- [Fiche d'entrée FOG Project](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_FOG-Project.md)
