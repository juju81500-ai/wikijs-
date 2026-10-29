# 📄 VM_Debian_12_Systeme_Locale-Timezone.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Système & Services / Localisation
- **Tags** : `[debian12]`, `[debian-family]`, `[locale]`, `[timezone]`, `[timedatectl]`, `[utf-8]`

## 🎯 Problème précis à résoudre
Configurer la locale système (UTF-8, français) et le fuseau horaire d'un serveur Debian 12, avec une horloge matérielle en UTC, pour que les journaux, les sauvegardes planifiées et les accents s'affichent de façon cohérente.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Consultation de l'horloge et du fuseau actuels :
   `timedatectl status`
   👉 Explication : Affiche le fuseau horaire, l'heure locale, l'état de la synchronisation NTP et le mode de l'horloge matérielle (RTC).
2. Consultation de la locale active :
   `localectl status`
   👉 Explication : Affiche les variables `LANG` et `LC_*` ainsi que la disposition du clavier de la console.
3. Installation des générateurs de locales :
   `sudo apt-get update && sudo apt-get install -y locales`
   👉 Explication : Installe le paquet `locales` qui fournit `locale-gen` et les fichiers de traduction.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation des locales françaises et anglaises :
   `sudoedit /etc/locale.gen`
   👉 Explication : Décommenter les lignes `fr_FR.UTF-8 UTF-8` et `en_US.UTF-8 UTF-8`, puis exécuter `sudo locale-gen` pour compiler les locales.
2. Définition de la locale par défaut :
   `sudo localectl set-locale LANG=fr_FR.UTF-8`
   👉 Explication : Écrit la locale par défaut dans `/etc/default/locale`, prise en compte par les nouvelles sessions.
3. Définition du fuseau horaire :
   `sudo timedatectl set-timezone Europe/Paris`
   👉 Explication : Associe le fuseau horaire de Paris au système (gère automatiquement l'heure d'été et d'hiver).

---

## 🔒 3. Production — Façon Sécurisée (Horloge UTC & Vérification)
1. Horloge matérielle en UTC :
   `sudo timedatectl set-local-rtc 0`
   👉 Explication : Conserve l'horloge matérielle en UTC, ce qui évite les décalages de journaux lors des changements d'heure et les conflits avec d'autres systèmes.
2. Vérification de la synchronisation et du fuseau :
   `timedatectl show -p Timezone -p NTPSynchronized -p LocalRTC`
   👉 Explication : Confirme le fuseau `Europe/Paris`, la synchronisation NTP active et la valeur `LocalRTC=no`.
3. Vérification de la présence de la locale compilée :
   `locale -a | grep -i fr_FR`
   👉 Explication : Liste les locales françaises réellement disponibles ; si la ligne est absente, relancer `sudo locale-gen`.
