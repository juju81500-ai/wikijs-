# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Configurer les serveurs DNS.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les DNS (remplacer l'IP) :
   ```bash
   sudoedit /etc/resolv.conf
   ```
   👉 Explication : ligne `nameserver 192.0.2.53`; si le fichier est géré (DHCP, resolvconf), configurer la source (`dns-nameservers` dans `/etc/network/interfaces`).

2. Tester :
   ```bash
   getent hosts debian.org
   resolvectl status 2>/dev/null | head
   ```
   👉 Explication : vérifie la résolution par le même chemin que les applications.

## 2. Production — Contrôles

Deux serveurs DNS internes minimum.

## 3. Production — Sécurité

Éviter les DNS publics sur les machines de domaine.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Debian 13 Samba AD DC Resolveur Demarrage](</01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-resolveur-demarrage>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)