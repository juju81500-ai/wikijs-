# Installer et utiliser Wireshark sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark depuis les dépôts Debian configurés
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : installation APT, analyse hors ligne et capture locale ou explicitement autorisée
- **Catégorie** : analyse réseau / diagnostic
- **Tags** : `wireshark`, `debian13`, `tshark`, `dumpcap`, `pcap`, `diagnostic-reseau`

## 1. Périmètre et version

Fiche simple : [cadrer périmètre et version](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Perimetre_Version.md).

Wireshark est un analyseur de protocoles pour examiner des fichiers de capture et, si les privilèges le permettent, capturer le trafic d'une interface. Cette fiche installe la version du paquet Debian 13 provenant des sources APT déjà approuvées. Le projet amont publie ses versions séparément; la version disponible sur Debian peut différer. Relever la version candidate et suivre les mises à jour de sécurité de Debian avant tout usage.

L'analyse et la capture doivent porter uniquement sur des appareils, interfaces et réseaux possédés ou pour lesquels une autorisation explicite existe. Cette procédure ne couvre ni scan de réseaux tiers, ni interception de communications, ni déchiffrement de session, ni déploiement d'un capteur réseau.

## 2. Installer les paquets Debian

Fiche simple : [installer les paquets Debian](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Installer.md).

Vérifier l'architecture et la provenance des paquets, puis installer l'interface et les outils en ligne de commande :

```bash
dpkg --print-architecture
sudo apt update
apt-cache policy wireshark wireshark-qt tshark
sudo apt install -y wireshark wireshark-qt tshark
wireshark --version
tshark --version
```

Utiliser uniquement les dépôts Debian approuvés et ne pas ajouter de dépôt tiers pour obtenir une version plus récente sans revue de compatibilité et de signature. À la question debconf « Should non-superusers be able to capture packets? », répondre **No** si l'usage est l'analyse de fichiers existants. L'application GUI et TShark peuvent lire ces fichiers en tant qu'utilisateur normal.

## 3. Autoriser la capture live avec des privilèges séparés

Fiche simple : [autoriser la capture avec privilèges séparés](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Privileges_Capture.md).

La capture live requiert un accès privilégié aux interfaces. La conception Wireshark sépare le programme `dumpcap`, qui capture, de l'interface et des dissectors exécutés comme utilisateur. Ne pas lancer l'interface graphique ou TShark avec `sudo`.

Pour un utilisateur nominatif qui a un besoin opérationnel approuvé, reconfigurer le paquet et activer l'accès non-root :

```bash
sudo dpkg-reconfigure wireshark-common
```

Répondre **Yes** à la question autorisant les non-superusers, puis ajouter uniquement le compte de capture autorisé au groupe dédié :

```bash
sudo usermod -aG wireshark "$USER"
```

Fermer la session graphique puis la rouvrir pour que le nouveau groupe soit pris en compte. Vérifier les groupes et les interfaces exposées :

```bash
id
dumpcap -D
getcap "$(command -v dumpcap)"
```

L'appartenance au groupe `wireshark` permet la capture live sur les interfaces accessibles par `dumpcap`, pas seulement sur une interface spécifique. Ne pas ajouter de comptes génériques ou de service à ce groupe. Si le besoin est ponctuel ou les utilisateurs ne doivent pas avoir un droit permanent de capture, conserver la réponse debconf à **No** et utiliser le workflow privilégié validé par l'administrateur : `dumpcap` peut enregistrer la capture, ensuite analysée par Wireshark sous le compte normal. Ne pas modifier à la main les capabilities, le propriétaire ou le bit setuid de `dumpcap`; le paquet Debian gère ces paramètres.

## 4. Valider l'application avec un fichier hors ligne

Fiche simple : [valider avec un fichier hors ligne](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Fichier_Hors_Ligne.md).

Pour un premier essai sans capture live, ouvrir un fichier PCAP/PCAPNG d'exemple provenant du projet Wireshark ou un fichier de test approuvé. Vérifier le nombre de paquets, l'interface et les horodatages, puis appliquer un filtre d'affichage simple comme `tcp` ou `dns`.

Un filtre de capture est appliqué avant l'enregistrement et utilise la syntaxe libpcap, par exemple `host 127.0.0.1`; un filtre d'affichage tel que `ip.addr == 127.0.0.1` ne fait que masquer ou montrer les paquets d'un fichier déjà capturé. Ces syntaxes ne sont pas interchangeables.

