# Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Reception.md

- **Environnement** : Poste Debian 13 avec Wireshark
- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark des dépôts Debian
- **Catégorie** : analyse reseau / recette
- **Tags** : `wireshark`, `debian13`, `recette`, `controle`

---

## Problème précis à résoudre

Contrôler que l'installation respecte les règles de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les versions et la provenance :
   ```bash
   apt-cache policy wireshark tshark
   dumpcap --version
   ```
   👉 Explication : on consigne les versions issues du dépôt Debian attendu.

2. Vérifier les groupes et les droits de capture :
   ```bash
   id
   getcap "$(command -v dumpcap)"
   ```
   👉 Explication : les privilèges doivent être limités au groupe nominatif approuvé.

3. Contrôler qu'aucun Wireshark ne tourne en root :
   ```bash
   ps -C wireshark -o user,cmd
   ```
   👉 Explication : la colonne utilisateur ne doit pas afficher `root`.

## 2. Production — Contrôles

Valider sur un poste pilote avant généralisation.

## 3. Production — Sécurité

- L'interface graphique ne doit pas tourner en root.
- Promiscuous et capture WLAN ne sont pas activés par défaut.

## Validation et retour arrière

- **Validation** : Versions consignées, privilèges limités, test local réussi.
- **Retour arrière** : Retirer le compte du groupe `wireshark` si les contrôles échouent.

## Si le problème n'est pas résolu

- [Wireshark — téléchargements](https://www.wireshark.org/download.html)
- [Wireshark — README.Debian](https://gitlab.com/wireshark/wireshark/-/raw/master/packaging/debian/README.Debian)
- [Guide complet Wireshark Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/83_Installation_Wireshark_Debian_13_Analyse_Capture.md#7-verifications-de-reception)
