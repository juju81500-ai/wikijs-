# Fiche_Simple_-_VM_Debian_13_Wireshark_Valider_Capture_Locale.md

- **Environnement** : Wireshark/TShark depuis APT Debian 13, fichier PCAPNG de test ou capture loopback autorisée
- **OS / Version** : Debian 13 Trixie amd64
- **Catégorie** : diagnostic réseau / analyse de capture
- **Tags** : `debian13`, `wireshark`, `dumpcap`, `pcapng`, `diagnostic`, `confidentialite`

---

## Problème précis à résoudre

Vérifier l'installation et l'analyse d'une capture de test sans lancer Wireshark en root ni enregistrer des paquets hors du périmètre autorisé.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les versions :
   ```bash
   wireshark --version | head -1
   tshark --version | head -1
   apt-cache policy wireshark wireshark-common
   ```
   👉 Explication : relever la version et l'origine du paquet.

2. Ouvrir un PCAP d'exemple approuvé avec un filtre d'affichage :
   ```bash
   wireshark -r exemple.pcapng -Y 'tcp'
   tshark -r exemple.pcapng -Y 'dns' | head
   ```
   👉 Explication : remplacer le fichier; en GUI : **Fichier > Ouvrir**, puis saisir le filtre dans la barre.

3. Si la capture live est nécessaire et autorisée, contrôler les droits :
   ```bash
   sudo dpkg-reconfigure wireshark-common
   getent group wireshark
   ```
   👉 Explication : choisir « Non » si l'analyse hors ligne suffit; sinon `sudo usermod -aG wireshark UTILISATEUR` (reconnexion nécessaire).

4. Capturer uniquement sur loopback :
   ```bash
   umask 077; mkdir -p ~/cap-test && cd ~/cap-test
   dumpcap -i lo -f 'host 127.0.0.1' -a duration:10 -w local.pcapng &
   ping -c 3 127.0.0.1
   wait
   ```
   👉 Explication : `umask 077` protège le fichier; durée limitée à 10 s.

5. Analyser et nettoyer :
   ```bash
   tshark -r local.pcapng -Y icmp | head
   rm -f local.pcapng
   ```
   👉 Explication : en GUI : **Fichier > Ouvrir**, filtre `icmp`; ne conserver le fichier que si nécessaire.

## 2. Production — Contrôles

Toute capture non locale requiert un périmètre écrit, une durée, des interfaces et filtres approuvés, un propriétaire du fichier, un emplacement chiffré et une échéance de suppression.

## 3. Production — Sécurité

- Ne jamais exécuter Wireshark ou TShark comme root.
- Le groupe `wireshark` autorise la capture via dumpcap; ne le réserver qu'aux utilisateurs qui en ont réellement besoin.
- Les filtres d'affichage n'effacent pas les paquets du PCAP. Inspecter et protéger le fichier brut comme une donnée sensible.
- Ne pas activer promiscuous/monitor mode ni capturer des interfaces, réseaux ou appareils tiers sans autorisation explicite.
- Maintenir les paquets à jour; ne pas modifier manuellement setuid/capabilities de dumpcap.

## Validation et retour arrière

- **Validation** : analyse hors ligne réussie; si nécessaire, capture loopback limitée à 10 secondes et au dossier privé; privilèges vérifiés.
- **Retour arrière** : arrêter la capture, supprimer le PCAP de test, retirer l'utilisateur du groupe `wireshark` si le besoin d'accès prend fin, puis ouvrir une nouvelle session.

## Si le problème n'est pas résolu

- [Wireshark — FAQ](https://www.wireshark.org/faq.html)
- [Wireshark Wiki — privilèges de capture](https://wiki.wireshark.org/CaptureSetup/CapturePrivileges)
- [Guide complet Wireshark Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/83_Installation_Wireshark_Debian_13_Analyse_Capture.md)