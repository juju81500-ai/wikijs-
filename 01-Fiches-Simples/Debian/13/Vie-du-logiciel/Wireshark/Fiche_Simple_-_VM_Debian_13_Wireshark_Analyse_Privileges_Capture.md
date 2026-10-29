# Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Privileges_Capture.md

- **Environnement** : Poste Debian 13 avec Wireshark installé
- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark des dépôts Debian
- **Catégorie** : analyse reseau / privileges
- **Tags** : `wireshark`, `debian13`, `dumpcap`, `groupe`

---

## Problème précis à résoudre

Autoriser la capture live à un compte nominatif sans lancer Wireshark en root.

## 1. Hors-Production (Lab / Test / POC)

1. Reconfigurer le paquet :
   ```bash
   sudo dpkg-reconfigure wireshark-common
   ```
   👉 Explication : répondre **Yes** pour autoriser les non-superusers; `dumpcap` capture, l'interface reste sans privilège.

2. Ajouter uniquement le compte autorisé au groupe :
   ```bash
   sudo usermod -aG wireshark "$USER"
   ```
   👉 Explication : seul ce compte pourra capturer.

3. Fermer puis rouvrir la session graphique, puis vérifier :
   ```bash
   id
   dumpcap -D
   getcap "$(command -v dumpcap)"
   ```
   👉 Explication : le groupe `wireshark` doit apparaître et les interfaces être listées.

## 2. Production — Contrôles

Si le besoin est ponctuel, garder **No** et faire capturer par un administrateur avec `dumpcap`.

## 3. Production — Sécurité

- Ne pas lancer l'interface graphique ni TShark avec `sudo`.
- Ne pas ajouter de compte générique ou de service au groupe.
- Ne pas modifier à la main les capabilities ni le bit setuid de `dumpcap`.

## Validation et retour arrière

- **Validation** : `dumpcap -D` liste les interfaces sous le compte nominatif.
- **Retour arrière** : `sudo gpasswd -d "$USER" wireshark` puis `sudo dpkg-reconfigure wireshark-common` en répondant **No**.

## Si le problème n'est pas résolu

- [Wireshark Wiki — privilèges de capture](https://wiki.wireshark.org/CaptureSetup/CapturePrivileges)
- [Wireshark — README.Debian](https://gitlab.com/wireshark/wireshark/-/raw/master/packaging/debian/README.Debian)
- [Guide complet Wireshark Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/83_Installation_Wireshark_Debian_13_Analyse_Capture.md#3-autoriser-la-capture-live-avec-des-privileges-separes)
