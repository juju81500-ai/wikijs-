---
title: "Leçon — Cryptographie appliquée : chiffrer, hacher, signer, certifier"
description: "À la fin de cette leçon, vous serez capable de :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "securite", "durcissement", "cryptographie", "tls", "certificats"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Cryptographie appliquée : chiffrer, hacher, signer, certifier

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `securite`, `durcissement`, `cryptographie`, `tls`, `certificats`
- **Niveau** : Débutant à intermédiaire (administrateur systèmes et réseaux)
- **Durée estimée** : 3 h (cours 1 h 15, laboratoire 1 h, exercices et quiz 45 min)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous serez capable de :

1. **distinguer** chiffrement symétrique, asymétrique, hachage, signature et code d'authentification, et dire quel outil répond à quel besoin ;
2. **expliquer** pourquoi un mot de passe se stocke avec un sel et une fonction lente, et choisir une fonction adaptée ;
3. **lire** un certificat X.509 (sujet, émetteur, [[Glossary:SAN]], dates) et décrire sa chaîne de confiance ;
4. **décrire** une poignée de main [[Glossary:TLS]] 1.3 et reconnaître les erreurs de validation fréquentes ;
5. **appliquer** de bonnes pratiques de gestion des clés : génération, droits, stockage, rotation, révocation ;
6. **repérer** les erreurs classiques et les corriger ;
7. **réaliser** un laboratoire local avec OpenSSL sur des clés jetables.

## Prérequis et durée

- Terminal Linux (commandes de base, redirections, `chmod`) ; notions de réseau (client/serveur, port 443).
- Une [[Glossary:VM]] Linux jetable avec OpenSSL 3.x. Aucun accès à un serveur de production.
- Durée : environ 3 h. Domaines `example.com` et `example.test`, adresses de documentation (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, `2001:db8::/32`). Aucune vraie clé ni aucun vrai mot de passe : vous générez vos propres valeurs de test. Suite logique : [VPN et segmentation](/fr/00-cours-theoriques/tout-en-un/05-securite-et-durcissement/lecons/lecon-vpn-segmentation).

## L'essentiel en bref

- **Chiffrer** protège la confidentialité ; **hacher** donne une empreinte à sens unique ; **signer** prouve l'origine et l'intégrité ; **certifier** relie une clé publique à une identité.
- On chiffre les données avec une clé **symétrique** (rapide) et on échange ou signe avec une paire **asymétrique** : TLS combine les deux.
- Un mot de passe ne se chiffre pas : on stocke une **empreinte salée et lente** (Argon2id, scrypt, bcrypt, PBKDF2).
- La solidité repose sur la **clé**, pas sur le secret de l'algorithme : n'inventez jamais votre cryptographie.
- La **gestion des clés** cause plus d'incidents que la faiblesse mathématique des algorithmes.
- Le cadenas du navigateur signifie « connexion chiffrée vers un nom couvert par un certificat valide », pas « site honnête ».

![Schéma comparant le chiffrement symétrique, où Alice et Bob partagent une même clé secrète, et le chiffrement asymétrique, où Alice chiffre avec la clé publique de Bob et seule la clé privée de Bob déchiffre](images/crypto-appliquee-1.svg)

*Figure 1 — Une clé partagée (gauche) contre une paire de clés publique/privée (droite). Schéma original, domaine public (CC0).*

---

## 1. Les quatre briques

| Besoin | Brique | Analogie postale | Exemple |
|---|---|---|---|
| Que personne ne lise | Chiffrement | Enveloppe cadenassée | AES-GCM, ChaCha20-Poly1305 |
| Détecter une modification | Hachage, MAC | Scellé numéroté | SHA-256, HMAC |
| Prouver qui a écrit | Signature | Signature légalisée | Ed25519, ECDSA, RSA-PSS |
| Savoir à qui appartient une clé | Certificat | Carte d'identité | X.509 |

Trois idées :

