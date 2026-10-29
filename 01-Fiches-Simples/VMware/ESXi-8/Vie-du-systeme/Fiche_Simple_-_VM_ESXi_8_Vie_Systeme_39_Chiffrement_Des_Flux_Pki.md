# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-39`

---

## Problème précis à résoudre

Remplacer le certificat auto-signé de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Sécurité > Certificats** (afficher). Pour installer un certificat signé, copier la clé et le certificat dans `/etc/vmware/ssl/` (SSH) :
   ```sh
   ls -l /etc/vmware/ssl/
   openssl x509 -in /etc/vmware/ssl/rui.crt -noout -subject -dates
   ```
   👉 Explication : `rui.crt` et `rui.key` sont le certificat et la clé du Host Client.

2. Remplacer le certificat (après sauvegarde des anciens) puis redémarrer les agents :
   ```sh
   cp /etc/vmware/ssl/rui.crt /etc/vmware/ssl/rui.crt.bak
   cp NOUVEAU.crt /etc/vmware/ssl/rui.crt
   cp NOUVEAU.key /etc/vmware/ssl/rui.key
   /etc/init.d/hostd restart && /etc/init.d/vpxa restart
   ```
   👉 Explication : `NOUVEAU.crt` = certificat de l'AC interne; `hostd` recharge l'interface web.

3. Pour un hôte sous vCenter, utiliser la VMCA (vSphere Client : **Hôte > Configurer > Système > Certificat > Renouveler**).
   👉 Explication : vCenter gère les certificats de ses hôtes.

## 2. Production — Contrôles

Suivre les dates d'expiration dans la supervision.

## 3. Production — Sécurité

Clé privée en `600`; ne jamais l'envoyer par e-mail.

## Validation et retour arrière

- **Validation** : Le navigateur n'affiche plus d'alerte de certificat.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
