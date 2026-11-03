# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-39`

---

## Problème précis à résoudre

Remplacer le certificat auto-signé de l'interface web.

## 1. Hors-Production (Lab / Test / POC)

1. [[Glossary:GUI]] : **Nœud > System > Certificates > [[Glossary:ACME]]** (Let's Encrypt) ou **Upload Custom Certificate** pour un certificat de l'AC interne. En ligne de commande :
   ```bash
   pvenode cert info
   pvenode acme account register DEFAULT ADMIN_MAIL
   pvenode config set --acme domains=pve01.domaine.local
   pvenode acme cert order
   ```
   👉 Explication : ACME nécessite que le nom soit résolvable et validable ([[Glossary:HTTP]] ou [[Glossary:DNS]]); sinon utiliser l'AC interne.

2. Avec une AC interne, importer la chaîne :
   ```bash
   pvenode cert set cert.pem key.pem --force --restart
   ```
   👉 Explication : installe le certificat et redémarre `pveproxy`.

3. Contrôler le certificat servi :
   ```bash
   openssl s_client -connect IP_HOTE:8006 -servername $(hostname -f) </dev/null 2>/dev/null | openssl x509 -noout -dates -subject
   ```
   👉 Explication : affiche le sujet et les dates de validité.

## 2. Production — Contrôles

Suivre les dates d'expiration dans la supervision.

## 3. Production — Sécurité

Clé privée en `600`; ne jamais l'envoyer par e-mail.

## Validation et retour arrière

- **Validation** : Le navigateur n'affiche plus d'alerte de certificat.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Securiser](../vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-securiser.md)
- [Vie du système : les 50 étapes, tous OS](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md)
- [Sommaire Proxmox VE 8](./sommaire-vie-du-systeme-proxmox-ve-8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
