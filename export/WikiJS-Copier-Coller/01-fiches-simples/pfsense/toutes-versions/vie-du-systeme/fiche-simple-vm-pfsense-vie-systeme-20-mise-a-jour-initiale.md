# Fiche_Simple_-_VM_pfSense_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Appliquer les correctifs disponibles dès l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans System > Update > System Update : lire la version disponible, puis Confirm pour lancer la mise à jour.
   👉 Explication : télécharge et applique les mises à jour; le pare-feu redémarre.

2. Ou en shell (console option 13 « Update from console » ou SSH) :
   ```sh
   pfSense-upgrade -c
   pfSense-upgrade
   ```
   👉 Explication : `-c` vérifie si une mise à jour existe; sans option, l'outil met à jour interactivement.

3. Prendre une sauvegarde de `config.xml` et un environnement de démarrage avant, puis contrôler :
   ```sh
   cat /etc/version
   pfSense-repoc 2>/dev/null | head -3
   ```
   👉 Explication : affiche la version atteinte.

## 2. Production — Contrôles

Planifier une fenêtre de maintenance et sauvegarder la configuration avant la mise à jour.

## 3. Production — Sécurité

Lire les notes de version pour les changements incompatibles.

## Validation et retour arrière

- **Validation** : `cat /etc/version` renvoie la version cible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)