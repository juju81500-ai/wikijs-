# Fiche_Simple_-_VM_Debian_13_MongoDB_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Prérequis et limites
- **Tags** : `debian13`, `mongodb`, `prerequis`

---

## Problème précis à résoudre

Vérifier qu'un MongoDB Community peut être installé sur Debian 13 et cadrer les limites.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS, le processeur et l'espace disque :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   grep -m1 -o -w avx /proc/cpuinfo || echo 'AVX absent'
   df -h /var/lib /var/backups
   ```
   👉 Explication : MongoDB 5.0 et plus exige un processeur avec AVX ; prévoir de l'espace pour données, journal et sauvegardes (XFS recommandé par l'éditeur).

2. Vérifier le support de Debian 13 :
   👉 Explication : MongoDB Community est distribué par son propre dépôt APT : vérifier dans la matrice de compatibilité de la version visée que Debian 13 est prise en charge ; à défaut utiliser une distribution listée ou un conteneur officiel.

3. Contrôler le port :
   ```bash
   sudo ss -tlnp | grep -E ':27017\b' || echo 'port 27017 libre'
   ```
   👉 Explication : aucun autre mongod ne doit écouter.

## 2. Production — Contrôles

Consigner version, volumétrie, clients, responsable, RPO/RTO.

## 3. Production — Sécurité

- Pas d'exposition réseau avant la fiche Sécuriser.
- Limites : instance unique ; replica set et sharding hors périmètre.
- Ne pas utiliser un MongoDB sans authentification.

## Validation et retour arrière

- **Validation** : support de la version et matériel vérifiés.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [MongoDB — Installer](Fiche_Simple_-_VM_Debian_13_MongoDB_Installer.md)
- [MongoDB — Configurer](Fiche_Simple_-_VM_Debian_13_MongoDB_Configurer.md)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](Fiche_Simple_-_VM_Debian_13_MongoDB_Securiser.md)
- [MongoDB — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MongoDB_Valider.md)
- [MongoDB — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MongoDB_Sauvegarder_Restaurer.md)
- [MongoDB — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MongoDB_Mettre_A_Jour.md)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
