# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

---

## Problème précis à résoudre

Exécuter les services sans privilèges.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte système sans shell (remplacer `svc-app`) :
   ```bash
   sudo useradd -r -s /usr/sbin/nologin -d /var/lib/svc-app svc-app
   id svc-app
   ```
   👉 Explication : compte non interactif réservé au service.

2. Appliquer dans l'unité systemd :
   ```bash
   sudo systemctl edit svc-app.service
   ```
   👉 Explication : ajouter `User=svc-app`, `NoNewPrivileges=yes`, `ProtectSystem=strict`.

## 2. Production — Contrôles

Un compte par service.

## 3. Production — Sécurité

Ne jamais donner de shell ni de sudo.

## Validation et retour arrière

- **Validation** : `ps -o user= -C svc-app` montre le compte dédié.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 24.04](./Sommaire_-_Vie_du_systeme_Ubuntu_24.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
