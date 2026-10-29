# Fiche_Simple_-_VM_Debian_13_Apache_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Apache HTTP Server
- **Catégorie** : serveur Web / Apache / Valider (recette)
- **Tags** : `debian13`, `apache`, `recette`

---

## Problème précis à résoudre

Prouver qu'Apache HTTP Server est correctement installé, configuré et sécurisé avant mise en service.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la syntaxe et l'état :
   ```bash
   sudo apache2ctl configtest
   systemctl is-active apache2
   systemctl is-enabled apache2
   ```
   👉 Explication : `Syntax OK` est attendu ; le service doit être actif et activé au démarrage.

2. Lister les hôtes virtuels et modules actifs :
   ```bash
   sudo apache2ctl -S
   sudo apache2ctl -M | sort
   ```
   👉 Explication : vérifier que seuls les modules nécessaires sont chargés.

3. Tester HTTP et HTTPS :
   ```bash
   curl -sI http://SITE.example.net/ | head -5
   curl -sI https://SITE.example.net/ | head -8
   ```
   👉 Explication : remplacer `SITE.example.net` (à remplacer) ; contrôler les codes, la redirection et les en-têtes.

4. Contrôler les ports et les journaux :
   ```bash
   sudo ss -tlnp | grep apache2
   sudo tail -n 20 /var/log/apache2/error.log
   ```
   👉 Explication : seuls les ports prévus écoutent ; aucune erreur récurrente.

## 2. Production — Contrôles

Consigner date, version (`apache2 -v`), opérateur et résultats ; activer la supervision (code HTTP, certificat, disque).

## 3. Production — Sécurité

- Ne pas exposer `server-status` hors localhost.
- Vérifier `ServerTokens Prod` et `ServerSignature Off`.
- Ne laisser aucun contenu de test.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis et consignés.
- **Retour arrière** : ne pas ouvrir au public ; revenir à la configuration sauvegardée.

## Si le problème n'est pas résolu

- [Apache — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Apache_Sauvegarder_Restaurer.md)
- [Apache — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Apache_Mettre_A_Jour.md)
- [Guide complet Apache Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/124_Deploiement_Apache_HTTP_Server_Debian_13.md)
- [Apache HTTP Server — documentation](https://httpd.apache.org/docs/2.4/)
