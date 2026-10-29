# Fiche_Simple_-_VM_Debian_13_HAProxy_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Sécuriser (TLS, pare-feu, durcissement)

---

## Problème précis à résoudre

Activer HTTPS sur HAProxy, limiter l'exposition et durcir la configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Lab : générer un certificat auto-signé et le concaténer clé + certificat :
   ```bash
   sudo install -d -m 0750 -o root -g haproxy /etc/haproxy/certs
   sudo openssl req -x509 -nodes -newkey rsa:3072 -days 90 -keyout /etc/haproxy/certs/SITE.key -out /etc/haproxy/certs/SITE.crt -subj '/CN=SITE.example.net'
   sudo sh -c 'cat /etc/haproxy/certs/SITE.crt /etc/haproxy/certs/SITE.key > /etc/haproxy/certs/SITE.pem'
   sudo chown root:haproxy /etc/haproxy/certs/*
   sudo chmod 0640 /etc/haproxy/certs/*
   ```
   👉 Explication : remplacer `SITE` (à remplacer) ; en production, utiliser un certificat d'une AC (HAProxy attend un `.pem` contenant certificat, chaîne et clé).

2. Ajouter le frontend HTTPS et la redirection :
   ```bash
   sudo tee -a /etc/haproxy/haproxy.cfg >/dev/null <<'EOF'

   frontend fe_https
       bind *:443 ssl crt /etc/haproxy/certs/SITE.pem alpn h2,http/1.1 ssl-min-ver TLSv1.2
       mode http
       http-response set-header Strict-Transport-Security "max-age=31536000"
       default_backend be_app
   EOF
   sudo sed -i 's|^    bind \*:80$|    bind *:80\n    http-request redirect scheme https unless { ssl_fc }|' /etc/haproxy/haproxy.cfg
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg && sudo systemctl reload haproxy
   ```
   👉 Explication : vérifier le fichier après le `sed` : la redirection ne doit apparaître que dans `fe_http` ; n'activer HSTS qu'une fois HTTPS stable.

3. Filtrer le réseau :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   ```
   👉 Explication : n'ouvrir que 80 et 443 ; ne pas ouvrir le port des statistiques.

4. Contrôler l'utilisateur d'exécution :
   ```bash
   ps -o user,group,cmd -C haproxy
   ```
   👉 Explication : HAProxy abandonne les privilèges (`user haproxy` dans `global`) après l'ouverture des ports.

## 2. Production — Contrôles

Certificats d'AC avec renouvellement supervisé, TLS 1.2 minimum, statistiques non exposées, journaux centralisés.

## 3. Production — Sécurité

- Clés en `0640` root:haproxy, jamais dans un dépôt ni un ticket.
- Aucun mot de passe en clair dans la configuration versionnée.
- Limiter l'administration SSH au réseau d'administration.

## Validation et retour arrière

- **Validation** : `curl -kI https://SITE.example.net/` répond, HTTP redirige vers HTTPS.
- **Retour arrière** : retirer le frontend HTTPS et la redirection, ou restaurer `haproxy.cfg.orig`, valider, recharger.

## Si le problème n'est pas résolu

- [HAProxy — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-prerequis-limites)
- [HAProxy — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-installer)
- [HAProxy — Configurer un frontend et des backends](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-configurer)
- [HAProxy — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-valider)
- [HAProxy — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-sauvegarder-restaurer)
- [HAProxy — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-mettre-a-jour)
- [Guide complet Keepalived VRRP + HAProxy](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy)