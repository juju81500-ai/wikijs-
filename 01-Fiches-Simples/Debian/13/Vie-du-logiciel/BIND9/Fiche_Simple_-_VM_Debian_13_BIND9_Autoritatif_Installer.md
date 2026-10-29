# Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Installer.md

- **Environnement** : VM Debian 13, paquet bind9 Debian
- **OS / Version** : Debian 13 Trixie; paquets bind9 de la distribution
- **Catégorie** : dns / installation
- **Tags** : `debian13`, `bind9`, `apt`, `systemd`

---

## Problème précis à résoudre

Installer le paquet bind9 Debian et démarrer le service.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt update
   sudo apt install bind9 bind9-utils dnsutils
   ```
   👉 Explication : `bind9` est le serveur, `bind9-utils` fournit `named-checkconf` et `named-checkzone`, `dnsutils` fournit `dig`.

2. Activer et démarrer le service :
   ```bash
   sudo systemctl enable --now bind9
   sudo systemctl --no-pager status bind9
   ```
   👉 Explication : le service doit être `active (running)` et démarrer au boot.

3. Confirmer la version et l'écoute :
   ```bash
   named -V
   ip -br address
   sudo ss -lntup '( sport = :53 )'
   ```
   👉 Explication : on contrôle la version installée et que `named` écoute sur le port 53. Ne pas ajouter de chroot ni changer récursivement les propriétaires de `/etc/bind`.

## 2. Production — Contrôles

Utiliser uniquement les dépôts Debian approuvés, suivre les mises à jour de sécurité et documenter la version installée.

## 3. Production — Sécurité

- Ne pas installer BIND depuis une source tierce non revue.
- Ne pas modifier récursivement les propriétaires de `/etc/bind`.
- Conserver la protection AppArmor du paquet.

## Validation et retour arrière

- **Validation** : `systemctl status bind9` actif et `named -V` affiche la version attendue.
- **Retour arrière** : Désactiver le service avec `sudo systemctl disable --now bind9`; ne pas purger le paquet pour corriger une erreur de configuration.

## Si le problème n'est pas résolu

- [Debian — paquet bind9 Trixie](https://packages.debian.org/trixie/bind9)
- [ISC BIND 9 — Manpages](https://bind9.readthedocs.io/en/latest/manpages.html)
- [Guide complet BIND9 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/63_Deploiement_BIND9_Autoritatif_Debian_13.md#2-installer-le-paquet-debian)
