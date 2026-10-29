# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Valider la détection des pannes.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter volontairement un service de test :
   ```bash
   sudo systemctl stop nginx
   ```
   👉 Explication : provoque une alerte.

2. Vérifier l'alerte et le redémarrage automatique :
   ```bash
   sudo systemctl start nginx
   sudo systemctl status nginx --no-pager
   ```
   👉 Explication : confirme la remontée dans la supervision.

3. Simuler une charge disque ou mémoire :
   ```bash
   stress-ng --vm 1 --vm-bytes 80% --timeout 60s
   ```
   👉 Explication : `stress-ng` (EPEL) valide les seuils d'alerte.

## 2. Production — Contrôles

Faire le test en fenêtre convenue.

## 3. Production — Sécurité

Pas de test destructif sur un système de production sans accord.

## Validation et retour arrière

- **Validation** : Alerte reçue et service rétabli.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Supervision Zabbix Agent2](<../Vie-du-logiciel/Zabbix/Fiche_Simple_-_VM_Rocky_9_Supervision_Zabbix_Agent2.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
