# Fiche_Simple_-_VM_Debian_13_cURL_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 avec réseau de test autorisé
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : transfert HTTP / diagnostic
- **Tags** : `debian13`, `curl`, `http`, `tls`, `api`
---

## Problème précis à résoudre

Préserver configuration et scripts associés à cURL; vérifier restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder fichiers de configuration non secrets
   ```bash
   umask 077
   cp -a ~/.curlrc ~/.curlrc.before
   ```
   👉 Explication : sauvegarder seulement options non secrètes.

2. Chiffrer et vérifier copie
   ```bash
   sha256sum ~/.curlrc.before
   ```
   👉 Explication : ne pas diffuser chemins ou données internes.

3. Restaurer sur une copie isolée
   ```text
   Navigateur > ouvrir la documentation officielle : https://curl.se/docs/manpage.html
   ```
   👉 Explication : s’assurer qu’aucun token en clair n’est contenu. Détail à confirmer dans la documentation officielle avant application : Restaurer le fichier `.curlrc` de test et retirer les réponses temporaires.

## 2. Production — Contrôles

Définir rétention, accès, chiffrement et test de restauration; ne pas sauvegarder les secrets en clair.

## 3. Production — Sécurité

- Ne pas traiter les fichiers secrets comme une sauvegarde ordinaire.
- Séparer sauvegarde et hôte de production.
- Tester la récupération avant dépendance.

## Validation et retour arrière

- **Validation** : Configuration de test est restaurée et les permissions attendues sont conservées.
- **Retour arrière** : Restaurer la copie connue et isoler la version suspecte.

## Si le problème n'est pas résolu

- [curl — manuel](https://curl.se/docs/manpage.html)
- [curl — certificats TLS](https://curl.se/docs/sslcerts.html)
- [Debian — paquet curl](https://packages.debian.org/trixie/curl)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_cURL_Prerequis_Limites.md>)
