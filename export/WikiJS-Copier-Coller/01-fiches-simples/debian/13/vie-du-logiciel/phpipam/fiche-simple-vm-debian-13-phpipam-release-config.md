# Fiche_Simple_-_VM_Debian_13_phpIPAM_Release_Config.md

- **Environnement** : VM Debian 13, phpIPAM avec MariaDB locale, PHP-FPM et Nginx
- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3; PHP 8.4
- **Catégorie** : IPAM / installation

---

## Problème précis à résoudre

Télécharger phpIPAM 1.8.3, vérifier son empreinte et créer sa configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   cd /tmp
   curl --fail --location --proto '=https' --tlsv1.2 -o phpipam-v1.8.3.tgz https://github.com/phpipam/phpipam/releases/download/v1.8.3/phpipam-v1.8.3.tgz
   ```
   👉 Explication : télécharge l'archive officielle en HTTPS.

2. Exécuter :
   ```bash
   echo '2fc737da5a04a842cda097f609c4db85c808270eaad5949c4ec03d10f874556d  phpipam-v1.8.3.tgz' | sha256sum --check
   ```
   👉 Explication : compare l'empreinte SHA-256 publiée; arrêter si le résultat n'est pas OK.

3. Exécuter :
   ```bash
   tar -tzf phpipam-v1.8.3.tgz | head
   sudo tar -xzf phpipam-v1.8.3.tgz -C /var/www
   ```
   👉 Explication : examine le contenu puis extrait l'archive dans `/var/www`.

4. Exécuter :
   ```bash
   sudo ln -s /var/www/phpipam-v1.8.3 /var/www/phpipam
   sudo cp /var/www/phpipam/config.dist.php /var/www/phpipam/config.php
   ```
   👉 Explication : lie le dossier (vérifier son nom réel) et crée la configuration; si le chemin existe déjà, suivre la procédure de mise à niveau.

5. Exécuter :
   ```bash
   sudoedit /var/www/phpipam/config.php
   ```
   👉 Explication : renseigner l'hôte `127.0.0.1`, l'utilisateur `phpipam`, son mot de passe, la base `phpipam` et le port `3306`; garder `$debugging = false` et `$api_allow_unsafe = false`.

6. Exécuter :
   ```bash
   sudo chown root:www-data /var/www/phpipam/config.php
   sudo chmod 0640 /var/www/phpipam/config.php
   ```
   👉 Explication : protège le fichier qui contient le secret SQL.

## 2. Production — Contrôles

Ne pas écraser une instance existante; ne laisser `www-data` écrire que dans un dossier de données validé.

## 3. Production — Sécurité

- Pas de `chown -R www-data` sur le code.
- En-têtes proxy désactivés tant qu'aucun proxy de confiance n'est utilisé.
- Ne pas continuer si l'empreinte diffère.

## Validation et retour arrière

- **Validation** : `sha256sum --check` affiche OK et `config.php` est en `root:www-data` 0640.
- **Retour arrière** : supprimer le lien `/var/www/phpipam` et le dossier extrait (avant initialisation).

## Si le problème n'est pas résolu

- [phpIPAM — installation](https://phpipam.net/documents/installation/)
- [phpIPAM — releases officielles](https://github.com/phpipam/phpipam/releases)
- [phpIPAM — mise à niveau et restauration](https://phpipam.net/documents/upgrade/)
- [phpIPAM — configuration de référence 1.8.3](https://github.com/phpipam/phpipam/blob/v1.8.3/config.dist.php)
- [Guide complet Déployer phpIPAM 1.8.3 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13#4-telecharger-la-release-et-configurer-lapplication)