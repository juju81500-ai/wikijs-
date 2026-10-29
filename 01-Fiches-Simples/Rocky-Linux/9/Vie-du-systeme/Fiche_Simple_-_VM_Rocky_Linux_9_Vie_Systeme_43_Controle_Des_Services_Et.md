# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Confirmer l'état des services.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services en échec :
   ```bash
   systemctl --failed
   ```
   👉 Explication : doit être vide.

2. Lister les ports en écoute :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : compare aux flux autorisés.

3. Rapprocher du pare-feu :
   ```bash
   sudo firewall-cmd --list-all
   ```
   👉 Explication : chaque port ouvert doit correspondre à un service.

## 2. Production — Contrôles

Comparer à la baseline.

## 3. Production — Sécurité

Tout port inconnu est enquêté.

## Validation et retour arrière

- **Validation** : Services et ports conformes au dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
