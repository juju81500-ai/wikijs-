# Déployer Centreon 26.10 sur Debian 13

- **OS / Version** : Debian 13 Trixie; Centreon 26.10
- **Type de fiche** : Installation/Déploiement
- **Environnement** : VM Linux dédiée, serveur central Centreon et base locale
- **Machine ciblée** : Centreon Central
- **Catégorie** : Supervision / métrologie
- **Tags** : `centreon`, `debian13`, `supervision`, `snmp`, `monitoring`, `tls`

## 1. Préparer le serveur

Fiche simple : [préparer le serveur Centreon](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Preparer.md).

Centreon 26.10 prend en charge Debian 13. Prévoir DNS, IP fixe, fuseau horaire, serveur SMTP, certificat TLS, espace disque pour les données métriques et une sauvegarde testable. Dimensionner selon nombre de hôtes, services, intervalles et rétention.

La procédure officielle unattended exécute des opérations privilégiées et installe dépôts/services. Télécharger le script vers un fichier, vérifier le dépôt HTTPS officiel et lire son contenu avant exécution. Ne pas copier un script dans `bash` directement depuis une URL.

## 2. Télécharger et contrôler le script officiel

Fiche simple : [télécharger et contrôler le script officiel](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Script.md).

```bash
sudo install -d -m 0700 /root/centreon-install
cd /root/centreon-install
sudo curl -fL https://download.centreon.com/26.10/unattended.sh -o unattended.sh
sudo less unattended.sh
sudo bash unattended.sh -h
```

Confirmer le domaine `download.centreon.com`, la version 26.10 et les options proposées dans cette version. Si le script récupéré diffère des docs officielles ou contient des URL inattendues, arrêter et contacter le support Centreon.

## 3. Installer le Central avec TLS

Fiche simple : [installer le Central avec TLS](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Installer_Central.md).

Après sauvegarde de la VM et validation du DNS/certificat, lancer la procédure officielle en mode TLS :

```bash
sudo bash /root/centreon-install/unattended.sh install -t central -v 26.10 --tls enabled
```

Suivre le journal d'installation et l'emplacement des identifiants générés affichés par l'outil. Les protéger dans un coffre, supprimer le fichier temporaire après récupération et ne jamais les intégrer à un ticket ou à la documentation. Ne pas utiliser `-s` pendant la première installation si l'automatisation complète n'a pas été préalablement validée.

Le script configure les paquets Centreon, MariaDB et services locaux. Vérifier ses étapes finales et ne pas supposer que le wizard Web ou les rôles d'accès ont été terminés automatiquement.

## 4. Terminer l'assistant Web

Fiche simple : [terminer l'assistant Web](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Assistant_Web.md).

Ouvrir `https://centreon.example.net/centreon` depuis le réseau d'administration. Vérifier les dépendances, conserver les chemins recommandés, créer le compte `admin` avec un secret unique conservé au coffre et laisser le wizard initialiser les bases et modules.

Après installation, ne pas laisser l'accès à la page d'installation. Contrôler que TLS est présenté avec le certificat attendu et que l'accès HTTP suit la politique de redirection approuvée.

## 5. Initialiser la supervision

Fiche simple : [initialiser la supervision](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Initialiser_Supervision.md).

Dans **Configuration > Pollers**, exporter la configuration du Central en cochant **Move Export Files** selon la procédure Centreon, puis redémarrer les services de collecte/gestion nécessaires. Tester d'abord `localhost` et un hôte pilote autorisé; vérifier les données et logs avant d'ajouter d'autres cibles.

Pour les équipements, utiliser SNMPv3 authPriv en lecture seule quand disponible, limiter UDP/161 aux pollers et ne pas utiliser une communauté publique. Les credentials de supervision doivent être distincts des comptes d'administration.

## 6. Vérifier les services

Fiche simple : [vérifier les services](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Verifier_Services.md).

```bash
sudo systemctl --no-pager status mariadb apache2 php8.4-fpm gorgoned cbd centengine
sudo journalctl -b -p err --no-pager
```

Adapter le nom de service PHP à la version installée par le dépôt Centreon et examiner les journaux liés aux composants concernés. Les services de trap SNMP peuvent rester inactifs s'ils ne sont pas utilisés.

## 7. Sécuriser et exploiter

Fiche simple : [sécuriser et exploiter Centreon](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Securiser_Exploiter.md).

- Restreindre l'interface au réseau de gestion, activer MFA/SSO selon l'édition et attribuer des profils nominatifs.
- Configurer TLS et certificats selon les étapes officielles; ne pas désactiver durablement le pare-feu.
- Vérifier l'état SELinux lorsque la plateforme le fournit. Si une procédure de paquet nécessite une exception temporaire, la retirer après installation et appliquer la politique Centreon documentée.
- Sauvegarder bases, configuration, clés de chiffrement, plugins et données RRD; tester la restauration isolée.
- Avant upgrade, suivre la matrice officielle et sauvegarder le Central et les pollers.

## Sources

- [Centreon 26.10 — Installation unattended](https://docs.centreon.com/docs/installation/installation-of-a-central-server/unattended-install-central/)
- [Centreon 26.10 — Installation par paquets](https://docs.centreon.com/docs/installation/installation-of-a-central-server/using-packages/)
- [Centreon — Installation Web et post-installation](https://docs.centreon.com/docs/installation/web-and-post-installation/)
- [Centreon — Sécuriser la plateforme](https://docs.centreon.com/docs/administration/secure-platform/)
- [Centreon — Téléchargement officiel](https://download.centreon.com/)