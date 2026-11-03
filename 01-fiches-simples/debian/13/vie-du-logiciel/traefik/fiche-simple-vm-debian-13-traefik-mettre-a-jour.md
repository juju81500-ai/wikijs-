# Fiche_Simple_-_VM_Debian_13_Traefik_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Mise à jour et retour arrière
- **Tags** : `debian13`, `traefik`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour le binaire Traefik et revenir à la version précédente si nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder binaire et configuration :
   ```bash
   sudo cp -a /usr/local/bin/traefik /usr/local/bin/traefik.avant-maj
   sudo tar -czpf /var/backups/traefik/avant-maj-$(date +%F).tar.gz /etc/traefik
   traefik version
   ```
   👉 Explication : le binaire conservé est la voie de retour.

2. Télécharger la nouvelle version et vérifier la somme :
   ```bash
   cd ~ && VERSION=VERSION_TRAEFIK
   curl -fLO https://github.com/traefik/traefik/releases/download/v${VERSION}/traefik_v${VERSION}_linux_amd64.tar.gz
   curl -fLO https://github.com/traefik/traefik/releases/download/v${VERSION}/traefik_v${VERSION}_checksums.txt
   sha256sum --ignore-missing -c traefik_v${VERSION}_checksums.txt
   ```
   👉 Explication : remplacer `VERSION_TRAEFIK` après lecture des notes de migration (une montée de version majeure peut changer la syntaxe).

3. Installer et redémarrer :
   ```bash
   tar -xzf traefik_v${VERSION}_linux_amd64.tar.gz traefik
   sudo systemctl stop traefik
   sudo install -o root -g root -m 0755 traefik /usr/local/bin/traefik
   sudo setcap 'cap_net_bind_service=+ep' /usr/local/bin/traefik
   sudo systemctl start traefik
   traefik version
   ```
   👉 Explication : le `setcap` doit être réappliqué à chaque nouveau binaire.

4. Revenir en arrière :
   ```bash
   sudo systemctl stop traefik
   sudo cp -a /usr/local/bin/traefik.avant-maj /usr/local/bin/traefik
   sudo systemctl start traefik
   ```
   👉 Explication : les capacités sont conservées par `cp -a` ; sinon refaire `setcap`.

## 2. Production — Contrôles

Pilote d'abord, lecture des notes de migration, fenêtre approuvée, surveillance des journaux.

## 3. Production — Sécurité

- Toujours vérifier la somme de contrôle.
- Ne pas sauter plusieurs versions majeures.
- Conserver le binaire précédent jusqu'à validation.

## Validation et retour arrière

- **Validation** : `traefik version` affiche la version cible et les routeurs répondent.
- **Retour arrière** : restaurer le binaire et la configuration d'avant mise à jour.

## Si le problème n'est pas résolu

- [Traefik — Prérequis et limites](fiche-simple-vm-debian-13-traefik-prerequis-limites.md)
- [Traefik — Installer](fiche-simple-vm-debian-13-traefik-installer.md)
- [Traefik — Configurer (statique, dynamique, premier service)](fiche-simple-vm-debian-13-traefik-configurer.md)
- [Traefik — Sécuriser (TLS, redirection, pare-feu)](fiche-simple-vm-debian-13-traefik-securiser.md)
- [Traefik — Valider (recette)](fiche-simple-vm-debian-13-traefik-valider.md)
- [Traefik — Sauvegarder et restaurer](fiche-simple-vm-debian-13-traefik-sauvegarder-restaurer.md)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](../../../../../02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker.md)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](../../../../transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-configuration-statique.md)
