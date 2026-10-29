# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Afficher un avertissement légal.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les bannières et couper les messages commerciaux du MOTD :
   ```bash
   sudoedit /etc/issue
   sudoedit /etc/issue.net
   sudoedit /etc/motd
   sudo sed -i 's/^ENABLED=1/ENABLED=0/' /etc/default/motd-news
   ```
   👉 Explication : texte d'avertissement avant et après connexion; `motd-news` n'affiche plus d'annonces (Ubuntu assemble le MOTD à partir de `/etc/update-motd.d/`).

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

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)