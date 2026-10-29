# Fiche_Simple_-_VM_Debian_13_Caddy_Retour_Arriere.md

- **Environnement** : VM Debian 13, Caddyfile sauvegardé et paquet provenant du dépôt approuvé
- **OS / Version** : Debian 13; Caddy stable
- **Catégorie** : serveur Web / gestion du changement
- **Tags** : `debian13`, `caddy`, `rollback`, `configuration`, `changement`

---

## Problème précis à résoudre

Annuler une modification de reverse proxy ou traiter une mise à niveau défectueuse sans laisser un amont exposé.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer le Caddyfile sauvegardé :
   ```bash
   sudo cp -a /etc/caddy/Caddyfile.pre-change /etc/caddy/Caddyfile
   ```
   👉 Explication : revient à la configuration précédente.

2. Valider puis recharger :
   ```bash
   sudo caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
   sudo systemctl reload caddy
   ```
   👉 Explication : ne pas recharger si la validation échoue.

3. Contrôler :
   ```bash
   systemctl status caddy --no-pager
   curl -fsSI https://app.example.net/
   ```
   👉 Explication : confirmer le retour du service.

## 2. Production — Contrôles

Exécuter le retour arrière dans une fenêtre approuvée avec propriétaire applicatif, réseau et certificat présents; consigner les versions et résultats avant/après.

## 3. Production — Sécurité

- En cas d'incident, isoler la publication via le mécanisme réseau approuvé sans exposer directement l'application.
- Ne pas restaurer une configuration non revue ni une clé privée depuis une sauvegarde non vérifiée.
- Ne pas purger les journaux nécessaires à l'analyse.
- Ne pas réessayer une mise à niveau ou un rechargement en boucle.

## Validation et retour arrière

- **Validation** : Caddy actif, TLS vérifié, application et flux conformes, aucun port inattendu.
- **Retour arrière** : si la restauration échoue, garder le service isolé et escalader au propriétaire; ne pas improviser une configuration de production.

## Si le problème n'est pas résolu

- [Caddy — commande validate](https://caddyserver.com/docs/command-line#caddy-validate)
- [Caddy — journalisation](https://caddyserver.com/docs/caddyfile/directives/log)
- [Guide complet Caddy Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/91_Deploiement_Caddy_Debian_13.md#6-retour-arriere)
