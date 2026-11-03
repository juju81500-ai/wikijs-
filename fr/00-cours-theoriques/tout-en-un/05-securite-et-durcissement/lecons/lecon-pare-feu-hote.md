---
title: "Leçon — Pare-feu hôte : nftables, ufw, firewalld et Pare-feu Windows Defender"
description: "À la fin de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "securite", "durcissement", "pare-feu", "nftables", "ufw", "firewalld", "windows"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Pare-feu hôte : nftables, ufw, firewalld et Pare-feu Windows Defender

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `securite`, `durcissement`, `pare-feu`, `nftables`, `ufw`, `firewalld`, `windows`
- **Niveau** : intermédiaire
- **Durée estimée** : 3 h 30 (lecture 1 h 15, laboratoire 1 h 45, exercices et quiz 30 min)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous saurez :

1. expliquer le rôle d'un **pare-feu hôte** et pourquoi la politique par défaut doit être le **refus** ;
2. écrire un jeu de **règles minimales** avec **nftables**, puis l'équivalent avec **ufw** et **firewalld** ;
3. configurer le **Pare-feu Windows Defender** (profils, règles, journalisation) ;
4. activer et lire la **journalisation** des paquets refusés sans saturer les disques ;
5. tester un **accès de secours** et appliquer une procédure **anti-lockout** (minuterie de retour arrière) ;
6. conduire chaque changement avec : **snapshot → console de secours → test → retour arrière**.

## Prérequis et durée

