# 📄 Fiche_Simple_-_VM_Alpine_Chrony_NTP_OpenRC.md

- **Environnement** : VM Alpine Linux
- **OS / Version** : Alpine Linux avec OpenRC et Chrony
- **Catégorie** : Services / Synchronisation horaire
- **Tags** : `[alpine]`, `[chrony]`, `[ntp]`, `[openrc]`, `[time]`, `[services]`

## 🎯 Problème précis à résoudre
Installer Chrony comme client NTP sur une VM Alpine, le gérer avec OpenRC et vérifier la synchronisation sans exposer inutilement un service NTP serveur.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer Chrony, l'activer au démarrage OpenRC et le lancer :
   ```sh
   apk add chrony
   rc-update add chronyd default
   rc-service chronyd start
   rc-service chronyd status
   ```
2. Vérifier les sources et l'état de synchronisation :
   ```sh
   chronyc sources -v
   chronyc tracking
   ```
   👉 *Explication : Chrony peut nécessiter un délai avant la première synchronisation; vérifier la connectivité vers les sources NTP autorisées.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder `/etc/chrony/chrony.conf`, puis déclarer les serveurs NTP internes validés :
   ```text
   server <ntp-interne> iburst
   ```
2. Redémarrer OpenRC et vérifier les sources :
   ```sh
   rc-service chronyd restart
   chronyc sources -v
   chronyc tracking
   ```
   👉 *Explication : adapter le chemin de configuration au paquet Alpine installé et ne garder que des sources approuvées par l'organisation.*

## 🔒 3. Production — Façon Sécurisée
1. Configurer la machine comme client seulement. Ne pas ajouter de directive `allow` ni ouvrir UDP/123 si elle ne doit pas servir d'autres équipements.
2. Ne pas utiliser `chronyc makestep` en fonctionnement courant sans évaluer l'effet d'un saut d'horloge sur les applications et les journaux.
3. En LXC, vérifier la stratégie de temps de l'hôte Proxmox : le conteneur partage le noyau et ne gère pas son horloge comme une VM autonome.

## ✅ Validation et retour arrière
- Confirmer que `chronyc tracking` indique une source sélectionnée et une dérive attendue.
- En cas de défaut, restaurer le fichier précédent et redémarrer `chronyd` avec OpenRC.
- Examiner les messages de service et la connectivité réseau vers la source NTP.