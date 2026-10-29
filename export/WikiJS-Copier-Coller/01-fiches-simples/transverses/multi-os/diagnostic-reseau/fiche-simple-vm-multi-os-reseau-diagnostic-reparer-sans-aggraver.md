# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Reparer_Sans_Aggraver.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / correction

---

## Problème précis à résoudre

Corriger la cause identifiée avec le changement le plus petit possible.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration réseau avant modification (exemple Netplan) :
   ```bash
   sudo cp -a /etc/netplan /etc/netplan.sauvegarde
   ```
   👉 Explication : une copie permet le retour arrière en cas d'erreur.

2. Corriger uniquement le profil possédé par le gestionnaire réseau actif (Netplan, NetworkManager, systemd-networkd, Windows, Proxmox).
   👉 Explication : modifier un autre outil créerait des conflits de configuration.

3. Pare-feu : lire d'abord les règles existantes, puis ajouter une règle minimale (source, destination, protocole, port).
   👉 Explication : on ouvre le strict nécessaire au lieu de désactiver la protection.

4. Refaire seulement le test qui avait échoué, en gardant une session de secours ouverte.
   👉 Explication : on confirme l'effet d'un seul changement à la fois.

## 2. Production — Contrôles

Une seule modification à la fois, avec fenêtre de maintenance approuvée.

## 3. Production — Sécurité

- Ne pas désactiver le pare-feu ni redémarrer toute la pile réseau pour « tester ».
- Ne pas figer `/etc/resolv.conf`.

## Validation et retour arrière

- **Validation** : Le test précédemment en échec passe.
- **Retour arrière** : Restaurer la sauvegarde (`sudo cp -a /etc/netplan.sauvegarde/. /etc/netplan/`) depuis la console puis rappliquer la configuration.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 9. Réparer sans aggraver la panne](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os#9-reparer-sans-aggraver-la-panne)