## 5. Effectuer un test de capture strictement local

Fiche simple : [tester une capture locale](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Capture_Locale.md).

Si une capture live est requise et autorisée, limiter l'essai à la boucle locale :

1. Créer un dossier réservé au compte et n'autoriser l'accès qu'à son propriétaire.

   ```bash
   umask 077
   mkdir -p "$HOME/captures"
   chmod 700 "$HOME/captures"
   ```

2. Dans un premier terminal, démarrer une capture de durée limitée sur `lo` et enregistrer dans ce dossier :

   ```bash
   dumpcap -i lo -f 'host 127.0.0.1' -a duration:10 -w "$HOME/captures/test-local.pcapng"
   ```

3. Pendant la capture, dans un autre terminal du même poste, générer uniquement du trafic loopback :

   ```bash
   ping -c 2 127.0.0.1
   ```

4. Ouvrir `test-local.pcapng` dans Wireshark et vérifier les paquets locaux avec le filtre d'affichage `icmp`.
5. Fermer le fichier et supprimer le PCAP de test si sa conservation n'est pas nécessaire.

Pour un diagnostic métier sur une autre interface, définir au préalable le périmètre, la durée, le filtre, l'emplacement sécurisé, les approbations et la purge. Ne jamais activer le mode promiscuous ou le monitor mode sans besoin documenté et autorisation. Une capture live ne montre que ce que l'interface et le point réseau peuvent effectivement observer.

## 6. Protéger les fichiers de capture

Fiche simple : [protéger les fichiers de capture](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Proteger_Captures.md).

Un PCAP/PCAPNG peut contenir des adresses, noms d'hôtes, métadonnées, données applicatives, cookies ou informations d'authentification transmises en clair. Les filtres appliqués après coup ne retirent pas les données du fichier source. Les filtres de capture limitent le volume collecté mais ne garantissent pas la suppression de données sensibles dans les paquets retenus.

- Définir un motif de collecte, une durée et des interfaces autorisées avant la capture.
- Enregistrer dans un dossier protégé, avec un nom de dossier et de fichier neutre; éviter `/tmp` partagé et les dépôts de code.
- Ne pas joindre une capture à un ticket, message ou dépôt sans revue et anonymisation approuvée.
- Chiffrer le stockage et le transfert suivant la politique locale; contrôler les copies automatiques et sauvegardes.
- Supprimer les captures à expiration de leur finalité; la suppression classique ne garantit pas l'effacement sur SSD, snapshots ou sauvegardes.
- Mettre à jour Wireshark par APT et appliquer rapidement les mises à jour de sécurité, car les dissectors analysent des données réseau potentiellement hostiles.

## 7. Vérifications de réception

Fiche simple : [vérifier la réception](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Reception.md).

- Wireshark, TShark et dumpcap proviennent du dépôt Debian attendu et leurs versions sont consignées.
- L'analyse d'un fichier de capture approuvé fonctionne sous le compte standard.
- Si la capture live est autorisée, les privilèges sont limités au groupe nominatif approuvé et une courte capture sur `lo` s'ouvre correctement.
- L'interface graphique n'est pas exécutée comme root; le mode promiscuous et la capture WLAN ne sont pas activés par défaut.
- Le PCAP de test est protégé pendant l'analyse et supprimé après validation s'il ne doit pas être conservé.

## Sources

- [Wireshark — téléchargements, version stable et signatures](https://www.wireshark.org/download.html)
- [Wireshark User's Guide — installation des paquets Debian](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallUnixInstallBins.html#_installing_from_debs_under_debian_ubuntu_and_other_debian_derivatives)
- [Wireshark — instructions Debian pour `dumpcap` et `wireshark-common`](https://gitlab.com/wireshark/wireshark/-/raw/master/packaging/debian/README.Debian)
- [Wireshark Wiki — privilèges de capture](https://wiki.wireshark.org/CaptureSetup/CapturePrivileges)
- [Wireshark User's Guide — options de capture](https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html)
- [Wireshark User's Guide — filtres d'affichage](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)
- [Wireshark FAQ — capture et confidentialité des traces](https://www.wireshark.org/faq.html)

La version APT, la configuration `dumpcap` et l'essai graphique ne sont pas vérifiés sur une machine Debian 13 dans cette fiche. Contrôler le paquet candidat et valider les droits sur un poste pilote avant généralisation.