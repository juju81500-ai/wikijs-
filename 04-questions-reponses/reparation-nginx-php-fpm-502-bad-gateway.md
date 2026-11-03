# Réparation : Nginx renvoie une erreur 502 avec PHP-FPM

- **Périmètre** : Nginx et PHP-FPM sous Linux
- **Tags** : `reparation`, `nginx`, `php-fpm`, `502`, `web`

## 1. Confirmer l'origine

```bash
sudo nginx -t
sudo systemctl --no-pager --full status nginx
systemctl list-units --type=service 'php*-fpm.service'
ls -l /run/php/
sudo journalctl -u nginx --since '-15 minutes' --no-pager
```

Un 502 indique généralement que Nginx ne peut pas joindre son upstream. Confirmer dans le journal si l'erreur mentionne un socket absent, un refus de connexion ou un délai dépassé.

## 2. Comparer socket et service

```bash
sudo grep -Rni 'fastcgi_pass' /etc/nginx/sites-enabled/
sudo ss -xl | grep php
```

Le chemin déclaré dans `fastcgi_pass` doit correspondre au socket présent sous `/run/php/` et au pool PHP-FPM démarré. Si le socket est absent, consulter `systemctl status` et `journalctl` du service PHP-FPM avant toute modification.

Sauvegarder le fichier Nginx puis corriger uniquement le chemin ou le nom du service. Valider avant rechargement :

```bash
sudo nginx -t
sudo systemctl restart php8.4-fpm
sudo systemctl reload nginx
```

Remplacer `php8.4-fpm` par le service effectivement installé ; ne pas copier ce nom sans vérifier la version locale.

## 3. Contrôler et revenir en arrière

```bash
curl -sS -o /dev/null -w '%{http_code}\n' -H 'Host: app.example.net' http://127.0.0.1/
sudo journalctl -u nginx --since '-5 minutes' --no-pager
```

Attendre le code HTTP prévu par l'application (souvent 200 ou une redirection). Si `nginx -t` échoue ou si le site reste indisponible, restaurer la sauvegarde, valider de nouveau puis recharger Nginx. Ne pas publier `phpinfo()` ou les messages d'erreur PHP en production.