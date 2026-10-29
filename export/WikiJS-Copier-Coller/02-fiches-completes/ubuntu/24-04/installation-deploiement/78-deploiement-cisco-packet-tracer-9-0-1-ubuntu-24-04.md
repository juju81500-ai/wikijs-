# Déployer Cisco Packet Tracer 9.0.1 sur Ubuntu 24.04

- **OS / Version** : Ubuntu Desktop 24.04 LTS amd64; Cisco Packet Tracer 9.0.1
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : simulateur pédagogique, installation du paquet Ubuntu officiel et topologie de cours isolée
- **Catégorie** : simulation réseau / formation

## 1. Version et prérequis

Fiche simple : [vérifier la version et les prérequis](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-version-prerequis).

Au 27 octobre 2026, le portail officiel Cisco Networking Academy présente Packet Tracer 9.0.1 pour Ubuntu 64 bits. Les systèmes officiellement indiqués sont Ubuntu 22.04 et 24.04 LTS, processeur amd64, 4 Go de RAM libre et 1,4 Go de disque. Debian 13 n'est pas listé comme plateforme prise en charge: ce guide cible Ubuntu Desktop 24.04.

Le téléchargement est réservé aux utilisateurs connectés au portail Cisco/NetAcad. L'accès peut être obtenu par inscription au cours gratuit « Getting Started with Cisco Packet Tracer ». Ne pas télécharger le logiciel depuis un miroir tiers et ne pas automatiser l'authentification du compte.

Packet Tracer est un simulateur pédagogique simplifié, pas une image IOS ni un environnement de production. Il ne valide pas les comportements d'un équipement réel ou de toutes les versions Cisco.

## 2. Télécharger depuis Cisco

Fiche simple : [télécharger depuis Cisco](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-telecharger-cisco).

1. Ouvrir le [Resource Hub Cisco Networking Academy](https://www.netacad.com/resources/lab-downloads) et se connecter avec son compte Cisco/NetAcad.
2. Si nécessaire, s'inscrire au cours gratuit de démarrage Packet Tracer pour obtenir l'accès aux ressources.
3. Sélectionner uniquement le téléchargement « Packet Tracer 9.0.1 Ubuntu 64bit ».
4. Conserver le nom d'origine du fichier et noter la version obtenue. Si le portail propose une version différente, vérifier ses prérequis et le manuel associé avant de poursuivre.

L'éditeur ne publie pas de digest SHA-256 pour ce téléchargement sur la page consultée. Le contrôle de provenance repose donc sur la connexion HTTPS au portail officiel et la sélection du paquet Linux qui y est publié; ne pas fabriquer ni réutiliser une empreinte provenant d'un site tiers.

## 3. Installer le paquet

Fiche simple : [installer le paquet](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-installer-paquet).

Vérifier l'OS et l'architecture avant installation :

```bash
cat /etc/os-release
dpkg --print-architecture
free -h
df -h "$HOME"
```

Dans le gestionnaire de fichiers, ouvrir le dossier de téléchargement, vérifier que le fichier est bien le paquet Ubuntu `.deb` récupéré depuis Cisco, puis l'ouvrir avec l'installateur logiciel Ubuntu et confirmer l'installation avec l'authentification système. Ne pas lancer un script provenant d'un forum pour contourner une dépendance.

Si l'installation signale une dépendance manquante, annuler, vérifier que le système est bien Ubuntu 24.04 amd64 et que les dépôts officiels sont à jour; ne pas ajouter de dépôt Debian ou Ubuntu tiers. Redémarrer la session graphique si l'application n'apparaît pas immédiatement dans le menu.

## 4. Premier lancement et authentification

Fiche simple : [premier lancement et authentification](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-premier-lancement-auth).

Lancer Cisco Packet Tracer depuis le menu des applications. Lorsqu'il le demande, utiliser le bouton de connexion Skills for All/NetAcad et le compte propriétaire. Ne pas partager le compte de cours entre opérateurs.

Les diagrammes d'exercice doivent rester dans le répertoire utilisateur ou l'espace de cours approuvé. Ne pas y copier les configurations réelles, les mots de passe, les données d'un client ou des extraits de production.

## 5. Vérifier une topologie de cours isolée

Fiche simple : [vérifier une topologie de cours isolée](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-topologie-isolee).

1. Créer un nouveau fichier de simulation et y ajouter deux postes et un commutateur proposés par Packet Tracer.
2. Utiliser uniquement des adresses réservées à la documentation ou au cours, sans liaison à une carte physique ou à un réseau externe.
3. Relier les deux postes au commutateur et saisir leurs paramètres IP dans l'interface de l'outil.
4. Vérifier la connectivité au moyen du mécanisme de simulation intégré et examiner les événements affichés dans le mode Simulation.
5. Enregistrer le projet, fermer l'application, rouvrir le fichier et vérifier que les équipements, liens et paramètres sont conservés.

Ce test prouve le fonctionnement de la maquette pédagogique dans Packet Tracer uniquement. Pour un équipement réel, confirmer la configuration avec la documentation de sa version et la procédure de changement approuvée.

## 6. Sauvegarder et maintenir

Fiche simple : [sauvegarder et maintenir](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-sauvegarder-maintenir).

Conserver le fichier source de simulation et ses éventuelles pièces jointes dans un espace versionné ou sauvegardé. Une capture d'écran ou un PDF d'export n'est pas un substitut au fichier Packet Tracer modifiable.

Pour mettre à jour l'application, retourner au Resource Hub Cisco, relever la nouvelle version et ses systèmes supportés, puis installer uniquement le paquet publié pour Ubuntu. Tester une copie du projet après mise à jour et garder une copie de la version précédente selon la politique de poste.

## Sources

- [Cisco Networking Academy — téléchargements des ressources Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco Networking Academy — cours gratuit de démarrage](https://www.netacad.com/courses/getting-started-cisco-packet-tracer)
- [Cisco — instructions officielles de téléchargement et installation](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf)
- [Cisco Networking Academy — conditions d'utilisation](https://www.netacad.com/netacad/tnc/netacad-terms-and-conditions-en.pdf)

Le paquet propriétaire n'a pas été téléchargé ni installé par cette fiche, car son accès nécessite une session Cisco. La version installée et l'authentification doivent être testées par l'utilisateur sur le poste pilote.