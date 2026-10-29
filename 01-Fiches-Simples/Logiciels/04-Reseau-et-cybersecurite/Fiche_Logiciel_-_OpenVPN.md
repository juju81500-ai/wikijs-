# 📄 OpenVPN

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Multiplateforme
- **Produit (matrice)** : OpenVPN / WireGuard
- **Statut dans le pack** : Couvert
- **Tags** : `logiciel`, `04-Reseau-et-cybersecurite`, `couvert`

## 📚 Couverture dans le pack

Couvert — OpenVPN Community Edition : serveur Debian 13, Ubuntu 24.04 et Rocky Linux 9 (EPEL); client Windows 11. PKI, comptes, routes et révocation sont à adapter à l’organisation; OpenVPN Access Server non couvert. Procédures non testées sur chaque OS.

Fiches simples du guide : [prérequis et limites](../../Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Prerequis_Limites.md), [installation](../../Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Installer.md), [configuration](../../Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Configurer.md), [sécurisation](../../Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Securiser.md), [validation](../../Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Valider.md), [sauvegarde/restauration](../../Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Sauvegarder_Restaurer.md), [mise à jour/retour arrière](../../Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Mise_A_Jour_Retour_Arriere.md)., [Ubuntu 24.04 — prérequis et limites](../../Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Prerequis_Limites.md), [Ubuntu 24.04 — installation](../../Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Installer.md), [Ubuntu 24.04 — configuration](../../Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Configurer.md), [Ubuntu 24.04 — sécurisation](../../Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Securiser.md), [Ubuntu 24.04 — validation](../../Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Valider.md), [Ubuntu 24.04 — sauvegarde/restauration](../../Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Sauvegarder_Restaurer.md), [Ubuntu 24.04 — mise à jour/retour arrière](../../Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Mise_A_Jour_Retour_Arriere.md), [Rocky Linux 9 — prérequis et limites](../../Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Prerequis_Limites.md), [Rocky Linux 9 — installation](../../Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Installer.md), [Rocky Linux 9 — configuration](../../Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Configurer.md), [Rocky Linux 9 — sécurisation](../../Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Securiser.md), [Rocky Linux 9 — validation](../../Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Valider.md), [Rocky Linux 9 — sauvegarde/restauration](../../Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Sauvegarder_Restaurer.md), [Rocky Linux 9 — mise à jour/retour arrière](../../Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Mise_A_Jour_Retour_Arriere.md), [Windows 11 — prérequis et limites](../../Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Prerequis_Limites.md), [Windows 11 — installation](../../Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Installer.md), [Windows 11 — configuration](../../Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Configurer.md), [Windows 11 — sécurisation](../../Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Securiser.md), [Windows 11 — validation](../../Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Valider.md), [Windows 11 — sauvegarde/restauration](../../Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Sauvegarder_Restaurer.md), [Windows 11 — mise à jour/retour arrière](../../Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Mise_A_Jour_Retour_Arriere.md)

## 🧭 Périmètre

Complément défensif à la fiche OpenVPN existante. Gérer les profils par utilisateur, authentification forte, certificats valides, restrictions réseau explicitement approuvées et journaux de connexion. Protéger les clés privées et sauvegardes; révoquer rapidement l’accès lors d’un départ ou incident. Pour Access Server, OpenVPN Community Edition ou une offre managée, suivre la documentation exacte de l’édition/version et les conditions applicables.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Tester avec un compte pilote et un seul profil autorisé, contrôler l’authentification, les routes et les journaux attendus. Pour rollback, restaurer la configuration sauvegardée et révoquer les profils de test; conserver un accès d’administration hors bande approuvé. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [OpenVPN Access Server administration guide](https://openvpn.net/vpn-server-resources/administration-guide/) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.
