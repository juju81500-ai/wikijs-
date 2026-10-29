# Fiche_Simple_-_Appliance_OPNsense_Installation_Installer_Systeme.md

- **Environnement** : Appliance physique ou VM dédiée avec interfaces réseau identifiées
- **OS / Version** : OPNsense Community ou Business Edition, release maintenue compatible avec la plateforme
- **Catégorie** : pare-feu / installation

---

## Problème précis à résoudre

Installer OPNsense sur le disque réservé et attribuer les interfaces.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer sur le média officiel et choisir le mode d'installation pris en charge par le matériel.
   👉 Explication : le mode dépend du matériel (écran/clavier ou série).

2. Dans l'installateur, sélectionner le disque réservé après double vérification du périphérique.
   👉 Explication : l'opération efface le disque choisi.

3. Retirer le média et redémarrer, puis dans le menu console choisir **1) Assign interfaces** et attribuer WAN et LAN.
   👉 Explication : associe chaque carte réseau à son rôle.

4. Dans le menu console, choisir **2) Set interface IP address** pour une adresse de gestion temporaire isolée.
   👉 Explication : permet de vérifier l'accès local avant raccordement au réseau réel.

5. Contrôler les interfaces :
   ```sh
   ifconfig
   ```
   👉 Explication : Dans le shell de la console (menu **8) Shell**), liste les interfaces et leurs adresses.

## 2. Production — Contrôles

Double-vérifier le disque cible et la correspondance des cartes réseau.

## 3. Production — Sécurité

- Ne pas raccorder au réseau réel avant la fin de l'assistant initial.

## Validation et retour arrière

- **Validation** : le système démarre, les interfaces WAN/LAN sont attribuées et l'accès local fonctionne.
- **Retour arrière** : recommencer l'installation sur le disque réservé ou restaurer le snapshot de la VM.

## Si le problème n'est pas résolu

- [OPNsense — Installation](https://docs.opnsense.org/manual/install.html)
- [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html)
- [Guide complet — étape 2](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production#2-installer-le-systeme)