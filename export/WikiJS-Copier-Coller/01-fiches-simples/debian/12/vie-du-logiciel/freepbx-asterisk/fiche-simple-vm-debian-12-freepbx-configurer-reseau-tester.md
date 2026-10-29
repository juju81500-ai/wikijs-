# Fiche_Simple_-_VM_Debian_12_FreePBX_Configurer_Reseau_Tester.md

- **Environnement** : VLAN voix, téléphones pilotes et trunk de test fournis par l'opérateur
- **OS / Version** : FreePBX/Asterisk selon versions supportées
- **Catégorie** : téléphonie IP / réseau et recette

---

## Problème précis à résoudre

Valider les appels et les flux SIP/RTP tout en limitant l'exposition aux seuls terminaux et opérateurs attendus.

## 1. Hors-Production (Lab / Test / POC)

1. Limiter SIP/TLS et RTP aux réseaux de téléphones et aux adresses de l'opérateur (exemple nftables, à adapter) :
   ```bash
   sudo nft add rule inet filter input ip saddr 192.0.2.0/24 tcp dport 5061 accept
   sudo nft add rule inet filter input ip saddr 192.0.2.0/24 udp dport 10000-20000 accept
   ```
   👉 Explication : remplacer le réseau; table et chaîne `inet filter input` supposées existantes. Pas d'ouverture à Internet.

2. Désactiver les services inutiles : **Settings > Asterisk SIP Settings** (désactiver chan_sip si inutilisé) et vérifier :
   ```bash
   sudo ss -lunp | grep -E 'asterisk|:5060|:5061'
   ```
   👉 Explication : aucun port de découverte ou de protocole non utilisé.

3. Tester les appels internes, entrants et sortants avec un numéro de test convenu avec l'opérateur :
   ```bash
   sudo asterisk -rvvv
   ```
   👉 Explication : suivre les appels en direct; **jamais** de vrais appels d'urgence. Quitter avec `exit`.

4. Vérifier l'enregistrement du trunk et des journaux :
   ```bash
   sudo asterisk -rx 'pjsip show registrations'
   sudo tail -50 /var/log/asterisk/full
   ```
   👉 Explication : contrôler aussi l'horloge, puis simuler une perte du trunk (le désactiver) et constater le comportement.

## 2. Production — Contrôles

Valider tests d'appel, destinations, plages RTP, règles pare-feu, qualité audio, procédure de panne opérateur et obligations locales.

## 3. Production — Sécurité

- Ne pas exposer SIP ou l'administration à tout Internet.
- Ne pas lancer d'appel réel d'urgence en test.
- Ne pas autoriser des flux provenant d'adresses non confirmées par l'opérateur.
- Protéger les journaux d'appel et données de messagerie vocale selon leur classification.

## Validation et retour arrière

- **Validation** : appels de test contrôlés, audio et DTMF conformes, flux minimaux appliqués et panne trunk détectée.
- **Retour arrière** : retirer les règles temporaires et revenir au plan réseau précédent sans perdre l'accès console.

## Si le problème n'est pas résolu

- [FreePBX — documentation](https://www.freepbx.org/documentation/)
- [Asterisk — documentation](https://docs.asterisk.org/)
- [Guide complet FreePBX/Asterisk Debian](/02-fiches-completes/debian/12/installation-deploiement/13-telephonie-ip-freepbx-asterisk-20-debian-12)