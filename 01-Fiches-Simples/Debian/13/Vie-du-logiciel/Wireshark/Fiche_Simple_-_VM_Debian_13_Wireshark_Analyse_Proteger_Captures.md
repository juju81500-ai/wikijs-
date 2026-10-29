# Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Proteger_Captures.md

- **Environnement** : Poste Debian 13 avec captures
- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark des dépôts Debian
- **Catégorie** : analyse reseau / confidentialite
- **Tags** : `wireshark`, `debian13`, `pcap`, `confidentialite`

---

## Problème précis à résoudre

Limiter l'exposition des données contenues dans les captures.

## 1. Hors-Production (Lab / Test / POC)

1. Restreindre les droits du dossier et des fichiers :
   ```bash
   chmod 700 "$HOME/captures"
   chmod 600 "$HOME"/captures/*.pcapng
   ```
   👉 Explication : seul le propriétaire lit les captures.

2. Lister les captures existantes :
   ```bash
   ls -l "$HOME/captures"
   ```
   👉 Explication : on repère celles dont la finalité est expirée.

3. Supprimer une capture expirée (nom à remplacer) :
   ```bash
   rm -i "$HOME/captures/test-local.pcapng"
   ```
   👉 Explication : `-i` demande confirmation; sur SSD ou snapshots la suppression ne garantit pas l'effacement.

## 2. Production — Contrôles

Chiffrer stockage et transfert selon la politique locale; contrôler copies et sauvegardes automatiques.

## 3. Production — Sécurité

- Ne pas joindre de capture à un ticket, message ou dépôt sans revue et anonymisation.
- Éviter `/tmp` partagé et les dépôts de code.
- Un PCAP peut contenir cookies et identifiants en clair.

## Validation et retour arrière

- **Validation** : Captures en droits restreints et purge appliquée.
- **Retour arrière** : Restaurer les droits d'origine avec `chmod` si nécessaire.

## Si le problème n'est pas résolu

- [Wireshark — FAQ](https://www.wireshark.org/faq.html)
- [Wireshark Wiki — privilèges de capture](https://wiki.wireshark.org/CaptureSetup/CapturePrivileges)
- [Guide complet Wireshark Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/83_Installation_Wireshark_Debian_13_Analyse_Capture.md#6-proteger-les-fichiers-de-capture)
