---
title: "Leçon — Temps et certificats : NTP/chrony et PKI"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "services-infrastructure", "ntp", "chrony", "pki", "certificats", "openssl", "acme", "letsencrypt"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Temps et certificats : NTP/chrony et PKI

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `services-infrastructure`, `ntp`, `chrony`, `pki`, `certificats`, `openssl`, `acme`, `letsencrypt`
- **Niveau** : intermédiaire
- **Durée estimée** : 4 à 5 heures (cours 1 h 30, laboratoire 2 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. expliquer pourquoi un serveur dont l'heure dérive provoque des pannes de certificats, de journaux et d'authentification ;
2. configurer et contrôler un client ou un serveur de temps **chrony** ;
3. décrire les rôles d'une **PKI** : autorité racine, intermédiaire, certificat de feuille, chaîne de confiance ;
4. créer une autorité de certification interne de laboratoire, produire une **CSR** et émettre un certificat serveur avec `openssl` ;
5. installer une autorité interne dans le magasin de confiance d'un système ;
6. expliquer le principe d'**ACME** (Let's Encrypt) et le renouvellement automatique ;
7. **dépanner** un certificat avec `openssl` : expiration, nom, chaîne incomplète, clé qui ne correspond pas.

## Prérequis et durée

- Terminal Linux, notions de réseau (UDP/TCP, DNS) et leçon [Serveur web et reverse proxy](/fr/00-cours-theoriques/tout-en-un/03-services-d-infrastructure/lecons/lecon-serveur-web-et-reverse-proxy) conseillée (HTTPS).
- Une VM jetable Debian 12 ou Ubuntu avec `sudo`, sans donnée réelle. Les adresses `192.0.2.0/24`, `203.0.113.0/24` et les noms `example.com` / `example.test` sont des valeurs de documentation. Durée : 4 à 5 heures.

## L'essentiel en bref

- Un certificat n'est valable que **dans une plage de dates** : une horloge fausse invalide tous les certificats, et Kerberos refuse les écarts de plus de 5 minutes par défaut.
- **chrony** synchronise l'horloge (NTP, UDP 123) ; `chronyc tracking` et `chronyc sources` sont les commandes de diagnostic.
- Une **PKI** relie une clé publique à une identité par une signature ; la confiance vient d'une **racine** installée chez le client.
- On génère la **clé privée** sur le serveur, on envoie seulement la **CSR** ; la clé ne circule jamais.
- Un serveur doit présenter sa **chaîne** (feuille + intermédiaires) et un **SAN** correspondant au nom visité.
- **ACME** automatise l'émission et le renouvellement ; la surveillance de l'expiration reste indispensable.
- `openssl s_client`, `x509` et `verify` règlent la plupart des problèmes.

---

## 1. Pourquoi l'heure est une infrastructure

Des convives aux montres différentes ne peuvent plus se donner rendez-vous à 20 h. Dans un SI, l'heure sert à :

- **valider les certificats** (`notBefore` / `notAfter`) : un serveur en retard de deux jours reçoit un certificat « pas encore valide » ;
- **corréler les journaux** de plusieurs machines pendant un incident ;
- **authentifier** : Kerberos (donc Active Directory) tolère 5 minutes d'écart par défaut ; les codes à usage unique (TOTP) dépendent de l'horloge ;
- **planifier** (tâches cron, sauvegardes) et horodater des preuves.

Une VM est particulièrement exposée : après suspension ou migration, son horloge peut sauter.

## 2. NTP et la hiérarchie des strates

**NTP** (Network Time Protocol, RFC 5905) mesure le décalage et le délai aller-retour avec plusieurs serveurs, puis corrige l'horloge locale. Les sources sont organisées en **strates** : la strate 0 est une horloge de référence (GNSS, atomique), la strate 1 est directement reliée à elle, la strate 2 se synchronise sur la strate 1, etc. Le numéro indique la **distance** à la référence, pas la qualité.