- Notions de TCP/IP (adresse, port, connexion établie) ; aisance avec un terminal Linux et PowerShell.
- Laboratoire : **deux VM jetables** (serveur Debian 12 ou Ubuntu Server LTS `198.51.100.20`, poste d'administration `192.0.2.10`), avec **snapshot** et **console de l'hyperviseur** ; facultatif : une VM Windows `198.51.100.50`. Adresses de documentation uniquement (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, `2001:db8::/32`).
- Durée : environ 3 h 30.

> ⚠️ **Périmètre.** Une règle de pare-feu peut vous couper de votre propre machine en une seconde. Ne l'essayez que sur un laboratoire, avec la console de secours ouverte.

## L'essentiel en bref

- Le pare-feu hôte protège la machine même si le pare-feu du réseau est contourné.
- Politique par défaut : **tout refuser en entrée**, puis autoriser **le strict nécessaire** (règles minimales, limitées par adresse source quand c'est possible).
- Toujours autoriser en premier le **trafic déjà établi** et votre **accès d'administration**, *avant* d'activer le refus.
- **Journaliser avec modération** : on veut voir les refus utiles, pas remplir le disque.
- **Anti-lockout** : accès console, seconde session de test, et **minuterie de retour arrière** qui annule la règle si vous ne confirmez pas.
- Un **seul outil de gestion** par machine : nftables **ou** ufw **ou** firewalld (ces deux derniers pilotent nftables).

---

## 1. À quoi sert un pare-feu hôte, et pourquoi « refuser par défaut »

**Analogie.** Imaginez le videur d'un immeuble avec **liste d'invités** : si votre nom n'y figure pas, vous n'entrez pas. L'autre philosophie, « entre sauf si tu es interdit », oblige à connaître tous les indésirables à l'avance : impossible. La première est la **politique par défaut refus** (*default deny*).

Le pare-feu **hôte** s'exécute sur la machine elle-même. Il complète le pare-feu **périmétrique** du réseau : si un attaquant est déjà dans le réseau interne, ou si un service est lancé par erreur, il bloque quand même l'accès.

![Schéma original du parcours d'un paquet entrant : connexion déjà établie acceptée, règle minimale acceptée, sinon journalisation limitée puis refus par la politique par défaut](images/pare-feu-hote-1.svg)

*Figure 1 — Un paquet entrant est accepté s'il est attendu ; sinon, il est journalisé puis refusé. Création originale Pack Master (CC0).*

**Les trois idées clés :**

1. **Suivi d'état** (*stateful*) : le pare-feu mémorise les connexions ; la réponse à une connexion que **vous** avez ouverte est acceptée automatiquement (`established,related`).
2. **Entrée refusée, sortie permissive** : sur un serveur ordinaire, on refuse l'entrée et on autorise la sortie (mises à jour, DNS, NTP). Restreindre la sortie est plus lourd à maintenir.
3. **Règles minimales** : une règle = *qui* (source), *quoi* (protocole, port), *vers où* (interface/adresse). Plus elle est précise, plus la surface exposée est faible. `tcp dport 22 accept` autorise le monde entier ; `ip saddr 192.0.2.0/24 tcp dport 22 accept` autorise le seul réseau d'administration.

**Ordre des règles.** Les règles sont lues de haut en bas ; la première qui correspond s'applique (en nftables, `accept` ou `drop` met fin à l'évaluation de la chaîne). Une règle `drop` trop haute annule les règles `accept` qui suivent.

---

## 2. La règle d'or : ne pas s'enfermer dehors

Activez `policy drop` sans règle SSH : la session en cours survit grâce au suivi d'état (fausse impression de réussite), mais la suivante échoue.

![Schéma original de la chronologie anti-lockout : session A ouverte, minuterie de retour arrière, application des règles, session B de test, puis annulation de la minuterie ou restauration automatique](images/pare-feu-hote-2.svg)

*Figure 2 — Anti-lockout : une minuterie restaure l'ancien état si vous ne confirmez pas. Création originale Pack Master (CC0).*

**Procédure obligatoire**, à chaque modification :

1. **Snapshot préalable** de la VM, et sauvegarde des règles actuelles dans un fichier.
2. **Accès console de secours** testé : la console de l'hyperviseur fonctionne sans réseau.
3. **Session A ouverte** (SSH ou RDP) et conservée jusqu'à la fin.
4. **Minuterie de retour arrière** armée avant d'appliquer (voir ci-dessous).
5. **Application** des règles, puis **session B de test** ouverte depuis le poste d'administration (`192.0.2.10`).
6. Si B réussit : **annuler la minuterie** et rendre persistant. Si B échoue : attendre la minuterie (ou la console) et corriger.

### Minuterie de retour arrière sous Linux (nftables)

```bash
sudo mkdir -p /root/pare-feu
( echo "flush ruleset"; sudo nft list ruleset ) | sudo tee /root/pare-feu/avant.nft >/dev/null
sudo systemd-run --on-active=300 --unit=retour-pare-feu /usr/sbin/nft -f /root/pare-feu/avant.nft
systemctl list-timers retour-pare-feu.timer --no-pager
```

👉 Explication : (1) crée un dossier pour les sauvegardes ; (2) enregistre les règles actuelles précédées de `flush ruleset` pour qu'elles **remplacent** les nouvelles à la restauration ; (3) planifie le rechargement de cet état **dans 300 secondes** ; (4) vérifie que la minuterie existe. Sur Red Hat, le chemin de `nft` peut être `/usr/sbin/nft` ou `/sbin/nft` (contrôlez avec `command -v nft`).

Après validation :

```bash
sudo systemctl stop retour-pare-feu.timer
```

👉 Explication : annule la restauration programmée. Si vous oubliez, l'ancien état revient : c'est volontaire.

### Équivalents

- **ufw** : pas de retour arrière natif ; planifiez `systemd-run --on-active=300 --unit=retour-ufw /usr/sbin/ufw disable` (le pare-feu sera désactivé et non restauré : acceptable en laboratoire).
- **firewalld** : les modifications **sans `--permanent`** sont *temporaires* (runtime) et disparaissent au rechargement ou au redémarrage ; c'est un filet naturel. On rend permanent seulement après test (`--runtime-to-permanent`).
- **Windows** : `netsh advfirewall export` avant, tâche planifiée de restauration (section 7).

---

## 3. nftables : le moteur moderne de Linux

**nftables** a remplacé iptables comme interface du filtrage réseau dans le noyau (**Netfilter**). Trois concepts :

- **Table** : un conteneur, rattaché à une famille (`inet` regroupe IPv4 et IPv6).
- **Chaîne** : une liste de règles accrochée à un point du noyau (*hook*) : `input` (vers la machine), `forward` (traversée), `output` (depuis la machine). Une chaîne de base porte la **politique** (`policy drop`).
- **Règle** : conditions + verdict (`accept`, `drop`, `reject`, `log`…).

### Lire l'existant (lecture seule)

```bash
sudo nft list ruleset
sudo nft list tables
systemctl is-enabled nftables 2>/dev/null; systemctl is-active nftables 2>/dev/null
ss -lntup
```

👉 Explication : affiche toutes les règles, liste les tables, indique si le service de chargement au démarrage est activé et actif, puis liste les ports en écoute. Une sortie vide de `nft list ruleset` ne prouve pas l'absence de filtrage : ufw ou firewalld peuvent gérer les règles autrement, et Docker ajoute les siennes.

### Un jeu de règles minimal

Fichier `/etc/nftables.conf` pour un serveur web administré depuis `192.0.2.0/24` :

```nft
#!/usr/sbin/nft -f
flush ruleset

table inet filtre {
  chain entree {
    type filter hook input priority filter; policy drop;

    ct state established,related accept
    ct state invalid drop
    iif "lo" accept

    icmp type echo-request limit rate 5/second accept
    icmpv6 type { echo-request, nd-neighbor-solicit, nd-neighbor-advert, nd-router-solicit, nd-router-advert } accept

    ip saddr 192.0.2.0/24 tcp dport 22 ct state new accept
    tcp dport { 80, 443 } ct state new accept

    limit rate 5/minute log prefix "nft-refus: "
  }
  chain transit {
    type filter hook forward priority filter; policy drop;
  }
  chain sortie {
    type filter hook output priority filter; policy accept;
  }
}
```

👉 Explication : une seule table `inet` pour IPv4 et IPv6 ; en entrée, politique **refus**, acceptation des connexions établies et du bouclage, rejet des paquets invalides, ping limité, ICMPv6 de découverte de voisins (**indispensable** pour que IPv6 fonctionne), SSH uniquement depuis `192.0.2.0/24`, web ouvert, puis journalisation **limitée** de ce qui reste avant le refus par la politique. La chaîne de transit refuse tout (la machine n'est pas un routeur). Fichier à adapter : retirez 80 et 443 si ce n'est pas un serveur web.

Application sûre :

```bash
sudo cp -a /etc/nftables.conf /etc/nftables.conf.bak-20261101
sudo nft -c -f /etc/nftables.conf && echo "syntaxe OK"
sudo nft -f /etc/nftables.conf
sudo systemctl enable --now nftables
```

👉 Explication : sauvegarde le fichier, **vérifie** la syntaxe sans appliquer (`-c`), charge les règles, puis fait en sorte qu'elles soient rechargées au démarrage. La minuterie de la section 2 doit être **armée avant** la troisième commande. Retour arrière : relancer `avant.nft` ou restaurer le snapshot.

---

## 4. ufw : la façade simple d'Ubuntu

**ufw** (*Uncomplicated Firewall*) écrit les règles nftables/iptables à votre place. Il convient pour un serveur simple.

```bash
sudo ufw status verbose
sudo ufw show added
```

👉 Explication : affiche l'état et les règles ajoutées sans rien modifier (`show added` liste même celles qui ne sont pas encore actives).

Séquence sûre (console ouverte, session A conservée, **règle SSH avant l'activation**) :

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.0.2.0/24 to any port 22 proto tcp
sudo ufw allow 443/tcp
sudo ufw logging low
sudo ufw --dry-run enable | head -n 5
sudo ufw enable
sudo ufw status numbered
```

👉 Explication : politique refus en entrée et autorisation en sortie, SSH limité à `192.0.2.0/24`, HTTPS ouvert, journalisation de niveau faible, simulation, activation, puis liste numérotée. ufw prévient que l'activation « peut perturber les connexions SSH existantes » : c'est pourquoi la règle SSH vient avant. Retour arrière : `sudo ufw delete <numéro>` ou `sudo ufw disable`.

Les refus sont dans `/var/log/ufw.log` ou `journalctl -k | grep UFW`.

---

## 5. firewalld : zones et configuration dynamique (famille Red Hat)

**firewalld** raisonne en **zones** : chaque interface appartient à une zone (`public`, `internal`, `trusted`, `drop`…) qui porte un niveau de confiance et des services autorisés. La zone `public` refuse par défaut les connexions entrantes non autorisées.

```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all
```

👉 Explication : vérifie que le démon tourne, quelles zones sont actives et ce que la zone par défaut autorise (services, ports, règles riches). Lecture seule.

**Runtime ou permanent ?** Sans `--permanent`, la règle s'applique tout de suite mais est **perdue au rechargement** ; avec `--permanent`, elle est écrite mais **inactive** jusqu'au rechargement. Méthode sûre : tester en runtime, valider, puis `--runtime-to-permanent`.

```bash
sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.0.2.0/24" service name="ssh" accept'
sudo firewall-cmd --remove-service=ssh
sudo firewall-cmd --set-log-denied=unicast
sudo firewall-cmd --list-all
sudo firewall-cmd --runtime-to-permanent
```

👉 Explication : autorise SSH **seulement** depuis `192.0.2.0/24` (règle ajoutée *avant* de retirer le service SSH ouvert à tous), active la journalisation des refus unicast, affiche le résultat, puis rend permanent **après** test depuis une seconde session. Retour arrière avant validation : `sudo firewall-cmd --reload` restaure l'état permanent.

> ⚠️ N'utilisez jamais `--panic-on` en distant : il coupe tout le trafic, y compris votre session.

---

## 6. Journalisation et lecture des refus

La journalisation répond à trois questions : **qu'est-ce qui a été refusé, d'où, et pourquoi ?** Mais journaliser tout, c'est noyer l'information et saturer le disque (un scan produit des milliers de lignes).

| Outil | Comment journaliser | Où lire |
|---|---|---|
| nftables | `limit rate 5/minute log prefix "nft-refus: "` | `journalctl -k` |
| ufw | `ufw logging low` (ou `medium`) | `/var/log/ufw.log`, `journalctl -k` |
| firewalld | `--set-log-denied=unicast` | `journalctl -k` (messages `FINAL_REJECT`) |
| Windows | `Set-NetFirewallProfile -LogBlocked True` | fichier `pfirewall.log` |

```bash
sudo journalctl -k --since "10 min ago" --no-pager | grep -E 'nft-refus|UFW BLOCK|FINAL_REJECT' | tail -n 10
```

👉 Explication : cherche dans les messages du noyau des dix dernières minutes les refus journalisés par chacun des trois outils ; lecture seule. Les champs utiles sont `SRC` (source), `DST`, `PROTO` et `DPT` (port destination).

**Bonnes pratiques de journalisation.**

- **Limiter le débit** (`limit rate`), n'enregistrer que les refus, utiliser un **préfixe explicite**.
- **Centraliser** les journaux et assurer la **rotation**.
- Une source qui frappe sur beaucoup de ports en peu de temps est probablement un scan ; une source qui insiste sur SSH évoque une force brute.

---

## 7. Pare-feu Windows Defender

Le **Pare-feu Windows Defender avec fonctions avancées** est intégré à Windows. Il filtre selon des **profils** correspondant au type de réseau.

![Schéma original des trois profils du Pare-feu Windows Defender : Domaine, Privé et Public, avec trafic entrant bloqué par défaut, sortant autorisé, et RDP limité au réseau d'administration](images/pare-feu-hote-4.svg)

*Figure 3 — Trois profils, trois niveaux de confiance. Création originale Pack Master (CC0).*

- **Domaine** : réseau d'entreprise authentifié auprès d'Active Directory ;
- **Privé** : réseau de confiance (domicile, labo) ;
- **Public** : réseau non fiable (café, hôtel). Profil le plus strict.

Par défaut, **l'entrée est bloquée** et la **sortie autorisée** pour chaque profil : c'est déjà la bonne politique. Les erreurs viennent des **règles d'autorisation trop larges** et de la **désactivation** du pare-feu « pour dépanner ».

### Contrôler (lecture seule)

```powershell
Get-NetConnectionProfile | Select-Object Name, NetworkCategory, InterfaceAlias
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction, LogBlocked, LogFileName
Get-NetFirewallRule -Enabled True -Direction Inbound -Action Allow | Select-Object DisplayName, Profile | Sort-Object DisplayName
```

👉 Explication : (1) le profil réseau actif de chaque interface, (2) l'état des trois profils (activé, actions par défaut, journalisation), (3) toutes les règles entrantes qui **autorisent** du trafic. Lisez la troisième liste comme la liste des portes ouvertes : chaque règle doit avoir une justification.

### Sauvegarder, puis durcir

```powershell
New-Item -ItemType Directory -Path C:\Sauvegardes -Force | Out-Null
netsh advfirewall export "C:\Sauvegardes\pare-feu-avant.wfw"
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True -DefaultInboundAction Block -DefaultOutboundAction Allow
Set-NetFirewallProfile -Profile Domain,Private,Public -LogBlocked True -LogMaxSizeKilobytes 16384
```

👉 Explication : exporte la configuration actuelle (retour arrière : `netsh advfirewall import "C:\Sauvegardes\pare-feu-avant.wfw"`), active les trois profils avec entrée bloquée et sortie autorisée, puis journalise les paquets bloqués dans le fichier par défaut `%systemroot%\system32\LogFiles\Firewall\pfirewall.log` avec une taille limitée à 16 Mio.

### Règle d'accès minimale et accès de secours

```powershell
New-NetFirewallRule -DisplayName "Admin-RDP-reseau-admin" -Direction Inbound -Protocol TCP -LocalPort 3389 -RemoteAddress 192.0.2.0/24 -Profile Domain,Private -Action Allow
Get-NetFirewallRule -DisplayName "Admin-RDP-reseau-admin" | Get-NetFirewallAddressFilter
```

👉 Explication : autorise RDP uniquement depuis `192.0.2.0/24` sur les profils Domaine et Privé (le profil Public reste fermé), puis relit l'adresse source configurée. Désactivez ensuite la règle intégrée plus large avec `Disable-NetFirewallRule -Name 'RemoteDesktop-UserMode-In-TCP'` **seulement après** avoir testé une seconde connexion.

### Minuterie de retour arrière Windows

```powershell
schtasks /create /tn "retour-pare-feu" /sc once /st 23:55 /ru SYSTEM /tr "netsh advfirewall import C:\Sauvegardes\pare-feu-avant.wfw"
schtasks /delete /tn "retour-pare-feu" /f
```

👉 Explication : planifie la restauration de la sauvegarde à l'heure indiquée (choisissez une heure proche, quelques minutes après l'application) ; la seconde commande **supprime** la tâche une fois le test validé. Adaptez `/st` à l'heure locale.

**Lecture des refus.** Le fichier `pfirewall.log` se lit avec `Get-Content "$env:SystemRoot\System32\LogFiles\Firewall\pfirewall.log" -Tail 20` (droits administrateur). Pour obtenir les événements 5152 (paquet bloqué) et 5157 (connexion bloquée) dans le journal Sécurité, activez l'audit « Filtering Platform » ; ils sont très volumineux : à n'activer que pour une investigation ciblée.

---

## 8. Tester l'accès de secours et vérifier

![Schéma original comparant les façades de pare-feu : ufw et firewalld pilotent nftables et Netfilter sous Linux ; le Pare-feu Windows Defender utilise des profils et le moteur de filtrage de Windows](images/pare-feu-hote-3.svg)

*Figure 4 — Plusieurs façades, un même moteur. Création originale Pack Master (CC0).*

Un pare-feu se **prouve par des tests**, des deux côtés.

**Depuis le poste d'administration (`192.0.2.10`)** :

```bash
ssh -o ConnectTimeout=5 admin-example@198.51.100.20 true && echo "SSH autorisé"
nc -vz -w 3 198.51.100.20 443
nc -vz -w 3 198.51.100.20 3306
```

👉 Explication : teste que SSH passe depuis le réseau d'administration, que HTTPS est ouvert et que 3306 est bien **bloqué** (la commande doit expirer ou être refusée). Un test de **non-accès** est aussi important qu'un test d'accès. Depuis Windows : `Test-NetConnection 198.51.100.50 -Port 3389`.

**Depuis une adresse hors périmètre** (`203.0.113.15`), le test SSH doit **échouer**. Vérifiez aussi **IPv6** (`2001:db8::20`) si la machine en a une. Sur la machine, `ss -lntup` ne doit montrer que des services prévus.

```bash
sudo nft list chain inet filtre entree | grep -n 'policy\|dport'
```

👉 Explication : affiche la chaîne d'entrée pour contrôler la politique et les ports autorisés ; lecture seule. Ajoutez `sudo nft list ruleset | grep counter` si vous avez ajouté des compteurs pour voir quelles règles sont utilisées.

> Un scan de vérification (`nmap`) ne se fait que sur vos machines de laboratoire, avec autorisation.

---

## Mise en pratique guidée

**Cadre.** Serveur `srv-lab` (`198.51.100.20`), client d'administration `adm-lab` (`192.0.2.10`), second client `ext-lab` (`203.0.113.15`). Durée : environ 1 h 45.

**Avant de commencer :** snapshot `avant-pare-feu` de `srv-lab`, console de l'hyperviseur testée, session SSH A ouverte depuis `adm-lab`.

1. **État initial.** `sudo nft list ruleset`, `ss -lntup`, puis depuis `adm-lab` : `nc -vz -w 3 198.51.100.20 22`. Notez les ports en écoute.
2. **Service de démonstration.** Installez `nginx` (80) sur `srv-lab` ; vérifiez que `ext-lab` l'atteint.
3. **Sauvegarde et minuterie.** Section 2 : fichier `avant.nft`, minuterie de 300 secondes.
4. **Application.** Écrivez le fichier de la section 3, validez avec `nft -c`, appliquez avec `nft -f`.
5. **Tests.** Depuis `adm-lab` : session B SSH réussie ; depuis `ext-lab` : SSH échoue, HTTP réussit. Lisez les refus : `sudo journalctl -k --since "5 min ago" | grep nft-refus`.
6. **Confirmation.** Si tout est correct : `sudo systemctl stop retour-pare-feu.timer`, puis `sudo systemctl enable --now nftables` pour la persistance.
7. **Simulation d'erreur (bien utile).** Rearmez la minuterie, **retirez** volontairement la règle SSH, appliquez, constatez que la session B échoue, puis **ne faites rien** : après 5 minutes, l'ancien état revient. Vous venez de vérifier que votre filet de sécurité fonctionne.
8. **Variantes.** Restaurez le snapshot et refaites l'exercice avec ufw (section 4), firewalld (section 5) ou, sur une VM Windows, avec la section 7.
9. **Retour arrière final.** Restaurez le snapshot `avant-pare-feu`.

---

## Exercices

1. **(Facile)** Expliquez la différence entre `drop` et `reject` et dites lequel est le plus discret.
2. **(Facile)** Pourquoi faut-il une règle `ct state established,related accept` en tête de chaîne ?
3. **(Facile)** Quelle différence entre le Pare-feu du réseau et le pare-feu hôte ?
4. **(Intermédiaire)** Écrivez la règle nftables autorisant SSH uniquement depuis `198.51.100.0/24`.
5. **(Intermédiaire)** Sous firewalld, vous ajoutez une règle sans `--permanent`, puis la machine redémarre. Que se passe-t-il ?
6. **(Intermédiaire)** Décrivez la séquence ufw qui active un refus par défaut sans couper votre session SSH.
7. **(Avancé)** Votre politique refuse l'entrée ; IPv6 ne fonctionne plus. Quelle cause probable et quelle règle ajouter ?
8. **(Avancé)** Concevez le plan de test d'un pare-feu sur un serveur web à distance : accès attendus, accès interdits, retour arrière.

---

## Corrigés des exercices

1. `drop` jette le paquet **sans répondre** : plus discret, ralentit les scans. `reject` répond par un refus explicite : plus simple à diagnostiquer, mais révèle un filtre.
2. Les réponses aux connexions que la machine a ouvertes et les paquets d'une session déjà autorisée reviennent en entrée ; sans cette règle, la session SSH existante tomberait.
3. Le pare-feu réseau protège un segment en bordure ; l'hôte protège la machine elle-même, y compris contre un attaquant déjà dans le réseau.
4. `ip saddr 198.51.100.0/24 tcp dport 22 ct state new accept`, placée **avant** la fin de chaîne et dans une chaîne dont la politique est `drop`.
5. La règle est **perdue** (elle n'existait qu'en runtime). Pour la conserver : tester, puis `firewall-cmd --runtime-to-permanent`, ou utiliser `--permanent` suivi de `--reload`.
6. `default deny incoming`, `default allow outgoing`, `allow from <réseau d'administration> to any port 22 proto tcp`, éventuellement `--dry-run enable`, puis `enable`, avec session A ouverte et test d'une session B avant de fermer A.
7. Le protocole de découverte de voisins (NDP, ICMPv6) est bloqué ; sans lui IPv6 ne résout plus les adresses de couche 2. Autoriser `icmpv6 type { nd-neighbor-solicit, nd-neighbor-advert, nd-router-solicit, nd-router-advert }`, et `echo-request` limité.
8. Prérequis : snapshot, console, session A, minuterie. Tests : SSH depuis le réseau d'administration (OK), HTTPS public (OK), SSH depuis une autre source (refusé), ports non prévus (refusés), IPv6 si utilisé ; journaux contrôlés. Un échec laisse la minuterie restaurer l'état précédent.

---

## Quiz

**Q1. Que signifie « politique par défaut refus » ?**
a) tout est autorisé sauf ce qui est interdit b) tout est refusé sauf ce qui est explicitement autorisé c) tout est journalisé d) tout est chiffré
**Réponse : b.** C'est la liste d'invités : on n'entre que si une règle l'autorise.

