# 📄 Wireshark

- **Environnement** : Poste d'analyse ou VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Wireshark 4.0.x et TShark du paquet `wireshark` de bookworm (à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité

## 🎯 Objectif
Installer Wireshark et TShark sur Debian 12, autoriser la capture sans root, réaliser une capture de test sur une interface autorisée puis relire le fichier produit. Les captures contiennent des données sensibles : elles ne se font que sur votre propre réseau de laboratoire ou avec une autorisation écrite.

---

## 🧪 1. Hors-Production (laboratoire)
1. Installation de Wireshark et TShark :
```bash
sudo apt update
sudo apt install -y wireshark tshark
```
👉 Explication : `wireshark` fournit l'interface graphique, `tshark` la version en ligne de commande. Pendant l'installation, répondre `Oui` à la question « Les utilisateurs non root doivent-ils pouvoir capturer ? ».

2. Autorisation de la capture pour le compte `julien` :
```bash
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark julien
groups julien
```
👉 Explication : Confirme le réglage de capture pour les non-root, puis ajoute `julien` au groupe `wireshark`. Il faut fermer la session (ou redémarrer) pour que le groupe soit pris en compte.

3. Vérification de la version et des interfaces :
```bash
tshark --version
dumpcap -D
```
👉 Explication : `dumpcap -D` liste les interfaces capturables, dont la carte miroir (par exemple `ens33`). Une interface absente indique un problème de droits ou de nom.

4. Capture de test sur l'interface autorisée :
```bash
sudo install -d -m 0700 /var/tmp/wireshark-lab
tshark -i ens33 -c 50 -w /var/tmp/wireshark-lab/capture-lab.pcapng
```
👉 Explication : Enregistre 50 paquets dans un fichier `.pcapng` protégé. Pendant la capture, générer un ping depuis une autre machine du laboratoire, par exemple vers `192.168.10.20` (adresse d'exemple).

5. Relecture du fichier capturé :
```bash
tshark -r /var/tmp/wireshark-lab/capture-lab.pcapng -c 10
tshark -r /var/tmp/wireshark-lab/capture-lab.pcapng -q -z io,phs
```
👉 Explication : La première commande affiche les 10 premiers paquets. La seconde donne la répartition des protocoles (`io,phs`). Les paquets ICMP du ping doivent apparaître.

6. Ouverture graphique du même fichier (poste de bureau uniquement) :
```bash
wireshark /var/tmp/wireshark-lab/capture-lab.pcapng
```
👉 Explication : Ouvre le fichier dans l'interface graphique pour inspection. Ne pas lancer sur un serveur sans bureau.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérification des droits de capture :
```bash
getcap /usr/bin/dumpcap
dumpcap -D
```
👉 Explication : `getcap` doit montrer les capacités `cap_net_admin` et `cap_net_raw` sur `dumpcap`, ce qui permet la capture sans root. Ce réglage est posé par le paquet ; à vérifier sur la version installée.

2. Capture filtrée en rotation, hors session SSH d'administration :
```bash
sudo install -d -m 0750 -o julien -g wireshark /var/capture/wireshark
tshark -i ens33 -f "not port 22" -b filesize:100000 -b files:5 -w /var/capture/wireshark/ens33.pcapng
```
👉 Explication : Le filtre BPF `not port 22` écarte le trafic SSH d'administration. `-b filesize:100000` ouvre un nouveau fichier toutes les 100 Mo et `-b files:5` ne conserve que cinq fichiers. Le répertoire appartient à `julien` et est accessible au groupe `wireshark` seulement.

3. Relecture d'un fichier de la rotation :
```bash
ls -lh /var/capture/wireshark/
tshark -r "$(ls /var/capture/wireshark/ens33_*.pcapng | head -n 1)" -q -z conv,ip
```
👉 Explication : Liste les fichiers produits, puis affiche les conversations IP du premier fichier. Les noms exacts (`ens33_00001_...pcapng`) dépendent de la version de TShark, à vérifier.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérification que le répertoire de captures est protégé :
```bash
sudo ls -ld /var/capture/wireshark
sudo chmod 750 /var/capture/wireshark
```
👉 Explication : Le répertoire doit être lisible par son propriétaire et le groupe `wireshark` seulement, et jamais par tous les utilisateurs. Les captures contiennent des données sensibles.

2. Relevé d'empreintes pour traçabilité :
```bash
sudo sha256sum /var/capture/wireshark/*.pcapng
```
👉 Explication : Calcule une empreinte SHA-256 de chaque fichier. La noter dans le dossier d'exploitation permet de prouver qu'une capture n'a pas été modifiée ensuite.

3. Recherche des captures anciennes à archiver ou supprimer :
```bash
sudo find /var/capture/wireshark -name "*.pcapng" -mtime +7 -print
```
👉 Explication : Liste les captures de plus de sept jours, sans les supprimer. La suppression ou l'archivage relève de la politique de conservation de l'organisation et doit être validée avant exécution.

4. Contrôle des capacités après une mise à jour :
```bash
getcap /usr/bin/dumpcap
dpkg -l wireshark-common
```
👉 Explication : Après chaque mise à jour du paquet, vérifier que `dumpcap` conserve ses capacités et que la version installée est celle attendue.

---