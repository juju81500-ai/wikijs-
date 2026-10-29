# Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu Server 24.04; Postfix depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / Postfix — Sauvegarder / restaurer

---

## Problème précis à résoudre

Sauvegarder configuration de Postfix et tester restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder / restaurer :
   ```bash
   sudo tar --xattrs -czf /root/postfix-config-$(date +%F).tgz /etc/postfix
sudo chmod 600 /root/postfix-config-*.tgz
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

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-prerequis-limites)
- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-installer)
- [Configurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-configurer)
- [Sécuriser](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-securiser)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-valider)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.postfix.org/documentation.html)