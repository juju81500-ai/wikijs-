# Déployer pfSense CE 2.9.0 en laboratoire Proxmox VE

- **OS / Version** : pfSense Community Edition 2.9.0, VM x86-64 sur Proxmox VE
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : installation de laboratoire à deux interfaces; pas de raccordement à un réseau de production
- **Catégorie** : Pare-feu et routage
- **Tags** : `pfsense`, `ce`, `2.9.0`, `proxmox`, `virtualisation`, `firewall`, `lab`

## 1. Périmètre, prérequis et réseau

Fiche simple : [périmètre, prérequis et réseau](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Perimetre_Prerequis_Reseau.md).

Au 27 octobre 2026, Netgate répertorie pfSense CE 2.9.0 parmi les versions prises en charge. La version CE 2.9.0 utilise FreeBSD 16-CURRENT comme système de base. Ce guide installe CE en VM à des fins d'apprentissage et de validation; il ne remplace ni une conception de pare-feu de production, ni un guide d'appliance Netgate, ni une procédure haute disponibilité.

Prérequis de laboratoire : un hôte Proxmox VE opérationnel, un poste ou VM d'administration, une image d'installation obtenue depuis le portail Netgate, et deux réseaux de laboratoire distincts. Préparer `vmbr-pfsense-wan` et `vmbr-pfsense-lan`; le pont WAN doit fournir un accès amont contrôlé nécessaire à l'installateur en ligne. Le pont LAN ne doit être connecté ni au réseau de gestion Proxmox, ni à un segment de production. Si le test n'a pas besoin d'Internet, isoler aussi le WAN après l'installation.

Ne pas brancher directement les deux interfaces de cette VM sur le même réseau. Vérifier que le sous-réseau LAN initial `192.168.1.0/24` et le LAN cible choisi ne chevauchent aucun réseau de l'hôte ou du site.

## 2. Télécharger et vérifier l'image CE

