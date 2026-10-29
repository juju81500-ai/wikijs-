# Fiche_Simple_-_VM_Debian_13_Traefik_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Prérequis et limites
- **Tags** : `debian13`, `traefik`, `prerequis`

---

## Problème précis à résoudre

Cadrer l'installation de Traefik en service systemd sur un hôte Debian 13 (hors conteneur).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS, l'architecture et les ports :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   uname -m
   sudo ss -tlnp | grep -E ':(80|443)\b' || echo 'ports libres'
   ```
   👉 Explication : l'archive officielle dépend de l'architecture (`x86_64` → `amd64`).

2. Lister les services à publier :
   👉 Explication : adresse, port, protocole et nom DNS de chaque application ; Traefik les atteint via le fournisseur de fichiers (file provider).

3. Noter les limites :
   👉 Explication : cette série installe Traefik v3 en binaire sous systemd ; la variante Docker est dans la série `Docker/Traefik` du pack ; la version est à vérifier sur la page des publications officielles.

## 2. Production — Contrôles

Consigner DNS, certificats (ACME ou fichiers), responsable, fenêtre de maintenance, sauvegarde.

## 3. Production — Sécurité

- Ne pas utiliser le fournisseur Docker avec un accès non protégé au socket Docker.
- Ne pas exposer le tableau de bord.
- Prévoir la validation DNS ou le port 80 pour ACME.

## Validation et retour arrière

- **Validation** : ports libres, architecture et périmètre consignés.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [Traefik — Installer](Fiche_Simple_-_VM_Debian_13_Traefik_Installer.md)
- [Traefik — Configurer (statique, dynamique, premier service)](Fiche_Simple_-_VM_Debian_13_Traefik_Configurer.md)
- [Traefik — Sécuriser (TLS, redirection, pare-feu)](Fiche_Simple_-_VM_Debian_13_Traefik_Securiser.md)
- [Traefik — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Traefik_Valider.md)
- [Traefik — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Traefik_Sauvegarder_Restaurer.md)
- [Traefik — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Traefik_Mettre_A_Jour.md)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](../../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/06_Reverse_Proxy_Traefik_v31_LetsEncrypt_Docker.md)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](../../../../Transverses/Docker/Traefik/Fiche_Simple_-_Docker_Conteneur_Traefik_Configuration_Statique.md)
