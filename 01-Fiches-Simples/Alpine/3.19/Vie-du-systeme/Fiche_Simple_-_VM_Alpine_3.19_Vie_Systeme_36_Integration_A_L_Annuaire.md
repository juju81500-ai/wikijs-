# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Rattacher la machine à l'exploitation (Alpine n'a pas de `realm join`).

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la joignabilité du serveur d'annuaire (remplacer `SERVEUR_ANNUAIRE`) :
   ```sh
   nc -zv SERVEUR_ANNUAIRE 389
   nc -zv SERVEUR_ANNUAIRE 636
   ```
   👉 Explication : contrôle les ports LDAP et LDAPS.

2. Chercher le client d'authentification disponible :
   ```sh
   apk search -v sssd openldap-clients
   ```
   👉 Explication : indique si SSSD et les outils LDAP sont proposés dans les dépôts 3.19.

3. Enregistrer la machine dans le réseau d'administration (DNS, supervision, bastion) :
   ```sh
   hostname -f
   ip -br addr
   ```
   👉 Explication : relever le nom et l'adresse à enregistrer dans les systèmes d'inventaire.

## 2. Production — Contrôles

Les comptes locaux nominatifs avec clés SSH restent la méthode par défaut pour Alpine.

## 3. Production — Sécurité

Ne pas stocker de mot de passe de liaison LDAP en clair dans un fichier lisible par tous.

## Validation et retour arrière

- **Validation** : Le port de l'annuaire est joignable, la décision d'authentification est consignée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](<../Vie-du-logiciel/OpenSSH/Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
