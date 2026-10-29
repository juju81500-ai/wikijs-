# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-46`

---

## Problème précis à résoudre

Vérifier que la configuration survit au redémarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer : Système > Alimentation > Redémarrer, ou console option 6; en shell :
   ```sh
   configctl system reboot
   ```
   👉 Explication : redémarre proprement le pare-feu.

2. Contrôler après redémarrage :
   ```sh
   uptime
   ifconfig -l
   pfctl -si | head -3
   sockstat -4 -l | head
   ```
   👉 Explication : interfaces, pf et services doivent être revenus comme avant.

## 2. Production — Contrôles

Planifier le test en fenêtre de maintenance.

## 3. Production — Sécurité

Prévoir l'accès console en cas de blocage.

## Validation et retour arrière

- **Validation** : Interfaces, règles et services identiques après redémarrage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
