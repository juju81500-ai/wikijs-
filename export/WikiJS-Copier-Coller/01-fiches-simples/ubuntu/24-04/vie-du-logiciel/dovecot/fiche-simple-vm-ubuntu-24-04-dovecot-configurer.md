# Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Configurer

- **Environnement** : VM Ubuntu Server 24.04; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / Dovecot — Configurer

---

## Problème précis à résoudre

Configurer Dovecot sans ouvrir un relais ou une authentification non maîtrisés.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer :
   ```bash
   sudo doveconf -n
sudo cp -a /etc/dovecot/dovecot.conf /etc/dovecot/dovecot.conf.prechange
sudo tee /etc/dovecot/conf.d/99-local.conf >/dev/null <<'EOF'
mail_location = maildir:~/Maildir
EOF
sudo doveconf -n
   ```
   👉 Explication : Sauvegarde et fixe le stockage Maildir dans un fichier local séparé; vérifier la compatibilité avec la version de Dovecot et le mode de livraison Postfix.

## 2. Production — Contrôles

Tracer les paramètres, les domaines et les réseaux autorisés; contrôler la syntaxe avec `doveconf -n` avant rechargement.

## 3. Production — Sécurité

Postfix : garder `reject_unauth_destination` et limiter `mynetworks`. Dovecot : activer TLS selon la version et les protocoles utilisés.

## Validation et retour arrière

- **Validation** : `doveconf -n` réussit et le service reste actif après rechargement.
- **Retour arrière** : Restaurer la copie `.prechange`, relancer `doveconf -n` puis redémarrer dovecot.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-prerequis-limites)
- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-installer)
- [Sécuriser](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-securiser)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-mise-a-jour-retour-arriere)
- [Documentation officielle](https://doc.dovecot.org/)