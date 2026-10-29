# Fiche_Simple_-_VM_OPNsense_Config_Restaurer.md

- **Environnement** : Appliance OPNsense physique ou virtuelle, seule ou en HA
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / sauvegarde-restauration

---

## Problème précis à résoudre

Restaurer l'export complet sur une release compatible.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le modèle de matériel, les interfaces et la version cible; installer une release compatible.
   👉 Explication : restaurer sur une version trop différente peut échouer.

2. **System > Configuration > Backups > Restore** : choisir le fichier, saisir le mot de passe de chiffrement, sélectionner la configuration complète puis **Restore configuration**.
   👉 Explication : la configuration est restaurée en entier.

3. Sur du matériel différent, conserver la console : réaffecter les interfaces dans **Interfaces > Assignments** ou via la console.
   👉 Explication : les noms d'interface peuvent changer.

4. Redémarrer si demandé : **Power > Reboot**.
   👉 Explication : certaines restaurations demandent un redémarrage.

5. Valider WAN/LAN, règles, DNS, VPN, certificats et administration avant de reconnecter au réseau.
   👉 Explication : on évite d'exposer un pare-feu mal configuré.

## 2. Production — Contrôles

Privilégier la restauration complète : les partielles créent des incohérences.

## 3. Production — Sécurité

- Ne pas reconnecter l'appliance au réseau avant validation.

## Validation et retour arrière

- **Validation** : Interfaces, règles et services conformes à l'export.
- **Retour arrière** : Réinstaller et restaurer la sauvegarde précédente ou revenir au snapshot ZFS (**System > Snapshots**).

## Si le problème n'est pas résolu

- [OPNsense — Sauvegardes de configuration](https://docs.opnsense.org/manual/backups.html)
- [OPNsense — Snapshots système](https://docs.opnsense.org/manual/snapshots.html)
- [Guide complet — restaurer](/02-fiches-completes/opnsense/toutes-versions/autres/36-sauvegarde-restauration-configuration-opnsense#4-restaurer)