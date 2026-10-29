# Fiche_Simple_-_VM_Debian_13_cURL_Securiser

- **Environnement** : VM Debian 13 avec réseau de test autorisé
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : transfert HTTP / diagnostic

---

## Problème précis à résoudre

Réduire les risques d’exécution, de transfert et de fuite liés à cURL.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier droits et entrées
   ```bash
   curl -sS -o /dev/null -w "%{http_code}\n" https://example.com/
   ```
   👉 Explication : remplacer par API à remplacer; utiliser uniquement endpoint approuvé.

2. Activer contrôles adaptés
   ```text
   Navigateur > ouvrir la documentation officielle : https://curl.se/docs/manpage.html
   ```
   👉 Explication : ne pas utiliser `-k`; vérifier destination et redirections. Détail à confirmer dans la documentation officielle avant application : Toujours valider TLS et limiter redirections vers HTTPS.

3. Contrôler les sorties et logs
   ```bash
   curl --fail --show-error --location --max-redirs 3 --proto "=https" --proto-redir "=https" https://example.com/ -o /dev/null
   ```
   👉 Explication : remplacer l’URL et contrôler la destination finale.

## 2. Production — Contrôles

Faire relire commandes automatisées et limiter les destinations, privilèges et données envoyées.

## 3. Production — Sécurité

- Ne pas utiliser `eval` sur des entrées inconnues.
- Ne pas désactiver validation TLS; ne pas transmettre secrets en URL.
- Masquer données personnelles et credentials dans journaux.

## Validation et retour arrière

- **Validation** : Revue confirme droits minimaux, validation des données et absence de secrets dans les sorties.
- **Retour arrière** : Arrêter tâche, révoquer secret exposé et restaurer les fichiers modifiés.

## Si le problème n'est pas résolu

- [curl — manuel](https://curl.se/docs/manpage.html)
- [curl — certificats TLS](https://curl.se/docs/sslcerts.html)
- [Debian — paquet curl](https://packages.debian.org/trixie/curl)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-prerequis-limites>)