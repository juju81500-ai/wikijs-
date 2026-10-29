# Fiche_Simple_-_VM_Debian_13_OpenVPN_Prerequis_Limites

- **Environnement** : VM Debian 13 dédiée à OpenVPN Community Edition
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : OpenVPN Community Edition / prérequis et limites
- **Tags** : `openvpn`, `debian13`, `vie-du-logiciel`, `prerequis_limites`

---

## Problème précis à résoudre

Définir un service VPN autorisé et ses dépendances avant toute installation.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer OS et paquets candidats :
   ```bash
   cat /etc/os-release
   apt-cache policy openvpn easy-rsa
   ```
   👉 Explication : Les versions dépendent des dépôts Debian activés; confirmer les paquets et leur origine.

2. Relever interfaces, adresses et routes prévues :
   ```bash
   ip -br address
   ip route
   ```
   👉 Explication : Documenter les réseaux d’administration et VPN approuvés; ne pas reprendre d’adresse d’exemple comme plan réel.

3. Faire approuver le propriétaire, les utilisateurs, la PKI, le port UDP et les routes avant le changement.
   👉 Explication : Ne pas activer de routage, NAT ou exposition réseau sans validation du propriétaire réseau.

## 2. Production — Contrôles

Vérifier l’approbation, la procédure de révocation, l’accès d’urgence hors tunnel et les critères de retour arrière.

## 3. Production — Sécurité

- Ne pas placer la clé privée de la CA sur le serveur; prévoir des certificats nominatifs révocables.

## Validation et retour arrière

- **Validation** : Périmètre, port, PKI et routes approuvés; aucune modification effectuée.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [OpenVPN Community Edition — documentation officielle](https://openvpn.net/community-resources/)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_OpenVPN_Installer.md)
