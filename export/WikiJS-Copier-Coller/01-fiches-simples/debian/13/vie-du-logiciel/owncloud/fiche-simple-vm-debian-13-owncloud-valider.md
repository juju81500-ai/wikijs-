# Fiche_Simple_-_VM_Debian_13_ownCloud_Valider

- **Environnement** : VM Debian 13; ownCloud Infinite Scale (oCIS), binaire officiel, Nginx
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / ownCloud — Valider (recette)

---

## Problème précis à résoudre

Recetter ownCloud Infinite Scale : service, accès web, authentification et dépôt de fichier.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le service :
   ```bash
   systemctl is-active ocis nginx
   sudo ss -tlnp | grep -E ':(9200|443)\b'
   ```
   👉 Explication : oCIS doit écouter en 127.0.0.1:9200, Nginx sur 443.

2. Tester le point de découverte OIDC :
   ```bash
   curl -fsS https://OCIS.EXAMPLE.NET/.well-known/openid-configuration | head -c 300
   ```
   👉 Explication : une réponse JSON confirme que le service d'authentification est joignable.

3. Se connecter à l'interface Web avec le compte administrateur, créer un espace de test, déposer puis télécharger un fichier : chemin GUI.
   👉 Explication : valide la chaîne HTTPS/proxy/stockage ; vérifier aussi un client de synchronisation.

4. Lire les journaux :
   ```bash
   sudo journalctl -u ocis -n 30 --no-pager
   ```
   👉 Explication : pas d'erreur répétée.

## 2. Production — Contrôles

Consigner version et résultats, vérifier les quotas, supprimer l'espace et le compte de test.

## 3. Production — Sécurité

- Supprimer les comptes de test.
- Ne pas exposer les journaux (ils peuvent contenir des noms d'utilisateurs).

## Validation et retour arrière

- **Validation** : URL publique répond, connexion OK, fichier envoyé et relu.
- **Retour arrière** : revenir à la configuration précédente (proxy ou variables systemd) et redémarrer.

## Si le problème n'est pas résolu

- [ownCloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-prerequis-limites)
- [ownCloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-installer)
- [ownCloud Infinite Scale — documentation officielle](https://doc.owncloud.com/ocis/next/)
- [ownCloud — téléchargements](https://owncloud.com/download-server/)