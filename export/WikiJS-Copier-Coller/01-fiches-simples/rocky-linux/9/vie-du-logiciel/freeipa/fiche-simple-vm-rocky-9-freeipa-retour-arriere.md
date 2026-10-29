# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Retour_Arriere.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / retour arrière

---

## Problème précis à résoudre

Revenir à l'état antérieur après un échec d'installation ou un incident.

## 1. Hors-Production (Lab / Test / POC)

1. Avant installation : restaurer le snapshot de la VM.
   👉 Explication : le plus sûr et le plus rapide.

2. Désinstaller après échec (serveur non en production) :
   ```bash
   sudo ipa-server-install --uninstall
   ```
   👉 Explication : Après un échec d'installation : supprime la configuration IdM locale. À corriger (DNS, nom d'hôte, heure) avant de recommencer.

3. Après mise en production : restaurer le snapshot ou la sauvegarde sur une VM isolée, puis basculer les clients.
   👉 Explication : évite toute coupure sur le domaine utilisé.

## 2. Production — Contrôles

Ne jamais désinstaller le seul serveur IdM d'un domaine utilisé.

## 3. Production — Sécurité

- `--uninstall` supprime la configuration : l'utiliser seulement hors production ou après sauvegarde.

## Validation et retour arrière

- **Validation** : le serveur est revenu à l'état voulu et les clients s'authentifient.
- **Retour arrière** : restaurer la sauvegarde `ipa-backup` la plus récente sur VM isolée.

## Si le problème n'est pas résolu

- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 8](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9#8-retour-arriere)