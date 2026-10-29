---
title: "Déployer Caddy sur Debian 13"
description: "Fiche simple : [cadrer le pilote Caddy](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Caddy/FicheSimple-VMDebian13CaddyCadrerPilote.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["caddy", "debian13", "reverse-proxy", "https", "tls", "systemd"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer Caddy sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; paquet de la branche stable du dépôt officiel Caddy
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : service Caddy systemd, reverse proxy HTTPS d'un service local, validation de configuration et retour arrière
- **Catégorie** : serveur Web / reverse proxy
- **Tags** : `caddy`, `debian13`, `reverse-proxy`, `https`, `tls`, `systemd`

## 1. Périmètre et prérequis

Fiche simple : [cadrer le pilote Caddy](/01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-cadrer-pilote).

Cette procédure installe Caddy depuis son dépôt APT officiel et publie un service HTTP local derrière un nom DNS. Elle ne configure pas de DNS, d'application amont, de SSO, de haute disponibilité ni de politique WAF.

Prérequis : VM Debian 13 dédiée ou approuvée, nom de domaine contrôlé, DNS public/interne adapté, service amont actif, accès administrateur et sauvegarde des fichiers de configuration. Pour un certificat ACME public, le nom doit résoudre vers cette machine et les challenges nécessaires doivent être joignables. Ne jamais exposer le port de gestion ou une application amont non protégée.

## 2. Installer depuis le dépôt officiel

Fiche simple : [installer Caddy depuis le dépôt officiel](/01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-installer).

Examiner d'abord la configuration de dépôts existante, puis installer les prérequis et suivre les instructions APT de Caddy pour Debian/Ubuntu :

```bash
sudo apt update
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl gnupg
sudo install -d -m 0755 /usr/share/keyrings
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo chmod o+r /usr/share/keyrings/caddy-stable-archive-keyring.gpg /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
apt-cache policy caddy
sudo apt install caddy
```

Vérifier la version, son origine et le service :

```bash
caddy version
systemctl status caddy --no-pager
```

Pour la production, consigner et maîtriser la version par le processus de mise à jour de l'organisation. Ne pas importer de binaire d'origine inconnue ni désactiver la vérification des signatures APT.

## 3. Configurer un reverse proxy local

Fiche simple : [configurer le reverse proxy pilote](/01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-configurer-proxy).

Confirmer que l'application amont écoute sur `127.0.0.1:8080` (ou adapter l'adresse/port). Sauvegarder la configuration actuelle avant modification :

```bash
sudo cp -a /etc/caddy/Caddyfile /etc/caddy/Caddyfile.pre-change
sudoedit /etc/caddy/Caddyfile
```

Exemple à adapter au nom DNS et à l'application :

```caddyfile
app.example.net {
    reverse_proxy 127.0.0.1:8080
}
```

Caddy configure automatiquement HTTPS lorsque le nom de domaine et les challenges de certificat sont valides. Ne pas configurer un domaine de production vers un service amont de test, ni transmettre des en-têtes d'identité sans vérifier l'application et le proxy de confiance.

Valider le fichier avant de recharger :

```bash
sudo caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
sudo systemctl reload caddy
sudo systemctl --no-pager status caddy
```

Si l'application n'écoute pas sur loopback, choisir un réseau dédié et des règles d'accès appropriées. Ouvrir seulement les ports entrants nécessaires (généralement TCP/80 et TCP/443 pour HTTP-01/TLS-ALPN-01), après vérification du gestionnaire de pare-feu actif.

## 4. Vérifier le service

Fiche simple : [valider le service et TLS](/01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-valider-service).

```bash
curl -fsSI https://app.example.net/
sudo journalctl -u caddy --since '15 minutes ago' --no-pager
sudo ss -ltnp
```

Confirmer le certificat, le nom, l'expiration, le code HTTP et le comportement de l'application. Vérifier que le service amont n'est pas accessible depuis des réseaux non autorisés et que les journaux ne contiennent pas de secrets.

## 5. Certificats, permissions et maintenance

Fiche simple : [contrôler certificats et maintenance](/01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-maintenance).

- Laisser Caddy gérer son stockage de certificats par son service et son compte système; ne pas déplacer ni exposer ce stockage sans procédure documentée.
- Limiter les permissions des fichiers de configuration et des journaux, et éviter d'y inscrire des clés privées.
- Mettre à jour Caddy via APT après lecture des notes de version et validation dans un environnement pilote.
- Sauvegarder le Caddyfile et tout certificat/configuration géré manuellement; les certificats ACME peuvent généralement être renouvelés, mais la dépendance DNS et la disponibilité doivent être documentées.

## 6. Retour arrière

Fiche simple : [préparer le retour arrière Caddy](/01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-retour-arriere).

Si la validation ou le rechargement échoue, remettre le Caddyfile sauvegardé, valider, puis recharger :

```bash
sudo cp -a /etc/caddy/Caddyfile.pre-change /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
sudo systemctl reload caddy
```

En cas d'indisponibilité persistante, vérifier les journaux Caddy et l'application amont. Pour une mise à niveau de paquet problématique, réinstaller une version précédente uniquement si elle est encore disponible et approuvée dans les dépôts; tester aussi la compatibilité des fichiers de configuration.

## Sources

- [Caddy — Installation](https://caddyserver.com/docs/install)
- [Caddy — Installation Debian/Ubuntu](https://caddyserver.com/docs/install#debian-ubuntu-raspbian)
- [Caddy — Directive reverse_proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)
- [Caddy — HTTPS automatique](https://caddyserver.com/docs/automatic-https)
- [Caddy — Commande validate](https://caddyserver.com/docs/command-line#caddy-validate)
- [Debian — notes de publication Trixie](https://www.debian.org/releases/trixie/)

La version du dépôt, l'émission ACME et le proxy vers le service réel doivent être validés sur un système pilote avant publication.