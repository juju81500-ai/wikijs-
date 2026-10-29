# Fiche_Simple_-_VM_Debian_12_FreePBX_Configurer_Base.md

- **Environnement** : PBX installé, interface locale protégée et identifiants opérateur fournis par canal sûr
- **OS / Version** : FreePBX/Asterisk officiellement compatibles
- **Catégorie** : téléphonie IP / configuration
- **Tags** : `debian12`, `freepbx`, `asterisk`, `sip`, `tls`, `srtp`

---

## Problème précis à résoudre

Configurer les accès, trunks et routes d'appel de base sans exposer de secrets ni permettre les appels non autorisés.

## 1. Hors-Production (Lab / Test / POC)

1. Se connecter à l'interface locale protégée : **https://pbx.example.net/admin**, puis **Admin > Administrators > Add Administrator**.
   👉 Explication : créer un compte nominatif, puis supprimer ou désactiver les identifiants initiaux.

2. Créer le trunk : **Connectivity > Trunks > Add SIP (chan_pjsip) Trunk**.
   👉 Explication : saisir nom, hôte, identifiants fournis par l'opérateur; secret unique.

3. Créer deux extensions de test : **Applications > Extensions > Add Extension > Add New SIP [chan_pjsip] Extension**.
   👉 Explication : secret fort et unique par extension.

4. Configurer les routes : **Connectivity > Inbound Routes** et **Connectivity > Outbound Routes**.
   👉 Explication : restreindre les destinations (pas d'international ni de numéros surtaxés par défaut) et limiter le coût.

5. Activer TLS/SRTP : **Settings > Asterisk SIP Settings > Chan PJSIP Settings** (transport TLS) puis, par extension, **Advanced > Media Encryption**.
   👉 Explication : uniquement si tous les terminaux et l'opérateur le prennent en charge.

6. Appliquer : cliquer sur **Apply Config**.
   👉 Explication : sans ce clic, rien n'est pris en compte.

## 2. Production — Contrôles

Faire valider extensions, trunk, routes, destinations, coûts, comptes, certificats, protocole et responsabilités métier.

## 3. Production — Sécurité

- Ne pas conserver les identifiants initiaux.
- Ne pas réutiliser les secrets SIP et ne pas les inscrire dans la documentation.
- Interdire les destinations et routes à risque non nécessaires.
- Ne pas activer TLS/SRTP sans vérifier la compatibilité des terminaux et de l'opérateur.

## Validation et retour arrière

- **Validation** : comptes maîtrisés, extensions de test isolées et plan d'appel limité aux destinations approuvées.
- **Retour arrière** : restaurer la configuration précédente ou désactiver le trunk concerné sans supprimer les sauvegardes.

## Si le problème n'est pas résolu

- [FreePBX — documentation](https://www.freepbx.org/documentation/)
- [Asterisk — documentation](https://docs.asterisk.org/)
- [Guide complet FreePBX/Asterisk Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/13_Telephonie_IP_FreePBX_Asterisk_20_Debian_12.md)
