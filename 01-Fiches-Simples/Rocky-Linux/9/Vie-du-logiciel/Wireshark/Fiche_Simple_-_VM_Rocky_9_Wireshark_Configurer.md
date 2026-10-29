# Fiche_Simple_-_VM_Rocky_9_Wireshark_Configurer

- **Environnement** : VM Rocky Linux 9 dédiée à Wireshark
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / privilèges de capture et analyse
- **Tags** : `wireshark`, `rocky9`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Autoriser une capture minimale via dumpcap et analyser un fichier hors ligne.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter un compte nominatif au groupe de capture :
   ```bash
   sudo usermod -aG wireshark NOM_UTILISATEUR
   id NOM_UTILISATEUR
   ```
   👉 Explication : `usermod -aG` ajoute le groupe `wireshark` sans retirer les autres; NOM_UTILISATEUR est à remplacer. Se reconnecter pour appliquer. Le paquet réserve normalement `dumpcap` au groupe `wireshark`; vérifier avec `ls -l /usr/bin/dumpcap` et `getcap /usr/bin/dumpcap`.

2. Lister les interfaces :
   ```bash
   dumpcap -D
   ```
   👉 Explication : Montre ce que dumpcap peut capturer avec les droits du compte.

3. Capturer de façon bornée :
   ```bash
   dumpcap -i INTERFACE_AUTORISEE -c 200 -f "host HOTE_AUTORISE" -w /var/tmp/TICKET.pcapng
   ```
   👉 Explication : `-c` limite les paquets, `-f` applique un filtre de capture, `-w` écrit le fichier; HOTE_AUTORISE est à remplacer.

4. Analyser hors ligne en CLI :
   ```bash
   capinfos /var/tmp/TICKET.pcapng
   tshark -r /var/tmp/TICKET.pcapng -q -z io,phs
   ```
   👉 Explication : `capinfos` résume le fichier; `-z io,phs` affiche la hiérarchie des protocoles sans interpréter de contenu applicatif.

5. Ouvrir dans la GUI : menu Fichier > Ouvrir, sélectionner le .pcapng, puis Statistiques > Hiérarchie des protocoles.
   👉 Explication : La GUI est réservée aux postes avec session graphique; l’analyse reste hors ligne.

## 2. Production — Contrôles

Vérifier que seul le groupe `wireshark` a le droit de capture et que les captures sont stockées avec droits restreints.

## 3. Production — Sécurité

- Droit de capture nominatif, pas de compte partagé.
- Aucune injection ni rejeu de trafic.

## Validation et retour arrière

- **Validation** : Un fichier .pcapng est produit puis lu par tshark.
- **Retour arrière** : Retirer le compte du groupe : `sudo gpasswd -d NOM_UTILISATEUR wireshark`, et supprimer le fichier de test.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Wireshark_Securiser.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Wireshark_Installer.md)
