# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-39`

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

- [Fiche détaillée : VM Ubuntu 26.04 Securite Certbot TLS](<../Vie-du-logiciel/Certbot/Fiche_Simple_-_VM_Ubuntu_26.04_Securite_Certbot_TLS.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
