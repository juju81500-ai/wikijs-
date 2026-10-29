# Fiche_Simple_-_VM_Ubuntu_24.04_OpenStack_DevStack_Installer_Lab

- **Environnement** : VM jetable isolée sur Proxmox VE 8.x; console locale
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); DevStack selon branche/doc officielle
- **Catégorie** : cloud privé / installation de lab
- **Tags** : `openstack`, `devstack`, `ubuntu2404`, `lab`, `non-production`

---

## Problème précis à résoudre

Installer un OpenStack mono-nœud de développement pour tester concepts et API, sans exposition ni charge de production.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier VM Ubuntu 24.04 LTS propre, isolée, sortie contrôlée vers dépôts. DevStack demande un compte non-root disposant de sudo; préparer exactement comme dans Quick Start officiel.
   👉 Explication : DevStack modifie le système et demande des privilèges; limiter ce compte à la VM jetable.
2. Dans la VM, cloner le dépôt officiel et entrer dans son répertoire :
   ```bash
   git clone https://opendev.org/openstack/devstack
   cd devstack
   ```
   👉 Explication : pour un essai reproductible, consigner branche/commit et consulter sa documentation.
3. Créer `local.conf` d’après le Quick Start avec quatre secrets uniques générés localement. Les valeurs en majuscules sont des placeholders « à remplacer »; respecter les restrictions de caractères et ne pas versionner/partager le fichier.
   ```ini
   [[local|localrc]]
   ADMIN_PASSWORD=MOT_DE_PASSE_ADMIN_A_REMPLACER
   DATABASE_PASSWORD=MOT_DE_PASSE_BDD_A_REMPLACER
   RABBIT_PASSWORD=MOT_DE_PASSE_RABBIT_A_REMPLACER
   SERVICE_PASSWORD=MOT_DE_PASSE_SERVICE_A_REMPLACER
   ```
   👉 Explication : aucun vrai secret dans cette fiche ou dans un dépôt.
4. Depuis le répertoire DevStack, lancer uniquement dans cette VM : `./stack.sh`.
   👉 Explication : arrêter et diagnostiquer les erreurs au lieu de rejouer aveuglément.
5. Après succès, accéder à Horizon depuis l’admin du lab; vérifier le catalogue via la CLI locale sans afficher les identifiants :
   ```bash
   source openrc
   openstack service list
   ```
   👉 Explication : valide authentification et catalogue; URL/identifiants restent propres au lab.

## 2. Production — Contrôles

- DevStack est réservé au développement/essais, pas à la production, la HA ou aux données réelles. Toute plateforme réelle exige méthode et support explicitement documentés.

## 3. Production — Sécurité

- Ne pas ouvrir d’endpoint Internet; secrets propres au lab; compte sudo limité à la VM; expurger journaux avant partage.

## Validation et retour arrière

- **Validation** : catalogue retourné et Horizon accessible uniquement depuis le lab. **Retour arrière** : supprimer la VM ou restaurer le snapshot préalable; ne pas nettoyer manuellement les paquets pour recycler l’OS.

## Si le problème n'est pas résolu

- [DevStack — Quick Start/prérequis](https://docs.openstack.org/devstack/latest/)
- [DevStack — installation mono-machine](https://docs.openstack.org/devstack/latest/guides/single-machine.html)
- [OpenStack — documentation officielle](https://docs.openstack.org/)
