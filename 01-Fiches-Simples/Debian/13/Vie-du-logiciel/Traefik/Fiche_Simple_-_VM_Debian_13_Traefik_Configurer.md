# Fiche_Simple_-_VM_Debian_13_Traefik_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Configurer (statique, dynamique, premier service)
- **Tags** : `debian13`, `traefik`, `configuration`

---

## Problème précis à résoudre

Écrire la configuration statique de Traefik, un routeur dynamique vers une application locale et démarrer le service.

## 1. Hors-Production (Lab / Test / POC)

1. Créer la configuration statique :
   ```bash
   sudo tee /etc/traefik/traefik.yml >/dev/null <<'EOF'
   entryPoints:
     web:
       address: ":80"
     websecure:
       address: ":443"
   providers:
     file:
       directory: /etc/traefik/dynamic
       watch: true
   log:
     level: INFO
     filePath: /var/log/traefik/traefik.log
   EOF
   sudo chown root:traefik /etc/traefik/traefik.yml && sudo chmod 0640 /etc/traefik/traefik.yml
   ```
   👉 Explication : aucun tableau de bord ni API n'est activé.

2. Déclarer un routeur et un service :
   ```bash
   sudo tee /etc/traefik/dynamic/app.yml >/dev/null <<'EOF'
   http:
     routers:
       app:
         rule: "Host(`APP.example.net`)"
         entryPoints: [web]
         service: app
     services:
       app:
         loadBalancer:
           servers:
             - url: "http://127.0.0.1:PORT_APP"
   EOF
   ```
   👉 Explication : remplacer `APP.example.net` et `PORT_APP` (à remplacer) ; le fichier est rechargé automatiquement.

3. Démarrer et contrôler :
   ```bash
   sudo systemctl enable --now traefik
   systemctl status traefik --no-pager
   sudo tail -n 20 /var/log/traefik/traefik.log
   ```
   👉 Explication : aucune erreur de configuration ne doit apparaître.

4. Tester le routage :
   ```bash
   curl -s -H 'Host: APP.example.net' http://127.0.0.1/ | head -3
   ```
   👉 Explication : le contenu de l'application doit être retourné.

## 2. Production — Contrôles

Séparer configuration statique (rarement modifiée) et dynamique (versionnée dans Git) ; relire avant chaque déploiement.

## 3. Production — Sécurité

- Ne pas activer `api.insecure`.
- Droits `0640 root:traefik` sur la configuration.
- Ne publier que les routeurs voulus.

## Validation et retour arrière

- **Validation** : le routage fonctionne et le journal est propre.
- **Retour arrière** : supprimer `/etc/traefik/dynamic/app.yml` (rechargé à chaud) ou arrêter le service.

## Si le problème n'est pas résolu

- [Traefik — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Traefik_Prerequis_Limites.md)
- [Traefik — Installer](Fiche_Simple_-_VM_Debian_13_Traefik_Installer.md)
- [Traefik — Sécuriser (TLS, redirection, pare-feu)](Fiche_Simple_-_VM_Debian_13_Traefik_Securiser.md)
- [Traefik — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Traefik_Valider.md)
- [Traefik — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Traefik_Sauvegarder_Restaurer.md)
- [Traefik — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Traefik_Mettre_A_Jour.md)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](../../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/06_Reverse_Proxy_Traefik_v31_LetsEncrypt_Docker.md)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](../../../../Transverses/Docker/Traefik/Fiche_Simple_-_Docker_Conteneur_Traefik_Configuration_Statique.md)
