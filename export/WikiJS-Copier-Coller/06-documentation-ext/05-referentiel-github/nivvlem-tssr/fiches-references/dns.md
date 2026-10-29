# DNS (Domain Name System)

## 📌 Présentation

Le DNS est le système qui permet de traduire des noms de domaine lisibles (comme `www.google.com`) en adresses IP (`142.250.74.36`). Il constitue une **brique essentielle d’Internet** et des réseaux d’entreprise. Sans DNS, les utilisateurs devraient taper des adresses IP à la place des noms.

---

## 🧱 Types de serveurs DNS

| Type | Rôle |
|------|------|
| **Résolveur** (client) | Interroge un serveur DNS pour résoudre un nom |
| **Cache DNS** | Garde temporairement les résultats pour accélérer les réponses |
| **Serveur faisant autorité** | Contient les enregistrements officiels d’un domaine |
| **Serveur racine** | Point de départ de toute résolution DNS |

---

## 🧰 Commandes utiles
### 🔎 Diagnostics Linux / Windows

| Commande | Usage |
|----------|-------|
| `nslookup nom_domaine` | Résolution de nom (Linux/Windows) |
| `dig nom_domaine` | Requête DNS détaillée (Linux) |
| `host nom_domaine` | Requête rapide (Linux) |
| `ipconfig /displaydns` | Voir le cache DNS (Windows) |
| `ipconfig /flushdns` | Vider le cache DNS (Windows) |
| `systemd-resolve --status` | Voir les serveurs DNS (Linux systemd) |

## 🧾 Types d'enregistrements courants

| Type | Description | Exemple |
|------|-------------|---------|
| `A` | Lien entre nom et IPv4 | `web.entreprise.local → 192.168.1.20` |
| `AAAA` | Lien vers une IPv6 | `srv6 → fe80::1` |
| `CNAME` | Alias vers un autre nom DNS | `intranet → web.local` |
| `MX` | Serveur mail du domaine | `mail.entreprise.com` |
| `PTR` | Résolution inverse IP → nom | `192.168.1.20 → web.entreprise.local` |
| `NS` | Déclare les serveurs faisant autorité pour un domaine | |
| `TXT` | Texte libre (souvent SPF, DKIM, vérifications) | |

## ⚙️ Configuration BIND9 (Linux)
Fichier principal : `/etc/bind/named.conf.local`

### Exemple de zone directe :

```dns
zone "entreprise.local" {
  type master;
  file "/etc/bind/zones/db.entreprise.local";
};
```

### Exemple d'enregistrement dans la zone :

```dns
web   IN   A     192.168.1.20
mail  IN   A     192.168.1.21
@     IN   MX 10 mail.entreprise.local.
```

---

## 🔎 Cas d’usage courant

- Résolution de noms internes dans un réseau d’entreprise (ex : `srv-fichiers.local`)
- Hébergement de son propre DNS pour un domaine public ou intranet
- Création de noms d’alias (`CNAME`) pour simplifier les URLs
- Mise en place de messagerie d’entreprise (`MX`, `SPF`, `DMARC`)

---

## ⚠️ Erreurs fréquentes

- Mauvais TTL : trop long → lente propagation ; trop court → surcharge
- Oublier le point final dans les noms de domaine complets (`entreprise.local.`)
- Conflits d’IP si plusieurs A records pointent vers des hôtes différents
- Zones mal déléguées (NS manquants ou mal configurés)

---

## ✅ Bonnes pratiques

- Structurer son plan de nommage dès le départ (ex : `srv-ldap`, `nas-bureau`, `web-prod`…)
- Répliquer les zones DNS (primaire/secondaire) pour tolérance de panne
- Sécuriser son DNS (éviter le transfert de zone public, journaliser les requêtes)
- Documenter tous les enregistrements manuels, surtout PTR et MX

---

## 📚 Ressources complémentaires

- `man dig`, `man named`
- [ISC BIND9 Documentation](https://bind9.readthedocs.io/en/latest/)
- [DigitalOcean – DNS Explained](https://www.digitalocean.com/community/tutorials/an-introduction-to-dns-terminology-components-and-concepts)