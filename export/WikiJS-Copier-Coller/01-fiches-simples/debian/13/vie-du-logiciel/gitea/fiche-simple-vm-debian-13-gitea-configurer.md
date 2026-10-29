# Fiche_Simple_-_VM_Debian_13_Gitea_Configurer

- **Environnement** : VM Debian 13 isolée; domaine et stockage définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration

---

## Problème précis à résoudre

Configurer URL canonique, écoute locale et compte administrateur pour une première instance isolée.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une configuration protégée
   ```bash
   sudo install -o root -g git -m 0640 /dev/null /etc/gitea/app.ini
   sudoedit /etc/gitea/app.ini
   ```
   👉 Explication : éditer localement sans placer de secret dans l’historique.

2. Fixer FQDN et écoute backend
   ```ini
   [server]
   DOMAIN = forge.example.com
   ROOT_URL = https://forge.example.com/
   HTTP_ADDR = 127.0.0.1
   HTTP_PORT = 3000
   
   [repository]
   ROOT = /var/lib/gitea/data/gitea-repositories
   ```
   👉 Explication : remplacer forge.example.com par le FQDN à remplacer; backend lié à localhost pour n’être servi que par le proxy.

3. Activer et contrôler le service
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now gitea
   sudo systemctl --no-pager status gitea
   ```
   👉 Explication : l’unité doit avoir été relue et ses chemins confirmés avant activation.

4. Créer le premier compte depuis un réseau d’administration
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitea.com/installation/install-from-binary
   ```
   👉 Explication : ne pas saisir de mot de passe dans le terminal, une fiche ou une capture. Détail à confirmer dans la documentation officielle avant application : Ouvrir l’assistant sur le FQDN approuvé depuis le réseau d’administration. Créer un compte nominatif et fermer l’inscription publique après initialisation.

## 2. Production — Contrôles

Valider URL, backend, droits de fichiers, mode d’inscription et configuration de base avant import de dépôts.

## 3. Production — Sécurité

- Limiter `/etc/gitea/app.ini` au groupe du service.
- N’utiliser ni compte partagé ni inscription publique non approuvée.
- Ne pas stocker jetons ou clés privées dans les dépôts.

## Validation et retour arrière

- **Validation** : Le service est actif, écoute localement et le compte nominatif ouvre l’URL canonique.
- **Retour arrière** : Restaurer la copie protégée de `app.ini` et l’unité précédente puis redémarrer.

## Si le problème n'est pas résolu

- [Gitea — installation depuis un binaire](https://docs.gitea.com/installation/install-from-binary)
- [Gitea — configuration](https://docs.gitea.com/administration/config-cheat-sheet)
- [Gitea — sauvegarde/restauration](https://docs.gitea.com/administration/backup-and-restore)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-prerequis-limites>)