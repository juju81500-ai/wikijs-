# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'heure exacte.

## 1. Hors-Production (Lab / Test / POC)

1. Installer chrony :
   ```bash
   sudo apt install chrony
   sudoedit /etc/chrony/chrony.conf
   ```
   👉 Explication : ajouter `server ntp.exemple.lan iburst` (remplacer par le serveur interne).

2. Activer et contrôler :
   ```bash
   sudo systemctl enable --now chrony
   chronyc tracking
   chronyc sources -v
   ```
   👉 Explication : affiche le décalage et la source de temps.

## 2. Production — Contrôles

Deux sources internes, pas de dépendance directe à Internet.

## 3. Production — Sécurité

Autoriser seulement UDP 123 vers les serveurs de temps.

## Validation et retour arrière

- **Validation** : `chronyc tracking` : décalage faible, `Leap status: Normal`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
