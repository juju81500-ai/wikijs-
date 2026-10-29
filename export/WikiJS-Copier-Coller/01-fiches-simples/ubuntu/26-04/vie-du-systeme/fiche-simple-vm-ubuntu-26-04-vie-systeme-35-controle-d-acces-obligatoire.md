# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Confiner les services.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler AppArmor (actif par défaut) et installer les outils :
   ```bash
   sudo apt install apparmor-utils apparmor-profiles
   sudo aa-status
   ```
   👉 Explication : liste les profils chargés et en mode `enforce`.

2. Passer un profil en application (remplacer le chemin) :
   ```bash
   sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
   ```
   👉 Explication : force le blocage; utiliser `aa-complain` pour apprendre.

## 2. Production — Contrôles

Passer en `complain` pour tester avant `enforce`.

## 3. Production — Sécurité

Lire `sudo journalctl -k | grep -i apparmor` pour les refus.

## Validation et retour arrière

- **Validation** : `aa-status` montre les profils en `enforce`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)