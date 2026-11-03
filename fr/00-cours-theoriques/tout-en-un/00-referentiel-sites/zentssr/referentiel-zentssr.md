---
title: "Référentiel — ZenTSSR"
description: "Méthode. Ce référentiel recense la structure du site public <https://zentssr.com> (application monopage) à la date du 2026-11-01. Les pages viennent du [sitemap](https://zentssr.com/sitemap.xml) ; les titres, catégories et comptes viennent du bundle JavaScript public https://zentssr.com/assets/index"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "referentiel", "zentssr"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Référentiel — ZenTSSR

- **Tags** : `transverse`, `tout-en-un`, `referentiel`, `zentssr`

**Méthode.** Ce référentiel recense la structure du site public <https://zentssr.com> (application monopage) à la date du 2026-11-01. Les pages viennent du [sitemap](https://zentssr.com/sitemap.xml) ; les titres, catégories et comptes viennent du bundle JavaScript public `https://zentssr.com/assets/index-DasSrAz9.js` (modules, thèmes de cours, quiz, jeux, labs, guides). Liens et titres uniquement, contenu non reproduit, droits réservés à l’éditeur : aucune question, réponse, commande ou texte de cours n’est recopié ; les descriptions ci-dessous sont rédigées pour ce référentiel et les nombres entre parenthèses sont des comptes d’éléments. Le site étant une application monopage, les sections d’une même page partagent son adresse et les comptes peuvent évoluer avec les versions du bundle.

Types : cours, quiz, jeu, lab, outil, guide.

## 1. Pages du sitemap

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Accueil — Page d’accueil : présentation du site, accès rapides aux modules, au QCM du jour et aux outils. | Pages du site | outil | <https://zentssr.com> |
| modules — Liste des modules de révision, séparés entre prérequis et modules CCP+. | Pages du site | cours | <https://zentssr.com/modules> |
| quiz — Choix du module pour lancer un QCM de révision. | Pages du site | quiz | <https://zentssr.com/quiz> |
| jeux-labs — Page à deux onglets regroupant les jeux/quiz et les labs interactifs. | Pages du site | jeu | <https://zentssr.com/jeux-labs> |
| games — Alias de la page jeux-labs ouvert sur l’onglet jeux et quiz. | Pages du site | jeu | <https://zentssr.com/games> |
| labs — Alias de la page jeux-labs ouvert sur l’onglet labs en terminal simulé. | Pages du site | lab | <https://zentssr.com/labs> |
| installation — Catalogue de guides d’installation pas à pas de services TSSR. | Pages du site | guide | <https://zentssr.com/installation> |
| scripting-cours — Cours interactifs Bash et PowerShell avec quiz dédiés. | Pages du site | cours | <https://zentssr.com/scripting-cours> |
| subnetting-table — Calculateur de sous-réseaux IP avec table des puissances de 2. | Pages du site | outil | <https://zentssr.com/subnetting-table> |
| infos-exam — Informations sur le déroulé de l’examen TSSR, domaines clés et mode test. | Pages du site | guide | <https://zentssr.com/infos-exam> |
| entretien-oral — Conseils pour l’oral devant le jury et catégories de questions types. | Pages du site | guide | <https://zentssr.com/entretien-oral> |
| faq-examen — Foire aux questions sur l’examen avec moteur de recherche. | Pages du site | guide | <https://zentssr.com/faq-examen> |
| guide — Assistant conversationnel de recherche de ressources du site. | Pages du site | outil | <https://zentssr.com/guide> |
| saint-cedric — Page « À propos » présentant l’auteur, le projet collaboratif et les remerciements. | Pages du site | guide | <https://zentssr.com/saint-cedric> |

