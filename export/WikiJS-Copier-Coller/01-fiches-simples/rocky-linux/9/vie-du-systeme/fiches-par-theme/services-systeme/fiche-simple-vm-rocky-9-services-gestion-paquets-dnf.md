# 📄 VM_Rocky_9_Services_Gestion-Paquets-DNF.md

- **Environnement** : VM (Rocky Linux 9 / RHEL 9)
- **OS / Version** : Rocky Linux 9 - Famille RedHat
- **Catégorie** : Système & Services / Gestionnaires de paquets

## 🎯 Problème précis à résoudre
Gérer l'installation, la recherche, la mise à jour et la suppression de logiciels sous Rocky Linux 9 / RHEL 9 via le gestionnaire de paquets DNF/RPM, et activer les dépôts d'entreprise EPEL.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Recherche d'un paquet dans les dépôts actifs :
   `dnf search htop`
   👉 Explication : Interroge la base de métadonnées pour trouver le nom exact du paquet.
2. Installation rapide d'un logiciel :
   `dnf install -y htop`
   👉 Explication : Télécharge et installe le paquet demandé et ses dépendances.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation des dépôts supplémentaires d'entreprise EPEL et CRB :
   `dnf install -y epel-release && dnf config-manager --set-enabled crb`
   👉 Explication : Étend le catalogue de logiciels d'entreprise disponibles pour Rocky Linux 9.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activation de l'outil `dnf-automatic` pour les correctifs de sécurité critiques :
   `dnf install -y dnf-automatic`
   👉 Explication : Installe le service de mise à jour automatique des paquets RPM.