**Q2. Quelle règle doit venir en premier dans une chaîne d'entrée ?**
a) le journal b) l'acceptation des connexions établies et du bouclage c) le refus final d) le NAT
**Réponse : b.** Elle laisse passer les réponses légitimes et le trafic local avant les règles spécifiques.

**Q3. `nft -c -f fichier` fait quoi ?**
a) charge les règles b) vérifie la syntaxe sans appliquer c) supprime les règles d) sauvegarde les règles
**Réponse : b.** `-c` signifie contrôle (*check*) : une erreur de syntaxe n'est pas appliquée.

**Q4. Sous firewalld, une règle ajoutée sans `--permanent` est…**
a) permanente b) appliquée immédiatement mais perdue au rechargement ou redémarrage c) ignorée d) appliquée seulement après redémarrage
**Réponse : b.** C'est la configuration *runtime*, utile pour tester avant de valider.

**Q5. Pourquoi ouvrir la règle SSH avant d'activer ufw ?**
a) c'est plus rapide b) sinon la prochaine connexion SSH est refusée c) ufw l'exige d) pour la journalisation
**Réponse : b.** La session ouverte survit grâce au suivi d'état, mais une nouvelle connexion échouerait.

**Q6. Pourquoi limiter le débit de journalisation (`limit rate`) ?**
a) pour accélérer le pare-feu b) pour ne pas saturer le disque lors d'un scan c) c'est obligatoire d) pour masquer les attaques
**Réponse : b.** Un scan peut générer des milliers de refus ; un débit limité garde le journal lisible.