## 2. Modules de révision

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Prérequis Fondamentaux — Socle Cisco, Linux, PowerShell et Active Directory à maîtriser avant le reste. | Prérequis | cours | <https://zentssr.com/modules/prerequis> |
| Support Utilisateur — Module d’assistance aux utilisateurs : tickets, diagnostic poste et réseau, accès distants. | CCP 1 | cours | <https://zentssr.com/modules/ccp1> |
| Windows Server / AD — Module d’exploitation des serveurs Windows et de l’annuaire Active Directory. | CCP 2 | cours | <https://zentssr.com/modules/ccp2> |
| Linux — Module d’exploitation des serveurs Linux : fichiers, droits, services et planification. | CCP 3 | cours | <https://zentssr.com/modules/ccp3> |
| VMware vSphere — Module consacré à l’infrastructure virtualisée VMware vSphere. | CCP 5 | cours | <https://zentssr.com/modules/ccp5> |
| Sécurité Réseau — Module de sécurisation des accès Internet autour du pare-feu pfSense. | CCP 7 | cours | <https://zentssr.com/modules/ccp7> |
| Sauvegardes / PRA / PCA — Module sur les sauvegardes, restaurations et plans de reprise ou de continuité. | CCP 8 | cours | <https://zentssr.com/modules/ccp8> |
| Déploiement Postes — Module de déploiement et de maintenance des postes de travail. | CCP 9 | cours | <https://zentssr.com/modules/ccp9> |
| Subnetting & CIDR — Module de calcul d’adressage IP, CIDR et découpage VLSM. | Modules transverses CCP+ | cours | <https://zentssr.com/modules/subnetting> |
| Ports & Protocoles — Module de référence sur les ports, protocoles et acronymes réseau. | Modules transverses CCP+ | cours | <https://zentssr.com/modules/ports> |
| Scripting Bash & PS — Module d’introduction au scripting Bash et PowerShell. | Modules transverses CCP+ | cours | <https://zentssr.com/modules/scripting> |
| Cisco IOS — Module sur la configuration de base des équipements Cisco IOS. | Modules transverses CCP+ | cours | <https://zentssr.com/modules/cisco> |
| GLPI & Supervision — Module sur la gestion de parc, la supervision et le stockage réseau. | Modules transverses CCP+ | cours | <https://zentssr.com/modules/glpi> |
| Entretien Technique Oral — Module renvoyant vers la page de préparation à l’entretien oral du jury. | Modules transverses CCP+ | guide | <https://zentssr.com/entretien-oral> |

