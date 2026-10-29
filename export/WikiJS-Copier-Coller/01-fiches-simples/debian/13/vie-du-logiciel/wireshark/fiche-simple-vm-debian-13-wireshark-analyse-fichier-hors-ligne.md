# Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Fichier_Hors_Ligne.md

- **Environnement** : Poste Debian 13 avec Wireshark installé
- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark des dépôts Debian
- **Catégorie** : analyse reseau / validation

---

## Problème précis à résoudre

Tester Wireshark sur un fichier de capture existant, sans capture live.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir un fichier d'exemple approuvé (remplacer `exemple.pcapng` par votre fichier) :
   ```bash
   wireshark exemple.pcapng
   ```
   👉 Explication : on analyse sous le compte normal.

2. Vérifier le nombre de paquets, l'interface et les horodatages dans la barre d'état, puis saisir le filtre d'affichage `tcp` ou `dns`.
   👉 Explication : un filtre d'affichage masque seulement des paquets d'un fichier déjà capturé.

3. Lire le même fichier en ligne de commande :
   ```bash
   tshark -r exemple.pcapng -Y dns
   ```
   👉 Explication : `-Y` applique un filtre d'affichage; ne pas le confondre avec le filtre de capture (`-f`, syntaxe libpcap).

## 2. Production — Contrôles

Utiliser des fichiers d'exemple du projet Wireshark ou des captures approuvées.

## 3. Production — Sécurité

- Les filtres d'affichage ne retirent pas les données sensibles du fichier source.

## Validation et retour arrière

- **Validation** : Le fichier s'ouvre et les filtres fonctionnent sous le compte standard.
- **Retour arrière** : Fermer le fichier; supprimer la copie de test si inutile.

## Si le problème n'est pas résolu

- [Wireshark — filtres d'affichage](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)
- [Wireshark — options de capture](https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html)
- [Guide complet Wireshark Debian 13](/02-fiches-completes/debian/13/installation-deploiement/83-installation-wireshark-debian-13-analyse-capture#4-valider-lapplication-avec-un-fichier-hors-ligne)