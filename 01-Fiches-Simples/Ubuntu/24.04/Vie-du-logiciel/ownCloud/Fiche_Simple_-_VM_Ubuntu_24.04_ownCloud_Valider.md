# Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Valider

- **Environnement** : VM Ubuntu Server 24.04; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / ownCloud — Valider (recette)
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Vérifier service, logs et URL TLS.

## 1. Hors-Production (Lab / Test / POC)

1. Valider (recette) :
   ```bash
   /usr/local/bin/ocis version
systemctl is-active ocis
sudo journalctl -u ocis -n 80 --no-pager
curl -fsSI https://CLOUD.EXAMPLE.NET/
   ```
   👉 Explication : Remplacer le FQDN; tester connexion puis un fichier non sensible depuis un client autorisé.


## 2. Production — Contrôles

Valider authentification, stockage et cycle de fichier depuis poste approuvé.

## 3. Production — Sécurité

Ne pas utiliser données sensibles ou comptes démo.

## Validation et retour arrière

- **Validation** : Service actif, TLS valide, scénario utilisateur réussi.
- **Retour arrière** : Fermer l’accès proxy et restaurer configuration validée.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Securiser.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)