## 3. Thèmes de cours par module

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Schéma réseau — DHCP, ARP, DNS, NAT en interaction | Prérequis Fondamentaux | cours | <https://zentssr.com/cours/prerequis> |
| Modèle OSI — Les 7 couches | Prérequis Fondamentaux | cours | <https://zentssr.com/cours/prerequis> |
| Cisco IOS — Les indispensables | Prérequis Fondamentaux | cours | <https://zentssr.com/cours/prerequis> |
| Linux — Les commandes essentielles | Prérequis Fondamentaux | cours | <https://zentssr.com/cours/prerequis> |
| PowerShell — Les bases essentielles | Prérequis Fondamentaux | cours | <https://zentssr.com/cours/prerequis> |
| Active Directory — Les fondamentaux | Prérequis Fondamentaux | cours | <https://zentssr.com/cours/prerequis> |
| Réseau — Le strict minimum | Prérequis Fondamentaux | cours | <https://zentssr.com/cours/prerequis> |
| Cycle de vie d'un ticket | Support Utilisateur | cours | <https://zentssr.com/cours/ccp1> |
| Niveaux de priorité | Support Utilisateur | cours | <https://zentssr.com/cours/ccp1> |
| Diagnostic réseau Windows | Support Utilisateur | cours | <https://zentssr.com/cours/ccp1> |
| Active Directory côté support | Support Utilisateur | cours | <https://zentssr.com/cours/ccp1> |
| Bureau à distance (RDP) | Support Utilisateur | cours | <https://zentssr.com/cours/ccp1> |
| Structure Active Directory | Windows Server / AD | cours | <https://zentssr.com/cours/ccp2> |
| Gestion des utilisateurs PowerShell | Windows Server / AD | cours | <https://zentssr.com/cours/ccp2> |
| Stratégies de groupe (GPO) | Windows Server / AD | cours | <https://zentssr.com/cours/ccp2> |
| DNS Windows Server | Windows Server / AD | cours | <https://zentssr.com/cours/ccp2> |
| Permissions NTFS & Partages | Windows Server / AD | cours | <https://zentssr.com/cours/ccp2> |
| Système de fichiers Linux | Linux | cours | <https://zentssr.com/cours/ccp3> |
| Permissions Linux | Linux | cours | <https://zentssr.com/cours/ccp3> |
| Commandes essentielles | Linux | cours | <https://zentssr.com/cours/ccp3> |
| Services systemd | Linux | cours | <https://zentssr.com/cours/ccp3> |
| Tâches planifiées (cron) | Linux | cours | <https://zentssr.com/cours/ccp3> |
| ESXi & Architecture vSphere | VMware vSphere | cours | <https://zentssr.com/cours/ccp5> |
| Snapshots | VMware vSphere | cours | <https://zentssr.com/cours/ccp5> |
| HA & DRS | VMware vSphere | cours | <https://zentssr.com/cours/ccp5> |
| Réseau & Stockage VMware | VMware vSphere | cours | <https://zentssr.com/cours/ccp5> |
| pfSense - Pare-feu | Sécurité Réseau | cours | <https://zentssr.com/cours/ccp7> |
| VPN | Sécurité Réseau | cours | <https://zentssr.com/cours/ccp7> |
| VLAN | Sécurité Réseau | cours | <https://zentssr.com/cours/ccp7> |
| IDS / IPS & Sécurité avancée | Sécurité Réseau | cours | <https://zentssr.com/cours/ccp7> |
| Types de sauvegardes | Sauvegardes / PRA / PCA | cours | <https://zentssr.com/cours/ccp8> |
| RPO & RTO | Sauvegardes / PRA / PCA | cours | <https://zentssr.com/cours/ccp8> |
| PRA & PCA | Sauvegardes / PRA / PCA | cours | <https://zentssr.com/cours/ccp8> |
| Outils de sauvegarde | Sauvegardes / PRA / PCA | cours | <https://zentssr.com/cours/ccp8> |
| Sysprep | Déploiement Postes | cours | <https://zentssr.com/cours/ccp9> |
| WDS - Déploiement réseau | Déploiement Postes | cours | <https://zentssr.com/cours/ccp9> |
| DISM - Gestion d'images | Déploiement Postes | cours | <https://zentssr.com/cours/ccp9> |
| MDT - Déploiement avancé | Déploiement Postes | cours | <https://zentssr.com/cours/ccp9> |
| Bases du subnetting | Subnetting & CIDR | cours | <https://zentssr.com/cours/subnetting> |
| Méthode du bloc | Subnetting & CIDR | cours | <https://zentssr.com/cours/subnetting> |
| Adresses privées & spéciales | Subnetting & CIDR | cours | <https://zentssr.com/cours/subnetting> |
| VLSM | Subnetting & CIDR | cours | <https://zentssr.com/cours/subnetting> |
| Modèle OSI — Les 7 couches (priorité examen) | Ports & Protocoles | cours | <https://zentssr.com/cours/ports> |
| Définitions ITSM — Vocabulaire indispensable | Ports & Protocoles | cours | <https://zentssr.com/cours/ports> |
| Tableau complet des ports TSSR | Ports & Protocoles | cours | <https://zentssr.com/cours/ports> |
| Ports essentiels à connaître | Ports & Protocoles | cours | <https://zentssr.com/cours/ports> |
| Ports réseau & services | Ports & Protocoles | cours | <https://zentssr.com/cours/ports> |
| TCP vs UDP | Ports & Protocoles | cours | <https://zentssr.com/cours/ports> |
| Enregistrements DNS | Ports & Protocoles | cours | <https://zentssr.com/cours/ports> |
| Bash - Les bases | Scripting Bash & PS | cours | <https://zentssr.com/cours/scripting> |
| Bash - Conditions & Boucles | Scripting Bash & PS | cours | <https://zentssr.com/cours/scripting> |
| PowerShell - Les bases | Scripting Bash & PS | cours | <https://zentssr.com/cours/scripting> |
| PowerShell - Avancé | Scripting Bash & PS | cours | <https://zentssr.com/cours/scripting> |
| Modes de configuration Cisco | Cisco IOS | cours | <https://zentssr.com/cours/cisco> |
| VLANs sur Switch Cisco | Cisco IOS | cours | <https://zentssr.com/cours/cisco> |
| Configurer SSH | Cisco IOS | cours | <https://zentssr.com/cours/cisco> |
| Routage & ACL | Cisco IOS | cours | <https://zentssr.com/cours/cisco> |
| GLPI — Gestion de parc ITSM | GLPI & Supervision | cours | <https://zentssr.com/cours/glpi> |
| NAS & SAN — Stockage réseau | GLPI & Supervision | cours | <https://zentssr.com/cours/glpi> |
| Zabbix — Supervision d'infrastructure | GLPI & Supervision | cours | <https://zentssr.com/cours/glpi> |
| iSCSI — Stockage bloc via IP | GLPI & Supervision | cours | <https://zentssr.com/cours/glpi> |

