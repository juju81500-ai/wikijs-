# Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Configurer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à tcpdump
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / capture bornée
- **Tags** : `tcpdump`, `ubuntu24.04`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Réaliser une capture courte, filtrée et bornée avec tcpdump, puis la relire hors ligne.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un répertoire de captures réservé :
   ```bash
   sudo install -d -m 0700 /var/tmp/captures
   ```
   👉 Explication : Le mode 0700 empêche les autres comptes de lire les fichiers de capture.

2. Lancer une capture bornée (100 paquets, filtre explicite) :
   ```bash
   sudo tcpdump -i INTERFACE_AUTORISEE -nn -c 100 -s 96 -w /var/tmp/captures/TICKET.pcap host HOTE_AUTORISE and port PORT_AUTORISE
   ```
   👉 Explication : `-i` choisit l’interface, `-nn` désactive la résolution DNS/ports, `-c` borne le nombre de paquets, `-s 96` limite le contenu capturé aux en-têtes, `-w` écrit le fichier. INTERFACE_AUTORISEE, TICKET, HOTE_AUTORISE et PORT_AUTORISE sont à remplacer.

3. Relire la capture hors ligne :
   ```bash
   sudo tcpdump -nn -r /var/tmp/captures/TICKET.pcap | head -n 20
   ```
   👉 Explication : `-r` lit le fichier sans toucher au réseau.

4. Pour une rotation limitée, utiliser une durée et un nombre de fichiers :
   ```bash
   sudo tcpdump -i INTERFACE_AUTORISEE -nn -G 60 -W 5 -w /var/tmp/captures/TICKET-%H%M%S.pcap port PORT_AUTORISE
   ```
   👉 Explication : `-G 60` ouvre un nouveau fichier toutes les 60 s et `-W 5` s’arrête après 5 fichiers; sans `-W`, la capture continue.

## 2. Production — Contrôles

Vérifier que le filtre ne couvre que les flux autorisés et que la taille du fichier est cohérente (`ls -lh`). AppArmor : le profil `/etc/apparmor.d/usr.bin.tcpdump` peut refuser l’écriture hors des chemins prévus; en cas de refus, chercher `apparmor="DENIED"` dans `sudo journalctl -k`.

## 3. Production — Sécurité

- Toujours borner (`-c`, `-G`/`-W`) et filtrer.
- Ne pas rejouer ni injecter de trafic; tcpdump sert ici à observer.

## Validation et retour arrière

- **Validation** : Un fichier .pcap lisible existe et ne contient que les flux autorisés.
- **Retour arrière** : Supprimer le fichier de test avec `shred` ou `rm` selon la politique de données, et arrêter toute capture résiduelle (`pgrep -a tcpdump`).

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_tcpdump.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Securiser.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Installer.md)
