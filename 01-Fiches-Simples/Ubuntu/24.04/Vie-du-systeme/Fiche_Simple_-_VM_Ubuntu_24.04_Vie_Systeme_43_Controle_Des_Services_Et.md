# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier l'état de service.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler :
   ```bash
   systemctl --failed
   sudo ss -tulpn
   ```
   👉 Explication : aucun service en échec et seulement les ports prévus.

## 2. Production — Contrôles

Comparer à l'inventaire des ports du dossier.

## 3. Production — Sécurité

Tout port non documenté est un écart.

## Validation et retour arrière

- **Validation** : `systemctl --failed` : 0 unité.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 24.04](./Sommaire_-_Vie_du_systeme_Ubuntu_24.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
