# Fiche_Simple_-_VM_Rocky_9_Dovecot_Configurer

- **Environnement** : VM Rocky Linux 9; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Dovecot — Configurer
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `configurer`

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

- [Prérequis et limites](Fiche_Simple_-_VM_Rocky_9_Dovecot_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Rocky_9_Dovecot_Installer.md)
- [Sécuriser](Fiche_Simple_-_VM_Rocky_9_Dovecot_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Rocky_9_Dovecot_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Rocky_9_Dovecot_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Rocky_9_Dovecot_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://doc.dovecot.org/)
