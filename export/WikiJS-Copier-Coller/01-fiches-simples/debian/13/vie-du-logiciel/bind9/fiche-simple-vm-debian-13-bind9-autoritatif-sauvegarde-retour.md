# Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Sauvegarde_Retour.md

- **Environnement** : VM Debian 13 avec bind9 autoritatif
- **OS / Version** : Debian 13 Trixie; paquets bind9 de la distribution
- **Catégorie** : dns / sauvegarde

---

## Problème précis à résoudre

Sauvegarder la configuration BIND et savoir restaurer sans réinstaller.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver la configuration et les zones :
   ```bash
   sudo tar -czf "$HOME/bind-etc-$(date +%F).tar.gz" /etc/bind
   ```
   👉 Explication : l'archive contient configuration et zones; la stocker dans un emplacement protégé.

2. Restaurer en cas d'échec (nom d'archive à remplacer par le vôtre) :
   ```bash
   sudo tar -xzf "$HOME/bind-etc-2026-10-27.tar.gz" -C /
   ```
   👉 Explication : on remet les fichiers précédents à leur place.

3. Revalider avant rechargement :
   ```bash
   sudo named-checkconf -z /etc/bind/named.conf
   sudo systemctl reload bind9
   ```
   👉 Explication : on contrôle puis on recharge; ne jamais purger le paquet pour une erreur de zone.

## 2. Production — Contrôles

Tester la restauration dans un environnement isolé et comparer les réponses DNS attendues; sans cela, la sauvegarde n'est pas vérifiée.

## 3. Production — Sécurité

- Protéger l'archive : elle contient la topologie interne.
- Ne pas conserver de sauvegardes accessibles à tous.

## Validation et retour arrière

- **Validation** : Restauration testée en environnement isolé avec réponses DNS identiques.
- **Retour arrière** : Remettre l'archive précédente; supprimer l'archive de test si elle est inutile.

## Si le problème n'est pas résolu

- [ISC BIND 9 — Configurations and Zone Files](https://bind9.readthedocs.io/en/latest/chapter3.html)
- [Debian — paquet bind9 Trixie](https://packages.debian.org/trixie/bind9)
- [Guide complet BIND9 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13#6-sauvegarde-et-retour-arriere)