# Fiche_Simple_-_VM_Ubuntu_24.04_Migration_26.04_Valider.md

- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers 26.04 LTS (Resolute)
- **Catégorie** : migration de version
- **Tags** : `ubuntu24.04`, `ubuntu26.04`, `migration`, `validation`

---

## Problème précis à résoudre

Contrôler le système et les applications après la migration.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier version, noyau et services :
   ```bash
   cat /etc/os-release
   uname -r
   systemctl --failed
   ```
   👉 Explication : on confirme Ubuntu 26.04 et l'absence de service en échec.

2. Vérifier réseau et DNS :
   ```bash
   ip -br address
   ip route
   resolvectl status
   ```
   👉 Explication : l'adressage, la route et le DNS doivent être inchangés.

3. Vérifier les paquets restants :
   ```bash
   apt list --upgradable
   ```
   👉 Explication : on termine les mises à jour éventuelles.

4. Contrôler services, tâches, certificats, dépôts, pare-feu, sauvegarde et supervision, puis tester chaque parcours applicatif depuis un client.
   👉 Explication : on valide le service rendu, pas seulement l'OS.

## 2. Production — Contrôles

Garder le snapshot jusqu'à la fin de la période de validation.

## 3. Production — Sécurité

- Contrôler que le pare-feu et SSH sont toujours correctement configurés.

## Validation et retour arrière

- **Validation** : Ubuntu 26.04 en place, services actifs et parcours applicatifs validés.
- **Retour arrière** : Restaurer la sauvegarde ou le snapshot validé.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet — valider après redémarrage](../../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/22_Migration_Ubuntu_Server_24.04_vers_26.04_LTS.md#6-valider-apres-redemarrage)
