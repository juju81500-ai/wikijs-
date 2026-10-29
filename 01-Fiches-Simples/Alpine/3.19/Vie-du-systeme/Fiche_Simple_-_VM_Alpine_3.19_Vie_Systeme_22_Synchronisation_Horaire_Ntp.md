# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'horloge exacte avec `chrony`.

## 1. Hors-Production (Lab / Test / POC)

1. Installer et activer chrony :
   ```sh
   doas apk add chrony
   doas rc-update add chronyd default
   doas rc-service chronyd start
   ```
   👉 Explication : `chronyd` est le service OpenRC; il est lancé au démarrage.

2. Pointer vers les sources internes (remplacer `SERVEUR_NTP`) dans `/etc/chrony/chrony.conf` :
   ```sh
   doas sh -c 'cat >> /etc/chrony/chrony.conf <<EOF
   server SERVEUR_NTP iburst
   EOF'
   doas rc-service chronyd restart
   ```
   👉 Explication : ajoute la source puis relit la configuration; `iburst` accélère la première synchronisation.

3. Contrôler la synchronisation :
   ```sh
   chronyc tracking
   chronyc sources -v
   ```
   👉 Explication : `Leap status : Normal` et une source marquée `^*` confirment la synchronisation.

## 2. Production — Contrôles

Utiliser au moins deux sources internes.

## 3. Production — Sécurité

Ne pas ouvrir le port NTP du serveur vers l'extérieur sans besoin.

## Validation et retour arrière

- **Validation** : `chronyc tracking` affiche un écart inférieur à la seconde.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