- Les briques sont **complémentaires** : un message chiffré mais non authentifié peut être modifié en route. On utilise donc des modes **AEAD** (AES-GCM) qui chiffrent et protègent l'intégrité.
- **Principe de Kerckhoffs** : tout doit rester sûr même si l'attaquant connaît l'algorithme ; seule la clé est secrète. Un algorithme public, étudié pendant des années, vaut mieux qu'un procédé « maison ».
- Taille de clé et algorithme sont des **paramètres de sécurité** : un ordre de grandeur courant associe 128 bits symétriques, [[Glossary:RSA]] 3072 et une courbe de 256 bits.

## 2. Chiffrement symétrique

**La même clé** chiffre et déchiffre : un coffre dont Alice et Bob détiennent chacun un exemplaire de la clé. C'est rapide, y compris sur des téraoctets (instructions AES-NI). À retenir : **[[Glossary:AES]]** (128 ou 256 bits) et **ChaCha20-Poly1305**.

**Modes de fonctionnement** (AES traite 16 octets à la fois) :

- **ECB** : blocs chiffrés indépendamment ; deux blocs identiques donnent deux blocs identiques, ce qui laisse voir la structure des données. **À proscrire.**
- **CBC** : chaînage par vecteur d'initialisation, mais **sans authentification** (attaques de type *padding oracle*).
- **GCM**, ChaCha20-Poly1305 : AEAD avec étiquette d'authentification. **Choix par défaut.**

