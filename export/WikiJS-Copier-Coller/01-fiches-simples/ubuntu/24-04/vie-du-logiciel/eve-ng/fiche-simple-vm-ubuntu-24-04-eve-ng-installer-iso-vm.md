# Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Installer_ISO_VM

- **Environnement** : VM EVE-NG (appliance basée sur Ubuntu Server 24.04 LTS) hébergée sur un poste ou serveur de virtualisation
- **OS / Version** : EVE-NG 7.x (7.2.0-18 au contrôle du 29/10/2026), Ubuntu 24.04 LTS embarqué; Community 6.2.0-4 (Ubuntu 22.04) en fin de support juin 2026
- **Catégorie** : simulation réseau / installation

---

## Problème précis à résoudre

Installer EVE-NG dans une VM à partir de l'ISO officiel. EVE-NG installe son propre Ubuntu Server 24.04 : il n'existe pas de procédure documentée consistant à ajouter EVE-NG par `apt` sur une Ubuntu existante.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO depuis la page officielle **Download** puis contrôler l'empreinte (remplacer `ISO_EVE_FICHIER` par le nom du fichier téléchargé et `SHA256_OFFICIEL` par la valeur SHA256 affichée sur la page) :
   ```bash
   cd ~/Téléchargements
   sha256sum ISO_EVE_FICHIER
   echo 'SHA256_OFFICIEL  ISO_EVE_FICHIER' | sha256sum -c -
   ```
   👉 Explication : seul un ISO dont l'empreinte correspond est installé; les valeurs `ISO_EVE_FICHIER` et `SHA256_OFFICIEL` sont à remplacer par les vôtres.

2. Dans VMware Workstation Pro : **File > New Virtual Machine > Custom > Next**, choisir **I will install the operating system later**, système invité **Linux**, version **Ubuntu 64-bit**, nommer la VM `EVE-NG-LAB`.
   👉 Explication : procédure du cookbook officiel (section 3.1); la VM est créée sans OS pour fixer d'abord le matériel.

3. Régler le matériel : processeurs selon le dimensionnement, **cores per processor = 1**, RAM selon le calculateur, disque d'au moins 200 Go en **un seul fichier**, contrôleur LSI Logic, disque SCSI, carte réseau NAT (portable) ou Bridged (poste fixe).
   👉 Explication : valeurs du cookbook; Internet et DNS doivent être joignables depuis la VM.

4. Dans **Customize Hardware > Processors**, cocher **Virtualize Intel VT-x/EPT or AMD-V/RVI** et **Virtualize IOMMU**; dans **CD/DVD**, choisir **Use ISO image file** et sélectionner l'ISO EVE-NG. En firmware UEFI, désactiver **Secure Boot**.
   👉 Explication : sans virtualisation imbriquée, les nœuds QEMU ne démarrent pas; Secure Boot doit être désactivé selon le cookbook.

5. Démarrer la VM, choisir **Install EVE NG Pro Server**, langue **English**, clavier **English US**, puis **Continue**. Ne pas se connecter pendant la phase 2.
   👉 Explication : phase 1 (Ubuntu) puis redémarrage automatique; phase 2 (EVE-NG) s'exécute seule. ⚠️ La version 7 annonce un « installateur avec interface au premier démarrage » : les écrans peuvent différer légèrement du cookbook 7.9; suivre l'assistant affiché.

6. À l'écran de connexion CLI, se connecter avec l'identifiant par défaut documenté `root` / `eve`, puis renseigner l'assistant IP : nom d'hôte `HOTE_EVE`, adresse `IP_EVE`, masque `MASQUE_EVE`, passerelle `PASSERELLE_EVE`, DNS `DNS_EVE` et un mot de passe root fort `MOT_DE_PASSE_ROOT_EVE`.
   👉 Explication : les valeurs en majuscules sont à remplacer par celles de votre lab; l'IP statique est la méthode préférée par l'éditeur. Le mot de passe root par défaut est remplacé dans cet assistant : ne jamais conserver `eve`.

7. Après redémarrage, se connecter en SSH ou à la console et vérifier la version et le réseau :
   ```bash
   dpkg -l eve-ng-pro
   ping -c 3 www.eve-ng.net
   df -h /
   ```
   👉 Explication : `dpkg -l eve-ng-pro` doit afficher une version 7.x; une absence de résultat signale un problème Internet ou DNS.

8. Ouvrir `https://IP_EVE/` dans un navigateur et se connecter avec le compte web par défaut documenté `admin` / `eve`, puis changer immédiatement ce mot de passe (voir la fiche Sécuriser).
   👉 Explication : première validation de l'interface; le compte `admin` ne doit pas être supprimé selon la doc.

## 2. Production — Contrôles

- Prendre un instantané de la VM une fois EVE-NG installé et mis à jour, avant d'ajouter des images.
- Documenter l'IP, la version et la date d'installation.
- Ne pas faire de mise à jour depuis la console HTML5 Desktop.

## 3. Production — Sécurité

- Utiliser une IP de gestion sur un réseau d'administration isolé; ne pas exposer les ports 22 et 443 directement sur Internet.
- Changer les mots de passe par défaut `root` et `admin` dès la première connexion.
- Ne pas activer d'accès root distant supplémentaire sans besoin.

## Validation et retour arrière

- **Validation** : `dpkg -l eve-ng-pro` affiche une version 7.x et l'interface `https://IP_EVE/` s'ouvre avec la page de connexion.
- **Retour arrière** : éteindre la VM, restaurer l'instantané précédent ou supprimer la VM dans VMware Workstation (**Manage > Delete from Disk**) et supprimer l'ISO si inutile.

## Si le problème n'est pas résolu

- [EVE-NG — téléchargements](https://www.eve-ng.net/index.php/download/)
- [EVE-NG — installation en machine virtuelle](https://www.eve-ng.net/index.php/documentation/installation/virtual-machine-install/)
- [EVE-NG — Professional Cookbook (PDF, chapitres 3 et 4)](https://www.eve-ng.net/wp-content/uploads/2026/09/EVE-PE-BOOK-7.9-2026.pdf)
[EVE-NG — documentation officielle](https://www.eve-ng.net/index.php/documentation/)
- [Fiche logiciel EVE-NG](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-eve-ng)
- [Prérequis, licences et hôtes supportés](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-prerequis-licence-support)
- [Sécuriser EVE-NG](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-securiser)