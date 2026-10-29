# Fiche_Simple_-_VM_Rocky_9_tcpdump_Installer

- **Environnement** : VM Rocky Linux 9 dédiée à tcpdump
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / installation

---

## Problème précis à résoudre

Installer tcpdump depuis les dépôts officiels Rocky.

## 1. Hors-Production (Lab / Test / POC)

1. Actualiser les index et vérifier le candidat :
   ```bash
   sudo dnf makecache
   dnf info tcpdump
   ```
   👉 Explication : Confirme l’origine et la version du paquet avant installation; la version exacte dépend de la publication, à vérifier sur l’hôte.

2. Installer l’outil et consigner sa version :
   ```bash
   sudo dnf install tcpdump
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
- **Retour arrière** : Désinstaller si l’outil n’est plus justifié : `sudo dnf remove tcpdump`.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-tcpdump)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-configurer)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-prerequis-limites)