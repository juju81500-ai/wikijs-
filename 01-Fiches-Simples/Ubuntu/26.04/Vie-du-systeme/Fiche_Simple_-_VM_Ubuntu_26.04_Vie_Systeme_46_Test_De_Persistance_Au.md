# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-46`

---

## Problème précis à résoudre

Vérifier le démarrage sans intervention.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer puis contrôler :
   ```bash
   sudo reboot
   # après reconnexion :
   uptime
   cloud-init status
   findmnt --verify
   ip -br address
   sudo ufw status
   systemctl --failed
   ```
   👉 Explication : disques montés, réseau, pare-feu et services revenus; `cloud-init status` doit indiquer `done`.

## 2. Production — Contrôles

Prévoir la fenêtre et l'accès console.

## 3. Production — Sécurité

Vérifier le pare-feu après redémarrage.

## Validation et retour arrière

- **Validation** : Tout revient sans action manuelle.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
