# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Inscrire la machine et les accès dans l'inventaire.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les éléments d'identité :
   ```sh
   hostname -f
   cat /etc/alpine-release
   uname -r
   ip -br addr
   ```
   👉 Explication : nom, version, noyau et adresses à enregistrer dans la CMDB.

2. Relever les comptes et les droits :
   ```sh
   getent group wheel
   awk -F: '$3 >= 1000 {print $1}' /etc/passwd
   ```
   👉 Explication : liste les administrateurs et les comptes d'utilisateurs.

3. Relever les clés SSH autorisées :
   ```sh
   doas find /home -name authorized_keys -exec wc -l {} +
   ```
   👉 Explication : compte les clés par compte pour la revue d'accès.

## 2. Production — Contrôles

Désigner un propriétaire, un contact et une criticité pour la machine.

## 3. Production — Sécurité

Réviser les accès à chaque départ ou changement de poste.

## Validation et retour arrière

- **Validation** : La fiche CMDB correspond à la machine.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
