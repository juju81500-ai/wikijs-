# Déployer OpenMediaVault 8 sur Debian 13

- **OS / Version** : Debian 13 Trixie minimal, OpenMediaVault 8.0 « Synchrony »
- **Type de fiche** : Installation/Déploiement
- **Rôle** : NAS autonome de laboratoire ou de petite structure

## 1. Choisir le mode de déploiement

Fiche simple : [choisir le mode de déploiement](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-choisir-mode).

Pour un serveur x86-64 dédié, la documentation recommande l'image ISO OpenMediaVault. Cette procédure couvre le cas d'une Debian 13 déjà installée, utile pour une VM ou un matériel où Debian a été préparé séparément.

**Ne pas installer OMV dans LXC ou un autre conteneur.** Ne pas convertir un serveur Debian qui héberge déjà des services critiques : OMV gère les paquets et peut remplacer la configuration réseau, SSH, Samba, Nginx et les montages. Prévoir un accès console hors bande, une sauvegarde et une fenêtre de maintenance.

Architecture minimale recommandée : disque système dédié et un ou plusieurs disques de données distincts, réseau Ethernet filaire, adresse IP statique et DNS fonctionnel. OMV ne considère pas officiellement le disque système comme disque de partage de données.

## 2. Préparer Debian 13

Fiche simple : [préparer Debian 13](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-preparer-debian).

Installer Debian 13 sans environnement graphique ni serveur Web; conserver seulement les utilitaires standard et SSH si nécessaire. Définir un nom d'hôte et une adresse statique, valider la résolution DNS et mettre Debian à jour.

```bash
sudo hostnamectl
sudo ip -br address
sudo ip route
sudo getent hosts packages.openmediavault.org
sudo apt update
sudo apt full-upgrade
sudo reboot
```

Après redémarrage, confirmer que l'administration locale fonctionne. Relever les numéros de série des disques et vérifier que le système démarre bien depuis le disque prévu; ne pas initialiser ni effacer le disque système dans OMV.

## 3. Installer OpenMediaVault depuis le dépôt signé

Fiche simple : [installer OpenMediaVault depuis le dépôt signé](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-installer-omv).

La méthode Debian documentée exige que `systemd-resolved` soit installé et actif avant d'ajouter les paquets. Configurer un serveur DNS accessible, de préférence le résolveur approuvé par le site :

```bash
sudo apt install --yes systemd-resolved psmisc gnupg
sudo systemctl enable --now systemd-resolved.service
sudo resolvectl dns <interface> <adresse_dns>
resolvectl status
```

Télécharger la clé officielle et l'installer dans le trousseau APT :

```bash
wget --quiet --output-document=- https://packages.openmediavault.io/archive.key \
  | sudo gpg --dearmor --yes --output /usr/share/keyrings/openmediavault-archive-keyring.gpg
```

Ajouter le dépôt stable Debian 13 « synchrony » dans `/etc/apt/sources.list.d/openmediavault.list` :

```text
deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] http://packages.openmediavault.org/public/ synchrony main
```

Mettre à jour l'index puis installer le paquet OMV avec les options prescrites par sa documentation :

```bash
export LANG=C.UTF-8
export DEBIAN_FRONTEND=noninteractive
export APT_LISTCHANGES_FRONTEND=none
sudo apt-get update
sudo apt-get --yes --auto-remove --show-upgraded \
  --allow-downgrades --allow-change-held-packages --no-install-recommends \
  --option DPkg::Options::="--force-confdef" \
  --option DPkg::Options::="--force-confold" \
  install openmediavault
```

La transaction peut remplacer ou réorganiser des services existants. Ne pas interrompre `dpkg` ni fermer l'alimentation durant l'installation. Après la fin, lire les erreurs éventuelles, puis initialiser la base de configuration et accéder à la console locale si le réseau doit être repris :

```bash
sudo omv-confdbadm populate
sudo omv-firstaid
```

`omv-confdbadm populate` récupère certaines configurations existantes, mais ne garantit pas la reprise d'un réseau configuré avec tous les gestionnaires. La documentation précise que la configuration réseau existante peut être réécrite et que l'adresse IP peut changer à l'application.

## 4. Première connexion et réseau

Fiche simple : [première connexion et réseau](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-premiere-connexion).

Depuis un navigateur situé sur le réseau d'administration, ouvrir l'adresse IP affichée par la console. Changer immédiatement le mot de passe initial du compte Web `admin`, créer un compte nominatif de gestion si approprié et limiter l'accès à l'interface et à SSH au réseau d'administration.

Configurer une adresse IPv4 statique et DNS dans l'interface OMV (`Network | Interfaces`). Appliquer les changements depuis la console locale ou une console hyperviseur : une session SSH peut être interrompue lorsque les paramètres réseau sont redéployés. Vérifier ensuite l'adresse, la passerelle, DNS et l'accès Web depuis une seconde machine.

Ne pas installer un autre serveur Web sur l'hôte. OMV utilise Nginx pour son interface; la documentation avertit que l'installation du paquet Apache peut supprimer OMV.

## 5. Intégrer un disque de données

Fiche simple : [intégrer un disque de données](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-disque-donnees).

Vérifier le périphérique et son numéro de série avant toute opération :