## 4. Fiches de révision téléchargeables

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Fiche de révision — Support Utilisateur | Support Utilisateur | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/343ace411_FICHEREVISIONCCP1supportuser.docx> |
| Fiche de révision — Windows Server / AD | Windows Server / AD | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/767a99038_FICHEREVISIONCCP2AD.docx> |
| Fiche de révision — Linux | Linux | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/ef1b9d5a6_FICHEDERVISIONCCP3Linux.docx> |
| Fiche de révision — VMware vSphere | VMware vSphere | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/00d7bfeeb_FICHEREVISIONCCP5vmware.docx> |
| Fiche de révision — Sécurité Réseau | Sécurité Réseau | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/bacba2579_FICHEREVISIONCCP7securtitpfsense.docx> |
| Fiche de révision — Sauvegardes / PRA / PCA | Sauvegardes / PRA / PCA | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/66051685e_FICHEDERVISIONsauvegardePRAPCA.docx> |
| Fiche de révision — Déploiement Postes | Déploiement Postes | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/95394eeaa_FICHEREVISIONCCP9deploimentwds.docx> |
| Fiche de révision — Subnetting & CIDR | Subnetting & CIDR | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/10d775491_FICHEDERVISIONsubnetting.docx> |
| Fiche de révision — Ports & Protocoles | Ports & Protocoles | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/3d207b411_FICHEDERVISIONPortsprotocoles.docx> |
| Fiche de révision — Scripting Bash & PS | Scripting Bash & PS | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/4a0765dc0_FICHESCRIPTING.docx> |
| Fiche de révision — Cisco IOS | Cisco IOS | cours | <https://media.base44.com/files/public/user_692ae83bb7a254339467e78a/5236c4dcb_FichederevisonCISCOIOS.docx> |

## 5. Quiz QCM

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Quiz QCM — Prérequis Fondamentaux (110 questions) | Prérequis Fondamentaux | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Support Utilisateur (82 questions) | Support Utilisateur | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Windows Server / AD (73 questions) | Windows Server / AD | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Linux (85 questions) | Linux | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — VMware vSphere (60 questions) | VMware vSphere | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Sécurité Réseau (68 questions) | Sécurité Réseau | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Sauvegardes / PRA / PCA (67 questions) | Sauvegardes / PRA / PCA | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Déploiement Postes (66 questions) | Déploiement Postes | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Subnetting & CIDR (70 questions) | Subnetting & CIDR | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Ports & Protocoles (74 questions) | Ports & Protocoles | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Scripting Bash & PS (70 questions) | Scripting Bash & PS | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — Cisco IOS (70 questions) | Cisco IOS | quiz | <https://zentssr.com/quiz> |
| Quiz QCM — GLPI & Supervision (30 questions) | GLPI & Supervision | quiz | <https://zentssr.com/quiz> |
| Quiz Bash (28 questions, tirage de 20) | Scripting | quiz | <https://zentssr.com/scripting-cours> |
| Quiz PowerShell (33 questions, tirage de 20) | Scripting | quiz | <https://zentssr.com/scripting-cours> |
| Quiz Mixte (61 questions, tirage de 20) | Scripting | quiz | <https://zentssr.com/scripting-cours> |

