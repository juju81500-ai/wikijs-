# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-39`

---

## Problème précis à résoudre

Installer un certificat valide pour l'interface web.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Identifiants > Certificats > Ajouter > Importer un certificat (ou Créer une demande de signature CSR).
   ```bash
   sudo midclt call certificate.query | python3 -m json.tool | grep -E 'name|until'
   ```
   👉 Explication : liste les certificats et leurs dates d'expiration.

2. Appliquer le certificat : Système > Général > GUI > Certificat SSL GUI.
   ```bash
   sudo midclt call system.general.update '{"ui_certificate": ID_CERT}'
   ```
   👉 Explication : ID_CERT est l'identifiant du certificat dans la liste.

3. Tester :
   ```bash
   openssl s_client -connect NOM_NAS:443 </dev/null 2>/dev/null | openssl x509 -noout -dates -subject
   ```
   👉 Explication : affiche l'émetteur et les dates.

## 2. Production — Contrôles

Utiliser la PKI interne ou ACME ; surveiller l'expiration.

## 3. Production — Sécurité

Forcer HTTPS : Système > Général > Redirection HTTPS ; désactiver TLS 1.0/1.1.

## Validation et retour arrière

- **Validation** : Le navigateur ne signale plus d'erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
