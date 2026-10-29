# Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Sauvegarder_Restaurer.md

- **Environnement** : VM pfSense CE en laboratoire sur Proxmox VE, deux interfaces (WAN et LAN isolés)
- **OS / Version** : pfSense Community Edition 2.9.0 (VM x86-64 sur Proxmox VE)
- **Catégorie** : pare-feu et routage

---

## Problème précis à résoudre

Disposer d'une sauvegarde chiffrée et prouver qu'elle se restaure.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Diagnostics > Backup & Restore > Backup Configuration**, choisir **All**, cocher le chiffrement et saisir une phrase secrète gérée hors bande, puis **Download configuration as XML**.
   👉 Explication : un export non chiffré contient des informations sensibles.

2. Stocker le fichier hors de la VM et de l'hôte Proxmox, avec accès limité.
   👉 Explication : la sauvegarde doit survivre à la perte de la VM.

3. Créer un clone isolé de la VM : **VM > Plus > Cloner**, puis supprimer ou déconnecter ses cartes réseau du LAN de production.
   👉 Explication : le clone sert à tester sans risque.

4. Dans le clone : **Diagnostics > Backup & Restore > Restore Configuration**, choisir le fichier, saisir la phrase secrète, **Restore**.
   👉 Explication : une sauvegarde complète d'une révision antérieure peut être migrée; une restauration partielle d'une autre révision n'est pas prise en charge.

5. Vérifier interfaces, IP, DHCP, règles et GUI avant de reconnecter un réseau.
   👉 Explication : le test réussit si la VM redémarre sans erreur, les interfaces sont sur les bons ponts et les règles appliquées.

6. Supprimer le clone et les médias d'installation devenus inutiles.
   👉 Explication : évite de laisser une copie du pare-feu.

## 2. Production — Contrôles

Planifier des sauvegardes avant chaque changement réseau, mise à niveau ou ajout de paquet et tester la restauration régulièrement.

## 3. Production — Sécurité

- Ne jamais stocker la phrase secrète à côté du fichier.
- Limiter l'accès aux sauvegardes.

## Validation et retour arrière

- **Validation** : le clone restauré fonctionne avec les mêmes règles et interfaces.
- **Retour arrière** : supprimer le clone de test; la VM d'origine n'est pas modifiée.

## Si le problème n'est pas résolu

- [Netgate — sauvegarde](https://docs.netgate.com/pfsense/en/latest/backup/configuration.html)
- [Netgate — restauration](https://docs.netgate.com/pfsense/en/latest/backup/restore.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Guide complet](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab#7-sauvegarder-et-eprouver-la-restauration)