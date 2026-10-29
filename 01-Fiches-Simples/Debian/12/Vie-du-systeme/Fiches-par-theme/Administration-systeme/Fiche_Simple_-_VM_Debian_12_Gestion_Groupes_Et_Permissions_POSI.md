# 📄 VM_Debian_12_Utilisateurs_Gestion-Groupes-Et-Permissions.md

- **Environnement** : VM / LXC (Debian 12 / Ubuntu 24.04 / Linux)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Utilisateurs & Droits / Groupes & Permissions POSIX
- **Tags** : `[debian12]`, `[groupes]`, `[chmod]`, `[chown]`, `[permissions]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Créer des groupes d'utilisateurs d'entreprise, y ajouter ou supprimer des membres, et ajuster les autorisations POSIX (chmod, chown) et les bits spéciaux (SGID) sur les répertoires partagés.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer le groupe et ajouter le compte existant :
	```bash
	sudo groupadd --system grp_tssr_tech
	sudo usermod -aG grp_tssr_tech jdupont
	id jdupont
	```
	👉 Explication : Une nouvelle session est nécessaire pour que l'utilisateur récupère ses groupes.
2. Créer un nouveau répertoire de partage avec groupe propriétaire et bit SGID :
	`sudo install -d -o root -g grp_tssr_tech -m 2770 /srv/donnees_tssr`
	👉 Explication : Les nouveaux éléments héritent du groupe. Ne pas appliquer `chmod -R`/`chown -R` sans auditer le contenu existant.
3. Retirer un membre uniquement après validation de ses accès :
	`sudo gpasswd -d jdupont grp_tssr_tech`

---

## 🔒 3. Production — Façon Sécurisée (Hardening & SGID Bit)
1. Vérifier propriétaire et mode sans modifier récursivement les fichiers :
	```bash
	stat -c '%A %a %U:%G %n' /srv/donnees_tssr
	getfacl /srv/donnees_tssr
	```
2. Si le partage existe déjà, sauvegarder puis ajuster seulement les chemins qui doivent appartenir au groupe. Utiliser une ACL par défaut si les permissions applicatives nécessitent un contrôle plus fin ; vérifier le résultat avec un compte membre et un compte non membre.