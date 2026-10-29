# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier le démarrage sans intervention.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer puis contrôler :
   ```bash
   sudo reboot
   # après reconnexion :
   uptime
   findmnt --verify
   ip -br address
   systemctl --failed
   ```
   👉 Explication : disques montés, réseau et services revenus.

## 2. Production — Contrôles

Prévoir la fenêtre et l'accès console.

## 3. Production — Sécurité

Vérifier le pare-feu après redémarrage.

## Validation et retour arrière

- **Validation** : Tout revient sans action manuelle.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)