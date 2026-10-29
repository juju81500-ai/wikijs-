# Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Valider.md

- **Environnement** : VM Debian 13 avec bind9 configuré
- **OS / Version** : Debian 13 Trixie; paquets bind9 de la distribution
- **Catégorie** : dns / validation

---

## Problème précis à résoudre

Contrôler la syntaxe et les réponses DNS avant et après le rechargement.

## 1. Hors-Production (Lab / Test / POC)

1. Valider la configuration et les zones :
   ```bash
   sudo named-checkconf -z /etc/bind/named.conf
   sudo named-checkzone lab.example.test /etc/bind/db.lab.example.test
   sudo named-checkzone 2.0.192.in-addr.arpa /etc/bind/db.192.0.2
   ```
   👉 Explication : en cas d'erreur, corriger et ne surtout pas recharger.

2. Recharger puis lire l'état et les journaux :
   ```bash
   sudo systemctl reload bind9
   sudo rndc status
   sudo journalctl -u bind9 -n 50 --no-pager
   ```
   👉 Explication : le rechargement n'est pas une validation en soi; les journaux ne doivent pas contenir d'erreur.

3. Interroger le serveur (adresse d'exemple à remplacer) :
   ```bash
   dig @192.0.2.53 lab.example.test SOA +norecurse
   dig @192.0.2.53 srv1.lab.example.test A +norecurse
   dig @192.0.2.53 -x 192.0.2.20 +norecurse
   dig @192.0.2.53 debian.org A +recurse
   ```
   👉 Explication : les trois premières réponses doivent porter le drapeau `aa` (autoritatif); la dernière ne doit pas être résolue récursivement.

4. Refaire le test depuis une adresse non autorisée.
   👉 Explication : l'ACL doit refuser la requête.

## 2. Production — Contrôles

Intégrer ces contrôles à chaque changement de zone et tester depuis un client autorisé et un client non autorisé.

## 3. Production — Sécurité

- Ne jamais recharger après un échec de `named-checkconf` ou `named-checkzone`.
- Vérifier que la récursion est bien refusée.

## Validation et retour arrière

- **Validation** : Contrôles de syntaxe réussis, réponses `aa` correctes, récursion refusée.
- **Retour arrière** : Restaurer les fichiers précédents, relancer `named-checkconf -z` et `named-checkzone`, puis `sudo systemctl reload bind9`.

## Si le problème n'est pas résolu

- [ISC BIND 9 — Manpages](https://bind9.readthedocs.io/en/latest/manpages.html)
- [ISC BIND 9 — Security Configurations](https://bind9.readthedocs.io/en/latest/chapter7.html)
- [Guide complet BIND9 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13#4-valider-avant-activation)