# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Disposer des outils d'exploitation de base.

## 1. Hors-Production (Lab / Test / POC)

1. Utiliser le menu console (option 8 : Shell) et les outils intégrés d'Interfaces > Diagnostics : Ping, Traceroute, Capture de paquets, Tables d'états.
   👉 Explication : ces outils couvrent la plupart des diagnostics sans paquet supplémentaire.

2. Vérifier les commandes essentielles en shell :
   ```sh
   which tcpdump pfctl drill sockstat netstat
   tcpdump -ni vtnet0 -c 5
   ```
   👉 Explication : confirme la présence des outils et capture 5 paquets sur l'interface `vtnet0`.

## 2. Production — Contrôles

Documenter les commandes de diagnostic standard dans le runbook.

## 3. Production — Sécurité

Les captures de paquets contiennent des données sensibles : les supprimer après usage.

## Validation et retour arrière

- **Validation** : Les outils répondent et la capture fonctionne.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
