# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les bannières :
   ```bash
   sudoedit /etc/issue
   sudoedit /etc/issue.net
   sudoedit /etc/motd
   ```
   👉 Explication : texte d'avertissement avant et après connexion.

2. Activer la bannière SSH :
   ```bash
   echo 'Banner /etc/issue.net' | sudo tee /etc/ssh/sshd_config.d/10-banner.conf
   sudo sshd -t && sudo systemctl reload ssh
   ```
   👉 Explication : vérifie la syntaxe puis recharge sshd.

## 2. Production — Contrôles

Texte validé par le juridique.

## 3. Production — Sécurité

Ne pas indiquer la version ni le rôle du serveur.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion SSH.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 13](./Sommaire_-_Vie_du_systeme_Debian_13.md)
- [Documentation officielle](https://www.debian.org/doc/)