## 6. Jeux et mémorisation

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Drag & Drop — Prérequis Fondamentaux : « Associe le concept fondamental » | Prérequis Fondamentaux | jeu | <https://zentssr.com/games> |
| Drag & Drop — Ports & Protocoles : « Associe le port au service » | Ports & Protocoles | jeu | <https://zentssr.com/games> |
| Drag & Drop — Sauvegardes / PRA / PCA : « Associe le concept à sa définition » | Sauvegardes / PRA / PCA | jeu | <https://zentssr.com/games> |
| Drag & Drop — Windows Server / AD : « Associe la commande/terme AD » | Windows Server / AD | jeu | <https://zentssr.com/games> |
| Drag & Drop — Linux : « Associe la commande Linux à son rôle » | Linux | jeu | <https://zentssr.com/games> |
| Drag & Drop — VMware vSphere : « Associe le concept VMware » | VMware vSphere | jeu | <https://zentssr.com/games> |
| Drag & Drop — Cisco IOS : « Associe la commande Cisco » | Cisco IOS | jeu | <https://zentssr.com/games> |
| Drag & Drop — Sécurité Réseau : « Associe le concept sécurité » | Sécurité Réseau | jeu | <https://zentssr.com/games> |
| Drag & Drop — Subnetting & CIDR : « Associe le CIDR à ses caractéristiques » | Subnetting & CIDR | jeu | <https://zentssr.com/games> |
| Drag & Drop — Support Utilisateur : « Associe le concept support IT » | Support Utilisateur | jeu | <https://zentssr.com/games> |
| Drag & Drop — Scripting Bash & PS : « Associe la commande/concept scripting » | Scripting Bash & PS | jeu | <https://zentssr.com/games> |
| Drag & Drop — GLPI & Supervision : « Associe GLPI & Supervision » | GLPI & Supervision | jeu | <https://zentssr.com/games> |
| Drag & Drop — Déploiement Postes : « Associe le concept déploiement » | Déploiement Postes | jeu | <https://zentssr.com/games> |
| Flashcards — Prérequis Fondamentaux (12 cartes) | Prérequis Fondamentaux | jeu | <https://zentssr.com/games> |
| Flashcards — Support Utilisateur (5 cartes) | Support Utilisateur | jeu | <https://zentssr.com/games> |
| Flashcards — Windows Server / AD (5 cartes) | Windows Server / AD | jeu | <https://zentssr.com/games> |
| Flashcards — Linux (5 cartes) | Linux | jeu | <https://zentssr.com/games> |
| Flashcards — VMware vSphere (5 cartes) | VMware vSphere | jeu | <https://zentssr.com/games> |
| Flashcards — Sécurité Réseau (5 cartes) | Sécurité Réseau | jeu | <https://zentssr.com/games> |
| Flashcards — Sauvegardes / PRA / PCA (5 cartes) | Sauvegardes / PRA / PCA | jeu | <https://zentssr.com/games> |
| Flashcards — Déploiement Postes (5 cartes) | Déploiement Postes | jeu | <https://zentssr.com/games> |
| Flashcards — Subnetting & CIDR (5 cartes) | Subnetting & CIDR | jeu | <https://zentssr.com/games> |
| Flashcards — Ports & Protocoles (5 cartes) | Ports & Protocoles | jeu | <https://zentssr.com/games> |
| Flashcards — Scripting Bash & PS (3 cartes) | Scripting Bash & PS | jeu | <https://zentssr.com/games> |
| Flashcards — Cisco IOS (5 cartes) | Cisco IOS | jeu | <https://zentssr.com/games> |
| Flashcards — GLPI & Supervision (6 cartes) | GLPI & Supervision | jeu | <https://zentssr.com/games> |
| OSI Challenge | Réseau | jeu | <https://zentssr.com/games> |
| Maître des Ports | Ports & Protocoles | jeu | <https://zentssr.com/games> |
| Topology Game | Réseau | jeu | <https://zentssr.com/labs> |
| Chmod Game | Linux | jeu | <https://zentssr.com/labs> |

