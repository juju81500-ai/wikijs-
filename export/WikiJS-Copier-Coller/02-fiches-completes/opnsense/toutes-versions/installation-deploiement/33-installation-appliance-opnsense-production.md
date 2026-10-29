# Installer une appliance OPNsense en production

- **Type de fiche** : Installation / Déploiement
- **Environnement** : Appliance physique ou VM dédiée avec interfaces réseau identifiées
- **OS / Version** : OPNsense Community ou Business Edition, release maintenue compatible avec la plateforme
- **Rôle** : Installer le système, attribuer les interfaces et valider le routage et le filtrage

## 1. Préparer l'architecture

Fiche simple : [préparer l'architecture OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-appliance-opnsense-installation-preparer-architecture).

Définir WAN, LAN, VLAN, réseaux de gestion, adresses, passerelle, DNS, règles, NAT, VPN, journaux et procédure d'accès de secours. Prévoir au minimum une console locale ou série. Pour une VM, affecter des cartes réseau dédiées et conserver leur correspondance avec les interfaces virtuelles.

Télécharger l'image depuis le site officiel, vérifier son empreinte selon les instructions du projet et préparer le média d'installation. Ne pas connecter l'appliance à un réseau de production avant d'avoir défini les interfaces et les règles.

## 2. Installer le système

Fiche simple : [installer le système OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-appliance-opnsense-installation-installer-systeme).

1. Démarrer sur le média officiel et choisir le mode d'installation pris en charge par le matériel.
2. Installer sur le disque réservé après double vérification du périphérique cible; l'opération efface le disque choisi.
3. Retirer le média et redémarrer, puis attribuer les interfaces WAN/LAN depuis la console.
4. Utiliser une adresse de gestion temporaire isolée et vérifier l'accès local avant raccordement au réseau réel.

## 3. Effectuer l'assistant initial

Fiche simple : [assistant initial OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-appliance-opnsense-installation-assistant-initial).

Depuis un poste d'administration dédié, ouvrir l'interface Web via l'adresse LAN. Définir un mot de passe administrateur unique, le nom d'hôte et le domaine, la zone horaire, les DNS, le type d'adressage WAN et le plan IP LAN. Remplacer les paramètres temporaires par ceux approuvés et vérifier l'absence de conflit d'adresse.

Mettre à jour vers une version maintenue après consultation des notes de version et avant exposition externe. Exporter une première configuration protégée dès que l'administration est stable.

## 4. Créer les règles nécessaires

Fiche simple : [créer les règles nécessaires OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-appliance-opnsense-installation-regles-necessaires).

Partir du principe que les flux sont refusés sauf autorisation explicite. Ajouter uniquement les règles nécessaires, dans le bon ordre et sur la bonne interface; limiter les sources d'administration au sous-réseau dédié. N'autoriser aucune gestion Web/SSH depuis le WAN sans architecture sécurisée et justification.

Configurer DHCP, DNS, VLAN, NAT, VPN ou haute disponibilité uniquement si le rôle le nécessite. Procéder par étape, tester les flux avant d'ajouter la suivante, et garder la console accessible.

## 5. Recette

Fiche simple : [recette OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-appliance-opnsense-installation-recette).

- Vérifier interfaces, passerelles, DNS, route par défaut et heure.
- Depuis des clients de test, vérifier les flux autorisés et les refus attendus.
- Confirmer que l'administration n'est joignable que depuis le réseau prévu.
- Tester journaux firewall, sauvegarde de configuration, redémarrage contrôlé et restauration en lab.
- Consigner version, empreinte du média, interfaces, adresses, règles, responsable et résultat.

## 6. Retour arrière

Fiche simple : [retour arrière OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-appliance-opnsense-installation-retour-arriere).

En cas de perte d'accès, utiliser la console pour corriger l'affectation ou restaurer une configuration valide. Si une mise à jour empêche le démarrage, employer la procédure officielle de restauration propre à la version et au type de stockage; ne pas effacer l'installation ni réinitialiser sans sauvegarde vérifiée.

## Sources

- [OPNsense — Installation](https://docs.opnsense.org/manual/install.html)
- [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html)
- [OPNsense — Téléchargements et releases](https://opnsense.org/download/)