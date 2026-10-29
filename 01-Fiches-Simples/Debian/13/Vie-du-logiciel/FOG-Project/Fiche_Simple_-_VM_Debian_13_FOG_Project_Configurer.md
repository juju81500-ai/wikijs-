# Fiche_Simple_-_VM_Debian_13_FOG_Project_Configurer

- **Environnement** : VM Debian 13 dédiée FOG Project (clonage/déploiement d'images), réseau de laboratoire isolé
- **OS / Version** : Debian 13 Trixie; FOG Project (version et support Debian 13 à vérifier)
- **Catégorie** : automatisation / déploiement
- **Tags** : `debian13`, `fog-project`, `configuration`, `pxe`, `dhcp`

---

## Problème précis à résoudre

Configurer le démarrage réseau et les paramètres de base de FOG sans impacter le DHCP existant.

## 1. Hors-Production (Lab / Test / POC)

1. Si DHCP existant : renseigner sur le serveur DHCP les options 66 (IP_SERVEUR_FOG) et 67 (nom du fichier de démarrage indiqué par la documentation FOG pour BIOS/UEFI).
   👉 Explication : IP_SERVEUR_FOG est à remplacer ; le fichier de démarrage dépend du mode BIOS/UEFI : se référer à la documentation FOG.

2. Dans l'interface web : FOG Configuration → FOG Settings → vérifier les paramètres de réseau (TFTP/Web host).
   👉 Explication : les chemins de menu peuvent varier selon la version : vérifier dans la documentation correspondante.

3. Vérifier les services de démarrage :
   ```bash
   systemctl --no-pager status tftpd-hpa nfs-kernel-server
   ```
   👉 Explication : les noms d'unités peuvent différer selon la version de l'installeur ; adapter à `systemctl list-units | grep -Ei 'tftp|nfs'`.

4. Tester avec une seule VM de laboratoire en démarrage PXE, sans lancer de déploiement.
   👉 Explication : le test valide la chaîne DHCP→TFTP→menu FOG avant tout déploiement.

## 2. Production — Contrôles

Production : changement DHCP approuvé, VLAN ou machines pilotes limités, groupes d'hôtes et images nommés, droits des comptes de gestion séparés.

## 3. Production — Sécurité

- Ne pas activer de déploiement automatique à l'inscription des hôtes (auto-registration) sans validation.
- Limiter l'accès aux ports TFTP/NFS/HTTP aux VLAN de déploiement.
- Restreindre l'écrasement de disque : aucune tâche de déploiement sur un poste non désigné.

## Validation et retour arrière

- **Validation** : un hôte pilote atteint le menu FOG ; aucun autre poste du réseau n'est touché.
- **Retour arrière** : retirer les options DHCP 66/67 ; restaurer l'instantané en laboratoire.

## Si le problème n'est pas résolu

- [Documentation officielle FOG Project](https://docs.fogproject.org/)
- [Dépôt officiel FOG Project](https://github.com/FOGProject/fogproject)
- [Fiche d'entrée FOG Project](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_FOG-Project.md)
