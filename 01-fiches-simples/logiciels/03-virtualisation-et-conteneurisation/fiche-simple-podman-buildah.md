# 📄 Podman / Buildah

- **Environnement** : VM (Rocky Linux 9)
- **OS / Version** : Rocky Linux 9 (dépôt AppStream)
- **Version** : Podman et Buildah fournis par les dépôts Rocky 9, à vérifier avec `podman --version` et `buildah --version` sur la version déployée
- **Catégorie** : Virtualisation et conteneurisation
- **Tags** : `[rocky-9]`, `[podman]`, `[buildah]`, `[conteneurs]`, `[rootless]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Podman et Buildah sur Rocky Linux 9, vérifier qu'un conteneur s'exécute en mode rootless, construire une image à partir d'un Containerfile, puis durcir l'exécution (compte de service dédié, capacités réduites, politique de confiance des registres). Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Podman et Buildah :
```bash
sudo dnf install -y podman buildah
podman --version
buildah --version
```
👉 Explication : Podman exécute les conteneurs, Buildah construit les images. Les deux commandes affichent la version installée.

2. Vérification du mode rootless :
```bash
podman info | grep -i rootless
```
👉 Explication : Lancée par un utilisateur non root, la commande affiche `rootless: true`, attendu en lab.

3. Premier conteneur de test :
```bash
podman run --rm docker.io/library/alpine:3.20 echo "conteneur OK"
```
👉 Explication : Télécharge l'image Alpine 3.20 et affiche `conteneur OK`. Le nom complet `docker.io/library/alpine:3.20` évite toute ambiguïté de registre.

4. Création d'un Containerfile de test :
```bash
mkdir -p ~/build-test
cat > ~/build-test/Containerfile <<'EOF'
FROM docker.io/library/alpine:3.20
RUN apk add --no-cache curl
CMD ["echo", "image construite"]
EOF
```
👉 Explication : Crée un dossier de travail et un Containerfile minimal : image de base Alpine 3.20, installation de `curl`, commande par défaut.

5. Construction avec Buildah et exécution :
```bash
buildah bud -t localhost/test-alpine:1.0 -f ~/build-test/Containerfile ~/build-test
podman images localhost/test-alpine
podman run --rm localhost/test-alpine:1.0
```
👉 Explication : `buildah bud` construit l'image à partir du Containerfile. `podman images` la liste et `podman run` affiche `image construite`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un compte de service dédié :
```bash
sudo useradd -m -s /bin/bash svc-conteneurs
sudo loginctl enable-linger svc-conteneurs
grep svc-conteneurs /etc/subuid /etc/subgid
```
👉 Explication : Crée un compte sans droits d'administration qui exécute les conteneurs. `enable-linger` maintient ses processus actifs hors session. `grep` affiche la plage d'UID/GID subordonnés nécessaire au mode rootless. Si rien n'apparaît, l'ajouter avec `sudo usermod --add-subuids 100000-165535 --add-subgids 100000-165535 svc-conteneurs`.

2. Construction sous le compte de service :
```bash
sudo mkdir -p /srv/conteneurs/build-test
sudo cp ~/build-test/Containerfile /srv/conteneurs/build-test/
sudo chown -R svc-conteneurs:svc-conteneurs /srv/conteneurs
sudo -iu svc-conteneurs buildah bud -t localhost/test-alpine:1.0 -f /srv/conteneurs/build-test/Containerfile /srv/conteneurs/build-test
```
👉 Explication : Place le Containerfile dans un répertoire appartenant au compte de service, puis construit l'image sous ce compte, sans droits root sur les conteneurs.

3. Export de l'image et empreinte de contrôle :
```bash
sudo -iu svc-conteneurs podman save -o /srv/conteneurs/test-alpine-1.0.tar localhost/test-alpine:1.0
sudo sha256sum /srv/conteneurs/test-alpine-1.0.tar
```
👉 Explication : Exporte l'image dans une archive, puis calcule son empreinte SHA-256 à conserver pour vérifier l'intégrité lors d'un transfert.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Exécution avec capacités réduites :
```bash
sudo -iu svc-conteneurs podman run --rm --cap-drop=ALL --security-opt no-new-privileges --read-only docker.io/library/alpine:3.20 echo "execution durcie OK"
```
👉 Explication : `--cap-drop=ALL` retire toutes les capacités Linux, `no-new-privileges` interdit l'élévation via les binaires setuid, `--read-only` rend le système de fichiers du conteneur non modifiable.

2. Contrôle du mappage des identifiants :
```bash
sudo -iu svc-conteneurs podman unshare cat /proc/self/uid_map
```
👉 Explication : Affiche la correspondance entre l'UID 0 du conteneur et l'UID réel du compte `svc-conteneurs` sur l'hôte. Une ligne qui pointe vers un UID hôte de plage subordonnée confirme l'isolation.

3. Politique de confiance des registres :
```bash
sudo ls -l /etc/containers/policy.json
sudo -iu svc-conteneurs podman image trust show
```
👉 Explication : Vérifie que la politique de confiance est présente et affiche les règles appliquées aux registres. Point à vérifier : la liste des registres autorisés en production doit être décidée par l'équipe, la configuration par défaut n'est pas restrictive.

4. Contrôle des conteneurs présents et de l'espace utilisé :
```bash
sudo -iu svc-conteneurs podman ps -a
sudo -iu svc-conteneurs podman system df
```
👉 Explication : Liste tous les conteneurs, y compris arrêtés, et l'espace occupé par images et conteneurs. Tout conteneur non identifié est à remonter au responsable sécurité.

---
