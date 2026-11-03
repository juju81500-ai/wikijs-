# Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Mise_A_Jour_Retour_Arriere

- **Environnement** : [[Glossary:VM]] Ubuntu Server 24-04; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24-04
- **Catégorie** : Vie du logiciel / Dovecot — Mise à jour et retour arrière
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Mettre à jour Dovecot depuis dépôts configurés.

## 1. Hors-Production (Lab / Test / POC)

1. Mise à jour et retour arrière :
   ```bash
   sudo apt update && apt list --upgradable 2>/dev/null | grep -E "dovecot|^Listing"
sudo apt install --only-upgrade -y dovecot-core dovecot-imapd dovecot-pop3d
sudo systemctl restart dovecot
sudo doveconf -n
   ```
   👉 Explication : Liste les paquets puis met à jour en lab; contrôler les notes de version et la syntaxe après redémarrage.


## 2. Production — Contrôles

Préparer sauvegarde restaurable, fenêtre, espace disque et compatibilité clients.

## 3. Production — Sécurité

Utiliser paquets signés des dépôts autorisés.

## Validation et retour arrière

- **Validation** : Version mise à jour consignée, service actif et contrôle syntaxique réussi.
- **Retour arrière** : Restaurer un snapshot cohérent plutôt qu’un downgrade de paquet isolé.

## Si le problème n'est pas résolu

- [Prérequis et limites](fiche-simple-vm-ubuntu-24-04-dovecot-prerequis-limites.md)
- [Installer](fiche-simple-vm-ubuntu-24-04-dovecot-installer.md)
- [Configurer](fiche-simple-vm-ubuntu-24-04-dovecot-configurer.md)
- [Sécuriser](fiche-simple-vm-ubuntu-24-04-dovecot-securiser.md)
- [Valider (recette)](fiche-simple-vm-ubuntu-24-04-dovecot-valider.md)
- [Sauvegarder / restaurer](fiche-simple-vm-ubuntu-24-04-dovecot-sauvegarder-restaurer.md)
- [Documentation officielle](https://doc.dovecot.org/)
