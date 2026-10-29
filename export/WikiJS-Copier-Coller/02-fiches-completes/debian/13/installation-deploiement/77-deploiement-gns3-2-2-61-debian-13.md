# Déployer GNS3 2.2.61 sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : interface graphique et serveur GNS3 local par `pipx`, QEMU/KVM et laboratoire isolé
- **Catégorie** : simulation réseau / laboratoire

## 1. Version et périmètre

Fiche simple : [cadrer version et périmètre](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-version-perimetre).

Au 27 octobre 2026, GNS3 2.2.61 est la dernière version stable publiée; GNS3 3.1 est encore en préversion alpha. Le guide Linux amont documente Debian par `pipx` et précise que GNS3 n'est pas disponible dans les dépôts APT Debian en tant que paquet natif. La branche 3.1 alpha n'est pas utilisée ici.

Cette fiche installe l'interface et le serveur sur un poste Debian 13 amd64, avec QEMU/KVM pour les machines de lab. Le serveur reste local. Aucun lien Cloud, NAT externe, pont vers une carte physique, image propriétaire ou scénario d'attaque n'est inclus. Les appliances disponibles au Marketplace ne remplacent pas les images logicielles: obtenir ces images directement auprès de leur éditeur et respecter leurs licences.

Prévoir un environnement graphique, la virtualisation CPU activée dans le firmware, plusieurs coeurs/Go de mémoire et de l'espace disque dédié aux images et projets. Sur une machine virtuelle, la virtualisation imbriquée doit être prise en charge par l'hyperviseur.

## 2. Installer les dépendances Debian 13

Fiche simple : [installer les dépendances Debian](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-dependances).

Mettre APT à jour et installer les prérequis explicitement indiqués dans la documentation GNS3 pour les distributions Debian. Dynamips est volontairement omis; il est optionnel et son installation Debian 13 amont nécessite une compilation séparée.

```bash
sudo apt update
sudo apt install -y python3 python3-pip pipx python3-pyqt6 python3-pyqt6.qtwebsockets python3-pyqt6.qtsvg qemu-kvm qemu-utils libvirt-clients libvirt-daemon-system virtinst ubridge vpcs ca-certificates curl gnupg2
```

Vérifier les paquets et la virtualisation locale :

```bash
python3 --version
qemu-system-x86_64 --version
sudo systemctl enable --now libvirtd
ls -l /dev/kvm
```

Si `/dev/kvm` n'existe pas, arrêter: vérifier les extensions VT-x/AMD-V, le noyau et, si pertinent, la virtualisation imbriquée avant de créer des appliances QEMU. Ne pas contourner l'absence de virtualisation avec des réglages de privilèges non documentés.

## 3. Installer l'interface et le serveur stables