## 7. Labs interactifs

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Création de VLANs (Débutant) | Cisco IOS | lab | <https://zentssr.com/labs> |
| Assigner des ports à des VLANs (Débutant) | Cisco IOS | lab | <https://zentssr.com/labs> |
| Configuration SSH (Intermédiaire) | Cisco IOS | lab | <https://zentssr.com/labs> |
| Routes statiques (Débutant) | Cisco IOS | lab | <https://zentssr.com/labs> |
| ACL — Bloquer Telnet (Intermédiaire) | Cisco IOS | lab | <https://zentssr.com/labs> |
| Gérer les services Windows (Débutant) | PowerShell | lab | <https://zentssr.com/labs> |
| Créer un utilisateur Active Directory (Intermédiaire) | PowerShell | lab | <https://zentssr.com/labs> |
| Diagnostic réseau PowerShell (Débutant) | PowerShell | lab | <https://zentssr.com/labs> |
| Vérifier et appliquer les GPO (Débutant) | PowerShell | lab | <https://zentssr.com/labs> |
| Gestion fichiers et dossiers (Débutant) | PowerShell | lab | <https://zentssr.com/labs> |
| Analyser les logs d'événements (Intermédiaire) | PowerShell | lab | <https://zentssr.com/labs> |
| Gestion des utilisateurs Linux (Débutant) | Linux Bash | lab | <https://zentssr.com/labs> |
| Permissions et propriétaires (Débutant) | Linux Bash | lab | <https://zentssr.com/labs> |
| Gestion des services systemd (Débutant) | Linux Bash | lab | <https://zentssr.com/labs> |
| Diagnostic réseau Linux (Débutant) | Linux Bash | lab | <https://zentssr.com/labs> |
| Planification avec cron (Intermédiaire) | Linux Bash | lab | <https://zentssr.com/labs> |
| Dépannage service Linux (Débutant) | Linux Bash | lab | <https://zentssr.com/labs> |

## 8. Guides d’installation

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Windows Server + AD + OU | Windows | guide | <https://zentssr.com/installation> |
| GLPI sur serveur LAMP | GLPI | guide | <https://zentssr.com/installation> |
| Zabbix — Supervision réseau | Zabbix | guide | <https://zentssr.com/installation> |
| GLPI sur serveur WAMP (guide marqué « Attention ») | GLPI | guide | <https://zentssr.com/installation> |
| pfSense — Pare-feu | pfSense | guide | <https://zentssr.com/installation> |

