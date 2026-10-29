# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Fixer l'adresse IP du serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Repérer le nom de la connexion :
   ```bash
   nmcli connection show
   ```
   👉 Explication : donne le nom du profil, par exemple `ens18`.

2. Configurer l'IP statique (remplacer valeurs en MAJUSCULES : `CONN`, `192.0.2.10/24`, `192.0.2.1`) :
   ```bash
   sudo nmcli connection modify CONN ipv4.method manual ipv4.addresses 192.0.2.10/24 ipv4.gateway 192.0.2.1 ipv4.dns 192.0.2.53
   ```
   👉 Explication : `CONN` est le profil NetworkManager; adresse, passerelle et DNS sont à adapter.

3. Appliquer puis contrôler :
   ```bash
   sudo nmcli connection up CONN
   ip -br a
   ip r
   ```
   👉 Explication : réactive le profil; risque de coupure SSH, utiliser la console.

## 2. Production — Contrôles

Réserver l'adresse dans l'IPAM.

## 3. Production — Sécurité

Utiliser une console hors bande pendant le changement.

## Validation et retour arrière

- **Validation** : L'adresse fixe répond au ping depuis le réseau d'administration.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
