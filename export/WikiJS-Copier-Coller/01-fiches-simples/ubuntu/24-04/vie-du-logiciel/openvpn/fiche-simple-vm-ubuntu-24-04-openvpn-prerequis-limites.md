# Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Prerequis_Limites

- **Environnement** : VM Ubuntu 24.04 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Ubuntu 24.04 LTS Noble; version des dépôts à vérifier sur l'hôte
- **Catégorie** : OpenVPN Community Edition / prérequis et limites

---

## Problème précis à résoudre

Valider le cadre avant d'installer un serveur OpenVPN Community Edition : OS, réseau, PKI, périmètre.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'OS, le noyau et l'adresse IP de l'hôte :
   ```bash
   cat /etc/os-release
   uname -r
   ip -br address
   ip route
   ```
   👉 Explication : Confirmer que l'OS est Ubuntu 24.04 LTS à jour, dépôts main et universe standard et noter l'IP publique ou NATée à joindre depuis les clients.

2. Contrôler l'heure et le DNS :
   ```bash
   timedatectl
   resolvectl status 2>/dev/null || cat /etc/resolv.conf
   ```
   👉 Explication : Les certificats dépendent de l'heure : NTP synchronisé obligatoire.

3. Consigner les valeurs à décider avant de continuer :
   👉 Explication : VPN_NETWORK / VPN_NETMASK (réseau du tunnel), VPN_UDP_PORT (port UDP), SERVER_FQDN (nom public du serveur), PKI approuvée (CA hors ligne). Ces valeurs en majuscules sont à remplacer par le plan validé.

## 2. Production — Contrôles

Valider avec le propriétaire du service : utilisateurs, réseaux joignables, journalisation, fenêtre et accès de secours hors bande. Limites : édition Community uniquement (pas Access Server); pas de haute disponibilité ni de gestion de comptes intégrée.

## 3. Production — Sécurité

- La clé privée de la CA ne doit jamais résider sur le serveur VPN exposé.
- Aucune ouverture de port avant la fin de la recette.

## Validation et retour arrière

- **Validation** : Le tableau de décisions (réseau, port, FQDN, PKI) est rempli et approuvé.
- **Retour arrière** : Aucun changement n'a été fait à ce stade : rien à restaurer.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-installer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)