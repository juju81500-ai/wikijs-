# Fiche_Simple_-_VM_Debian_13_ownCloud_Prerequis_Limites

- **Environnement** : VM Debian 13; ownCloud Infinite Scale (oCIS), binaire officiel, Nginx
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / ownCloud — Prérequis et limites
- **Tags** : `debian13`, `owncloud`, `ocis`, `cloud`, `prerequis-limites`

---

## Problème précis à résoudre

Choisir la variante ownCloud adaptée à Debian 13 : ownCloud Infinite Scale (oCIS, binaire unique) car la compatibilité d'ownCloud Classic 10 (PHP 8.4 de Debian 13) n'est pas confirmée.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et les ressources :
   ```bash
   cat /etc/os-release | head -3
   free -h
   df -h /var
   ```
   👉 Explication : dimensionner selon la documentation officielle (RAM, stockage des données et des métadonnées).

2. Vérifier la prise en charge de la variante visée :
   👉 Explication : avant de choisir ownCloud Classic 10 (PHP, paquets du dépôt officiel), consulter la matrice officielle : Debian 13/PHP 8.4 n'y figure pas forcément (à vérifier). Pour Classic sur Debian 12, voir la fiche existante du pack (lien en bas). Cette série traite oCIS.

3. Contrôler que le port 9200 est libre et le nom DNS :
   ```bash
   sudo ss -tlnp | grep ':9200' || echo libre
   hostnamectl --static
   ```
   👉 Explication : oCIS écoute par défaut sur 9200 ; nom DNS `OCIS.EXAMPLE.NET` à remplacer.

4. Identifier la version à déployer :
   ```bash
   curl -fsSL https://download.owncloud.com/ocis/ocis/stable/ | head -40
   ```
   👉 Explication : la page liste les versions stables publiées (`OCIS_VERSION`, à remplacer) ; lire les notes de version avant de choisir.

## 2. Production — Contrôles

Documenter variante (Classic ou oCIS), version, FQDN, stockage, authentification (OIDC interne par défaut) et propriétaire. oCIS stocke données et métadonnées dans un dossier unique à sauvegarder.

## 3. Production — Sécurité

- Snapshot de VM avant installation.
- Ne pas confondre les deux produits : leurs procédures de sauvegarde et de mise à jour diffèrent.

## Validation et retour arrière

- **Validation** : variante, version et prérequis consignés.
- **Retour arrière** : aucune modification n'a été faite : rien à annuler.

## Si le problème n'est pas résolu

- [ownCloud — Installer](Fiche_Simple_-_VM_Debian_13_ownCloud_Installer.md)
- [ownCloud — Configurer](Fiche_Simple_-_VM_Debian_13_ownCloud_Configurer.md)
- [ownCloud Classic 10 sur Debian 12 (fiche existante)](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Simple_-_ownCloud.md)
- [ownCloud Infinite Scale — documentation officielle](https://doc.owncloud.com/ocis/next/)
- [ownCloud — téléchargements](https://owncloud.com/download-server/)
