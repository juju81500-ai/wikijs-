# Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Politique_Zones.md

- **Environnement** : VM Debian 13 avec bind9 installé
- **OS / Version** : Debian 13 Trixie; paquets bind9 de la distribution
- **Catégorie** : dns / configuration
- **Tags** : `debian13`, `bind9`, `zone`, `acl`

---

## Problème précis à résoudre

Configurer BIND en autoritatif strict et déclarer la zone directe et inverse.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer `/etc/bind/named.conf.options` (sans créer un second bloc `options`) :
   ```bash
   sudo nano /etc/bind/named.conf.options
   ```
   👉 Explication : on ouvre le fichier d'options pour y placer l'ACL et les options ci-dessous.

2. Ajouter l'ACL et ajuster le bloc `options` (adresses d'exemple à remplacer par les vôtres) :
   ```bash
   acl clients_dns {
       127.0.0.1;
       192.0.2.0/24;
   };

   options {
       directory "/var/cache/bind";
       listen-on { 192.0.2.53; };
       listen-on-v6 { none; };
       recursion no;
       allow-query { clients_dns; };
       allow-query-cache { none; };
       allow-transfer { none; };
       version "non divulguée";
       dnssec-validation auto;
   };
   ```
   👉 Explication : `recursion no` rend le serveur autoritatif uniquement; l'ACL limite les clients; les transferts sont interdits. Ne jamais remplacer l'ACL par `any`.

3. Déclarer les zones dans `/etc/bind/named.conf.local` :
   ```bash
   sudo nano /etc/bind/named.conf.local
   ```
   👉 Explication : on ouvre le fichier des zones locales.

4. Contenu à ajouter :
   ```bash
   zone "lab.example.test" {
       type primary;
       file "/etc/bind/db.lab.example.test";
       allow-query { clients_dns; };
       allow-transfer { none; };
       notify no;
   };

   zone "2.0.192.in-addr.arpa" {
       type primary;
       file "/etc/bind/db.192.0.2";
       allow-query { clients_dns; };
       allow-transfer { none; };
       notify no;
   };
   ```
   👉 Explication : une zone directe et une zone inverse de type `primary`, sans transfert ni notification.

5. Créer la zone directe :
   ```bash
   sudo nano /etc/bind/db.lab.example.test
   ```
   👉 Explication : puis y placer le contenu suivant.

6. Contenu de la zone directe :
   ```bash
   $TTL 3600
   @ IN SOA ns1.lab.example.test. hostmaster.lab.example.test. (
       2026102701 ; serial: incrémenter à chaque modification
       3600       ; refresh
       900        ; retry
       1209600    ; expire
       300        ; negative cache TTL
   )
   @    IN NS ns1.lab.example.test.
   ns1  IN A  192.0.2.53
   srv1 IN A  192.0.2.20
   ```
   👉 Explication : enregistrements SOA, NS et A; le numéro de série doit augmenter à chaque modification.

7. Créer la zone inverse :
   ```bash
   sudo nano /etc/bind/db.192.0.2
   ```
   👉 Explication : puis y placer le contenu suivant.

8. Contenu de la zone inverse :
   ```bash
   $TTL 3600
   @ IN SOA ns1.lab.example.test. hostmaster.lab.example.test. (
       2026102701
       3600
       900
       1209600
       300
   )
   @  IN NS  ns1.lab.example.test.
   20 IN PTR srv1.lab.example.test.
   53 IN PTR ns1.lab.example.test.
   ```
   👉 Explication : enregistrements PTR correspondant aux enregistrements A. Ne pas rendre ces fichiers inscriptibles par l'utilisateur `bind`.

## 2. Production — Contrôles

Faire relire l'ACL, les zones, le propriétaire de zone et la procédure d'incrément du numéro SOA; stocker les zones dans un dépôt de configuration protégé.

## 3. Production — Sécurité

- Ne jamais mettre `any` dans les ACL.
- Garder `allow-transfer { none; }` tant qu'aucun secondaire n'existe.
- Ne pas rendre la configuration inscriptible par l'utilisateur `bind`.
- Ne pas activer de mises à jour dynamiques basées sur une simple IP source.

## Validation et retour arrière

- **Validation** : Fichiers de zone et d'options créés, validés à l'étape suivante avant rechargement.
- **Retour arrière** : Restaurer l'archive sauvegardée de `/etc/bind` (ou les fichiers précédents) puis refaire les contrôles de l'étape de validation.

## Si le problème n'est pas résolu

- [ISC BIND 9 — Configurations and Zone Files](https://bind9.readthedocs.io/en/latest/chapter3.html)
- [ISC BIND 9 — Security Configurations](https://bind9.readthedocs.io/en/latest/chapter7.html)
- [Guide complet BIND9 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/63_Deploiement_BIND9_Autoritatif_Debian_13.md#3-definir-une-politique-autoritative)
