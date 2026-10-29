# Fiche_Simple_-_VM_Rocky_9_Wireshark_Installer

- **Environnement** : VM Rocky Linux 9 dédiée à Wireshark
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / installation
- **Tags** : `wireshark`, `rocky9`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Wireshark (GUI) et TShark (CLI) depuis les dépôts Rocky.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les paquets candidats :
   ```bash
   sudo dnf makecache
   dnf info wireshark wireshark-cli
   ```
   👉 Explication : Confirme noms, versions et origine avant installation; noms de paquets à vérifier si la distribution les a modifiés.

2. Installer :
   ```bash
   sudo dnf install wireshark wireshark-cli
   ```
   👉 Explication : Installe l’analyseur et les outils en ligne de commande. Le paquet réserve normalement `dumpcap` au groupe `wireshark`; vérifier avec `ls -l /usr/bin/dumpcap` et `getcap /usr/bin/dumpcap`.

3. Contrôler les versions :
   ```bash
   wireshark --version | head -n 1
   tshark --version | head -n 1
   dumpcap --version | head -n 1
   ```
   👉 Explication : Consigne la version; en session sans écran, `wireshark` peut échouer, ce qui est normal : tshark suffit.

## 2. Production — Contrôles

Consigner version et origine; décider qui reçoit le droit de capture.

## 3. Production — Sécurité

- Ne jamais lancer l’interface graphique en root.
- Préférer les dépôts de la distribution.

## Validation et retour arrière

- **Validation** : Les trois commandes affichent une version.
- **Retour arrière** : Désinstaller : `sudo dnf remove wireshark wireshark-cli`.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Wireshark_Configurer.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Wireshark_Prerequis_Limites.md)