Fiche simple : [installer l'interface et le serveur](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-installer-gui-serveur).

Installer une version identique du client et du serveur dans des environnements Python séparés. `pipx` évite d'écrire dans le Python système géré par Debian :

```bash
pipx ensurepath
pipx install gns3-server==2.2.61
pipx install gns3-gui==2.2.61
pipx inject gns3-gui gns3-server==2.2.61 PyQt6
```

Fermer puis rouvrir la session utilisateur pour que `~/.local/bin` soit dans le PATH. Contrôler les exécutables :

```bash
command -v gns3
command -v gns3server
gns3 --version
gns3server --version
```

Ne pas mélanger le dépôt PPA Ubuntu, les paquets système PyPI installés par `sudo pip` et les environnements `pipx`. En cas de dépendance indisponible sur Trixie, arrêter et revoir la compatibilité au lieu de forcer une version non stable.

## 4. Accorder les accès minimaux nécessaires

Fiche simple : [accorder les accès minimaux](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-acces-minimaux).

GNS3 et QEMU nécessitent des accès locaux pour créer des interfaces virtuelles et employer KVM/libvirt. Utiliser un compte nominatif de laboratoire et l'ajouter seulement aux groupes requis par les fonctions employées :

```bash
getent group ubridge libvirt kvm
sudo usermod -aG ubridge,libvirt,kvm "$USER"
```

Fermer puis rouvrir la session et vérifier les groupes avec `id`. N'ajouter `wireshark` que si une activité de capture distincte et autorisée le justifie. Ne pas ajouter le compte au groupe `docker` pour cette procédure: cet accès est équivalent à un contrôle privilégié de l'hôte.

## 5. Configurer le serveur local et lancer un projet isolé

Fiche simple : [configurer le serveur local et un projet isolé](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-projet-isole).

Lancer l'interface GNS3 depuis le menu de bureau ou avec `gns3`. Dans l'assistant de premier démarrage, choisir le serveur local et vérifier que l'adresse du serveur est la boucle locale. Ne pas configurer un serveur distant, un compute partagé ou une interface physique sans procédure de changement et contrôle d'accès séparés.

Créer un projet de laboratoire puis utiliser uniquement des éléments intégrés ou des images libres et vérifiées. Garder les noeuds et commutateurs internes dans le projet; ne pas relier le noeud Cloud à une interface physique et ne pas ajouter de lien NAT si l'objectif est un lab fermé.

Pour un essai d'interface sans image propriétaire, créer une topologie dessinée, enregistrer le projet, fermer et le rouvrir. Si une appliance QEMU est ajoutée, importer une image obtenue à sa source autorisée, vérifier son empreinte lorsqu'elle est publiée par l'éditeur et attribuer des ressources compatibles avec l'hôte.

Les templates du GNS3 Marketplace décrivent comment préparer une appliance; ils ne donnent pas automatiquement un droit d'utilisation des images d'OS, routeurs, pare-feux ou systèmes commerciaux. Ne pas télécharger d'images depuis des miroirs non autorisés.

## 6. Vérifier les projets et le périmètre réseau

Fiche simple : [vérifier projets et périmètre réseau](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-verifier-perimetre).

- L'interface se connecte au serveur local et l'état du serveur est sain.
- Le projet de test s'enregistre, se ferme et se rouvre sans image ou fichier manquant.
- Une appliance libre de test, si utilisée, démarre et s'arrête normalement sans dépassement des ressources de l'hôte.
- Le projet ne contient aucun lien vers une interface physique, un pont de production ou un réseau tiers.
- Les journaux, fichiers de configuration et projets ne contiennent pas de secrets réutilisables.

Un résultat d'émulation ne valide pas le fonctionnement d'un équipement réel ni sa configuration de production. Faire relire et documenter les hypothèses avant de réutiliser un diagramme ou un fichier de configuration.

## 7. Sauvegarder, mettre à jour et nettoyer

Fiche simple : [sauvegarder, mettre à jour et nettoyer](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-sauvegarde-maj).

Enregistrer le projet, les fichiers de configuration et les images séparément dans un espace contrôlé. Sauvegarder les fichiers du projet; sauvegarder les images uniquement si leur licence le permet. Tester l'ouverture de la copie dans un second profil ou poste compatible.

Avant une mise à niveau, fermer GNS3, sauvegarder les projets et consigner les versions GUI/serveur ainsi que les versions d'appliances. Mettre à niveau les deux paquets `pipx` vers la même stable; ouvrir une copie d'un projet représentatif avant reprise. Garder l'ancien environnement jusqu'à validation.

Après un exercice, arrêter les noeuds et le projet, supprimer les disques temporaires identifiés et vérifier les ressources libvirt. Ne pas effacer les images, snapshots ou projets d'autres personnes.

## Sources

- [GNS3 — version stable et guide de téléchargement](https://www.gns3.com/software/download)
- [GNS3 — installation Linux, instructions Debian](https://docs.gns3.com/docs/getting-started/installation/linux)
- [GNS3 — releases GUI et GNS3 VM 2.2.61](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.61)
- [GNS3 — releases serveur](https://github.com/GNS3/gns3-server/releases)
- [GNS3 — téléchargements de la VM](https://www.gns3.com/software/download-vm)
- [GNS3 — Marketplace des appliances](https://www.gns3.com/marketplace/appliances)
- [GNS3 — registre et politique des appliances/images](https://github.com/GNS3/gns3-registry)

Les versions Debian 13 et le lancement graphique n'ont pas été testés sur un poste dans cette fiche. Valider `pipx`, QEMU/KVM et le serveur local sur un poste pilote avant un cours ou un usage métier.