## 9. Examen, oral et FAQ

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Infos examen — Déroulé (onglet) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Infos examen — Domaines clés (onglet) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Infos examen — Test examen (onglet) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Domaine clé — Active Directory & Windows Server (4 points) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Domaine clé — Réseau & Équipements Cisco (4 points) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Domaine clé — Administration Linux (4 points) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Domaine clé — Scripting PowerShell / Bash (3 points) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Domaine clé — Théorie, Sauvegarde & Cloud (3 points) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Domaine clé — GLPI, Supervision & Stockage (5 points) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Domaine clé — Bonus : Anglais & Soft Skills (2 points) | Infos examen | guide | <https://zentssr.com/infos-exam> |
| Test examen — Active Directory & Windows Server (3 questions) | Infos examen | quiz | <https://zentssr.com/infos-exam> |
| Test examen — Réseau & Équipements Cisco (2 questions) | Infos examen | quiz | <https://zentssr.com/infos-exam> |
| Test examen — Administration Linux (2 questions) | Infos examen | quiz | <https://zentssr.com/infos-exam> |
| Test examen — Scripting PowerShell (2 questions) | Infos examen | quiz | <https://zentssr.com/infos-exam> |
| Test examen — GLPI, Supervision & Stockage (2 questions) | Infos examen | quiz | <https://zentssr.com/infos-exam> |
| Test examen — Théorie Générale (3 questions) | Infos examen | quiz | <https://zentssr.com/infos-exam> |
| Conseils généraux de l’oral (8 conseils) | Entretien oral | guide | <https://zentssr.com/entretien-oral> |
| Questions du jury — Active Directory & Windows Server (4 questions) | Entretien oral | guide | <https://zentssr.com/entretien-oral> |
| Questions du jury — DHCP & Services réseau (4 questions) | Entretien oral | guide | <https://zentssr.com/entretien-oral> |
| Questions du jury — Dépannage réseau (4 questions) | Entretien oral | guide | <https://zentssr.com/entretien-oral> |
| Questions du jury — Bonus : Linux & divers (3 questions) | Entretien oral | guide | <https://zentssr.com/entretien-oral> |
| FAQ — Documents & organisation (4 questions) | FAQ examen | guide | <https://zentssr.com/faq-examen> |
| FAQ — Mise en situation (pratique) (5 questions) | FAQ examen | guide | <https://zentssr.com/faq-examen> |
| FAQ — Questionnaire professionnel (5 questions) | FAQ examen | guide | <https://zentssr.com/faq-examen> |
| FAQ — Oral & jury (6 questions) | FAQ examen | guide | <https://zentssr.com/faq-examen> |
| FAQ — Conseils généraux (4 questions) | FAQ examen | guide | <https://zentssr.com/faq-examen> |

## 10. Outils et cours de scripting

| Page/Module | Catégorie | Type | Lien |
|---|---|---|---|
| Calculateur de sous-réseau IP | Subnetting | outil | <https://zentssr.com/subnetting-table> |
| Table des puissances de 2 (CIDR et hôtes) | Subnetting | outil | <https://zentssr.com/subnetting-table> |
| Bases fondamentales du scripting (onglet Fondamentaux) | Scripting | cours | <https://zentssr.com/scripting-cours> |
| Variables en Bash | Scripting Bash | cours | <https://zentssr.com/scripting-cours> |
| Conditions et tests en Bash | Scripting Bash | cours | <https://zentssr.com/scripting-cours> |
| Boucles en Bash | Scripting Bash | cours | <https://zentssr.com/scripting-cours> |
| Fonctions Bash | Scripting Bash | cours | <https://zentssr.com/scripting-cours> |
| Variables en PowerShell | Scripting PowerShell | cours | <https://zentssr.com/scripting-cours> |
| Conditions PowerShell | Scripting PowerShell | cours | <https://zentssr.com/scripting-cours> |
| Boucles PowerShell | Scripting PowerShell | cours | <https://zentssr.com/scripting-cours> |
| Fonctions PowerShell | Scripting PowerShell | cours | <https://zentssr.com/scripting-cours> |
| Pipeline et filtrage PowerShell | Scripting PowerShell | cours | <https://zentssr.com/scripting-cours> |
| Accueil — QCM Détente quotidien | Accueil | outil | <https://zentssr.com/> |
| Accueil — Accès rapide Ports & Protocoles | Accueil | outil | <https://zentssr.com/> |
| Accueil — Accès rapide CIDR & VLSM | Accueil | outil | <https://zentssr.com/> |
| Accueil — Accès rapide commandes Linux & PowerShell | Accueil | outil | <https://zentssr.com/> |
| Guide ZenTSSR (assistant) | Assistant | outil | <https://zentssr.com/guide> |

## Synthèse

| Catégorie | Nombre d’éléments |
|---|---:|
| Pages du sitemap | 14 |
| Modules de révision | 14 |
| Thèmes de cours par module | 61 |
| Fiches de révision téléchargeables | 11 |
| Quiz QCM | 16 |
| Jeux et mémorisation | 30 |
| Labs interactifs | 17 |
| Guides d’installation | 5 |
| Examen, oral et FAQ | 26 |
| Outils et cours de scripting | 17 |
| **Total** | **211** |