**Piège du nonce** : réutiliser le même couple clé + nonce avec AES-GCM est catastrophique (l'attaquant peut forger des messages). Laissez la bibliothèque le gérer.

**Reste le problème de la clé** : comment Alice la transmet-elle à Bob sans interception ? C'est le rôle de l'asymétrique.

## 3. Chiffrement asymétrique

Chaque acteur a une **clé publique** (diffusable) et une **clé privée** (secrète) liées mathématiquement. Analogie : une boîte aux lettres, où n'importe qui peut glisser un courrier (chiffrer avec la clé publique) mais où seul le détenteur de la clé relève le courrier (déchiffrer avec la clé privée).

| Famille | Exemples | Usage |
|---|---|---|
| RSA | RSA-3072, RSA-4096 | Signature, chiffrement de clés |
| Courbes elliptiques | ECDSA P-256, Ed25519 | Signature (clés courtes) |
| Échange de clés | ECDH, X25519 | Accord sur un secret (TLS 1.3, WireGuard) |

Ces algorithmes ne chiffrent pas de gros volumes : on établit une **clé de session symétrique** (chiffrement hybride) ou on **signe**.

**Confidentialité persistante** : dans un échange Diffie-Hellman **éphémère** (ECDHE, X25519), chaque partie crée des clés temporaires puis les détruit. Si la clé privée du serveur est volée des années plus tard, **les anciennes sessions enregistrées restent indéchiffrables** (*forward secrecy*, obligatoire en TLS 1.3).

## 4. Hachage, salage et mots de passe

Une fonction de hachage transforme une entrée quelconque en **empreinte** de taille fixe (256 bits pour SHA-256) : **déterministe**, **à sens unique**, **résistante aux collisions**. Analogie : l'empreinte digitale, qui identifie sans permettre de reconstituer la personne. Usages : intégrité d'un fichier téléchargé, identification de contenu, base des signatures. **MD5 et SHA-1 sont cassés** pour la sécurité.

**HMAC** mélange une clé secrète à l'empreinte : seuls ceux qui la connaissent produisent ou vérifient le code (jetons, webhooks).

**Pourquoi pas SHA-256 pour les mots de passe ?** Il est conçu pour être **rapide** : un processeur graphique en calcule des milliards par seconde. Après une fuite, l'attaquant teste des listes de mots de passe à cette vitesse ; deux utilisateurs au même mot de passe auraient la même empreinte et les tables précalculées (*rainbow tables*) fonctionneraient.

Deux ingrédients règlent le problème :

1. **Le sel** : valeur aléatoire **unique par utilisateur**, stockée à côté de l'empreinte. Il n'est pas secret ; il neutralise les tables précalculées et fait diverger les empreintes.
2. **La lenteur voulue** : une fonction de dérivation réglée pour consommer du temps et de la mémoire.

| Fonction | Point fort | Réglage |
|---|---|---|
| Argon2id | Coûteuse en mémoire, résiste aux GPU | mémoire, itérations, parallélisme |
| scrypt | Coûteuse en mémoire | N, r, p |
| bcrypt | Éprouvée | coût (≥ 12 aujourd'hui) |
| PBKDF2-HMAC-SHA-256 | Normalisée, répandue | itérations (centaines de milliers) |

Les coûts évoluent avec le matériel : suivez les fiches de l'OWASP ou de l'[[Glossary:ANSSI]] et **mesurez** (quelques centaines de millisecondes par vérification). Un **poivre** (secret global hors base) ajoute une protection, sans remplacer la fonction lente ni l'**authentification multifacteur**.

![Schéma du stockage d'un mot de passe : un mot de passe et un sel aléatoire passent dans une fonction lente, seule l'empreinte et le sel sont conservés ; à la connexion on recalcule et on compare](images/crypto-appliquee-2.svg)

*Figure 2 — Création puis vérification d'un mot de passe salé. Schéma original, domaine public (CC0).*

## 5. Signatures numériques

L'émetteur calcule l'empreinte du document et la **signe avec sa clé privée**. Tout le monde vérifie avec la **clé publique** : **intégrité** (rien n'a changé), **authenticité** (le détenteur de la clé a signé) et **non-répudiation** technique. Analogie : un sceau de cire, que seul le propriétaire de la bague produit mais que chacun peut contrôler.

On la rencontre dans les **dépôts de paquets** ([[Glossary:APT]], [[Glossary:RPM]]), les **commits Git** et images de conteneurs signés, les **certificats TLS**, les mises à jour de firmware.

**Signature ou somme de contrôle ?** Une somme publiée **sur la même page** que le fichier ne prouve rien : si la page est compromise, les deux sont remplacés. Une signature vérifiée avec une clé publique obtenue **par un autre canal fiable** apporte une vraie garantie.

## 6. Certificats et PKI

Une clé publique seule n'a pas de nom. Un **certificat X.509** l'associe à une identité et porte la **signature d'une autorité de certification** (AC). À savoir lire :

- **Subject** (titulaire) et **Subject Alternative Name (SAN)** : les noms valides, ce que vérifient les clients modernes ;
- **Issuer** : l'autorité signataire ;
- **Not Before / Not After** : validité ;
- **Key Usage / Extended Key Usage** : usages permis ; **Basic Constraints** : `CA:TRUE` si le certificat est lui-même une autorité.

**Chaîne de confiance.** Votre système contient un **magasin de confiance** d'autorités racines. Le serveur présente son certificat et ses **intermédiaires** ; le client remonte jusqu'à une racine connue.

![Chaîne de confiance : une autorité racine signe une autorité intermédiaire, qui signe le certificat du serveur www.example.com, avec la liste des vérifications du client et des échecs fréquents](images/crypto-appliquee-3.svg)

*Figure 3 — Chaîne de confiance et vérifications du client. Schéma original, domaine public (CC0).*

Le client contrôle les signatures de la chaîne, les **dates**, que **le nom demandé figure dans le SAN**, l'usage et, selon les cas, la révocation (OCSP, [[Glossary:CRL]]). Un seul échec doit faire refuser la connexion.

| Type | Qui signe | Usage |
|---|---|---|
| AC publique ([[Glossary:ACME]]) | Autorité reconnue des navigateurs | Services sur Internet |
| AC interne | Votre autorité, racine distribuée à vos postes | Services internes, mTLS |
| Auto-signé | Le certificat lui-même | **Laboratoire uniquement** |

Un certificat auto-signé n'est pas « moins chiffré » : il est **non vérifiable** par un tiers. Habituer les utilisateurs à cliquer sur « continuer malgré l'avertissement » est dangereux. Les durées de validité raccourcissent : la réponse aux pannes d'expiration est l'**automatisation** (ACME, renouvellement planifié, supervision de la date), pas la mémoire de l'administrateur.

## 7. TLS en pratique

TLS apporte **confidentialité** (chiffrement), **intégrité** (AEAD) et **authentification du serveur** (et du client avec mTLS) à HTTPS, SMTPS, IMAPS, LDAPS, etc.

**Poignée de main TLS 1.3 simplifiée :**

1. **ClientHello** : versions, suites, partage de clé éphémère, nom demandé (SNI).
2. **ServerHello** avec son partage de clé : les deux calculent le même secret et **tout le reste est chiffré**.
3. Le serveur envoie son **certificat** et une signature prouvant qu'il possède la clé privée.
4. Chacun envoie **Finished**, qui authentifie tout l'échange.
5. Les données applicatives circulent en AEAD.

![Diagramme de séquence TLS 1.3 : ClientHello, ServerHello, certificat, Finished du serveur, Finished du client, puis données applicatives chiffrées](images/crypto-appliquee-4.svg)

*Figure 4 — Poignée de main TLS 1.3 simplifiée. Schéma original, domaine public (CC0).*

**Réglages raisonnables** : TLS 1.3, TLS 1.2 si des clients l'exigent, [[Glossary:SSL]] et TLS 1.0/1.1 désactivés (RFC 8996), suites AEAD à échange éphémère (un générateur de profils à jour, comme celui de Mozilla, aide), **[[Glossary:HSTS]]** (RFC 6797) activé progressivement car une erreur de certificat devient alors bloquante. **mTLS** : le client présente aussi un certificat, utile entre services ; il faut gérer l'émission et la révocation.

## 8. Gestion des clés

Un algorithme sûr avec une clé mal gérée n'offre aucune protection. Raisonnez en **cycle de vie** :

| Phase | Bonnes pratiques |
|---|---|
| Génération | Aléa du système ou d'une bibliothèque reconnue, clé créée **là où elle sert** |
| Stockage | Droits `600`, propriétaire dédié, phrase de passe, HSM ou coffre pour les clés critiques |
| Distribution | Jamais en clair par courriel ou messagerie |
| Usage | Une clé, un usage |
| Rotation | Calendrier régulier, procédure testée avant l'urgence |
| Révocation | Savoir révoquer un certificat ou retirer une clé autorisée |
| Fin de vie | Sauvegarde chiffrée séparée si nécessaire ; destruction vérifiable |

- **Jamais de clé privée dans un dépôt Git** (même privé), une image de conteneur, un ticket ou une capture. Utilisez `.gitignore` et un détecteur de secrets. Si une clé a fuité, elle est **compromise** : révoquez et remplacez, ne supprimez pas seulement le commit.
- **Séparez** clés de test et de production ; celles de cette leçon sont jetables.
- Pour [[Glossary:SSH]], préférez des clés **Ed25519** protégées par phrase de passe et agent.
- Prévoyez un **séquestre** (coffre partagé à double contrôle) pour le cas où le seul détenteur d'une clé est indisponible.

## 9. Erreurs classiques

1. **Inventer son algorithme** ou « brouiller » les données (XOR constant) ; Base64 est un codage, pas une protection.
2. **MD5, SHA-1**, ou **SHA-256 nu pour les mots de passe**.
3. **Mode ECB**, IV fixe, nonce réutilisé.
4. **Désactiver la vérification TLS** (`curl -k`, `verify=False`) « temporairement », puis l'oublier.
5. **Clé privée dans un dépôt**, droits `644`, sauvegarde non chiffrée.
6. **Certificat sans SAN** adapté, **intermédiaire manquant**, **expiration oubliée**.
7. **Cadenas = confiance** : un site d'hameçonnage peut avoir un certificat valide pour son propre nom.
8. **Aléa faible** (`rand()`, l'heure) pour fabriquer clés ou jetons.

## 10. Mise en pratique guidée

> **Cadre.** Tout se passe **localement dans un répertoire de laboratoire jetable**, sur une VM de test, sans réseau externe (le serveur TLS n'écoute que la boucle locale). Les clés n'ont aucune valeur et sont détruites à la fin.
>
> **Pour toute modification de sécurité sur un système réel** (suites TLS, certificat, clé SSH) : **1.** snapshot de la VM ou copie des fichiers de configuration ; **2.** accès console de secours ouvert avant de recharger un service ou de modifier SSH ; **3.** test de configuration (`nginx -t`, `sshd -t`) puis vérification depuis un second terminal ; **4.** retour arrière documenté (restauration de la sauvegarde, ancien certificat).

### Étape 1 — Préparer le laboratoire

```bash
mkdir -p ~/lab-crypto && cd ~/lab-crypto
printf 'Message de test pour le laboratoire\n' > message.txt
openssl version
```

👉 Explication : crée un dossier isolé, un fichier d'essai et affiche la version d'OpenSSL (3.x attendue).

### Étape 2 — Chiffrement symétrique

```bash
openssl enc -aes-256-cbc -pbkdf2 -iter 600000 -salt -in message.txt -out message.enc
openssl enc -d -aes-256-cbc -pbkdf2 -iter 600000 -in message.enc
```

👉 Explication : chiffre avec une clé dérivée d'une phrase de passe saisie au clavier (sel aléatoire, PBKDF2), puis déchiffre à l'écran. La commande `enc` est pédagogique et n'authentifie pas les données : pour de vrais usages, `age`, GnuPG ou une bibliothèque AEAD. Ne tapez jamais la phrase dans la ligne de commande (historique, liste des processus). Un mauvais mot de passe doit faire échouer le déchiffrement.

### Étape 3 — Hachage et intégrité

```bash
sha256sum message.txt | tee message.txt.sha256
sha256sum -c message.txt.sha256
printf 'une ligne en plus\n' >> message.txt
sha256sum -c message.txt.sha256
```

👉 Explication : calcule puis revérifie l'empreinte (succès), modifie le fichier puis revérifie (échec) : un seul octet change toute l'empreinte. Rétablissez ensuite le fichier avec `printf 'Message de test pour le laboratoire\n' > message.txt`.

### Étape 4 — Sel et fonction lente

```bash
python3 -c "import hashlib,os; s=os.urandom(16); print(s.hex(), hashlib.scrypt(b'exemple-de-labo', salt=s, n=2**15, r=8, p=1, maxmem=64*1024*1024).hex())"
```

👉 Explication : produit un sel aléatoire et une empreinte scrypt d'un mot de passe d'exemple ; à chaque exécution le sel change, donc l'empreinte aussi pour la même entrée. Mesurez le coût avec `time` pour ajuster N en production.

### Étape 5 — Signature

```bash
openssl genpkey -algorithm ed25519 -out lab-ed25519.key
chmod 600 lab-ed25519.key
openssl pkey -in lab-ed25519.key -pubout -out lab-ed25519.pub
openssl pkeyutl -sign -rawin -inkey lab-ed25519.key -in message.txt -out message.sig
openssl pkeyutl -verify -rawin -pubin -inkey lab-ed25519.pub -in message.txt -sigfile message.sig
```

👉 Explication : génère une paire Ed25519 de laboratoire (clé privée en `600`), en extrait la clé publique, signe le message et vérifie : attendu `Signature Verified Successfully`.

```bash
printf 'falsification\n' >> message.txt
openssl pkeyutl -verify -rawin -pubin -inkey lab-ed25519.pub -in message.txt -sigfile message.sig
```

👉 Explication : après altération du message, la vérification échoue (`Signature Verification Failure`) : l'intégrité est démontrée.

### Étape 6 — Certificat auto-signé avec SAN

```bash
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -nodes \
  -keyout lab.key -out lab.crt -days 30 \
  -subj "/CN=www.example.test" \
  -addext "subjectAltName=DNS:www.example.test,DNS:localhost"
chmod 600 lab.key
openssl x509 -in lab.crt -noout -subject -issuer -dates -ext subjectAltName
openssl x509 -in lab.crt -noout -fingerprint -sha256
```

👉 Explication : crée une clé EC et un certificat auto-signé de 30 jours avec des noms de documentation ; `-nodes` laisse la clé non chiffrée, acceptable seulement ici car elle est jetable. Les commandes suivantes affichent sujet et émetteur (identiques : auto-signé), dates, SAN et empreinte.

### Étape 7 — Serveur TLS 1.3 local et deux clients

Premier terminal :

```bash
openssl s_server -accept 14443 -cert lab.crt -key lab.key -www -tls1_3
```

👉 Explication : mini serveur TLS 1.3 sur le port local 14443 ; arrêtez-le avec Ctrl+C en fin d'étape.

Second terminal :

```bash
echo | openssl s_client -connect 127.0.0.1:14443 -servername www.example.test -CAfile lab.crt -verify_hostname www.example.test 2>&1 | grep -E "Protocol|Cipher|Verif"
echo | openssl s_client -connect 127.0.0.1:14443 -servername www.example.test 2>&1 | grep -E "Verif|verify error"
```

👉 Explication : la première connexion donne le certificat comme ancre de confiance et le nom attendu : `TLSv1.3`, une suite AEAD (par exemple `TLS_AES_256_GCM_SHA384`) et `Verification: OK`. La seconde, sans ancre, signale `self-signed certificate` : le chiffrement fonctionne, la **confiance** non.

### Étape 8 — Nettoyage

```bash
cd ~ && shred -u ~/lab-crypto/*.key 2>/dev/null; rm -rf ~/lab-crypto
```

👉 Explication : efface les clés de laboratoire puis le dossier. `shred` ne garantit rien sur [[Glossary:SSD]] ou système de fichiers à journal ; l'enjeu est nul ici puisque les clés étaient jetables. Pour des clés réelles : chiffrement du disque et révocation.

## Exercices

1. **(Vocabulaire)** Associez chaque besoin à une brique : (a) vérifier qu'un ISO n'est pas corrompu ; (b) rendre illisible une sauvegarde sur disque externe ; (c) prouver qu'un paquet vient de l'éditeur ; (d) stocker les mots de passe d'une application web.
2. **(Choix d'algorithme)** Proposez un algorithme ou une famille pour : une sauvegarde de 500 Go, l'échange de clé initial d'une session web, une signature de commit, une empreinte de mot de passe.
3. **(Lecture de certificat)** Un client reçoit un certificat de SAN `www.example.com`, valide du 1er janvier au 31 mars 2026, et se connecte le 15 avril 2026 à `example.com`. Listez les raisons de l'échec.
4. **(Sel)** Deux utilisateurs ont le même mot de passe. Que voit un attaquant qui lit la base avec SHA-256 sans sel ? Avec Argon2id salé ?
5. **(Analyse)** Un développeur écrit `requests.get(url, verify=False)` « pour que ça marche avec le certificat interne ». Risque et deux corrections.
6. **(Gestion des clés)** Une clé privée de test a été publiée dans un dépôt Git privé, puis supprimée par un commit ultérieur. Marche à suivre en quatre étapes.
7. **(Laboratoire)** Reproduisez l'étape 5 et vérifiez la signature avec la clé publique d'une **seconde** paire. Que constatez-vous, et quelle propriété cela illustre-t-il ?

## Corrigés des exercices

1. (a) **Hachage** ; (b) **chiffrement symétrique** (AES-GCM) ; (c) **signature** vérifiée avec une clé publique d'éditeur obtenue par un canal fiable ; (d) **empreinte salée et lente** (Argon2id, scrypt, bcrypt).
2. Sauvegarde : **AES-256-GCM** ou ChaCha20-Poly1305. Échange initial : **ECDHE/X25519**. Signature de commit : **Ed25519**. Mot de passe : **Argon2id**.
3. Trois causes : certificat **expiré** depuis le 31 mars ; nom `example.com` **absent du SAN** ; éventuellement chaîne incomplète. Une seule suffit.
4. Sans sel : empreintes **identiques**, donc mots de passe identiques révélés et attaque par dictionnaire sur tous les comptes à la fois. Avec sel : empreintes **différentes**, chaque compte s'attaque séparément et lentement.
5. Sans vérification, un intermédiaire peut se faire passer pour le serveur. Corrections : fournir le certificat de l'autorité interne (`verify="/chemin/ac-interne.pem"`) ; installer la racine interne dans le magasin de confiance et corriger l'émission (SAN corrects). Ajouter une alerte de revue de code sur `verify=False`.
6. (1) Considérer la clé **compromise** ; (2) la **retirer** des `authorized_keys`, magasins et listes d'autorisation ; (3) **générer et déployer** une nouvelle paire ; (4) chercher des usages suspects dans les journaux, nettoyer l'historique Git **en plus** de la rotation, mettre en place un détecteur de secrets.
7. La vérification échoue : une signature n'est valable que pour la clé publique correspondant à la clé privée du signataire, ce qui illustre l'**authenticité**.

## Quiz

**Q1.** Quel chiffrement pour un disque de plusieurs téraoctets ?
- A. RSA-4096 — B. Symétrique (AES) — C. SHA-256 — D. Base64

**Q2.** Quelle propriété donne la confidentialité persistante ?
- A. Un certificat longue durée — B. Un échange de clés éphémère (ECDHE/X25519) — C. Un mot de passe long — D. Un HMAC

**Q3.** Pourquoi saler un mot de passe ?
- A. Le rendre réversible — B. Obtenir des empreintes différentes pour des mots de passe identiques et neutraliser les tables précalculées — C. Le chiffrer — D. Raccourcir l'empreinte

**Q4.** Fonction adaptée au stockage de mots de passe :
- A. MD5 — B. SHA-1 — C. SHA-256 nu — D. Argon2id

**Q5.** Une signature numérique est produite avec :
- A. La clé publique du destinataire — B. La clé privée de l'émetteur — C. Un sel — D. Un nonce

**Q6.** Quel champ de certificat valide le nom d'un site pour les clients modernes ?
- A. Issuer — B. Subject Alternative Name — C. Numéro de série — D. Empreinte SHA-1

**Q7.** Un certificat auto-signé présenté à un client qui ne le connaît pas provoque :
- A. Une absence de chiffrement — B. Une erreur de chaîne, alors que le canal peut rester chiffré — C. Un downgrade en TLS 1.0 — D. Aucune erreur

**Q8.** Une clé privée a été publiée par erreur dans un dépôt :
- A. Supprimer le fichier — B. La considérer compromise, la révoquer et la remplacer — C. Renommer le fichier — D. Attendre l'expiration

**Q9.** Pourquoi déconseiller le mode ECB ?
- A. Trop lent — B. Des blocs identiques donnent des blocs chiffrés identiques, ce qui révèle la structure — C. Il n'existe pas dans AES — D. Il impose une clé publique

**Q10.** Que garantit le cadenas du navigateur ?
- A. Que le site est honnête — B. Que la connexion est chiffrée et que le nom correspond à un certificat valide — C. Que le serveur est à jour — D. Que le site est sans virus

**Réponses justifiées.** **Q1 — B** : symétrique rapide ; RSA trop lent, SHA-256 ne chiffre pas, Base64 est un codage. **Q2 — B** : les clés éphémères sont détruites, leur vol ultérieur n'ouvre pas le trafic passé. **Q3 — B** : le sel, public mais unique, casse tables précalculées et égalité d'empreintes. **Q4 — D** : Argon2id est lent et gourmand en mémoire ; les autres sont trop rapides. **Q5 — B** : on signe avec sa clé privée, on vérifie avec la clé publique. **Q6 — B** : le SAN liste les noms valides. **Q7 — B** : le chiffrement peut fonctionner, l'identité n'est pas vérifiable. **Q8 — B** : une fuite se traite comme une compromission. **Q9 — B** : la structure des données reste visible, d'où les modes AEAD. **Q10 — B** : le cadenas parle de chiffrement et de certificat valide, pas d'honnêteté.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification / solution |
|---|---|---|
| `certificate has expired` | Date dépassée ou horloge cliente fausse | `openssl x509 -noout -dates -in cert.pem` ; `timedatectl` ; renouveler |
| `hostname mismatch` | Nom absent du SAN | Régénérer avec tous les noms utilisés |
| `unable to get local issuer certificate` | Intermédiaire non envoyé ou racine inconnue | Concaténer certificat et intermédiaire côté serveur ; installer la racine interne côté client |
| `bad decrypt` à l'étape 2 | Mauvaise phrase, ou options `-pbkdf2 -iter` différentes | Reprendre exactement les mêmes options |
| `UNPROTECTED PRIVATE KEY FILE` (SSH) | Droits trop larges | `chmod 600` |
| Port 14443 refusé | Port occupé ou clé illisible | `ss -ltn` ; vérifier les droits |
| Clients qui ne se connectent plus après un changement TLS | Version ou suite trop récente pour eux | Restaurer la configuration sauvegardée, tester un profil intermédiaire |

Isolez d'abord : `openssl s_client` depuis le client, comparez nom, dates, chaîne ; puis modifiez avec snapshot, console de secours, test, retour arrière.

## À retenir

- Chiffrer ≠ hacher ≠ signer ≠ certifier : chaque brique répond à un besoin.
- Gros volumes : **symétrique AEAD** ; échange et signature : **asymétrique** ; TLS combine les deux avec un échange éphémère.
- Mot de passe : **sel unique + fonction lente**, plus [[Glossary:MFA]].
- Un certificat n'est valide que si chaîne, dates, **nom (SAN)** et usage sont corrects.
- Jamais de vérification TLS désactivée, de clé publiée ou d'algorithme maison.
- La **gestion du cycle de vie des clés** fait la différence.
- Toute modification de sécurité : **snapshot, console de secours, test, retour arrière**.

## Pour aller plus loin

- RFC 8446 (TLS 1.3) : <https://www.rfc-editor.org/rfc/rfc8446>
- RFC 5280 (certificats X.509, CRL) : <https://www.rfc-editor.org/rfc/rfc5280>
- RFC 8996 (abandon de TLS 1.0 et 1.1) : <https://www.rfc-editor.org/rfc/rfc8996>
- RFC 6797 (HSTS) : <https://www.rfc-editor.org/rfc/rfc6797>
- RFC 9106 (Argon2) : <https://www.rfc-editor.org/rfc/rfc9106>
- RFC 8032 (Ed25519) : <https://www.rfc-editor.org/rfc/rfc8032>
- RFC 8555 (ACME) : <https://www.rfc-editor.org/rfc/rfc8555>
- Documentation OpenSSL : <https://docs.openssl.org/>
- ANSSI : <https://cyber.gouv.fr/>
- [[Glossary:NIST]] SP 800-57 Part 1 (gestion des clés) : <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>

## Crédits des images

| Fichier | Source (URL de la page Commons) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/crypto-appliquee-1.svg` | Création originale (pas de page Commons) | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/crypto-appliquee-2.svg` | Création originale | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/crypto-appliquee-3.svg` | Création originale | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/crypto-appliquee-4.svg` | Création originale | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |

Création originale du projet Pack Master, dédiée au domaine public (CC0).

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux, OpenSSL 3.5.9, Python 3.13 : étapes 2 à 7 (chiffrement `enc`, `sha256sum`, scrypt, signature Ed25519, certificat auto-signé, `s_server`/`s_client` en boucle locale) exécutées dans un répertoire jetable puis supprimé, sans droits administrateur ni réseau externe | Agent de rédaction du pack | Commandes validées localement (hors production) |
| 2026-11-01 | VM Debian/Ubuntu du laboratoire, serveurs web et SSH réels | — | Non testé sur plateforme cible |