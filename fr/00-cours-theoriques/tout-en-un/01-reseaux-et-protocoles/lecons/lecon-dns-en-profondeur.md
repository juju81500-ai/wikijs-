---
title: "Leçon — DNS en profondeur : hiérarchie, résolution, enregistrements, cache et dépannage"
description: "À la fin de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "reseaux", "dns", "dig", "nslookup", "resolve-dnsname", "diagnostic"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — DNS en profondeur : hiérarchie, résolution, enregistrements, cache et dépannage

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `reseaux`, `dns`, `dig`, `nslookup`, `resolve-dnsname`, `diagnostic`
- **Niveau** : intermédiaire (après les bases d'adressage [[Glossary:IP]])
- **Durée estimée** : 3 h 30 (lecture 1 h 30, laboratoire 1 h 15, exercices et quiz 45 min)
- **Catégorie** : Tout-en-un / Réseaux et protocoles

---

## Objectifs pédagogiques

À la fin de cette leçon, vous saurez :

1. lire un nom complet ([[Glossary:FQDN]]) de droite à gauche et décrire la hiérarchie racine, TLD, zone, délégation ;
2. distinguer client léger (stub resolver), résolveur récursif et serveur faisant autorité ;
3. comparer résolution récursive et itérative ;
4. écrire et reconnaître les enregistrements A, AAAA, [[Glossary:CNAME]], MX, TXT, PTR, NS et SOA ;
5. raisonner sur le cache, le [[Glossary:TTL]] et le cache négatif ;
6. interroger le [[Glossary:DNS]] avec `dig`, `nslookup` et `Resolve-DnsName`, et interpréter les codes de réponse ;
7. appliquer une méthode de dépannage qui isole le poste, le résolveur et la zone.

## Prérequis et durée

- Savoir lire une adresse IPv4 avec son masque et comprendre ce qu'est un port.
- Savoir ouvrir un terminal Linux ou PowerShell.
- Pour le laboratoire : une [[Glossary:VM]] Debian ou Ubuntu jetable (avec instantané), sans accès à la production.
- Durée totale : environ 3 h 30.

Tous les noms et adresses sont réservés à la documentation : `example.com`, `example.test`, `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, `2001:db8::/32`. Aucun secret ni donnée réelle n'est employé.

## l'essentiel en bref

- Le DNS est un **annuaire distribué et hiérarchique** qui traduit des noms en données (surtout des adresses IP) et inversement.
- Un nom se lit **de droite à gauche** : `www.example.com.` → racine, `com`, `example`, `www`.
- Le poste interroge un **résolveur récursif**, qui questionne la racine, le TLD puis le serveur **faisant autorité**.
- Chaque réponse porte un **TTL** (secondes) : pendant ce temps, elle est réutilisée depuis des caches.
- Codes de réponse : `NOERROR`, `NXDOMAIN` (le nom n'existe pas), `SERVFAIL` (échec de résolution), `REFUSED` (refus).
- Dépannage : tester l'IP, puis le nom comme le fait l'application, puis interroger chaque serveur avec `dig` ou `Resolve-DnsName`.

---

## 1. Pourquoi le DNS existe

Les machines se parlent avec des adresses IP, les humains retiennent des noms. Aux débuts d'Internet, un fichier unique `HOSTS.TXT` était recopié partout ; il s'est effondré avec la croissance du réseau. Le DNS (RFC 1034 et 1035) l'a remplacé par un système **réparti** : chaque organisation gère ses noms, et des renvois permettent de retrouver n'importe lequel.

**Analogie** : un annuaire national. Un bureau central sait quel service départemental répond pour chaque département ; chaque service sait quelle mairie gère chaque commune. Pour trouver un numéro, on suit les renvois.

Le DNS publie aussi la messagerie (MX), des politiques anti-usurpation (TXT), des services (SRV) et la résolution inverse (PTR). Quand « Internet ne marche pas », la cause est souvent le DNS alors que l'IP fonctionne.

## 2. La hiérarchie des noms

Un **FQDN** (nom pleinement qualifié) se termine par un point, la **racine** : `www.example.com.`

```text
www . example . com .
 │       │       │   └── racine
 │       │       └────── TLD (domaine de premier niveau)
 │       └────────────── domaine de l'organisation
 └────────────────────── nom d'hôte
```

Chaque étiquette (label) fait 63 caractères au plus, le nom entier 253.

![Arbre DNS : racine, TLD com, org et test, zone example.com et enregistrements www, mail et apex](images/dns-en-profondeur-3.svg)

*Figure 1 — La hiérarchie DNS : la racine délègue aux TLD, qui délèguent aux zones. Schéma original (CC0).*

**Zone et domaine.** Un domaine est une branche de l'arbre. Une zone est la portion dont **un même ensemble de serveurs est responsable**. Si `lab.example.com` est confié à une autre équipe, elle gère sa propre zone et la zone parente ne contient plus que des enregistrements **NS** de délégation.

**Autorité.** Un serveur faisant autorité détient la copie officielle d'une zone et répond avec le drapeau **AA**. Une délégation cassée (NS vers un serveur muet) provoque des échecs intermittents.

**Noms réservés.** Les RFC 2606 et 6761 réservent `example.com`, `example.net`, `example.org` et les TLD `.test`, `.example`, `.invalid`. Le laboratoire utilise `example.test`.

## 3. Les trois rôles

| Rôle | Où ? | Ce qu'il fait |
|---|---|---|
| **Client léger** (stub) | dans le système du poste | Pose une question au résolveur configuré, attend la réponse finale, garde un petit cache. |
| **Résolveur récursif** | fournisseur d'accès, routeur, serveur d'entreprise | Interroge les serveurs successifs, met en cache, retourne le résultat. |
| **Serveur faisant autorité** | hébergeur ou administrateur de la zone | Répond pour ses zones seulement, depuis ses propres données. |

![Schéma d'un poste : applications, résolveur du système avec cache local, puis résolveur du fournisseur d'accès qui lance la recherche récursive](images/dns-en-profondeur-1.svg)

*Figure 2 — De l'application au résolveur du fournisseur : plusieurs caches en série. Schéma de Lion Kimbro, domaine public, étiquettes en anglais (« Client Programs » = programmes clients ; « Operating System » = système d'exploitation ; « Your ISP » = votre fournisseur d'accès ; « recursive DNS search » = recherche DNS récursive).*

**Analogie** : le client léger commande « une pizza » ; le résolveur est le serveur de salle qui fait toutes les démarches ; le serveur faisant autorité est le fournisseur d'un ingrédient précis.

Conséquence : `nslookup` affiche « Réponse ne faisant pas autorité » quand la réponse vient du **cache d'un résolveur**. Ce n'est pas une erreur.

## 4. Résolution récursive et itérative

- **Récursive** (bit RD) : « Donne-moi la réponse finale. » C'est la requête du client léger à son résolveur.
- **Itérative** : « Donne ce que tu sais, sinon dis-moi qui peut répondre. » C'est la requête du résolveur aux serveurs d'autorité.

![Un itérateur DNS interroge la racine, puis le serveur de org, puis celui de wikipedia.org et reçoit l'adresse](images/dns-en-profondeur-2.svg)

*Figure 3 — Résolution itérative : chaque serveur renvoie vers le suivant jusqu'à la réponse. Schéma de Lion Kimbro, domaine public, étiquettes en anglais (« Where's www.wikipedia.org? » = où est www.wikipedia.org ? ; « root nameserver » = serveur racine ; « Try » = essayez ; « It's at » = c'est à). Les adresses de l'image sont celles de l'exemple d'origine.*

### Déroulé pour `www.example.com` (cache vide)

1. Le client léger envoie une requête **récursive** au résolveur `192.0.2.53`.
2. Le résolveur interroge un serveur racine, qui répond par un **renvoi** : les serveurs NS de `com` (avec leurs adresses, les *glue records*).
3. Un serveur de `com` renvoie vers les NS de `example.com`.
4. Un NS de `example.com` **fait autorité** : `www.example.com. 300 IN A 192.0.2.10`.
5. Le résolveur met en cache 300 s, répond au client avec le drapeau RA (récursion disponible).
6. Le client transmet l'adresse à l'application, qui ouvre une connexion [[Glossary:TCP]] vers `192.0.2.10`.

Les renvois de la racine et des TLD restent en cache longtemps : un résolveur actif ne contacte presque jamais la racine.

Un serveur d'autorité **ne doit pas** offrir la récursion à tout Internet (risque d'amplification). En entreprise, on réserve les résolveurs au réseau interne.

## 5. Les enregistrements essentiels

Un enregistrement (RR) a la forme `nom  TTL  classe  type  données`, la classe étant presque toujours `IN`.

| Type | Sens | Exemple |
|---|---|---|
| **A** | adresse IPv4 | `www 300 IN A 192.0.2.10` |
| **AAAA** | adresse IPv6 | `www 300 IN AAAA 2001:db8::10` |
| **CNAME** | alias | `blog 300 IN CNAME www.example.com.` |
| **MX** | messagerie, priorité la plus basse préférée | `@ 3600 IN MX 10 mail.example.com.` |
| **TXT** | texte ([[Glossary:SPF]], vérifications) | `@ 3600 IN TXT "v=spf1 mx -all"` |
| **PTR** | nom d'une adresse (inverse) | `10.2.0.192.in-addr.arpa. IN PTR www.example.com.` |
| **NS** | serveur de noms de la zone | `@ 86400 IN NS ns1.example.com.` |
| **SOA** | autorité : série, durées, TTL négatif | `@ IN SOA ns1.example.com. admin.example.com. (…)` |

Le symbole `@` désigne le nom de la zone (l'**apex**).

**Règles qui évitent les pannes**

- Un **CNAME ne coexiste pas** avec d'autres données du même nom : pas de CNAME à l'apex (qui porte NS et SOA). Les « ALIAS » de certains fournisseurs ne sont pas des types standard.
- Un **MX** pointe vers un nom qui a un A ou AAAA, jamais vers une IP brute.
- Le **PTR** vit dans `in-addr.arpa` (octets **inversés**) ou `ip6.arpa`, géré par le propriétaire du bloc d'adresses.
- Dans un fichier de zone, oublier le **point final** d'un nom complet ajoute la zone en suffixe : `mail.example.com.example.com.`

```text
$TTL 3600
@     IN SOA ns1.example.test. admin.example.test. (
          2026110101 ; série, à incrémenter à chaque modification
          7200 900 1209600
          300 )      ; TTL négatif (cache des NXDOMAIN)
      IN NS  ns1.example.test.
ns1   IN A   192.0.2.53
www   300 IN A     192.0.2.10
www   300 IN AAAA  2001:db8::10
blog  300 IN CNAME www.example.test.
@     IN MX 10 mail.example.test.
mail  IN A   192.0.2.25
@     IN TXT "v=spf1 mx -all"
```

Un même nom peut porter plusieurs types, et plusieurs A (répartition en tourniquet).

## 6. Cache, TTL et propagation

Le **TTL** est la durée, en secondes, pendant laquelle un résolveur réutilise une réponse. Une réponse reçue avec `TTL 300` affichera `TTL 120` deux minutes plus tard.

**Analogie** : la date limite de consommation. Le commerçant garde le produit jusqu'à cette date, puis en commande un nouveau.

**Étages de cache** : navigateur, client DNS du système (*Client DNS* Windows, `systemd-resolved` ou `dnsmasq` sous Linux), résolveur du réseau, éventuels redirecteurs.

Rien ne « se propage » : une modification est **visible immédiatement** sur l'autorité, et chaque cache sert l'ancienne valeur jusqu'à l'expiration de son TTL.

**Cache négatif.** Un `NXDOMAIN` est aussi mémorisé (RFC 2308), pendant la durée du dernier champ du SOA. Si vous interrogez un nom avant de le créer, le résolveur peut répondre « inexistant » plusieurs minutes. Testez donc directement sur l'autorité.

**Avant une migration** de `192.0.2.10` vers `198.51.100.10` :

1. abaisser le TTL (86400 → 300) plusieurs jours avant ;
2. attendre au moins l'**ancien** TTL ;
3. changer l'adresse ;
4. vérifier sur l'autorité, puis sur un résolveur public et un résolveur interne ;
5. remonter le TTL.

## 7. Transport et sécurité en bref

- **[[Glossary:UDP]]/53** : transport par défaut. **TCP/53** : réponses tronquées (bit TC), transferts de zone ; le filtrer provoque des pannes intermittentes sur les grosses réponses.
- **DoT** ([[Glossary:TLS]], port 853) et **DoH** (HTTPS, port 443) chiffrent le trajet client-résolveur.
- **[[Glossary:DNSSEC]]** signe les enregistrements ; un échec de validation donne `SERVFAIL` alors que l'autorité répond (test : `dig +cd`).
- Le DNS classique est **en clair** : un observateur lit les noms demandés.

## 8. Les outils d'interrogation

**`dig`** : `dig [@serveur] nom [type] [options]`. Options utiles : `+short`, `+noall +answer`, `+trace` (suit les délégations depuis la racine), `+norecurse`, `-x` (inverse), `+tcp`. L'en-tête donne le `status` et les drapeaux : `qr` (réponse), `aa` (autoritaire), `rd`, `ra`, `ad` (DNSSEC validé).

**`nslookup`** : présent partout, mais avec sa propre logique de résolution, légèrement différente de celle des applications.

**`Resolve-DnsName`** (PowerShell) : paramètres `-Name`, `-Type`, `-Server`, `-DnsOnly` (ni fichier hosts ni LLMNR). Retourne des objets exploitables.

**Comme une application.** Sous Linux, `getent hosts nom` suit `/etc/nsswitch.conf` (fichier hosts puis DNS). Si `dig` réussit et `getent` échoue, le défaut est dans la configuration locale (nsswitch, resolv.conf, domaines de recherche), pas dans le DNS.

## Mise en pratique guidée

**Cadre** : VM Debian ou Ubuntu jetable. Un petit serveur DNS local écoute sur le port 5353, sans toucher au DNS du système. Prenez un instantané avant de commencer.

### Étape 1 — Installer les outils

```bash
sudo apt update && sudo apt install -y dnsmasq bind9-dnsutils
```

👉 Explication : installe `dnsmasq` (serveur DNS léger) et `dig`/`nslookup` (paquet `bind9-dnsutils`). À exécuter dans la VM jetable uniquement ; nous lancerons notre propre instance de `dnsmasq`.

### Étape 2 — Écrire la configuration

```bash
mkdir -p ~/lab-dns && cd ~/lab-dns
cat > lab.conf <<'EOF'
port=5353
listen-address=127.0.0.1
bind-interfaces
no-resolv
no-hosts
log-queries
host-record=www.example.test,192.0.2.10,2001:db8::10
cname=blog.example.test,www.example.test
mx-host=example.test,mail.example.test,10
host-record=mail.example.test,192.0.2.25
txt-record=example.test,"v=spf1 mx -all"
ptr-record=10.2.0.192.in-addr.arpa,www.example.test
local-ttl=300
EOF
```

👉 Explication : crée un dossier et un fichier définissant des enregistrements A, AAAA, CNAME, MX, TXT et PTR pour la zone fictive `example.test`. `no-resolv` interdit toute sortie vers Internet ; `local-ttl=300` fixe le TTL.

### Étape 3 — Lancer le serveur

```bash
sudo dnsmasq --conf-file=lab.conf --keep-in-foreground --log-facility=- --pid-file=
```

👉 Explication : démarre `dnsmasq` au premier plan et affiche les requêtes. `sudo` est employé dans la VM car `dnsmasq` abandonne ses privilèges au démarrage ; `--pid-file=` (vide) évite d'écrire un fichier [[Glossary:PID]]. Laissez ce terminal ouvert, travaillez dans un second. Arrêt : `Ctrl+C`.

### Étape 4 — Interroger les types

```bash
dig @127.0.0.1 -p 5353 www.example.test A +noall +answer
dig @127.0.0.1 -p 5353 www.example.test AAAA +noall +answer
dig @127.0.0.1 -p 5353 blog.example.test +noall +answer
```

👉 Explication : demande l'IPv4, l'IPv6 puis l'alias. Pour `blog`, la réponse contient le CNAME puis l'adresse de la cible. Sortie attendue (exemple) : `www.example.test. 300 IN A 192.0.2.10`.

```bash
dig @127.0.0.1 -p 5353 example.test MX +short
dig @127.0.0.1 -p 5353 example.test TXT +short
dig @127.0.0.1 -p 5353 -x 192.0.2.10 +short
```

👉 Explication : interroge la messagerie (`10 mail.example.test.`), le texte SPF et la résolution inverse ; `-x` inverse les octets et ajoute `in-addr.arpa`.

### Étape 5 — Lire NXDOMAIN et NODATA

```bash
dig @127.0.0.1 -p 5353 inconnu.example.test A
dig @127.0.0.1 -p 5353 mail.example.test AAAA
```

👉 Explication : le premier nom n'existe pas (`status: NXDOMAIN`). Le second existe mais sans AAAA : `NOERROR` avec une section ANSWER vide (NODATA). Cette distinction est essentielle au diagnostic.

### Étape 6 — Observer le TTL

```bash
dig @127.0.0.1 -p 5353 www.example.test +noall +answer
sleep 5
dig @127.0.0.1 -p 5353 www.example.test +noall +answer
```

👉 Explication : ce serveur est local, son TTL reste à 300. Sur un résolveur avec cache, la seconde réponse afficherait environ 5 secondes de moins.

### Étape 7 — Côté Windows (facultatif)

```powershell
Resolve-DnsName -Name www.example.test -Type A -Server 192.0.2.53 -DnsOnly
nslookup -type=MX example.test 192.0.2.53
```

👉 Explication : même démarche sous Windows ; remplacez `192.0.2.53` par l'adresse de votre serveur de laboratoire (écoutant sur le port 53 standard pour ces outils).

### Étape 8 — Suivre la délégation réelle

```bash
dig +trace example.com A
```

👉 Explication : sur une VM avec accès Internet, `dig` repart de la racine et affiche chaque renvoi (Figure 3). Requête en lecture seule vers un domaine réservé.

### Étape 9 — Nettoyer

```bash
cd ~ && rm -r ~/lab-dns
```

👉 Explication : supprime le dossier du laboratoire après l'arrêt de `dnsmasq`. Restaurez l'instantané de la VM si vous le souhaitez.

## Exercices

1. **Lecture de nom.** Pour `intranet.rh.example.com.`, donnez dans l'ordre : TLD, domaine d'organisation, sous-domaine intermédiaire, nom d'hôte.
2. **Types.** Associez : (a) adresse IPv6 d'un site ; (b) serveur qui reçoit le courrier ; (c) `docs.example.com` pointe vers `www.example.com` ; (d) nom d'une adresse IP ; (e) politique SPF.
3. **PTR.** Écrivez le nom à interroger pour la résolution inverse de `198.51.100.77`.
4. **Zone.** Dans la zone de la section 5, ajoutez `ftp` en alias de `www`, et un second MX de priorité 20 vers `mail2.example.test.` (A : `192.0.2.26`).
5. **TTL.** `app.example.com` a un TTL de 3600. Un résolveur le met en cache à 9 h 45 ; vous changez l'adresse à 10 h 00. Quand ce résolveur servira-t-il la nouvelle valeur ?
6. **Codes.** Expliquez et donnez la première vérification : (a) `NXDOMAIN` pour `wwww.example.com` ; (b) `SERVFAIL` seulement sur le résolveur d'entreprise ; (c) `NOERROR` et réponse vide pour un AAAA.
7. **Outils.** Sous Linux, `dig www.example.test` renvoie `192.0.2.10` mais `ping www.example.test` échoue (« Name or service not known »). Proposez deux causes et leur contrôle.
8. **Scénario.** Rédigez la séquence DNS (valeurs de TTL comprises) d'une migration de serveur web prévue le samedi.

## Corrigés des exercices

1. TLD `com` ; domaine `example` (soit `example.com`) ; sous-domaine `rh` ; hôte `intranet`.
2. (a) AAAA ; (b) MX ; (c) CNAME ; (d) PTR ; (e) TXT.
3. `77.100.51.198.in-addr.arpa.` (octets inversés).
4. ```text
   ftp   IN CNAME www.example.test.
   @     IN MX 20 mail2.example.test.
   mail2 IN A     192.0.2.26
   ```
   Incrémentez le numéro de série du SOA ; `ftp` ne doit avoir aucun autre enregistrement.
5. Expiration à 9 h 45 + 1 h = **10 h 45** : le résolveur sert l'ancienne adresse jusque-là. Les caches situés en aval (système, navigateur) peuvent la conserver un peu au-delà.
6. (a) Le nom n'existe pas, probablement une faute de frappe : vérifier l'orthographe. (b) Le résolveur n'obtient pas de réponse valide : autorité injoignable, délégation cassée ou DNSSEC invalide ; comparer `dig @autorité` et `dig +cd` sur le résolveur. (c) NODATA : l'hôte n'a pas d'IPv6 publié, normal sauf attente contraire.
7. Cause 1 : `/etc/nsswitch.conf` ne place pas `dns` ou `resolve` dans la ligne `hosts` (contrôle : `getent hosts www.example.test`). Cause 2 : `dig` utilisait un `@serveur` explicite, différent du résolveur du système (contrôle : `resolvectl status`, `dig www.example.test` sans `@`). Possible aussi : une entrée contradictoire dans `/etc/hosts`.
8. Jeudi : TTL 3600 → 300. Vendredi (après au moins 1 h) : vérifier. Samedi : changer l'adresse, contrôler sur l'autorité puis deux résolveurs. Dimanche : surveiller. Lundi : TTL remis à 3600. Règle : attendre l'**ancien** TTL avant la bascule.

## Quiz

**Q1. Par où commence la résolution de `www.example.com.` ?**
A) Le nom d'hôte. B) La racine. C) Le serveur de messagerie. D) Le cache du navigateur uniquement.
**Réponse : B.** On part de la racine, qui renvoie vers le TLD, puis la zone, puis l'hôte.

**Q2. Qui envoie une requête récursive ?**
A) Le serveur d'autorité. B) Le serveur racine. C) Le client léger. D) Le serveur DHCP.
**Réponse : C.** Il demande la réponse finale au résolveur, qui procède ensuite par requêtes itératives.

**Q3. Quel enregistrement ne peut pas coexister avec d'autres sur le même nom ?**
A) A. B) CNAME. C) TXT. D) MX.
**Réponse : B.** Un CNAME remplace tout le nom ; il est interdit à l'apex qui porte SOA et NS.

**Q4. Quel statut signifie « ce nom n'existe pas » ?**
A) NOERROR. B) SERVFAIL. C) NXDOMAIN. D) REFUSED.
**Réponse : C.** SERVFAIL est un échec de résolution, REFUSED un refus, NOERROR sans réponse un NODATA.

**Q5. Nom de la zone inverse pour 192.0.2.10 :**
A) `192.0.2.10.in-addr.arpa.` B) `10.2.0.192.in-addr.arpa.` C) `10.2.0.192.arpa.` D) `in-addr.arpa.192.0.2.10`
**Réponse : B.** Les octets sont inversés pour suivre la hiérarchie des blocs d'adresses.

**Q6. Pourquoi une modification DNS n'est-elle pas visible partout tout de suite ?**
A) Les serveurs se synchronisent lentement. B) Les caches gardent l'ancienne réponse jusqu'à la fin du TTL. C) Les pare-feux bloquent les mises à jour. D) Il faut réinstaller le navigateur.
**Réponse : B.** Rien ne se propage activement : les caches expirent un à un.

**Q7. Quelle option de `dig` suit les délégations depuis la racine ?**
A) `+short` B) `+tcp` C) `+trace` D) `-x`
**Réponse : C.** `+trace` interroge la racine puis chaque niveau.

**Q8. Quelle commande PowerShell limite la résolution au DNS ?**
A) `Get-NetIPAddress` B) `Resolve-DnsName -DnsOnly` C) `Test-Connection` D) `ipconfig /all`
**Réponse : B.** `-DnsOnly` exclut le fichier hosts et les mécanismes locaux.

**Q9. Quel transport doit rester ouvert en plus d'UDP/53 ?**
A) TCP/53 B) UDP/67 C) TCP/25 D) UDP/123
**Réponse : A.** Les réponses tronquées sont redemandées en TCP/53.

**Q10. `dig` renvoie la bonne adresse, l'application échoue : que tester ?**
A) Changer le câble. B) `getent hosts nom` ou `Resolve-DnsName` sans `-Server`. C) Redémarrer l'autorité. D) Supprimer l'enregistrement.
**Réponse : B.** `dig @serveur` ignore la configuration du système (nsswitch, hosts, domaines de recherche) que l'application utilise.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification |
|---|---|---|
| Accès par IP, pas par nom | Résolveur injoignable ou mal configuré | `resolvectl status` ou `Get-DnsClientServerAddress`, puis `dig @résolveur nom` |
| Nom introuvable juste après création | Cache négatif | Interroger l'autorité ; attendre le TTL négatif |
| Ancienne adresse servie | TTL non expiré ou non abaissé | `dig nom` (TTL qui décroît) ; vider le cache local |
| Réponse différente selon le poste | Résolveurs différents, split-horizon | Comparer `dig @résolveur1` et `@résolveur2` |
| `mail.example.com.example.com` | Point final oublié | Relire la zone |
| Échecs sur grosses réponses | TCP/53 filtré | `dig +tcp nom` |
| SERVFAIL sur un seul résolveur | DNSSEC invalide ou autorité injoignable | `dig +cd nom` ; `dig @autorité nom` |
| Mauvaise réponse sous Windows | Cache client ou fichier hosts | `Get-DnsClientCache` ; lire `C:\Windows\System32\drivers\etc\hosts` |

**Méthode en cinq temps** : (1) `ping` de l'IP pour isoler la couche ; (2) tester comme l'application (`getent hosts`, `Resolve-DnsName`) ; (3) identifier le résolveur ; (4) interroger directement résolveur puis autorité ; (5) `dig +trace` pour repérer le niveau fautif.

```bash
resolvectl flush-caches
```

👉 Explication : sous Linux avec `systemd-resolved`, vide le cache local. Modifie l'état du cache, pas la configuration ; à réserver à un poste de test ou à un exploitant averti.

```powershell
Get-DnsClientCache | Select-Object -First 5
Clear-DnsClientCache
```

👉 Explication : liste le cache du client DNS Windows (lecture seule), puis le vide (équivalent de `ipconfig /flushdns`).

## À retenir

- Le DNS est distribué et hiérarchique ; la délégation relie chaque niveau au suivant.
- Trois rôles : client léger, résolveur récursif, serveur faisant autorité.
- Récursif : « rends-moi la réponse » ; itératif : « dis-moi qui sait ».
- A/AAAA adresses, CNAME alias (jamais à l'apex), MX messagerie, TXT texte, PTR inverse, NS délégation, SOA autorité.
- Le TTL gouverne les caches ; abaissez-le **avant** une migration. Les NXDOMAIN sont aussi mis en cache.
- NXDOMAIN, NODATA, SERVFAIL et REFUSED sont quatre situations distinctes.
- `dig` interroge un serveur précis ; `getent` et `Resolve-DnsName` sans `-Server` suivent la chaîne du système.
- UDP/53 et TCP/53 doivent rester ouverts.

## Pour aller plus loin

- RFC 1034 : https://www.rfc-editor.org/rfc/rfc1034
- RFC 1035 : https://www.rfc-editor.org/rfc/rfc1035
- RFC 2308 (cache négatif) : https://www.rfc-editor.org/rfc/rfc2308
- RFC 6761 (noms spéciaux) : https://www.rfc-editor.org/rfc/rfc6761
- RFC 5737 (adresses de documentation) : https://www.rfc-editor.org/rfc/rfc5737
- `Resolve-DnsName` (Microsoft Learn) : https://learn.microsoft.com/powershell/module/dnsclient/resolve-dnsname
- Documentation de BIND et de `dig` : https://bind9.readthedocs.io/
- `resolvectl` (systemd) : https://www.freedesktop.org/software/systemd/man/resolvectl.html
- Fiche du pack : [Tout-en-un — Diagnostic DNS](../tout-en-un-diagnostic-dns.md)

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/dns-en-profondeur-1.svg` | https://commons.wikimedia.org/wiki/File:DNS_in_the_real_world.svg | Lion Kimbro | Domaine public (« Public domain » sur la page Commons) | Aucune (fichier renommé) |
| `images/dns-en-profondeur-2.svg` | https://commons.wikimedia.org/wiki/File:Example_of_an_iterative_DNS_resolver.svg | Lion Kimbro | Domaine public (« Public domain » sur la page Commons) | Aucune (fichier renommé) |
| `images/dns-en-profondeur-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) : https://creativecommons.org/publicdomain/zero/1.0/ | Sans objet |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (dnsmasq, dig), Windows (Resolve-DnsName, nslookup) | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Précision : à la rédaction, seule une commande locale en lecture seule (`getent services`) a été exécutée ; `dig`, `nslookup` et `dnsmasq` n'étaient pas installés sur le poste de rédaction. Les sorties sont des exemples typiques, non des captures réelles. Les licences des images ont été relevées sur Wikimedia Commons le 2026-11-01.