# Fiche_Simple_-_VM_OPNsense_Config_Exporter.md

- **Environnement** : Appliance OPNsense physique ou virtuelle, seule ou en HA
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / sauvegarde-restauration
- **Tags** : `opnsense`, `sauvegarde`, `configuration`, `export`, `chiffrement`

---

## Problème précis à résoudre

Exporter la configuration complète protégée par mot de passe.

## 1. Hors-Production (Lab / Test / POC)

1. **System > Configuration > Backups** : dans la section Download, cocher l'option de chiffrement, saisir un mot de passe fort et unique puis cliquer sur **Download configuration**.
   👉 Explication : le fichier XML téléchargé est chiffré; ne jamais l'envoyer en clair.

2. Ranger le fichier et le mot de passe séparément, dans un coffre sécurisé.
   👉 Explication : qui possède les deux peut restaurer ou lire les secrets.

3. Option console : repérer le fichier de configuration actif et les sauvegardes locales :
   ```bash
   ls -l /conf/config.xml
   ls /conf/backup | tail
   ```
   👉 Explication : `/conf/config.xml` est la configuration en cours; `/conf/backup` garde les révisions locales.

## 2. Production — Contrôles

Exporter après chaque changement majeur et conserver un historique conforme à l'audit.

## 3. Production — Sécurité

- Ne pas exposer l'interface Web sur Internet pour automatiser la sauvegarde.
- Pour automatiser, utiliser SFTP ou une intégration approuvée en vérifiant l'authenticité du serveur distant.

## Validation et retour arrière

- **Validation** : Le fichier exporté est présent, daté et son mot de passe est dans le coffre.
- **Retour arrière** : L'export ne modifie rien : supprimer le fichier si nécessaire.

## Si le problème n'est pas résolu

- [OPNsense — Sauvegardes de configuration](https://docs.opnsense.org/manual/backups.html)
- [OPNsense — Snapshots système](https://docs.opnsense.org/manual/snapshots.html)
- [Guide complet — exporter une sauvegarde chiffrée](../../../../../../02-Fiches-Completes/OPNsense/Toutes-versions/Autres/36_Sauvegarde_Restauration_Configuration_OPNsense.md#2-exporter-une-sauvegarde-chiffree)
