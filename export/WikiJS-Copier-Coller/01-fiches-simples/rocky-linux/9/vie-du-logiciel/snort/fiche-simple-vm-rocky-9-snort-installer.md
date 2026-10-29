# Fiche_Simple_-_VM_Rocky_9_Snort_Installer

- **Environnement** : VM Rocky Linux 9 dédiée à Snort
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / installation

---

## Problème précis à résoudre

Installer Snort 3 et libdaq depuis les sources officielles sur VM Rocky Linux 9.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils de compilation et dépendances :
   ```bash
   sudo dnf install -y epel-release
   sudo dnf config-manager --set-enabled crb
   sudo dnf install -y gcc gcc-c++ make cmake git pkgconf-pkg-config flex bison libpcap-devel pcre2-devel libdnet-devel hwloc-devel luajit-devel openssl-devel zlib-devel libunwind-devel xz-devel libuuid-devel
   ```
   👉 Explication : Prépare la compilation. CRB et EPEL sont nécessaires pour les paquets -devel; certains noms (libdnet-devel, luajit-devel) sont à vérifier avec `dnf search`. Si un paquet manque, consulter le README de Snort 3.

2. Choisir et consigner les versions à compiler :
   ```bash
   git ls-remote --tags https://github.com/snort3/libdaq.git | tail -n 5
   git ls-remote --tags https://github.com/snort3/snort3.git | tail -n 5
   ```
   👉 Explication : Liste les derniers tags publiés; choisir une release stable (non une branche de développement) et la consigner : VERSION_LIBDAQ et VERSION_SNORT3 sont à remplacer.

3. Compiler et installer libdaq :
   ```bash
   mkdir -p ~/build-snort && cd ~/build-snort
   git clone --branch VERSION_LIBDAQ --depth 1 https://github.com/snort3/libdaq.git
   cd libdaq && ./bootstrap && ./configure --prefix=/opt/snort3 && make -j"$(nproc)" && sudo make install
   ```
   👉 Explication : libdaq est la couche d’acquisition des paquets; installée sous `/opt/snort3` pour ne pas écraser de paquet système.

4. Compiler et installer Snort 3 :
   ```bash
   cd ~/build-snort
   git clone --branch VERSION_SNORT3 --depth 1 https://github.com/snort3/snort3.git
   cd snort3
   export PKG_CONFIG_PATH=/opt/snort3/lib/pkgconfig:$PKG_CONFIG_PATH
   ./configure_cmake.sh --prefix=/opt/snort3
   cd build && make -j"$(nproc)" && sudo make install
   /opt/snort3/bin/snort -V
   ```
   👉 Explication : Construit puis installe Snort; le script `configure_cmake.sh` est celui fourni par le dépôt (vérifier le README de la release). `snort -V` consigne la version.

5. Option : contrôler d’abord le paquet de la distribution.
   ```bash
   dnf search snort
   ```
   👉 Explication : Vérifie la disponibilité de paquets; n’installer un paquet que si la branche et la maintenance sont acceptables. Ne pas mélanger deux installations dans le PATH.

## 2. Production — Contrôles

Consigner versions, tags, empreintes éventuelles et date de compilation; compiler sur une machine de build si la politique l’exige.

## 3. Production — Sécurité

- Compiler sous un compte non privilégié; seul `make install` utilise sudo.
- Vérifier l’origine du dépôt Git (organisation snort3).

## Validation et retour arrière

- **Validation** : `/opt/snort3/bin/snort -V` affiche la version compilée.
- **Retour arrière** : Supprimer l’installation : `sudo rm -rf /opt/snort3` (après sauvegarde de la configuration) et le dossier `~/build-snort`.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-snort)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-configurer)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-prerequis-limites)