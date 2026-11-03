---
title: "Messageries libres Zimbra, BlueMind et BleuKango : distinguer produits et versions, puis déployer en laboratoire"
description: "- Ce document compare des produits distincts de messagerie et de collaboration ; ils ne partagent ni installateur, ni procédure de mise à jour, ni modèle de licence."
published: true
date: 2026-11-03T09:36:14Z
tags: ["zimbra", "bluemind", "bluekango", "messagerie", "linux"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Messageries libres Zimbra, BlueMind et BleuKango : distinguer produits et versions, puis déployer en laboratoire

- **OS / Version** : Linux (selon la matrice de support de chaque produit et version)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Cadrage produit/édition/version, déploiement pilote de Zimbra ou BlueMind, validation, retour arrière
- **Catégorie** : Messagerie
- **Tags** : `zimbra`,`bluemind`,`bluekango`,`messagerie`,`linux`

## 1. Portée, hypothèses et licences

- Ce document compare des **produits distincts** de messagerie et de collaboration ; ils ne partagent ni installateur, ni procédure de mise à jour, ni modèle de licence.
- Hypothèse : un seul produit est retenu pour un pilote, sur une VM de laboratoire dédiée. La production exige la matrice de support, le calendrier de maintenance et le contrat de l'éditeur ou de l'intégrateur.
- Rien dans cette fiche ne remplace la documentation éditeur de la version retenue.

## 2. Cartographie à valider avant toute installation

| Produit | Éléments à établir (source éditeur) |
|---|---|
| Zimbra | Éditions : une version communautaire à code source ouvert et une édition commerciale à abonnement ; la disponibilité, la maintenance et les canaux de paquets dépendent de l'éditeur ou du distributeur de la version. Relever le numéro de version majeure et le support OS. |
| BlueMind | Solution de messagerie et collaboration d'un éditeur français ; existence d'une édition communautaire et d'abonnements (« Subscription ») à confirmer sur le site éditeur ; relever la version majeure et les OS pris en charge. |
| BleuKango | Nom non confirmé comme produit autonome dans les sources vérifiées pour cette fiche. **Ne pas l'installer ni lui associer des commandes** tant que l'éditeur, la version et la documentation officielle ne sont pas identifiés (demande au commanditaire ou au fournisseur). Créer une fiche dédiée ensuite. |

Remplir pour chaque produit : éditeur, édition, version, OS supportés, ports, licence, fin de support, mode de sauvegarde, intégration annuaire.

## 3. Prérequis communs

- VM de laboratoire sur un OS exactement listé par l'éditeur, nom d'hôte FQDN résolvable (DNS interne), horloge synchronisée (NTP).
- Ressources conformes à la documentation (RAM, disque) ; instantané avant installation.
- Ports limités : le courrier (25, 465/587, 143/993), HTTP(S) et l'administration restent filtrés ; ne pas ouvrir le port 25 vers Internet en lab.
- Enregistrements DNS MX/A du domaine de test ; aucun envoi de courrier réel.

## 4. Chemin Zimbra (pilote)

1. Télécharger l'archive d'installation ou les paquets depuis la source indiquée par l'éditeur de la version choisie ; vérifier la somme de contrôle ou la signature publiée.
2. Désactiver ou désinstaller le serveur de messagerie existant de la VM (Postfix, Sendmail) comme demandé par la documentation.
3. Lancer l'installateur de l'archive (script `install.sh` de l'archive dans les versions classiques, à confirmer dans le guide de la version), répondre aux invites, définir le mot de passe admin.
4. Vérifier les services avec l'utilisateur `zimbra` :

```bash
su - zimbra -c "zmcontrol status"
su - zimbra -c "zmcontrol -v"
```

5. Créer un domaine et un compte de test (`zmprov` ou console d'administration) et tester webmail, SMTP et IMAP en lab.

## 5. Chemin BlueMind (pilote)

1. Suivre la procédure d'installation de la version choisie sur la documentation officielle BlueMind : dépôts ou installateur fournis par l'éditeur, serveur unique pour le pilote.
2. Contrôler l'état des services avec l'outil d'administration documenté pour la version (`bmctl` selon la documentation : confirmer la syntaxe sur votre version).
3. Créer un domaine et un utilisateur de test dans la console d'administration, tester webmail, SMTP, IMAP et agenda.
4. Configurer l'annuaire LDAP/AD seulement après la validation du pilote.

## 6. Validation

- Tous les services attendus sont actifs, la version affichée correspond à la fiche d'identité remplie.
- Connexion webmail, envoi interne et réception, IMAP/SMTP authentifiés, certificat TLS valide (autorité interne en lab).
- Sauvegarde exécutée et restauration vérifiée sur une VM isolée.
- Journaux sans erreur critique ; plan de maintenance daté.

## 7. Retour arrière

Restaurer l'instantané de la VM de lab. Pour une désinstallation, suivre la procédure officielle de l'éditeur (ne pas supprimer manuellement des répertoires système). Ne pas basculer les MX de production sans plan de repli : conserver le MX d'origine et un TTL court jusqu'à la validation finale.

## Sources officielles

- [Zimbra — documentation](https://www.zimbra.com/documentation/)
- [Zimbra — wiki technique](https://wiki.zimbra.com/)
- [BlueMind — site officiel](https://www.bluemind.net/)
- [BlueMind — documentation](https://doc.bluemind.net/)

Aucun serveur Zimbra, BlueMind ou BleuKango n'a été installé pendant la rédaction ; identité, version et commandes doivent être confirmées avec l'éditeur.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |