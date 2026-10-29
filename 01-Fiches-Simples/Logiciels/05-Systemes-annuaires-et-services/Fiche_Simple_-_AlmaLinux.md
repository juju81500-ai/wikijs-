# Fiche_Simple_-_AlmaLinux

- **Environnement** : Hôte AlmaLinux; fiches opérationnelles de référence Rocky Linux 9
- **OS / Version** : AlmaLinux; vérifier la version majeure installée avant d’appliquer une procédure
- **Catégorie** : système Linux / renvoi de documentation
- **Tags** : `almalinux`, `rocky-linux-9`, `renvoi`, `systeme`

---

## Problème précis à résoudre

Réutiliser les procédures Rocky Linux 9 pertinentes sans créer une nouvelle série OS AlmaLinux dans ce pack.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer l’identité et la version de l’hôte :
   ```bash
   cat /etc/os-release
   rpm -q almalinux-release
   ```
   👉 Explication : vérifier que l’hôte est AlmaLinux et relever la version majeure avant de suivre une fiche Rocky Linux.

2. Choisir la fiche Rocky Linux 9 correspondant à l’étape :
   - [Cycle de vie Rocky Linux 9](../../Rocky-Linux/9/Vie-du-systeme/Cycle-de-vie-50-etapes.md)
   - [Récupération et vérification de l’image](../../Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_02_Recuperation_De_L_Image.md)
   - [Mise à jour initiale](../../Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_20_Mise_A_Jour_Initiale.md)
   - [Mises à jour et inventaire](../../Rocky-Linux/9/Vie-du-systeme/Fiches-par-theme/Securite/Fiche_Simple_-_VM_Rocky_9_Securite_Hardening_Mises_A_Jour_Inventaire.md)
   👉 Explication : les tâches communes DNF, firewalld et SELinux sont des repères; vérifier la compatibilité et le support applicables à l’hôte réel.

3. Avant un changement, comparer le dépôt, le paquet release et la documentation officielle AlmaLinux.
   👉 Explication : ne pas copier aveuglément un nom de dépôt, une clé de signature ou une commande de souscription Rocky/RHEL.

## 2. Production — Contrôles

Vérifier identité de distribution, version majeure, dépôts activés, signatures, avis de sécurité et cycle de support AlmaLinux avant d’appliquer une procédure Rocky Linux 9.

## 3. Production — Sécurité

- Les paquets release, dépôts, clés de signature et avis de sécurité sont propres à la distribution.
- Ne pas modifier les dépôts pour les rendre identiques à Rocky Linux.
- Pour une version AlmaLinux autre que 9, vérifier chaque procédure avec la documentation éditeur.

## Validation et retour arrière

- **Validation** : fiche Rocky Linux 9 choisie pour une tâche compatible, différences de distribution vérifiées et changement approuvé.
- **Retour arrière** : appliquer le retour arrière documenté pour l’étape concernée; ne pas basculer les dépôts ou paquets release entre distributions.

## Si le problème n’est pas résolu

- [AlmaLinux — documentation officielle](https://wiki.almalinux.org/)
- [Rocky Linux — documentation officielle](https://docs.rockylinux.org/)
- [Entrée AlmaLinux du pack](Fiche_Logiciel_-_AlmaLinux.md)
