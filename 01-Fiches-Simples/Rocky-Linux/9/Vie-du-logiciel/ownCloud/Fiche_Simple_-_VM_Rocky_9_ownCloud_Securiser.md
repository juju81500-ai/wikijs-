# Fiche_Simple_-_VM_Rocky_9_ownCloud_Securiser

- **Environnement** : VM Rocky Linux 9; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / ownCloud — Sécuriser
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Restreindre accès oCIS au reverse proxy HTTPS.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser :
   ```bash
   sudo ss -lntp | grep -E ":(443|9200)\b" || true
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
   ```
   👉 Explication : `ADMIN_CIDR` est un placeholder. Ouvrir HTTPS uniquement; 9200 reste au proxy local.


## 2. Production — Contrôles

Configurer certificat TLS valide et contrôler qu’aucune règle n’expose le backend.

## 3. Production — Sécurité

Protéger certificats/environnement, limiter sources et garder SELinux/pare-feu actifs.

## Validation et retour arrière

- **Validation** : HTTPS valide et 9200 non accessible depuis réseaux non autorisés.
- **Retour arrière** : Rétablir les règles précédentes sans couper l’administration.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Rocky_9_ownCloud_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Rocky_9_ownCloud_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Rocky_9_ownCloud_Configurer.md)
- [Valider (recette)](Fiche_Simple_-_VM_Rocky_9_ownCloud_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Rocky_9_ownCloud_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Rocky_9_ownCloud_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)
