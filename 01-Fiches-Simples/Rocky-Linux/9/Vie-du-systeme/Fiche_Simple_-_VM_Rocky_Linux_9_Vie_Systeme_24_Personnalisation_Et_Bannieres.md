# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal.

## 1. Hors-Production (Lab / Test / POC)

1. Définir la bannière avant connexion :
   ```bash
   echo 'Accès réservé aux personnes autorisées. Les actions sont journalisées.' | sudo tee /etc/issue.net
   ```
   👉 Explication : texte affiché avant l'authentification SSH.

2. L'activer dans sshd :
   ```bash
   echo 'Banner /etc/issue.net' | sudo tee /etc/ssh/sshd_config.d/20-banner.conf
   sudo sshd -t && sudo systemctl reload sshd
   ```
   👉 Explication : recharge sshd après test de syntaxe.

3. Personnaliser le message du jour :
   ```bash
   echo 'SRV01 - Rocky Linux 9 - Production' | sudo tee /etc/motd
   ```
   👉 Explication : affiché après connexion.

## 2. Production — Contrôles

Faire valider le texte par le service juridique.

## 3. Production — Sécurité

Ne pas révéler la version ni l'architecture dans la bannière.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion SSH.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
