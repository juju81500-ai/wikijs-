# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Obtenir un certificat.

## 1. Hors-Production (Lab / Test / POC)

1. Certbot (Let's Encrypt), remplacer le domaine :
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d srv01.exemple.fr
   ```
   👉 Explication : obtient et installe un certificat.

2. Ajouter une CA interne :
   ```bash
   sudo cp ca-entreprise.crt /usr/local/share/ca-certificates/
   sudo update-ca-certificates
   ```
   👉 Explication : fait confiance à la CA interne.

## 2. Production — Contrôles

Utiliser la CA interne pour les noms privés.

## 3. Production — Sécurité

Protéger les clés privées (`chmod 600`).

## Validation et retour arrière

- **Validation** : `openssl s_client -connect srv01:443` valide la chaîne.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Debian 12 Securite Certbot SSL Nginx](</01-fiches-simples/debian/12/vie-du-logiciel/certbot/fiche-simple-vm-debian-12-securite-certbot-ssl-nginx>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)