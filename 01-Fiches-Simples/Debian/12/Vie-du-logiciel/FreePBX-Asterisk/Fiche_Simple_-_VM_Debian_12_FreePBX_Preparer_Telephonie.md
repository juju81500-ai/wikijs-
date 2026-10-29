# Fiche_Simple_-_VM_Debian_12_FreePBX_Preparer_Telephonie.md

- **Environnement** : VM ou serveur dédié, VLAN voix et accès console de secours
- **OS / Version** : OS et versions FreePBX/Asterisk officiellement compatibles à confirmer
- **Catégorie** : téléphonie IP / préparation
- **Tags** : `debian12`, `freepbx`, `asterisk`, `voip`, `sip`, `telephonie`

---

## Problème précis à résoudre

Définir l'architecture téléphonique et les flux nécessaires avant l'installation d'un PBX.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier IP, DNS et horloge :
   ```bash
   ip -br a
   getent hosts pbx.example.net
   timedatectl | grep -E 'synchronized|Time zone'
   ```
   👉 Explication : IP réservée, DNS valide, heure synchronisée (indispensable pour SIP/TLS et CDR).

2. Consigner les paramètres opérateur : adresses SIP, plage RTP (ex. 10000-20000/UDP), codecs, extensions, plan d'appel.
   👉 Explication : coordonner SIP/RTP avec l'opérateur; isoler téléphones et PBX dans un VLAN dédié.

3. Garantir l'accès console local avant toute règle réseau :
   ```bash
   sudo nft list ruleset | head -20
   ```
   👉 Explication : relever le pare-feu actuel; sauvegarder la configuration avant de le modifier.

## 2. Production — Contrôles

Faire approuver compatibilité, plan d'adressage, opérateur, trunks, plages média, coûts, sauvegardes et accès administratifs.

## 3. Production — Sécurité

- Ne pas publier l'interface d'administration ni SIP directement sur Internet.
- Ne pas mettre en service un couple OS/FreePBX/Asterisk non officiellement supporté.
- Ne pas ouvrir les ports avant d'avoir défini les réseaux autorisés.
- Prévoir protection contre les appels frauduleux et les destinations à coût élevé.

## Validation et retour arrière

- **Validation** : compatibilité confirmée, plan d'appel, VLAN, accès console et stratégie de reprise documentés.
- **Arrêt** : ne pas installer si l'image ou la méthode supportée par l'éditeur n'est pas identifiée.

## Si le problème n'est pas résolu

- [FreePBX — documentation](https://www.freepbx.org/documentation/)
- [Asterisk — documentation](https://docs.asterisk.org/)
- [Guide complet FreePBX/Asterisk Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/13_Telephonie_IP_FreePBX_Asterisk_20_Debian_12.md)
