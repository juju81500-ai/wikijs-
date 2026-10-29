# Fiche_Simple_-_VM_pfSense_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Mesurer ce que voit Internet.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis une machine externe au réseau, lancer un scan de l'adresse publique `IP_WAN_PUBLIQUE` (avec autorisation écrite) :
   ```sh
   nmap -Pn -sS -p- IP_WAN_PUBLIQUE
   ```
   👉 Explication : ne doit montrer que les ports publiés volontairement (ex. 1194/UDP pour OpenVPN).

2. Comparer aux règles WAN (Firewall > Rules > WAN) et aux redirections (Firewall > NAT > Port Forward).
   👉 Explication : toute exposition doit correspondre à une règle documentée.

## 2. Production — Contrôles

Répéter le scan après chaque changement de règle ou de NAT.

## 3. Production — Sécurité

Ne scanner que les adresses dont on est responsable.

## Validation et retour arrière

- **Validation** : Les ports ouverts vus d'Internet correspondent à la liste autorisée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)