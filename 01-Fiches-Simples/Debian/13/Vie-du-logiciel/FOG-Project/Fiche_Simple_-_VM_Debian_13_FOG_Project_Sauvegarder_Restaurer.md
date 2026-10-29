# Fiche_Simple_-_VM_Debian_13_FOG_Project_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 dédiée FOG Project (clonage/déploiement d'images), réseau de laboratoire isolé
- **OS / Version** : Debian 13 Trixie; FOG Project (version et support Debian 13 à vérifier)
- **Catégorie** : automatisation / déploiement
- **Tags** : `debian13`, `fog-project`, `sauvegarde`, `restauration`, `mariadb`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration FOG (base de données, paramètres, images) de manière testée.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier ce qui doit être sauvegardé : base de données FOG, `/opt/fog/.fogsettings`, `/images` (images), configuration TFTP/web/NFS modifiée.
   👉 Explication : se référer à la documentation FOG pour le périmètre exact de la version installée.

2. Sauvegarder la base avec un compte dédié (NOM_BASE_FOG à remplacer ; le mot de passe sera demandé) :
   ```bash
   mkdir -p ~/sauvegardes
   sudo mariadb-dump --single-transaction NOM_BASE_FOG | gzip > ~/sauvegardes/fog_$(date +%F).sql.gz
   ```
   👉 Explication : la commande dépend du paramétrage de la base ; vérifier l'authentification locale. Alternative : sauvegarde de base depuis l'interface FOG Configuration.

3. Copier les fichiers de configuration :
   ```bash
   sudo install -d -m 700 ~/sauvegardes
   sudo cp -a /opt/fog/.fogsettings ~/sauvegardes/
   ```
   👉 Explication : contient des secrets : protéger la copie.

4. Tester la restauration sur une VM de laboratoire distincte, avec la même version de FOG.
   👉 Explication : seule une restauration testée prouve la sauvegarde ; la version FOG doit rester identique.

## 2. Production — Contrôles

Production : sauvegarde externalisée et chiffrée, rétention définie, volume d'images dimensionné, restauration testée périodiquement, RPO/RTO documentés.

## 3. Production — Sécurité

- Chiffrer les sauvegardes et limiter l'accès (elles contiennent secrets et images).
- Ne pas stocker les sauvegardes sur la VM seule.
- Ne pas commiter les fichiers de sauvegarde.

## Validation et retour arrière

- **Validation** : dump lisible (`gzip -t`), restauration réussie en laboratoire.
- **Retour arrière** : revenir à la dernière sauvegarde validée ou à l'instantané.

## Si le problème n'est pas résolu

- [Documentation officielle FOG Project](https://docs.fogproject.org/)
- [Dépôt officiel FOG Project](https://github.com/FOGProject/fogproject)
- [Fiche d'entrée FOG Project](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_FOG-Project.md)
