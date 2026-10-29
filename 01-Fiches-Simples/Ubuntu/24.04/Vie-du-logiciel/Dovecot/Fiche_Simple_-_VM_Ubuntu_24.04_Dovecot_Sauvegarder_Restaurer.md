# Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu Server 24.04; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / Dovecot — Sauvegarder / restaurer
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `sauvegarder_restaurer`

---

## Problème précis à résoudre

Sauvegarder configuration de Dovecot et tester restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder / restaurer :
   ```bash
   sudo tar --xattrs -czf /root/dovecot-config-$(date +%F).tgz /etc/dovecot
sudo chmod 600 /root/dovecot-config-*.tgz
   ```
   👉 Explication : Archive la configuration; chiffrer et copier hors hôte. Elle ne contient pas les courriels ni nécessairement la file de livraison.


## 2. Production — Contrôles

Dovecot : inclure boîtes et métadonnées selon backend; Postfix : traiter la file séparément si nécessaire. Définir RPO/RTO.

## 3. Production — Sécurité

Restreindre accès aux archives contenant secrets et clés.

## Validation et retour arrière

- **Validation** : Restauration de lab démarre le service et passe le contrôle de configuration.
- **Retour arrière** : Restaurer un snapshot cohérent service/configuration/données; downgrade de paquet isolé risqué.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Valider.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://doc.dovecot.org/)
