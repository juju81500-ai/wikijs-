# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Sauvegarder la configuration et les données.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive datée de la configuration et des données (remplacer `/var/lib/APPLI`) :
   ```sh
   doas install -d -m 0700 /var/backups
   doas tar czf /var/backups/etc-$(date +%F).tar.gz /etc /var/lib/APPLI
   doas cp /etc/apk/world /var/backups/world-$(date +%F).txt
   ```
   👉 Explication : l'archive contient `/etc`, les données et la liste des paquets demandés (`world`) pour reconstruire le système.

2. Pour un système diskless ou data, enregistrer la configuration :
   ```sh
   doas lbu status
   doas lbu commit
   ```
   👉 Explication : `lbu status` liste les fichiers modifiés; `lbu commit` crée l'archive `.apkovl`.

3. Envoyer la sauvegarde hors machine (remplacer `UTILISATEUR` et `SERVEUR_SAUVEGARDE`) :
   ```sh
   scp /var/backups/etc-*.tar.gz UTILISATEUR@SERVEUR_SAUVEGARDE:/sauvegardes/
   ```
   👉 Explication : copie l'archive sur un serveur distant par SSH.

## 2. Production — Contrôles

Planifier par `/etc/periodic/daily`, durée de rétention définie et testée.

## 3. Production — Sécurité

Chiffrer les sauvegardes qui contiennent des clés ou des secrets.

## Validation et retour arrière

- **Validation** : Archive présente sur le serveur distant et lisible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
