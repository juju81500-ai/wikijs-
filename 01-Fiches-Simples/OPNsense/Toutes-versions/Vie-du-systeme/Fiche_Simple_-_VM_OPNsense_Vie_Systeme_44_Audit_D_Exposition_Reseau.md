# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-44`

---

## Problème précis à résoudre

Mesurer ce que voit Internet.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis une machine externe au réseau, lancer un scan de l'adresse publique `IP_WAN_PUBLIQUE` (avec autorisation écrite) :
   ```sh
   nmap -Pn -sS -p- IP_WAN_PUBLIQUE
   ```
   👉 Explication : ne doit montrer que les ports publiés volontairement (ex. 51820/UDP pour WireGuard).

2. Depuis le pare-feu, comparer aux règles WAN (Pare-feu > Règles > WAN) et aux redirections (Pare-feu > NAT > Redirection de port).
   👉 Explication : toute exposition doit correspondre à une règle documentée.

## 2. Production — Contrôles

Répéter le scan après chaque changement de règle ou de NAT.

## 3. Production — Sécurité

Ne scanner que les adresses dont on est responsable.

## Validation et retour arrière

- **Validation** : Les ports ouverts vus d'Internet correspondent à la liste autorisée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