**Q7. Quel est le profil Windows le plus strict ?**
a) Domaine b) Privé c) Public d) Invité
**Réponse : c.** Il s'applique aux réseaux non fiables ; il doit rester le plus fermé.

**Q8. Qu'est-ce qu'une minuterie de retour arrière ?**
a) une pause avant le démarrage b) une tâche qui restaure l'ancien état si l'on ne confirme pas c) un délai de session d) un antivirus
**Réponse : b.** Si le test échoue ou si vous perdez l'accès, l'ancienne configuration revient seule.

**Q9. Quel test est indispensable après activation d'un pare-feu ?**
a) seulement les accès autorisés b) seulement les accès interdits c) les accès autorisés **et** interdits d) aucun
**Réponse : c.** Il faut prouver que ce qui devait passer passe, et que le reste est bloqué.

**Q10. Pourquoi ne pas utiliser ufw, firewalld et nftables en même temps ?**
a) c'est interdit b) ils écrivent chacun dans le même noyau et créent des règles imprévisibles c) trop de mémoire d) incompatibles avec SSH
**Réponse : b.** Un seul outil de gestion évite les conflits et les règles « fantômes ».

---

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Remède |
|---|---|---|
| Plus de SSH après `policy drop` | règle SSH absente ou source mal écrite | console, minuterie de retour arrière, corriger la règle |
| Règles perdues au redémarrage | `nftables` non activé, ou firewalld sans `--permanent` | `systemctl enable --now nftables`, `--runtime-to-permanent` |
| IPv6 en panne | NDP/ICMPv6 bloqué | autoriser les types ICMPv6 de voisinage |
| Règle ignorée | ordre : un `drop` plus haut l'intercepte | `nft list chain …` : replacer la règle plus haut |
| Journal saturé | journalisation sans limite | `limit rate`, niveau `low`, rotation |
| Conteneur joignable malgré ufw | Docker publie ses ports via ses propres règles | filtrer dans la chaîne dédiée (`DOCKER-USER`) ou ne publier que sur `127.0.0.1` |
| RDP coupé après règle Windows | adresse source ou profil incorrect | console ; `netsh advfirewall import` de la sauvegarde |

