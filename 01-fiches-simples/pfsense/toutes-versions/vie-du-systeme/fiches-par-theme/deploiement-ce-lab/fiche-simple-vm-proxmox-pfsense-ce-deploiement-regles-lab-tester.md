# fiche-simple-vm-proxmox-pfsense-ce-deploiement-regles-lab-tester.md

- **Environnement** : [[Glossary:VM]] pfSense CE en laboratoire sur Proxmox VE, deux interfaces ([[Glossary:WAN]] et [[Glossary:LAN]] isolés)
- **OS / Version** : pfSense Community Edition 2.9.0 (VM x86-64 sur Proxmox VE)
- **Catégorie** : pare-feu et routage
- **Tags** : `pfsense`, `ce`, `proxmox`, `firewall`, `lab`

---

## Problème précis à résoudre

Réduire les règles au strict nécessaire et vérifier leur effet.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Firewall > Rules > LAN** et remplacer la règle générale de sortie par les seuls flux d'essai : [[Glossary:DNS]] vers le résolveur désigné, [[Glossary:NTP]] si requis, flux applicatifs nécessaires.
   👉 Explication : refus par défaut et autorisation minimale, comme le recommande Netgate.

2. Documenter chaque règle et son motif dans sa description.
   👉 Explication : permet de relire et justifier les règles.

3. Ne créer aucune règle WAN « any/any ».
   👉 Explication : cela ouvrirait le pare-feu à l'amont.

4. Depuis le client autorisé, tester l'accès au [[Glossary:GUI]] et la résolution DNS (remplacer `exemple.lab` par un nom de votre lab) :
   ```bash
   nslookup exemple.lab 192.168.1.1
   ```
   👉 Explication : vérifie que le DNS attendu répond.

5. Tester un flux sortant autorisé, puis un flux non autorisé qui doit être bloqué.
   👉 Explication : confirme que la règle est appliquée comme prévu.

6. Depuis le segment WAN de lab, confirmer qu'aucun accès GUI/SSH entrant n'est accepté, puis lire **Status > System Logs > Firewall**.
   👉 Explication : les flux de test doivent apparaître sur la règle attendue.

## 2. Production — Contrôles

Soumettre les règles à revue réseau avant toute extension; ces vérifications ne servent pas à scanner un réseau tiers.

## 3. Production — Sécurité

- Ne tester que sur l'infrastructure de lab.

## Validation et retour arrière

- **Validation** : flux autorisé passant, flux interdit bloqué, aucun accès entrant WAN.
- **Retour arrière** : restaurer la sauvegarde de configuration précédente ou rétablir la règle LAN d'origine.

## Si le problème n'est pas résolu

- [Netgate — bonnes pratiques firewall](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Guide complet](../../../../../../02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab.md#6-definir-et-tester-les-regles-du-laboratoire)
