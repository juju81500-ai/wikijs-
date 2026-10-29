# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-46`

---

## Problème précis à résoudre

Prouver que la configuration survit au reboot.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer :
   ```bash
   sudo reboot
   ```
   👉 Explication : redémarrage contrôlé en fenêtre prévue.

2. Contrôler après redémarrage :
   ```bash
   systemctl --failed
   sudo firewall-cmd --list-all
   getenforce
   ip -br a
   ```
   👉 Explication : services, pare-feu, SELinux et réseau.

3. Contrôler le temps de démarrage :
   ```bash
   systemd-analyze blame | head
   ```
   👉 Explication : repère les services lents.

## 2. Production — Contrôles

Prévoir une console hors bande.

## 3. Production — Sécurité

Vérifier que les protections reviennent actives.

## Validation et retour arrière

- **Validation** : Tout est conforme après reboot.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
