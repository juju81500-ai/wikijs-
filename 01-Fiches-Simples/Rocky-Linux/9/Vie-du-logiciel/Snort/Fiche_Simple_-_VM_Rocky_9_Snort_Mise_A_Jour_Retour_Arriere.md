# Fiche_Simple_-_VM_Rocky_9_Snort_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 dédiée à Snort
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / mise à jour et retour arrière
- **Tags** : `snort`, `rocky9`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour Snort 3 (nouvelle release) et revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder (fiche Sauvegarder_Restaurer) et consigner la version :
   ```bash
   /opt/snort3/bin/snort -V | head -n 3
   sudo mv /opt/snort3 /opt/snort3-VERSION_ACTUELLE
   ```
   👉 Explication : Conserve l’installation actuelle sous un nom daté; VERSION_ACTUELLE est à remplacer. La configuration est recopiée ensuite.

2. Compiler la nouvelle release dans un nouveau préfixe :
   👉 Explication : Reprendre les étapes de la fiche Installer avec VERSION_SNORT3 mise à jour dans un nouveau préfixe. Même procédure que l’installation; vérifier les notes de version (changements de configuration possibles).

3. Réappliquer la configuration et tester :
   ```bash
   sudo cp -a /opt/snort3-VERSION_ACTUELLE/etc/snort/snort.lua /opt/snort3/etc/snort/snort.lua
   sudo /opt/snort3/bin/snort -c /opt/snort3/etc/snort/snort.lua -T
   ```
   👉 Explication : Réutilise la configuration puis la valide; adapter si la syntaxe a changé.

4. Retour arrière :
   ```bash
   sudo systemctl stop snort3-ids.service
   sudo mv /opt/snort3 /opt/snort3-ECHEC
   sudo mv /opt/snort3-VERSION_ACTUELLE /opt/snort3
   sudo systemctl start snort3-ids.service
   ```
   👉 Explication : Restaure l’installation précédente conservée.

## 2. Production — Contrôles

Tester en lab; surveiller faux positifs après changement de règles.

## 3. Production — Sécurité

- Suivre les avis de sécurité Snort.
- Ne jamais compiler en root.

## Validation et retour arrière

- **Validation** : Nouvelle version active, `snort -T` OK, alertes cohérentes.
- **Retour arrière** : Appliquer l’étape de retour arrière puis rejouer la recette.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Snort.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Snort_Sauvegarder_Restaurer.md)
