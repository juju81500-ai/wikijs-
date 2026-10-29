# Fiche_Simple_-_VM_Rocky_9_Postfix_Securiser

- **Environnement** : VM Rocky Linux 9; Postfix depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Postfix — Sécuriser

---

## Problème précis à résoudre

Limiter connexions réseau et protéger TLS et comptes de Postfix.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser :
   ```bash
   sudo postconf -e "smtpd_tls_security_level = may"
sudo postconf -e "smtpd_tls_cert_file = /etc/ssl/certs/SMTP_CERT.pem"
sudo postconf -e "smtpd_tls_key_file = /etc/ssl/private/SMTP_KEY.pem"
sudo postconf -e "smtpd_relay_restrictions = permit_mynetworks, reject_unauth_destination"
sudo postfix check
sudo postconf -n | grep -E "smtpd_tls|smtpd_relay_restrictions|mynetworks"
sudo systemctl reload postfix
sudo restorecon -Rv /etc/postfix
sudo firewall-cmd --permanent --add-service=smtp
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
   ```
   👉 Explication : Configure STARTTLS opportuniste et le refus du relais non autorisé. `SMTP_CERT`, `SMTP_KEY` et `ADMIN_CIDR` sont des placeholders à remplacer par les certificats installés et le réseau admin; sur Rocky, restorecon vérifie les labels sans désactiver SELinux.

## 2. Production — Contrôles

Ubuntu : UFW si prévu; Rocky : firewalld et SELinux enforcing. Autoriser uniquement les flux documentés.

## 3. Production — Sécurité

Protéger clés, limiter sources, empêcher le relais ouvert. Ouvrir 587 uniquement si authentification/TLS configurés.

## Validation et retour arrière

- **Validation** : Ports, certificat, restrictions et journaux correspondent à la matrice de flux.
- **Retour arrière** : Restaurer les règles et paramètres précédents, sans désactiver globalement le pare-feu.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-prerequis-limites)
- [Installer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-installer)
- [Configurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-configurer)
- [Valider (recette)](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.postfix.org/documentation.html)