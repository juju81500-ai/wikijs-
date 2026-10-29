# Fiche_Simple_-_VM_Debian_13_Caddy_Cadrer_Pilote.md

- **Environnement** : VM Debian 13 dédiée, service amont de test local
- **OS / Version** : Debian 13 Trixie; Caddy stable
- **Catégorie** : serveur Web / reverse proxy

---

## Problème précis à résoudre

Vérifier les prérequis DNS, service amont, TLS et réseau avant de publier un reverse proxy Caddy.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le DNS du nom et le service amont :
   ```bash
   getent hosts app.example.net
   curl -fsSI http://127.0.0.1:8080/
   ```
   👉 Explication : remplacer nom et port; le DNS doit pointer vers la VM et l'application amont répondre.

2. Vérifier les ports :
   ```bash
   sudo ss -ltnp | grep -E ':(80|443)\b' || echo "ports 80/443 libres"
   ```
   👉 Explication : Caddy doit pouvoir ouvrir 80 et 443 (challenges ACME).

3. Sauvegarder la configuration existante, si elle existe :
   ```bash
   sudo cp -a /etc/caddy /root/caddy.bak 2>/dev/null || echo "pas de configuration existante"
   ```
   👉 Explication : le périmètre exclut DNS, application amont et pare-feu.

## 2. Production — Contrôles

Définir les flux clients, la disponibilité, les politiques DNS, certificats, journaux, supervision, mises à jour et propriétaire applicatif avant publication.

## 3. Production — Sécurité

- Ne pas exposer l'application amont ni l'interface d'administration sans validation.
- Ne pas transmettre d'en-têtes d'identité sans vérifier les proxys de confiance.
- Ne pas ouvrir les ports 80/443 avant approbation réseau et vérification de leur usage par ACME.
- Conserver configuration et certificats privés dans leurs emplacements contrôlés.

## Validation et retour arrière

- **Validation** : domaine, amont, flux, certificat et plan de changement sont confirmés.
- **Arrêt** : ne pas publier si l'application cible ou le contrôle DNS appartient à un tiers non autorisé.

## Si le problème n'est pas résolu

- [Caddy — documentation](https://caddyserver.com/docs/)
- [Guide complet Caddy Debian 13](/02-fiches-completes/debian/13/installation-deploiement/91-deploiement-caddy-debian-13#1-perimetre-et-prerequis)