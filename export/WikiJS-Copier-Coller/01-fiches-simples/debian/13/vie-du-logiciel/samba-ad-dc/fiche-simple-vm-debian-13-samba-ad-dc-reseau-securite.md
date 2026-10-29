# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Reseau_Securite.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / sécurité réseau

---

## Problème précis à résoudre

Limiter les flux AD aux clients et serveurs approuvés.

## 1. Hors-Production (Lab / Test / POC)

1. Autoriser entre clients approuvés et DC : DNS 53 TCP/UDP, Kerberos 88 TCP/UDP, NTP 123 UDP, RPC 135 TCP, LDAP 389 TCP/UDP, SMB 445 TCP, changement de mot de passe 464 TCP/UDP et RPC dynamique TCP.
   👉 Explication : ce sont les flux nécessaires à un DC.

2. N'ouvrir NetBIOS 137-139 et Global Catalog 3268/3269 que si le scénario les exige.
   👉 Explication : réduit la surface exposée.

3. Exécuter :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : liste les ports en écoute sur le DC pour comparer avec la politique voulue.

## 2. Production — Contrôles

Restreindre SSH et la console, activer les mises à jour Debian, surveiller les échecs Kerberos et les changements AD.

## 3. Production — Sécurité

- Ne jamais publier LDAP, SMB, RPC ou Kerberos sur Internet.
- N'activer aucune compatibilité faible (NTLM, algorithmes hérités) sans exception approuvée.
- Protéger bases et secrets du DC.

## Validation et retour arrière

- **Validation** : seuls les flux listés sont autorisés depuis les réseaux approuvés.
- **Retour arrière** : retirer les règles ajoutées au pare-feu.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13#6-reseau-et-securite)