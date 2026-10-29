# Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Capture_Locale.md

- **Environnement** : Poste Debian 13 avec droits dumpcap
- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark des dépôts Debian
- **Catégorie** : analyse reseau / capture

---

## Problème précis à résoudre

Réaliser une capture courte limitée à la boucle locale.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un dossier réservé au compte :
   ```bash
   umask 077
   mkdir -p "$HOME/captures"
   chmod 700 "$HOME/captures"
   ```
   👉 Explication : seul le propriétaire accède aux captures.

2. Dans un premier terminal, capturer 10 secondes sur `lo` :
   ```bash
   dumpcap -i lo -f 'host 127.0.0.1' -a duration:10 -w "$HOME/captures/test-local.pcapng"
   ```
   👉 Explication : le filtre de capture et la durée limitent le volume.

3. Pendant ce temps, dans un autre terminal, générer du trafic loopback :
   ```bash
   ping -c 2 127.0.0.1
   ```
   👉 Explication : uniquement du trafic local.

4. Ouvrir `test-local.pcapng` dans Wireshark et appliquer le filtre d'affichage `icmp`.
   👉 Explication : les paquets locaux doivent apparaître.

5. Supprimer le test s'il n'est plus utile :
   ```bash
   rm -f "$HOME/captures/test-local.pcapng"
   ```
   👉 Explication : on ne garde pas de capture sans finalité.

## 2. Production — Contrôles

Pour une autre interface, définir périmètre, durée, filtre, emplacement sécurisé, approbations et purge.

## 3. Production — Sécurité

- Ne pas activer promiscuous ni monitor mode sans besoin documenté et autorisation.
- Une capture ne montre que ce que l'interface observe.

## Validation et retour arrière

- **Validation** : Le PCAP local s'ouvre et contient les paquets ICMP.
- **Retour arrière** : Supprimer le fichier et le dossier `captures` s'ils sont inutiles.

## Si le problème n'est pas résolu

- [Wireshark — options de capture](https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html)
- [Wireshark Wiki — privilèges de capture](https://wiki.wireshark.org/CaptureSetup/CapturePrivileges)
- [Guide complet Wireshark Debian 13](/02-fiches-completes/debian/13/installation-deploiement/83-installation-wireshark-debian-13-analyse-capture#5-effectuer-un-test-de-capture-strictement-local)