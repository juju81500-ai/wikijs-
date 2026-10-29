# DMZ (Demilitarized Zone – Zone démilitarisée réseau)

## 📌 Présentation

Une **DMZ (Demilitarized Zone)** est une **zone réseau isolée**, positionnée entre un réseau interne sécurisé (LAN) et un réseau non fiable (Internet). Elle héberge des services accessibles depuis Internet (ex : serveurs web, mail, DNS), tout en limitant l’accès direct au réseau interne.

Elle constitue une **mesure de sécurité périmétrique** essentielle pour segmenter l’infrastructure et contenir les attaques potentielles.

---

## 🧱 Architecture type

```
[Internet] <---> [Firewall externe] <---> [DMZ] <---> [Firewall interne] <---> [LAN interne]
```

Ou avec un seul firewall (ex : pfSense) :

```
[Internet] <---> [WAN] 
                      |
               [DMZ Interface]
                      |
                   [LAN]
```

## 🧩 Services typiques dans une DMZ

| Service | Exemple |
|---------|---------|
| HTTP/HTTPS | Serveur web (Apache, Nginx) |
| SMTP | Relai de messagerie (Postfix, Exim) |
| DNS | Serveur DNS public |
| VPN | Point d’entrée OpenVPN, WireGuard… |

---

## 🔐 Objectif de la DMZ

- **Isoler les services exposés** : empêcher qu’un attaquant compromette le LAN
- **Limiter les flux autorisés** : pare-feu entre chaque zone avec des règles strictes
- **Surveiller l’activité** : journalisation des accès, alertes, IDS/IPS

---

## 🔎 Cas d’usage courant

- Héberger un site web public en **évitant l’exposition du réseau interne**
- Mettre un relai mail SMTP externe (antispam) entre Internet et LAN
- Tester des services sans compromettre la production

---

## ⚠️ Erreurs fréquentes

- Autoriser des connexions non contrôlées entre DMZ et LAN
- Utiliser des mêmes credentials/services entre DMZ et interne
- Ne pas cloisonner physiquement/virtuellement les zones (VLAN mal configuré)
- Laisser des ports ouverts sans analyse du besoin réel

---

## ✅ Bonnes pratiques

- **Segmenter physiquement ou avec VLANs** (sur switch manageable)
- Appliquer la politique de **moindre privilège** (accès restreint, règles précises)
- Journaliser les accès et surveiller les logs (syslog, Suricata…)
- Utiliser des **reverse proxies ou pare-feu applicatifs** (ex : HAProxy, Nginx, WAF)
- Tester la résilience de la DMZ avec des outils comme `nmap`, `nikto`, `fail2ban`

---

## 📚 Ressources complémentaires

- [RFC 1918 – Private IP ranges](https://datatracker.ietf.org/doc/html/rfc1918)
- OWASP Secure Deployment Guidelines