# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-46`

---

## Problème précis à résoudre

Vérifier que tout redémarre seul.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer la machine :
   ```sh
   doas reboot
   ```
   👉 Explication : relance le système, en fenêtre de maintenance.

2. Après redémarrage, contrôler les services et l'uptime :
   ```sh
   uptime
   rc-status
   rc-status --crashed
   ```
   👉 Explication : tous les services attendus sont `started`, aucun service en échec.

3. Contrôler le réseau et l'heure :
   ```sh
   ip -br addr
   chronyc tracking | head -3
   ```
   👉 Explication : l'adresse fixe est restaurée et l'heure synchronisée.

## 2. Production — Contrôles

Planifier le test avant la mise en production et après chaque changement important.

## 3. Production — Sécurité

Sur un système diskless, vérifier que la configuration revient bien de l'archive `.apkovl`.

## Validation et retour arrière

- **Validation** : Tout est revenu à l'état attendu sans intervention.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
