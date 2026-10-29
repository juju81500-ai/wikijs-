# Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Acces_GUI_Premiers_Reglages.md

- **Environnement** : VM pfSense CE en laboratoire sur Proxmox VE, deux interfaces (WAN et LAN isolés)
- **OS / Version** : pfSense Community Edition 2.9.0 (VM x86-64 sur Proxmox VE)
- **Catégorie** : pare-feu et routage

---

## Problème précis à résoudre

Ouvrir le GUI depuis le LAN isolé et sécuriser les réglages initiaux.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis la VM cliente sur le pont LAN, ouvrir `https://192.168.1.1`.
   👉 Explication : le GUI n'est accessible que depuis le LAN isolé.

2. Se connecter avec les identifiants par défaut `admin` / `pfsense` puis changer immédiatement le mot de passe : **System > User Manager > admin > Edit**.
   👉 Explication : ne jamais laisser le mot de passe par défaut; ne jamais exposer GUI ou SSH sur WAN.

3. Dans l'assistant (**System > Setup Wizard**) : nom d'hôte et domaine de lab sans conflit DNS, fuseau horaire et NTP.
   👉 Explication : évite les incohérences d'heure et de nom.

4. Configurer WAN selon le réseau amont isolé et contrôler la passerelle; remplacer le LAN par un sous-réseau de lab non chevauchant.
   👉 Explication : puis renouveler l'adresse de la VM cliente et rouvrir le GUI sur la nouvelle adresse.

5. Si un DHCP existe déjà sur ce LAN, désactiver celui de pfSense : **Services > DHCP Server > LAN**, décocher **Enable**.
   👉 Explication : évite deux serveurs DHCP concurrents.

6. Installer un certificat GUI de confiance pour le lab et limiter l'administration au réseau de gestion autorisé.
   👉 Explication : protège la session d'administration.

7. Vérifier **Status > Interfaces**.
   👉 Explication : noms, adresses, liens et débits; le WAN ne doit pas être administrable depuis l'amont.

## 2. Production — Contrôles

Utiliser un compte d'administration nominatif et consigner le plan d'adressage; mot de passe stocké dans le coffre.

## 3. Production — Sécurité

- Ne pas importer de paramètres d'un fournisseur réel dans un lab partagé.
- Aucun accès GUI/SSH depuis le WAN.

## Validation et retour arrière

- **Validation** : le GUI répond en HTTPS depuis le LAN uniquement et le mot de passe par défaut est changé.
- **Retour arrière** : restaurer la configuration précédente via **Diagnostics > Backup & Restore** ou recréer la VM de test.

## Si le problème n'est pas résolu

- [Netgate — identifiants par défaut](https://docs.netgate.com/pfsense/en/latest/usermanager/defaults.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Guide complet](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab#5-acceder-au-gui-et-securiser-les-premiers-reglages)