---
title: "Installer et sécuriser FreeRADIUS pour l'authentification réseau"
description: "Installer FreeRADIUS, déclarer les clients RADIUS, brancher une source d'authentification (annuaire LDAP/AD ou fichier de test) et vérifier le fonctionnement en mode debug. Pour 802.1x/EAP, les certificats sont un prérequis."
published: true
date: 2026-11-03T09:36:14Z
tags: ["freeradius", "radius", "802.1x", "aaa", "wifi", "vpn"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Installer et sécuriser FreeRADIUS pour l'authentification réseau

- **OS / Version** : Linux (Debian/Ubuntu/RHEL et dérivés); FreeRADIUS 3.2.x ou version de la distribution
- **Type de fiche** : Installation/Déploiement
- **Environnement** : VM Linux dédiée, clients RADIUS déclarés
- **Machine ciblée** : Serveur RADIUS
- **Catégorie** : Authentification / AAA
- **Tags** : `freeradius`, `radius`, `802.1x`, `aaa`, `wifi`, `vpn`

## 1. Périmètre

Installer FreeRADIUS, déclarer les clients RADIUS, brancher une source d'authentification (annuaire LDAP/AD ou fichier de test) et vérifier le fonctionnement en mode debug. Pour 802.1x/EAP, les certificats sont un prérequis.

## 2. Prérequis

- VM Linux à jour avec IP fixe, NTP et pare-feu hôte.
- Liste des équipements clients (switchs, bornes Wi-Fi, VPN) avec adresse et secret partagé unique par client.
- Autorité de certification interne et certificat serveur pour EAP-TLS/PEAP.
- Source d'identité : LDAP, ou AD avec la méthode d'intégration choisie (certaines méthodes imposent Samba/winbind).
- Compte de service à moindre privilège pour la liaison à l'annuaire.

## 3. Variantes éditeur à distinguer

| Source | Paquet/chemin | Remarque |
|---|---|---|
| Distribution Debian/Ubuntu | Paquet `freeradius`, configuration sous `/etc/freeradius/3.0/` | Version fournie par la distribution |
| Distribution RHEL et dérivés | Paquet `freeradius`, configuration sous `/etc/raddb/` | Chemins différents de Debian |
| Paquets du projet FreeRADIUS (Network RADIUS) | Dépôts selon les instructions du projet | Pour une version plus récente |

Les chemins et noms de service varient selon la distribution.

## 4. Étapes vérifiables

### 4.1 Installer

Debian/Ubuntu :

```bash
sudo apt update
sudo apt install freeradius freeradius-ldap
```

RHEL et dérivés : installer `freeradius` et `freeradius-ldap` avec `dnf`, puis adapter les chemins.

### 4.2 Déclarer les clients

Éditer le fichier `clients.conf` du répertoire de configuration : une entrée par équipement avec adresse IP et secret fort et unique. Ne jamais déclarer de réseau large avec un secret commun.

### 4.3 Configurer la source d'identité

Activer le module LDAP ou le mode choisi, utiliser LDAPS/StartTLS avec validation du certificat, et un compte de lecture dédié. Désactiver les sites et modules inutiles.

### 4.4 Configurer EAP si 802.1x

Installer le certificat et la clé du serveur avec droits restreints, choisir EAP-TLS ou PEAP selon la politique, et désactiver les méthodes obsolètes.

### 4.5 Tester en mode debug

Arrêter le service, lancer le serveur au premier plan avec l'option de débogage, tester avec `radtest` depuis un client autorisé, puis redémarrer le service :

```bash
sudo systemctl stop freeradius
sudo freeradius -X
```

Sur RHEL le binaire peut être `radiusd`. Arrêter le mode debug avant production.

### 4.6 Activer le service et la journalisation

Activer le service, restreindre le pare-feu aux ports RADIUS (authentification UDP 1812, comptabilité UDP 1813) depuis les clients uniquement, envoyer les journaux au collecteur.

## 5. Validation

- Authentification réussie pour un compte de test et refusée pour un mauvais mot de passe.
- Seuls les clients déclarés reçoivent une réponse.
- Le service survit à un redémarrage et ne tourne pas en mode debug.
- Les journaux d'authentification sont centralisés.

## 6. Retour arrière

- Restaurer la configuration sauvegardée du répertoire FreeRADIUS et redémarrer.
- Remettre l'authentification locale des équipements en secours (compte local de dernier recours) avant bascule.
- Désinstaller le paquet et supprimer les secrets de `clients.conf` si abandon.

## 7. Limites de version et de licence

- Les chemins, modules et la syntaxe évoluent entre 3.0, 3.2 et 4.x; ne pas mélanger les versions.
- L'intégration AD dépend de la méthode retenue et de ses prérequis.
- Les secrets RADIUS protègent mal le trafic : envisager RadSec/TLS lorsque pris en charge.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [FreeRADIUS — documentation](https://freeradius.org/documentation/)
- [FreeRADIUS — wiki](https://wiki.freeradius.org/)
- [Debian — paquet freeradius](https://packages.debian.org/freeradius)