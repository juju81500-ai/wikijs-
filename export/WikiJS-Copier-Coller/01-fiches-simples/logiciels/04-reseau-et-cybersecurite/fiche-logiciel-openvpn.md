# 📄 OpenVPN

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Multiplateforme
- **Produit (matrice)** : OpenVPN / WireGuard
- **Statut dans le pack** : Couvert

## 📚 Couverture dans le pack

Couvert — OpenVPN Community Edition : serveur Debian 13, Ubuntu 24.04 et Rocky Linux 9 (EPEL); client Windows 11. PKI, comptes, routes et révocation sont à adapter à l’organisation; OpenVPN Access Server non couvert. Procédures non testées sur chaque OS.

Fiches simples du guide : [prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-prerequis-limites), [installation](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-installer), [configuration](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-configurer), [sécurisation](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-securiser), [validation](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-valider), [sauvegarde/restauration](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-sauvegarder-restaurer), [mise à jour/retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-mise-a-jour-retour-arriere)., [Ubuntu 24.04 — prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-prerequis-limites), [Ubuntu 24.04 — installation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-installer), [Ubuntu 24.04 — configuration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-configurer), [Ubuntu 24.04 — sécurisation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-securiser), [Ubuntu 24.04 — validation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-valider), [Ubuntu 24.04 — sauvegarde/restauration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-sauvegarder-restaurer), [Ubuntu 24.04 — mise à jour/retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-mise-a-jour-retour-arriere), [Rocky Linux 9 — prérequis et limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-prerequis-limites), [Rocky Linux 9 — installation](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-installer), [Rocky Linux 9 — configuration](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-configurer), [Rocky Linux 9 — sécurisation](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-securiser), [Rocky Linux 9 — validation](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-valider), [Rocky Linux 9 — sauvegarde/restauration](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-sauvegarder-restaurer), [Rocky Linux 9 — mise à jour/retour arrière](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-mise-a-jour-retour-arriere), [Windows 11 — prérequis et limites](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-prerequis-limites), [Windows 11 — installation](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-installer), [Windows 11 — configuration](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-configurer), [Windows 11 — sécurisation](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-securiser), [Windows 11 — validation](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-valider), [Windows 11 — sauvegarde/restauration](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-sauvegarder-restaurer), [Windows 11 — mise à jour/retour arrière](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-mise-a-jour-retour-arriere)

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