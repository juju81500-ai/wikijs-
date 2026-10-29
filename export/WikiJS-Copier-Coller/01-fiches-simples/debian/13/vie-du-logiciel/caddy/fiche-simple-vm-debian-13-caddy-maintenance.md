# Fiche_Simple_-_VM_Debian_13_Caddy_Maintenance.md

- **Environnement** : serveur Caddy Debian 13 en pilote avant production
- **OS / Version** : Debian 13; Caddy stable
- **Catégorie** : serveur Web / maintenance et certificats

---

## Problème précis à résoudre

Maintenir le Caddyfile, les certificats et le paquet sans perdre le renouvellement ou exposer des clés.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les permissions de la configuration :
   ```bash
   ls -l /etc/caddy
   sudo ls -ld /var/lib/caddy
   ```
   👉 Explication : le stockage des certificats reste géré par le service Caddy; ne pas le déplacer ni l'exposer.

2. Sauvegarder le Caddyfile :
   ```bash
   sudo cp -a /etc/caddy/Caddyfile /root/Caddyfile.$(date +%F)
   ```
   👉 Explication : sauvegarder aussi tout certificat géré manuellement; les certificats ACME se renouvellent, mais dépendent du DNS et des ports.

3. Mettre à jour après lecture des notes de version et test sur un pilote :
   ```bash
   apt list --upgradable 2>/dev/null | grep caddy
   sudo apt install --only-upgrade caddy
   caddy version
   ```
   👉 Explication : puis revalider avec `curl -fsSI https://app.example.net/`.

## 2. Production — Contrôles

Définir responsable de certificat, alertes de renouvellement, politique de rotation, sauvegarde, maintenance APT et procédure d'interruption.

## 3. Production — Sécurité

- Ne pas déplacer ni exposer le stockage ACME interne sans procédure éditeur documentée.
- Ne pas archiver les clés privées dans un dépôt ordinaire ou des journaux.
- Ne pas mettre à jour directement un service de production sans pilote et fenêtre approuvée.
- Protéger la configuration, les journaux et les accès de l'utilisateur de service.

## Validation et retour arrière

- **Validation** : certificats renouvelables, permissions minimales, sauvegarde récupérable et version maîtrisée.
- **Retour arrière** : restaurer le Caddyfile antérieur, valider et recharger; ne pas supposer qu'un certificat ACME périmé peut être récupéré depuis une copie quelconque.

## Si le problème n'est pas résolu

- [Caddy — installation et mises à jour](https://caddyserver.com/docs/install)
- [Caddy — HTTPS automatique](https://caddyserver.com/docs/automatic-https)
- [Guide complet Caddy Debian 13](/02-fiches-completes/debian/13/installation-deploiement/91-deploiement-caddy-debian-13#5-certificats-permissions-et-maintenance)