---

## À retenir

- Un pare-feu hôte **refuse par défaut** et n'autorise que le strict nécessaire, avec des sources précises.
- Toujours : **connexions établies d'abord**, **accès d'administration** avant l'activation du refus.
- nftables est le moteur ; **ufw** et **firewalld** sont des façades : **un seul** outil par machine.
- firewalld : **runtime** pour tester, **permanent** pour valider.
- Journaliser **avec limite**, avec préfixe, et centraliser.
- Windows : trois profils, entrée bloquée par défaut, règles limitées par adresse source, export avant modification.
- **Anti-lockout** : snapshot, console, session A conservée, minuterie de retour arrière, **session B de test**, test des accès **autorisés et interdits**.

---

## Pour aller plus loin

- Wiki nftables du projet Netfilter : <https://wiki.nftables.org/>
- Page de manuel de `nft` : <https://man7.org/linux/man-pages/man8/nft.8.html>
- Pare-feu sur Ubuntu Server (documentation officielle) : <https://documentation.ubuntu.com/server/how-to/security/firewalls/>
- Documentation firewalld : <https://firewalld.org/documentation/>
- Pare-feu Windows (Microsoft Learn) : <https://learn.microsoft.com/fr-fr/windows/security/operating-system-security/network-security/windows-firewall/>
- RFC 4890, *Recommendations for Filtering ICMPv6 Messages in Firewalls* : <https://www.rfc-editor.org/rfc/rfc4890>
- RFC 5737 (adresses IPv4 de documentation) : <https://www.rfc-editor.org/rfc/rfc5737> et RFC 3849 (adresses IPv6 de documentation) : <https://www.rfc-editor.org/rfc/rfc3849>
- NIST SP 800-41 Rev. 1, *Guidelines on Firewalls and Firewall Policy* : <https://csrc.nist.gov/pubs/sp/800/41/r1/final>

*Si une adresse a changé, cherchez le titre de la page sur le site officiel.*

---

## Crédits des images

Aucune image tierce n'est utilisée dans cette leçon : les quatre schémas sont des créations originales.

| Fichier | Source (URL de la page) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/pare-feu-hote-1.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet (œuvre originale) |
| `images/pare-feu-hote-2.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet |
| `images/pare-feu-hote-3.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet |
| `images/pare-feu-hote-4.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet |

*Création originale du projet Pack Master, dédiée au domaine public (CC0).*

---

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Debian 12 / Ubuntu Server LTS (nftables, ufw), Red Hat (firewalld), Windows Server 2022 (Pare-feu Defender) | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

*Les commandes ont été relues pour leur syntaxe, mais aucune n'a été exécutée sur une machine Linux ou Windows cible lors de la rédaction. Validez-les dans votre laboratoire, console de secours ouverte, avant tout usage.*