# Fiche_Simple_-_VM_Debian_13_FOG_Project_Prerequis_Limites

- **Environnement** : VM Debian 13 dédiée FOG Project (clonage/déploiement d'images), réseau de laboratoire isolé
- **OS / Version** : Debian 13 Trixie; FOG Project (version et support Debian 13 à vérifier)
- **Catégorie** : automatisation / déploiement
- **Tags** : `debian13`, `fog-project`, `prerequis`, `limites`, `pxe`

---

## Problème précis à résoudre

Vérifier, avant toute installation, que FOG est supporté sur Debian 13 et qu'il ne perturbera pas le réseau existant.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le système cible :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   ip -br addr
   df -h /
   free -h
   ```
   👉 Explication : la VM doit avoir une adresse IP fixe et un volume suffisant pour les images (`/images`) ; dimensionner selon la documentation FOG.

2. Consulter la documentation FOG et les notes de version : statut de support officiel de Debian 13, version stable publiée, versions de PHP/MariaDB attendues.
   👉 Explication : ne pas supposer que Debian 13 est supporté : le support doit être vérifié sur docs.fogproject.org et dans le dépôt officiel. S'il n'est pas confirmé, rester en laboratoire jetable ou choisir une distribution documentée.

3. Choisir le mode DHCP : DHCP existant (options 66/67 vers le serveur FOG) ou DHCP fourni par FOG.
   👉 Explication : un second serveur DHCP non maîtrisé sur le même VLAN peut couper le réseau ; en laboratoire, isoler le VLAN.

4. Lister les services que l'installeur FOG va configurer (serveur web, base de données, TFTP, NFS, éventuellement DHCP, pare-feu).
   👉 Explication : l'installeur modifie des services système : prévoir un instantané de la VM et une fenêtre de test avant de continuer.

## 2. Production — Contrôles

Production : valider l'accord du responsable réseau (DHCP/PXE, VLAN dédié), la matrice de support publiée, l'espace disque, la sauvegarde de la VM, le contrôle des licences des systèmes déployés et le plan de retour arrière.

## 3. Production — Sécurité

- Ne pas installer sur un VLAN de production partagé sans validation du DHCP/PXE.
- Prévoir un hôte dédié ; ne pas mutualiser avec d'autres services exposés.
- Ne pas ouvrir l'interface FOG sur Internet.

## Validation et retour arrière

- **Validation** : support Debian 13 confirmé par source officielle, VLAN et mode DHCP décidés, capacité disque dimensionnée.
- **Arrêt** : support non confirmé ou DHCP non validé ⇒ ne pas installer.

## Si le problème n'est pas résolu

- [Documentation officielle FOG Project](https://docs.fogproject.org/)
- [Dépôt officiel FOG Project](https://github.com/FOGProject/fogproject)
- [Fiche d'entrée FOG Project](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_FOG-Project.md)
