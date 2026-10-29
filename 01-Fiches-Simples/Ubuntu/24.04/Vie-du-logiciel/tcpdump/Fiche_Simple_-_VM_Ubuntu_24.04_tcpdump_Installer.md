# Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Installer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à tcpdump
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / installation
- **Tags** : `tcpdump`, `ubuntu24.04`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer tcpdump depuis les dépôts officiels Ubuntu.

## 1. Hors-Production (Lab / Test / POC)

1. Actualiser les index et vérifier le candidat :
   ```bash
   sudo apt update
   apt-cache policy tcpdump libpcap0.8t64
   ```
   👉 Explication : Confirme l’origine et la version du paquet avant installation; la version exacte dépend de la publication, à vérifier sur l’hôte.

2. Installer l’outil et consigner sa version :
   ```bash
   sudo apt install tcpdump
   tcpdump --version
   ```
   👉 Explication : Installe tcpdump et sa dépendance libpcap; `--version` consigne les versions de tcpdump et libpcap.

3. Lister les interfaces visibles :
   ```bash
   sudo tcpdump -D
   ```
   👉 Explication : Affiche les interfaces utilisables; la liste ne vaut pas autorisation de capture.

## 2. Production — Contrôles

Consigner version, origine du paquet et compte qui peut obtenir les privilèges de capture.

## 3. Production — Sécurité

- Ne pas positionner de capacités root permanentes (setcap) sur le binaire sans analyse de risque.
- Installer uniquement depuis les dépôts du système.

## Validation et retour arrière

- **Validation** : `tcpdump --version` répond et l’interface autorisée apparaît dans `tcpdump -D`.
- **Retour arrière** : Désinstaller si l’outil n’est plus justifié : `sudo apt remove tcpdump`.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_tcpdump.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Configurer.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Prerequis_Limites.md)