```bash
lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
sudo smartctl --scan-open
```

Dans l'interface, utiliser `Storage | Disks` pour identifier les disques. Si le disque de données doit être réinitialisé, sauvegarder d'abord les données et utiliser l'action de nettoyage seulement après avoir vérifié le numéro de série : **l'effacement supprime les signatures de partitions et de systèmes de fichiers**.

Créer le système de fichiers pris en charge via `Storage | File Systems`, puis le monter depuis la même interface. Ne pas ajouter manuellement le montage aux zones OMV de `/etc/fstab` : OMV conserve ses références de volumes dans sa base de configuration et redéploie les entrées gérées.

Pour un RAID logiciel, créer et surveiller l'ensemble mdadm via `Storage | RAID`. Choisir le niveau selon la capacité et la tolérance de panne attendues. Un RAID n'est pas une sauvegarde; ne jamais créer ou supprimer un ensemble sans sauvegarde vérifiée et plan de remplacement des disques.

## 6. Créer un partage SMB privé

Fiche simple : [créer un partage SMB privé](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-partage-smb).

1. Dans `Storage | Shared Folders`, créer un dossier sur le système de fichiers de données monté, par exemple `Equipe`, et attribuer des permissions initiales restrictives.
2. Dans `Users | Users` et `Users | Groups`, créer des comptes nominatifs et un groupe dédié. Ne pas partager le compte root.
3. Dans les permissions du dossier partagé, donner l'accès uniquement au groupe ou aux utilisateurs prévus. Les permissions OMV de service et les permissions POSIX/ACL sont deux couches distinctes; les deux doivent permettre l'accès.
4. Dans `Services | SMB/CIFS | Settings`, activer SMB et définir le groupe de travail selon l'environnement.
5. Dans `Services | SMB/CIFS | Shares`, créer un partage lié au dossier, activer l'accès non public, interdire l'invité et donner l'accès en lecture/écriture aux comptes nécessaires uniquement.
6. Enregistrer et appliquer les changements dans la bannière de configuration.

Tester depuis un client autorisé, sans inclure le mot de passe dans la ligne de commande :

```bash
smbclient -L //<adresse_omv> -U <utilisateur>
smbclient //<adresse_omv>/<partage> -U <utilisateur> -c 'ls'
```

Vérifier l'écriture et la suppression d'un fichier test avec un compte pilote. Vérifier qu'un compte non autorisé est refusé. Ne pas utiliser les modes « guest » ou permissions `777` pour résoudre un problème d'accès; analyser l'identité, les droits du partage, POSIX et ACL.

## 7. Durcissement, mises à jour et sauvegarde

Fiche simple : [durcissement, mises à jour et sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-durcissement).

- Garder SSH accessible uniquement au réseau d'administration; désactiver l'accès SSH direct à root une fois le service contrôlé et utiliser un compte non privilégié avec `sudo`.
- Restreindre l'interface Web à un VLAN ou sous-réseau de gestion. N'exposer aucun service NAS sur Internet; utiliser un VPN approuvé pour l'accès distant.
- Autoriser SMB sur TCP 445 uniquement depuis les clients prévus. Désactiver les options d'invité et d'anciens protocoles quand l'environnement le permet.
- Appliquer les mises à jour via `System | Update Management` ou `omv-upgrade`; ne pas mélanger Debian Backports, Testing ou Experimental dans le système OMV.
- Sauvegarder les données sur un autre système ou support hors ligne, avec une copie séparée des clés et éléments de configuration nécessaires. Tester périodiquement la restauration d'un dossier et d'un fichier avec leurs permissions.
- Si un plugin de sauvegarde de configuration est retenu, valider sa compatibilité OMV 8 et restaurer l'export sur une VM de test avant d'en dépendre.

## 8. Reprise et limites

Fiche simple : [reprise et limites](/01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-reprise).

Avant une mise à niveau majeure ou une modification de stockage, disposer d'une sauvegarde des données restaurable et d'un accès console. En cas d'échec réseau, utiliser la console et `omv-firstaid`; ne pas éditer directement les portions gérées d'`/etc/fstab` ou `smb.conf`.

Les commandes d'installation et le comportement décrits proviennent de la documentation OpenMediaVault 8 courante. L'installation, le partage SMB et la restauration n'ont pas été testés sur une VM dans ce workspace. La validation structurelle de cette fiche ne certifie pas l'état des disques ni la sécurité d'un réseau réel.

## Sources

- [OpenMediaVault 8 — Versions et Debian de base](https://docs.openmediavault.org/en/latest/releases.html)
- [OpenMediaVault — Installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — Prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [OpenMediaVault — Systèmes de fichiers](https://docs.openmediavault.org/en/latest/administration/storage/filesystems.html)
- [OpenMediaVault — Dossiers partagés et permissions](https://docs.openmediavault.org/en/latest/administration/storage/sharedfolders.html)
- [OpenMediaVault — Samba](https://docs.openmediavault.org/en/latest/administration/services/samba.html)
- [OpenMediaVault — RAID](https://docs.openmediavault.org/en/latest/administration/storage/raid.html)
- [OpenMediaVault — Mises à jour et paquets](https://docs.openmediavault.org/en/latest/various/apt.html)