Fiche simple : [télécharger et vérifier l'image CE](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Telecharger_Verifier_Image.md).

Le téléchargement du Netgate Installer est gratuit mais nécessite un compte Netgate Store. Depuis ce compte, télécharger l'image `AMD64 ISO` destinée aux VM x86-64. Dans la page des sommes de contrôle officielle, repérer la valeur SHA-256 correspondant exactement au fichier téléchargé et comparer cette valeur avant d'utiliser l'image :

```bash
sha256sum netgate-installer-amd64.iso.gz
```

Netgate publie les sommes pour les images compressées; si le portail fournit un fichier `.gz`, vérifier son empreinte avant décompression. En cas d'écart, supprimer l'image et la télécharger à nouveau. Transférer ensuite l'ISO validée dans le stockage ISO de Proxmox. Ne pas utiliser un ISO préinstallé provenant d'un tiers.

## 3. Créer la VM de pare-feu

Fiche simple : [créer la VM de pare-feu](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Creer_VM_Pare_Feu.md).

Dans Proxmox VE, créer une VM avec des identifiants documentés et les paramètres de laboratoire suivants :

- Firmware/BIOS et contrôleur système conformes à la recette Netgate retenue; ne pas mélanger BIOS/UEFI après installation.
- Disque VirtIO Block d'au moins 16 Go pour les essais, sur un stockage adapté.
- 2 vCPU et 2 Go de RAM pour un usage léger de laboratoire; les minimums publiés sont 1 CPU, 1 Go de RAM et 8 Go de disque, mais ils ne conviennent pas à tous les scénarios.
- Deux cartes réseau de type VirtIO : première sur `vmbr-pfsense-wan`, seconde sur `vmbr-pfsense-lan`.
- ISO Netgate Installer attachée au lecteur optique et console Proxmox disponible.

Créer séparément une VM cliente de test sur `vmbr-pfsense-lan`. Garder l'accès d'administration de l'hyperviseur hors de ce segment.

## 4. Installer pfSense CE

Fiche simple : [installer pfSense CE](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Installer_pfSense_CE.md).

Démarrer la VM sur le Netgate Installer et suivre l'assistant officiel. Choisir la cible disque de la VM, vérifier une dernière fois son identité, puis accepter le partitionnement uniquement si ce disque virtuel ne contient rien à préserver. L'installation efface la cible sélectionnée.

Si le matériel est éligible à pfSense Plus, sélectionner explicitement **Install CE** pour le scénario de ce guide. Choisir la version marquée courante/stable, terminer l'installation et redémarrer en retirant l'ISO du lecteur virtuel.

À l'assignation des interfaces, vérifier les MAC affichées par Proxmox et affecter `vtnet0` à WAN, `vtnet1` à LAN. Confirmer l'affectation dans la console avant de continuer. Ne pas se fier uniquement à l'ordre supposé des interfaces si les MAC ne correspondent pas.

La configuration initiale pfSense utilise généralement WAN en DHCP, LAN `192.168.1.1/24`, DHCP actif sur LAN, blocage des connexions entrantes WAN, et autorisation générale sortante depuis LAN. Elle peut aussi activer IPv6/DHCPv6 selon la délégation disponible. Cette ouverture sortante par défaut ne doit pas être considérée comme une politique finale.

## 5. Accéder au GUI et sécuriser les premiers réglages

Fiche simple : [accéder au GUI et sécuriser les premiers réglages](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Acces_GUI_Premiers_Reglages.md).

Depuis la VM cliente connectée au pont LAN isolé, obtenir une adresse LAN puis ouvrir `https://192.168.1.1`. Au premier accès, les identifiants par défaut sont `admin` / `pfsense`; changer le mot de passe immédiatement avant toute autre tâche. Ne jamais exposer le GUI ou SSH sur WAN.

Dans l'assistant de configuration :

1. Définir un nom d'hôte et un domaine de laboratoire qui ne crée pas de conflit DNS.
2. Vérifier le fuseau horaire et NTP.
3. Configurer WAN selon le réseau amont isolé et contrôler la passerelle; ne pas importer de paramètres de fournisseur réel dans un lab partagé.
4. Remplacer le LAN par un sous-réseau réservé au lab, non chevauchant, puis renouveler l'adresse de la VM cliente et rouvrir le GUI sur la nouvelle adresse.
5. Si un DHCP existe déjà sur ce LAN, désactiver le DHCP pfSense pour éviter deux serveurs concurrents; sinon définir une seule plage de lab clairement documentée.
6. Installer un certificat GUI de confiance pour le laboratoire et restreindre l'administration au réseau de gestion autorisé.

Vérifier sur **Status > Interfaces** les noms, adresses, liens et débits; confirmer depuis la VM cliente l'accès au GUI sur LAN. L'interface WAN ne doit pas être administrable depuis le réseau amont.

## 6. Définir et tester les règles du laboratoire

Fiche simple : [définir et tester les règles du laboratoire](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Regles_Lab_Tester.md).

La stratégie durable recommandée par Netgate est le refus par défaut et l'autorisation minimale requise. Les règles LAN par défaut permettent généralement toute sortie; réduire cette règle au jeu d'essai : DNS vers le résolveur désigné, NTP si requis, et flux applicatifs explicitement nécessaires. Documenter les règles et leurs motifs; ne pas créer de règle WAN « any/any ».

Tester dans cet ordre :

1. Depuis le client autorisé, confirmer l'accès GUI sur LAN et la résolution DNS attendue.
2. Tester un flux sortant explicitement autorisé et vérifier ses états/logs.
3. Tester un flux sortant non autorisé et confirmer son blocage.
4. Depuis le segment WAN de laboratoire, confirmer qu'aucun accès GUI/SSH entrant n'est accepté.
5. Vérifier les journaux de pare-feu et que les flux de test apparaissent sur la règle attendue.

Ne pas utiliser ces vérifications pour scanner un réseau tiers ou l'infrastructure de production.

## 7. Sauvegarder et éprouver la restauration

Fiche simple : [sauvegarder et éprouver la restauration](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Sauvegarder_Restaurer.md).

Dans **Diagnostics > Backup & Restore**, télécharger une configuration complète en cochant le chiffrement et en choisissant une phrase secrète gérée hors bande. Un export XML sans chiffrement contient des informations sensibles. Stocker le backup hors de la VM et de l'hôte Proxmox, avec accès limité.

Pour éprouver la restauration, cloner ou recréer une seconde VM de test, déconnecter ses cartes du réseau amont et du LAN de production, puis restaurer la configuration sur une version compatible. pfSense compare la révision de configuration; une sauvegarde complète d'une révision antérieure peut être migrée, mais une restauration partielle d'une autre révision n'est pas prise en charge. Vérifier interfaces, IP, DHCP, règles et GUI avant de reconnecter un réseau de laboratoire.

Le test est réussi si la VM restaurée démarre sans erreur, que les interfaces sont affectées aux bons ponts, et que les règles/politiques attendues sont effectivement appliquées. Nettoyer le clone et supprimer les médias d'installation quand ils ne sont plus nécessaires.

## 8. Exploitation et limites

Fiche simple : [exploitation et limites](../../../../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Deploiement-CE-Lab/Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Exploitation_Limites.md).

- Garder pfSense CE sur une version prise en charge; lire l'Upgrade Guide et les notes de version avant mise à niveau. Pour CE 2.9.0, vérifier les errata matériels des plateformes visées et les certificats TLS faibles.
- Sauvegarder la configuration avant une modification réseau, une mise à niveau ou l'ajout d'un paquet.
- N'installer que les paquets nécessaires, après vérification de leur compatibilité avec la version cible.
- Cette fiche ne couvre pas CARP/pfsync, multi-WAN, VPN, règles de production, matériel Netgate ou dimensionnement de débit. Ces sujets nécessitent un plan de changement distinct et des essais dédiés.

## Sources

- [Netgate — versions supportées et notes de version](https://docs.netgate.com/pfsense/en/latest/releases/index.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Netgate — exigences matérielles minimales](https://docs.netgate.com/pfsense/en/latest/hardware/minimum-requirements.html)
- [Netgate — obtenir l'image d'installation et vérifier son empreinte](https://docs.netgate.com/pfsense/en/latest/install/download-installer-image.html)
- [Netgate — assistant d'installation](https://docs.netgate.com/pfsense/en/latest/install/install-walkthrough.html)
- [Netgate — virtualiser sur Proxmox VE](https://docs.netgate.com/pfsense/en/latest/recipes/virtualize-proxmox-ve.html)
- [Netgate — identifiants par défaut](https://docs.netgate.com/pfsense/en/latest/usermanager/defaults.html)
- [Netgate — bonnes pratiques de règles firewall](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html)
- [Netgate — sauvegarde GUI](https://docs.netgate.com/pfsense/en/latest/backup/configuration.html)
- [Netgate — restaurer une sauvegarde](https://docs.netgate.com/pfsense/en/latest/backup/restore.html)

Aucune VM pfSense n'a été créée ni testée sur cet environnement; les étapes opérationnelles restent à valider sur un hôte Proxmox de laboratoire compatible.