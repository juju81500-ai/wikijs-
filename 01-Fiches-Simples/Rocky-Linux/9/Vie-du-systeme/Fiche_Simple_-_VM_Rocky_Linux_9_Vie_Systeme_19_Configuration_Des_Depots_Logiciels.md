# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Disposer de dépôts fiables.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les dépôts actifs :
   ```bash
   dnf repolist
   ls /etc/yum.repos.d/
   ```
   👉 Explication : BaseOS et AppStream sont activés par défaut; aucun abonnement n'est requis.

2. Activer CRB et EPEL si nécessaire :
   ```bash
   sudo dnf config-manager --set-enabled crb
   sudo dnf install -y epel-release
   ```
   👉 Explication : CRB fournit des dépendances de développement; EPEL ajoute des paquets communautaires (fail2ban...).

3. Vérifier que la signature GPG est exigée :
   ```bash
   grep -H gpgcheck /etc/yum.repos.d/*.repo
   ```
   👉 Explication : doit afficher `gpgcheck=1`.

## 2. Production — Contrôles

Utiliser un miroir ou un dépôt interne (Pulp, Katello) en production.

## 3. Production — Sécurité

Ne jamais mettre `gpgcheck=0`.

## Validation et retour arrière

- **Validation** : `dnf repolist` liste les dépôts attendus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
