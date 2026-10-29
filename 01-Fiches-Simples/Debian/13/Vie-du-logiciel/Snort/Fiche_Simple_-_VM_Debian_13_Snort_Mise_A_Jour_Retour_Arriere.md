# Fiche_Simple_-_VM_Debian_13_Snort_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 dédiée à Snort IDS passif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : Snort IDS passif / mise à jour et retour arrière
- **Tags** : `snort`, `debian13`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Mettre Snort et ses règles à jour en contrôlant compatibilité et restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Relever version installée, candidat et mises à jour :
   ```bash
   dpkg-query -W snort
   apt-cache policy snort
   apt list --upgradable
   ```
   👉 Explication : Examiner avis Debian/éditeur et compatibilité des règles.

2. Sauvegarder configuration et règles, puis tester le candidat en laboratoire.
   👉 Explication : Ne pas remplacer un capteur en service sans test syntaxique et comparaison d’alertes.

3. Après approbation, mettre à jour puis retrouver le chemin de configuration :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade snort
   snort -V
   dpkg-query -L snort | grep -E "snort.*(conf|lua)"
   ```
   👉 Explication : Relancer `sudo snort -T -c CHEMIN_CONFIG`; CHEMIN_CONFIG est à remplacer par le chemin découvert.

## 2. Production — Contrôles

Organiser la fenêtre; vérifier propriétaire, compatibilité règles/configuration, alertes et pertes de paquets.

## 3. Production — Sécurité

- Ne pas désactiver la détection silencieusement ni revenir à un binaire vulnérable sans dérogation.

## Validation et retour arrière

- **Validation** : Version attendue, configuration testée et événement pilote confirmé.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [Snort IDS passif — documentation officielle](https://www.snort.org/documents)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_Snort_Prerequis_Limites.md)
