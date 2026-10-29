---
title: "Squid & SquidGuard (Proxy + Filtrage avancé)"
description: "Squid est un serveur proxy open source utilisé pour filtrer, journaliser et accélérer les connexions HTTP/HTTPS. Il agit comme intermédiaire entre les clients et Internet."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Squid & SquidGuard (Proxy + Filtrage avancé)

## 📌 Présentation

**Squid** est un serveur proxy open source utilisé pour **filtrer, journaliser et accélérer** les connexions HTTP/HTTPS. Il agit comme **intermédiaire entre les clients et Internet**.

**SquidGuard** est un **plugin de filtrage URL** pour Squid. Il permet d’appliquer des politiques de filtrage plus poussées : **blocage par catégories**, listes noires, filtrage horaire, redirection personnalisée.

L’association des deux outils permet de mettre en place une **solution de proxy filtrant complète**, très utilisée en milieu scolaire, associatif et administratif.

---

## 🔧 Installation
### Debian / Ubuntu

```bash
sudo apt install squid squidguard
```

### Fichiers principaux

| Fichier | Description |
|--------|-------------|
| `/etc/squid/squid.conf` | Configuration de Squid (port, ACL, journalisation…) |
| `/etc/squidguard/squidGuard.conf` | Règles de filtrage, listes, redirections… |

---

## 🧰 Fonctions principales combinées

| Fonction | Fournie par |
|----------|-------------|
| Proxy HTTP/HTTPS | Squid |
| Mise en cache locale | Squid |
| ACL IP/méthode/URL | Squid |
| Filtrage par catégories | SquidGuard |
| Redirection personnalisée | SquidGuard |
| Filtrage horaire | SquidGuard |
| Logs détaillés | Squid + SquidGuard |

---

## ✏️ Exemple de configuration minimale
### Dans `squid.conf`

```conf
http_port 3128
url_rewrite_program /usr/bin/squidGuard -c /etc/squidguard/squidGuard.conf
http_access allow all
```

### Dans `squidGuard.conf
`
```conf
dbhome /var/lib/squidguard/db
logdir /var/log/squidguard

src profs {
    ip 192.168.52.10
}

dest interdit {
    domainlist interdit/domains
    urllist interdit/urls
}

acl {
    profs  pass !interdit all
    default pass none
    redirect http://127.0.0.1/bloque.html
}
```

> ⚠️ Penser à exécuter `squidGuard -C all` après modification pour recompiler les bases.

---

## 📂 Structure de dossiers SquidGuard (exemple)

```bash
/var/lib/squidguard/db/interdit/
  ├── domains   # domaines interdits (ex : facebook.com)
  └── urls      # URLs spécifiques à bloquer
```

---

## 🔎 Cas d’usage courant

- Blocage de réseaux sociaux, sites adultes ou e-commerce en entreprise
- Proxy pédagogique en milieu scolaire (catégories horaires)
- Surveillance et traçabilité de la navigation web
- Redirection vers une page informative en cas de tentative interdite

---

## ⚠️ Erreurs fréquentes

- Oublier de recompiler la base (`squidGuard -C all`) après modification
- Droits incorrects sur les fichiers de listes
- Ordre des ACL mal structuré (règles inefficaces)
- Ne pas intégrer squidGuard dans squid.conf (`url_rewrite_program` absent)

---

## ✅ Bonnes pratiques

- **Test en local** avant production (localhost ou réseau isolé)
- Mettre à jour régulièrement les listes noires (ex : [blacklists UT Capitole](https://dsi.ut-capitole.fr/blacklists/))
- Créer des **groupes d’IP ou d’utilisateurs** avec des politiques distinctes
- Surveiller les logs (`/var/log/squid/access.log`, `/var/log/squidguard/squidGuard.log`)
- Utiliser des **pages de blocage claires et personnalisées**

---

## 📚 Ressources complémentaires

- [Squid Documentation](http://www.squid-cache.org/Doc/)
- [SquidGuard Manual](http://www.squidguard.org/Doc/)
- [Blacklist UT Capitole](https://dsi.ut-capitole.fr/blacklists/)
- `man squid`, `man squidGuard`