![Hiérarchie des strates NTP : de l'horloge de référence de strate 0 jusqu'aux postes de strate 4, en passant par un serveur chrony interne 192.0.2.5 de strate 3](images/temps-et-certificats-1.svg)

*Figure 1 — Les strates NTP : plus le chiffre est élevé, plus on est loin de la référence. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

Bonne pratique : **un ou deux serveurs de temps internes** se synchronisent sur des sources externes fiables et les autres équipements les interrogent : moins d'UDP 123 vers Internet, cohérence interne même sans Internet. Utilisez **trois ou quatre** sources pour pouvoir écarter une source erronée.

Correction : un petit écart est résorbé en **accélérant ou ralentissant** l'horloge (« slew ») ; un grand écart au démarrage est **sauté** (« step »). Bases de données et journaux préfèrent le premier mode.

## 3. chrony en pratique

**chrony** (`chronyd` + client `chronyc`) est le client/serveur NTP par défaut de nombreuses distributions. Il converge vite, gère bien les machines intermittentes et les VM. L'alternative **systemd-timesyncd** est un client SNTP minimal, sans fonction serveur.

### 3.1 Installer et contrôler

```bash
sudo apt install chrony
systemctl status chrony --no-pager
timedatectl
```

👉 Explication : installe chrony (le service s'appelle `chrony` sous Debian/Ubuntu et `chronyd` sous Red Hat) ; `timedatectl` indique le fuseau, l'heure et si l'horloge est signalée comme synchronisée.

```bash
chronyc tracking
chronyc sources -v
chronyc sourcestats
```

👉 Explication : lecture seule. `tracking` donne la strate locale, l'écart courant (`System time`) et la dispersion ; `sources -v` liste les serveurs avec leur état (`^*` = source sélectionnée, `^+` = source acceptable, `^?` = inaccessible ou non fiable) ; `sourcestats` montre la dérive estimée de chaque source.

Un `tracking` sain affiche par exemple `Leap status : Normal` et un `System time` de quelques millisecondes. `Leap status : Not synchronised` signale une horloge non synchronisée.

### 3.2 Configurer un client interne

Fichier `/etc/chrony/chrony.conf` (Debian) ou `/etc/chrony.conf` (Red Hat) :

```text
server 192.0.2.5 iburst
server 192.0.2.6 iburst
driftfile /var/lib/chrony/chrony.drift
makestep 1.0 3
rtcsync
```

👉 Explication : `server … iburst` interroge les serveurs internes, avec des échanges rapprochés au démarrage ; `driftfile` mémorise l'erreur de fréquence de l'horloge matérielle ; `makestep 1.0 3` autorise un saut si l'écart dépasse 1 s, uniquement pendant les 3 premières mises à jour ; `rtcsync` recopie périodiquement l'heure vers l'horloge matérielle. Retirez les lignes `pool` par défaut pour n'utiliser que des sources internes.

### 3.3 Configurer un serveur de temps interne

```text
pool 2.debian.pool.ntp.org iburst maxsources 4
allow 192.0.2.0/24
local stratum 10
```

👉 Explication : `pool` obtient plusieurs sources publiques ; `allow` autorise **uniquement** `192.0.2.0/24` à interroger ce serveur (sans `allow`, chrony ne sert personne) ; `local stratum 10` continue de servir l'heure locale si toutes les sources sont perdues (sites isolés seulement).

Ouvrez ensuite l'**UDP 123** entre les clients et ce serveur seulement. Après modification :

```bash
sudo systemctl restart chrony
chronyc sources -v
sudo chronyc clients
```

👉 Explication : redémarre le service pour relire la configuration, puis contrôle l'état des sources ; `chronyc clients` (droits administrateur) liste les machines qui interrogent le serveur.

### 3.4 Corriger une grosse dérive

```bash
sudo chronyc makestep
chronyc tracking
```

👉 Explication : force un saut immédiat de l'horloge vers l'heure des sources ; à n'utiliser que ponctuellement, sur une machine où un saut ne perturbera ni base de données ni application critique.

### 3.5 Sécurité du temps

NTP classique n'est pas authentifié : un attaquant sur le trajet peut fausser l'heure. **NTS** (RFC 8915) ajoute l'authentification ; chrony le gère (`server nom iburst nts`) si le serveur le propose. N'exposez pas un serveur NTP ouvert à Internet sans nécessité (risque d'amplification).

Sous Windows, `w32tm /query /status` affiche l'état ; dans un domaine Active Directory, les stations suivent le contrôleur de domaine.

---

## 4. La PKI : les concepts

Une **PKI** (Public Key Infrastructure) est l'ensemble des acteurs, règles et outils qui lient une **clé publique** à une **identité** par une signature numérique. Analogie : **une carte d'identité**. La préfecture (l'autorité) vérifie l'identité, appose un cachet difficile à falsifier, et chacun reconnaît ce cachet sans appeler la préfecture à chaque contrôle.

Éléments à connaître :

- **Paire de clés** : la clé **privée** reste secrète sur le serveur ; la clé **publique** est incluse dans le certificat.
- **Certificat X.509** : document signé contenant sujet, clé publique, émetteur, dates de validité, usages et **SAN** (Subject Alternative Name, la liste des noms valables : c'est lui que les navigateurs vérifient, pas le « CN »).
- **CSR** (Certificate Signing Request, demande de signature) : contient la clé publique et les noms souhaités, signée par la clé privée correspondante. L'autorité signe et renvoie le certificat ; **la clé privée n'est jamais transmise**.
- **CA** (autorité de certification) : entité qui signe. Une **CA racine** s'auto-signe ; elle est gardée **hors ligne** et signe peu de choses. Une **CA intermédiaire** signe les certificats du quotidien.
- **Chaîne de confiance** : feuille → intermédiaire → racine. Le client fait confiance à la racine parce qu'elle figure déjà dans son **magasin de confiance** ; il remonte la chaîne en vérifiant chaque signature, les dates et les usages.

![Schéma d'une PKI interne : la CA racine hors ligne signe la CA intermédiaire, qui signe le certificat du serveur www.example.com à partir d'une demande CSR envoyée par le serveur ; le client ne fait confiance qu'à la racine installée dans son magasin](images/temps-et-certificats-2.svg)

*Figure 2 — Qui signe qui : racine, intermédiaire, certificat serveur, et circulation de la CSR. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 4.1 Pourquoi une autorité interne ?

Pour des noms **privés** (`intranet.example.test`), une autorité publique ne peut pas émettre : ces noms ne sont pas vérifiables. Une CA interne chiffre et authentifie les services internes, à condition de **distribuer sa racine** et de **protéger ses clés** : qui détient la clé d'une CA émet des certificats que tout le parc croira. D'où le modèle à deux niveaux.

### 4.2 Durées de vie et révocation

Plus un certificat vit longtemps, plus un vol de clé est dangereux. Ordres de grandeur : racine 10 à 20 ans, intermédiaire 3 à 10 ans, serveur 90 jours à 13 mois. La **révocation** (CRL, OCSP) invalide un certificat avant son terme mais est inégalement vérifiée : la meilleure parade est la **courte durée de vie avec renouvellement automatique**.

---

## 5. Construire une PKI de laboratoire avec openssl

Cette section reproduit un scénario complet. **Tout se passe dans un dossier jetable**, avec des noms `example.test`.

```bash
mkdir -p ~/pki-lab && cd ~/pki-lab && umask 077
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out root.key
openssl req -x509 -new -key root.key -sha256 -days 3650 \
  -subj "/O=Example Lab/CN=Example Lab Root CA" \
  -addext "basicConstraints=critical,CA:TRUE" \
  -addext "keyUsage=critical,keyCertSign,cRLSign" -out root.crt
```

👉 Explication : `umask 077` rend les fichiers créés illisibles aux autres utilisateurs ; la première commande crée la clé privée de la racine (courbe elliptique P-256) ; la seconde crée le certificat **auto-signé** de racine, valable 10 ans, marqué comme CA (`CA:TRUE`) et autorisé à signer des certificats (`keyCertSign`). En production, cette clé serait générée sur une machine hors ligne, idéalement dans un module matériel (HSM).

### 5.1 Autorité intermédiaire

```bash
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out inter.key
openssl req -new -key inter.key -subj "/O=Example Lab/CN=Example Lab Issuing CA" -out inter.csr
printf "basicConstraints=critical,CA:TRUE,pathlen:0\nkeyUsage=critical,keyCertSign,cRLSign\nsubjectKeyIdentifier=hash\nauthorityKeyIdentifier=keyid\n" > inter.ext
openssl x509 -req -in inter.csr -CA root.crt -CAkey root.key -CAcreateserial -days 1825 -sha256 -extfile inter.ext -out inter.crt
```

👉 Explication : crée la clé et la **CSR** de l'intermédiaire, puis la racine signe cette CSR en appliquant les extensions du fichier `inter.ext` ; `pathlen:0` interdit à l'intermédiaire de créer d'autres autorités sous elle ; `-CAcreateserial` génère le numéro de série.

### 5.2 Certificat de serveur : clé, CSR, signature

```bash
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out www.key
openssl req -new -key www.key -subj "/CN=www.example.test" \
  -addext "subjectAltName=DNS:www.example.test,DNS:example.test" -out www.csr
openssl req -in www.csr -noout -verify -text | grep -E "verify|DNS:"
```

👉 Explication : crée la clé privée du serveur (qui **reste sur le serveur**), puis la CSR avec les noms souhaités ; la dernière commande confirme que la signature de la CSR est valide et affiche les noms demandés. C'est ce fichier `.csr` seul que l'on transmet à l'autorité.

```bash
printf "basicConstraints=CA:FALSE\nkeyUsage=critical,digitalSignature\nextendedKeyUsage=serverAuth\nsubjectAltName=DNS:www.example.test,DNS:example.test\n" > www.ext
openssl x509 -req -in www.csr -CA inter.crt -CAkey inter.key -CAcreateserial -days 90 -sha256 -extfile www.ext -out www.crt
cat www.crt inter.crt > fullchain.pem
```

👉 Explication : l'intermédiaire signe la CSR pour 90 jours, avec l'usage `serverAuth` ; **les extensions demandées dans la CSR ne sont pas recopiées automatiquement** par cette commande : l'autorité décide du contenu, d'où le fichier `www.ext`. `fullchain.pem` assemble la feuille puis l'intermédiaire, dans cet ordre, pour le serveur web.

### 5.3 Vérifier la chaîne

```bash
openssl verify -CAfile root.crt -untrusted inter.crt www.crt
openssl verify -CAfile root.crt www.crt
openssl verify -CAfile root.crt -untrusted inter.crt -verify_hostname www.example.test www.crt
```

👉 Explication : la première commande doit répondre `www.crt: OK` (racine de confiance + intermédiaire fournie, non fiable par elle-même) ; la deuxième **échoue** avec `unable to get local issuer certificate` car l'intermédiaire manque : c'est exactement la panne d'une « chaîne incomplète » ; la troisième vérifie en plus que le nom correspond.

### 5.4 Inspecter

```bash
openssl x509 -in www.crt -noout -subject -issuer -dates -ext subjectAltName
openssl x509 -in www.crt -noout -checkend 86400 && echo "valide encore 24 h"
openssl x509 -in www.crt -noout -fingerprint -sha256
```

👉 Explication : affiche sujet, émetteur, dates et SAN ; `-checkend 86400` renvoie 0 si le certificat n'expire pas dans les 86 400 s (utile en supervision) ; l'empreinte SHA-256 identifie le certificat sans ambiguïté.

### 5.5 Installer la racine dans un système

```bash
sudo cp root.crt /usr/local/share/ca-certificates/example-lab-root.crt
sudo update-ca-certificates
```

👉 Explication : sous Debian/Ubuntu, copie la racine (extension `.crt` obligatoire) dans le dossier des autorités locales et reconstruit le magasin ; sous Red Hat : copie dans `/etc/pki/ca-trust/source/anchors/` puis `sudo update-ca-trust`. Firefox, Java ou Python (`certifi`) ont leur propre magasin. **N'installez que des racines dont vous contrôlez l'origine.**

---

## 6. Let's Encrypt et le protocole ACME

**ACME** (Automatic Certificate Management Environment, RFC 8555) automatise l'émission : un **client** sur le serveur prouve à l'autorité qu'il contrôle le nom, puis récupère le certificat. **Let's Encrypt** est une autorité publique gratuite fondée sur ce protocole ; certaines CA internes (ex. `step-ca`) le proposent aussi.

![Échanges ACME entre un client sur le serveur et une autorité : demande, défi, preuve par fichier HTTP ou enregistrement DNS TXT, puis certificat signé, avec renouvellement automatique](images/temps-et-certificats-3.svg)

*Figure 3 — Principe d'ACME. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 6.1 Les défis

- **HTTP-01** : l'autorité demande un fichier précis sous `http://nom/.well-known/acme-challenge/…` sur le **port 80**. Simple, mais impossible pour un serveur non joignable depuis Internet, et sans certificat joker.
- **DNS-01** : le client publie un enregistrement `TXT` `_acme-challenge.nom`. Fonctionne sans serveur exposé et **seul défi permettant un certificat joker** (`*.example.com`), mais il exige un accès automatisable à la zone DNS : protégez ce jeton, avec des droits limités à cette zone.

### 6.2 Utilisation d'un client (illustration)

```bash
sudo apt install certbot
sudo certbot certonly --webroot -w /var/www/www.example.com/public -d www.example.com --dry-run
```

👉 Explication : installe `certbot` puis simule une demande par la méthode « webroot » (le fichier de défi est déposé dans la racine du site) ; `--dry-run` utilise l'environnement de **test** de l'autorité, sans émettre de vrai certificat ni consommer les limites de fréquence. Retirez `--dry-run` seulement pour un **vrai domaine** que vous contrôlez ; `example.com` ne sera jamais accepté par une autorité publique. Les certificats sont placés dans `/etc/letsencrypt/live/<nom>/` (`fullchain.pem`, `privkey.pem`).

### 6.3 Renouvellement

Les certificats Let's Encrypt durent 90 jours (cette durée peut évoluer ; consultez la documentation du service) et se renouvellent généralement quand il reste environ un tiers de la vie. Le paquet installe un minuteur `systemd` ou une tâche cron :

```bash
systemctl list-timers | grep -i certbot
sudo certbot renew --dry-run
```

👉 Explication : vérifie la présence du minuteur de renouvellement puis simule un renouvellement de tous les certificats gérés ; si le test échoue, le vrai renouvellement échouera aussi, c'est le meilleur moment pour le découvrir.

Un renouvellement est inutile si le service présente encore l'ancien certificat : configurez un **hook de déploiement** (`--deploy-hook "systemctl reload nginx"`) et **surveillez l'expiration** de l'extérieur. Respectez les **limites de fréquence** de l'autorité ; pour les tests, utilisez son environnement de staging.

---

## 7. Dépanner un certificat avec openssl

### 7.1 Voir ce que le serveur présente réellement

```bash
openssl s_client -connect 192.0.2.10:443 -servername www.example.test -showcerts </dev/null 2>&1 | grep -E "^ *[0-9] s:|i:|Verify return|Verification"
```

👉 Explication : se connecte avec SNI, affiche chaque certificat de la chaîne servie (`s:` sujet, `i:` émetteur) et le code de vérification final ; si la chaîne ne contient que la feuille, l'intermédiaire n'est pas servi. Ajoutez `-CAfile root.crt` pour vérifier avec votre racine de laboratoire.

### 7.2 Table des erreurs courantes

| Message openssl | Signification | Correction |
|---|---|---|
| `error 20 … unable to get local issuer certificate` (souvent suivi de `error 21 … unable to verify the first certificate`) | Intermédiaire manquante, ou racine inconnue du client | Servir `fullchain.pem` ; installer la racine chez le client |
| `error 18 … self-signed certificate` | Certificat auto-signé non approuvé | Installer l'autorité de confiance ou émettre via une CA |
| `error 10 … certificate has expired` | Date `notAfter` dépassée | Renouveler ; vérifier l'horloge du client **et** du serveur |
| `error 9 … certificate is not yet valid` | `notBefore` dans le futur | Horloge du client en retard : vérifier chrony |
| `error 62 … hostname mismatch` | Le nom visité n'est pas dans le SAN | Réémettre avec le bon SAN ; visiter le nom prévu (pas l'IP) |
| `error 26 … unsupported certificate purpose` | Usage (`serverAuth`) absent | Réémettre avec les bonnes extensions |

### 7.3 Clé et certificat correspondent-ils ?

```bash
openssl pkey -in www.key -pubout | openssl sha256
openssl x509 -in www.crt -pubkey -noout | openssl sha256
```

👉 Explication : calcule l'empreinte de la clé publique déduite de la clé privée puis celle contenue dans le certificat ; **les deux résultats doivent être identiques**. Sinon, le serveur refusera de démarrer (« key values mismatch ») ou présentera le mauvais fichier.

### 7.4 Autres réflexes

- Comparer l'heure de la machine fautive : `date -u` et `chronyc tracking`.
- Vérifier le **fichier réellement lu** par le service (`nginx -T | grep ssl_certificate`).
- Protéger la clé (`chmod 600`) ; ne jamais l'envoyer par courriel ni dans un ticket.
- Client en échec alors que le navigateur réussit : magasins de confiance différents.

---

## Mise en pratique guidée

**Objectif** : faire émettre un certificat par une CA de laboratoire, le présenter par un serveur de test et diagnostiquer deux pannes volontaires. **Contexte** : VM jetable ; tout reste sur `127.0.0.1`.

1. **Contrôler le temps** : exécutez `chronyc tracking` et `chronyc sources -v`, relevez la strate et l'écart.
2. **Construire la PKI** : reprenez les commandes des sections 5 à 5.2 dans `~/pki-lab`.
3. **Vérifier** : exécutez les trois `openssl verify` de la section 5.3 et notez le message d'erreur de la deuxième.
4. **Lancer un serveur TLS de test** :

```bash
openssl s_server -accept 8443 -cert www.crt -cert_chain inter.crt -key www.key -www -quiet &
sleep 1
openssl s_client -connect 127.0.0.1:8443 -servername www.example.test -CAfile root.crt -verify_hostname www.example.test </dev/null 2>&1 | grep -E "Verif|depth"
```

👉 Explication : `s_server` joue un mini serveur HTTPS (`-www` répond avec une page d'état) en présentant la feuille et l'intermédiaire ; `s_client` s'y connecte en vérifiant avec la racine et le nom ; vous devez lire `Verification: OK`. Le `&` place le serveur en arrière-plan.

5. **Panne 1 — nom incorrect** : relancez `s_client` avec `-verify_hostname autre.example.test` et constatez `hostname mismatch`.
6. **Panne 2 — intermédiaire absente** : arrêtez le serveur (`kill %1`), relancez-le sans l'option `-cert_chain`, puis reconnectez-vous : les erreurs 20 (`unable to get local issuer certificate`) puis 21 (`unable to verify the first certificate`) apparaissent.
7. **Nettoyage** :

```bash
kill %1 2>/dev/null
cd ~ && rm -rf ~/pki-lab
```

👉 Explication : arrête le serveur de test s'il tourne encore et supprime le dossier contenant les clés de laboratoire.

---

## Exercices

1. **(Facile)** Citez trois services qui cessent de fonctionner correctement quand l'horloge dérive.
2. **(Facile)** Que signifie `^*` dans `chronyc sources` ?
3. **(Facile)** Quelle information envoie-t-on à une autorité de certification : la clé privée ou la CSR ?
4. **(Moyen)** Pourquoi la racine d'une PKI interne est-elle gardée hors ligne ?
5. **(Moyen)** Écrivez la configuration chrony d'un serveur interne servant `198.51.100.0/24`.
6. **(Moyen)** Un navigateur affiche « nom non valide » alors que le certificat est valide et la chaîne complète. Quelle est la cause la plus probable ?
7. **(Avancé)** Concevez une supervision de l'expiration d'un certificat en ligne de commande.
8. **(Avancé)** Vous devez obtenir un certificat pour `*.example.com`. Quel défi ACME choisir et pourquoi ?

## Corrigés des exercices

1. Validation des certificats TLS, authentification Kerberos/Active Directory, codes TOTP, corrélation des journaux, tâches planifiées (réponses acceptées : toute trois de cette liste).
2. La source est **sélectionnée** et sert de référence actuelle pour l'horloge.
3. La **CSR** ; la clé privée ne quitte jamais le serveur.
4. Elle signe les intermédiaires, et sa compromission invaliderait toute la confiance du parc ; l'isoler réduit fortement le risque de vol.
5. ```text
   pool 2.debian.pool.ntp.org iburst maxsources 4
   allow 198.51.100.0/24
   ```
   👉 Explication : sources publiques en amont, et autorisation limitée au réseau demandé, avec l'UDP 123 ouvert pour lui seul.
6. Le nom visité est absent du **SAN** (par exemple visite par l'adresse IP ou par un alias non listé).
7. ```bash
   echo | openssl s_client -connect www.example.test:443 -servername www.example.test 2>/dev/null \
     | openssl x509 -noout -checkend $((21*86400)) || echo "ALERTE : expire dans moins de 21 jours"
   ```
   👉 Explication : récupère le certificat réellement présenté, puis signale une alerte s'il expire dans moins de 21 jours ; à planifier dans l'outil de supervision.
8. **DNS-01**, seul défi qui permet un certificat joker ; il demande une automatisation DNS aux droits limités.

## Quiz

**1.** Quel protocole synchronise l'horloge ? A. SNMP — B. NTP — C. LDAP — D. SMTP. **Réponse : B** ; NTP (UDP 123).

**2.** Que montre `chronyc tracking` ? A. Les routes — B. L'état de synchronisation et l'écart de l'horloge — C. Les certificats — D. Les utilisateurs. **Réponse : B**.

**3.** Écart maximal par défaut toléré par Kerberos ? A. 5 secondes — B. 5 minutes — C. 5 heures — D. aucun. **Réponse : B**.

**4.** Que contient une CSR ? A. La clé privée — B. La clé publique et les noms demandés, signés par la clé privée — C. Le mot de passe de l'autorité — D. La liste de révocation. **Réponse : B**.

**5.** Quel champ les navigateurs utilisent-ils pour vérifier le nom ? A. CN seul — B. SAN — C. Numéro de série — D. Émetteur. **Réponse : B**.

**6.** Pourquoi une racine hors ligne ? A. Elle est plus rapide — B. Pour protéger la clé dont la compromission ruinerait la confiance — C. Pour économiser de l'espace — D. Elle expire plus vite. **Réponse : B**.

**7.** Quel défi ACME permet un certificat joker ? A. HTTP-01 — B. DNS-01 — C. Aucun — D. Ping. **Réponse : B**.

**8.** `error 20 unable to get local issuer certificate` indique souvent… A. Une horloge fausse — B. Une chaîne incomplète ou une racine inconnue — C. Un port fermé — D. Un mot de passe incorrect. **Réponse : B**.

**9.** Que fait `certbot renew --dry-run` ? A. Renouvelle en production — B. Simule le renouvellement sur l'environnement de test — C. Supprime les certificats — D. Révoque tout. **Réponse : B**.

**10.** Certificat valide mais refusé par un client « pas encore valide » : cause probable ? A. Clé trop courte — B. Horloge du client en retard — C. DNS inversé — D. TLS 1.3. **Réponse : B** ; `notBefore` est dans le futur pour ce client.

---

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification / correction |
|---|---|---|
| `Not synchronised` | UDP 123 bloqué, serveurs injoignables, `allow` absent côté serveur | `chronyc sources -v`, pare-feu, journaux `journalctl -u chrony` |
| Écart d'heure après redémarrage de VM | Pas de saut initial autorisé | `makestep 1.0 3`, synchronisation hyperviseur |
| Le navigateur réussit, `curl` échoue | Magasins de confiance différents | `curl --cacert root.crt`, importer la racine dans le bon magasin |
| Chaîne incomplète | Seule la feuille est servie | Servir `fullchain.pem` (feuille puis intermédiaire) |
| `key values mismatch` | Clé et certificat non appariés | Comparer les empreintes (section 7.3) |
| Renouvellement ACME en échec | Port 80 filtré, DNS erroné, hook manquant | `certbot renew --dry-run`, journaux, `deploy-hook` |
| Certificat expiré en production | Renouvellement non supervisé | Alerte à 21 et 7 jours avec `-checkend` |
| Clé privée copiée dans un dépôt | Mauvaise hygiène | Révoquer, réémettre, purger l'historique, rotation des secrets |

Méthode : vérifier d'abord **l'heure**, puis **ce qui est réellement présenté** (`s_client`), puis la **chaîne**, puis le **nom**.

## À retenir

- L'heure est une dépendance de sécurité : la dérive casse certificats, Kerberos et journaux.
- chrony : sources multiples, serveur interne, `tracking` et `sources` pour diagnostiquer ; `allow` et pare-feu pour le service.
- PKI : racine hors ligne, intermédiaire pour l'émission, certificat de feuille à courte durée.
- La clé privée ne circule jamais ; seule la CSR est transmise.
- Un SAN correct et une chaîne complète conditionnent la confiance du client.
- ACME automatise, mais **renouvellement, rechargement et surveillance** doivent être testés.
- `openssl s_client`, `x509`, `verify` : trois commandes pour comprendre presque toutes les pannes.

## Pour aller plus loin

- Documentation de chrony : <https://chrony-project.org/documentation.html>
- RFC 5905, NTP version 4 : <https://www.rfc-editor.org/rfc/rfc5905>
- RFC 8915, Network Time Security : <https://www.rfc-editor.org/rfc/rfc8915>
- RFC 5280, profil de certificat X.509 et CRL : <https://www.rfc-editor.org/rfc/rfc5280>
- RFC 8555, ACME : <https://www.rfc-editor.org/rfc/rfc8555>
- Documentation de Let's Encrypt : <https://letsencrypt.org/docs/>
- Manuel de `openssl` : <https://docs.openssl.org/master/>
- Leçon précédente : [Serveur web et reverse proxy](/fr/00-cours-theoriques/tout-en-un/03-services-d-infrastructure/lecons/lecon-serveur-web-et-reverse-proxy)

## Crédits des images

| Fichier | Source (URL de la page Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/temps-et-certificats-1.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/temps-et-certificats-2.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/temps-et-certificats-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Debian 12 / chrony / certbot | Rédaction assistée (Copilot) | Non testé sur plateforme cible |
| 2026-11-01 | OpenSSL 3.5.9 (runtime Flatpak Freedesktop SDK 25.08, dossier de travail jetable, sans sudo) | Rédaction assistée (Copilot) | Commandes des sections 5 et 7.3 et de l'atelier (clés, CSR, signature, `verify`, `x509`, `-checkend`, comparaison d'empreintes, `s_server`/`s_client` sur 127.0.0.1 avec les cas nom incorrect et chaîne incomplète) exécutées avec les résultats annoncés ; chrony, certbot, installation dans le magasin système et `s_client` distant non testés |