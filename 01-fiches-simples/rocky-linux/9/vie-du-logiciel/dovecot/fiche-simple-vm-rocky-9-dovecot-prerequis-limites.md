# Fiche_Simple_-_VM_Rocky_9_Dovecot_Prerequis_Limites

- **Environnement** : [[Glossary:VM]] Rocky Linux 9; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Dovecot — Prérequis et limites
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `prerequis_limites`

---

## Problème précis à résoudre

Vérifier rôle, paquets et flux nécessaires à Dovecot.

## 1. Hors-Production (Lab / Test / POC)

1. Prérequis et limites :
   ```bash
   cat /etc/os-release | head -5
free -h
df -h /
sudo ss -lntup
   ```
   👉 Explication : Confirme l’OS, ressources et sockets avant changement.


## 2. Production — Contrôles

Documenter rôle [[Glossary:SMTP]]/IMAP, domaines, réseaux autorisés et ports.

## 3. Production — Sécurité

Ne pas exposer de port avant configuration; sur Rocky, conserver SELinux enforcing.

## Validation et retour arrière

- **Validation** : Le paquet candidat et le plan de changement sont consignés.
- **Retour arrière** : Aucun changement; arrêter si provenance ou prérequis incertains.

## Si le problème n'est pas résolu

- [Installer](fiche-simple-vm-rocky-9-dovecot-installer.md)
- [Configurer](fiche-simple-vm-rocky-9-dovecot-configurer.md)
- [Sécuriser](fiche-simple-vm-rocky-9-dovecot-securiser.md)
- [Valider (recette)](fiche-simple-vm-rocky-9-dovecot-valider.md)
- [Sauvegarder / restaurer](fiche-simple-vm-rocky-9-dovecot-sauvegarder-restaurer.md)
- [Mise à jour et retour arrière](fiche-simple-vm-rocky-9-dovecot-mise-a-jour-retour-arriere.md)
- [Documentation officielle](https://doc.dovecot.org/)
