# Fiche_Simple_-_VM_Rocky_9_Dovecot_Securiser

- **Environnement** : VM Rocky Linux 9; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Dovecot — Sécuriser
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Limiter connexions réseau et protéger TLS et comptes de Dovecot.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser :
   ```bash
   sudo tar --xattrs -czf /root/dovecot-pre-tls-DATE.tgz /etc/dovecot
sudo tee /etc/dovecot/conf.d/99-tls.conf >/dev/null <<'EOF'
ssl = required
disable_plaintext_auth = yes
ssl_cert = </etc/ssl/certs/IMAP_FULLCHAIN.pem
ssl_key = </etc/ssl/private/IMAP_PRIVATE_KEY.pem
EOF
sudo doveconf -n
sudo systemctl reload dovecot
sudo doveconf -n | grep -E "ssl|disable_plaintext_auth|auth_mechanisms" || true
sudo restorecon -Rv /etc/dovecot
sudo firewall-cmd --permanent --add-service=imaps
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
   ```
   👉 Explication : Impose TLS et refuse l’authentification en clair; `IMAP_FULLCHAIN.pem`, `IMAP_PRIVATE_KEY.pem` et `ADMIN_CIDR` sont à remplacer. Installer les certificats avant rechargement; sur Rocky, ne pas désactiver SELinux.


## 2. Production — Contrôles

Ubuntu : UFW si prévu; Rocky : firewalld et SELinux enforcing. Autoriser uniquement les flux documentés.

## 3. Production — Sécurité

Protéger clés, limiter sources, empêcher le relais ouvert. Ouvrir 587 uniquement si authentification/TLS configurés.

## Validation et retour arrière

- **Validation** : Ports, certificat, restrictions et journaux correspondent à la matrice de flux.
- **Retour arrière** : Remplacer `DATE` par la date de l’archive, restaurer `/etc/dovecot`, vérifier les certificats puis recharger Dovecot; rétablir les règles pare-feu précédentes sans couper l’administration.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Rocky_9_Dovecot_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Rocky_9_Dovecot_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Rocky_9_Dovecot_Configurer.md)
- [Valider (recette)](Fiche_Simple_-_VM_Rocky_9_Dovecot_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Rocky_9_Dovecot_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Rocky_9_Dovecot_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://doc.dovecot.org/)
