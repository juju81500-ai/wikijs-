# Fiche_Simple_-_VM_Debian_13_Ansible_Production_Retour_Arriere.md

- **Environnement** : dépôt Ansible revu, sauvegarde vérifiée et cibles approuvées
- **OS / Version** : Debian 13 sur le nœud de contrôle; hôtes gérés selon inventaire
- **Catégorie** : automatisation / validation et retour arrière

---

## Problème précis à résoudre

Exécuter un playbook approuvé de façon limitée, vérifier les résultats et restaurer l'état en cas d'échec.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le dépôt et exclure les fichiers sensibles :
   ```bash
   cd ~/ansible-lab
   git status --short
   printf '%s\n' '*.retry' '*.key' 'vault-pass*' >> .gitignore
   ```
   👉 Explication : inventaire et playbooks sont versionnés et revus; clés et mots de passe Vault jamais.

2. Sauvegarder les fichiers ciblés avant un changement :
   ```bash
   ansible linux_lab -i inventory.ini --limit serveur-test.example.net -b -m ansible.builtin.fetch -a "src=/etc/FICHIER dest=./sauvegardes/"
   ```
   👉 Explication : remplacer le fichier; consigner le résultat attendu et la procédure de restauration.

3. Exécuter sur un hôte pilote et contrôler :
   ```bash
   ansible-playbook -i inventory.ini --limit serveur-test.example.net playbook.yml; echo "code=$?"
   ```
   👉 Explication : `0` = succès; vérifier les hôtes réellement ciblés et tester l'application.

4. En cas d'échec, restaurer uniquement les fichiers sauvegardés :
   ```bash
   ansible linux_lab -i inventory.ini --limit serveur-test.example.net -b -m ansible.builtin.copy -a "src=./sauvegardes/serveur-test.example.net/etc/FICHIER dest=/etc/FICHIER backup=yes"
   ```
   👉 Explication : arrêter les exécutions suivantes et confirmer l'état du service avant d'élargir.

5. Retrait de l'installation, après archivage approuvé :
   ```bash
   sudo apt remove ansible-core
   ```
   👉 Explication : ne jamais supprimer les inventaires ou dépôts de production sans validation.

## 2. Production — Contrôles

Consigner l'approbation, la fenêtre, la sauvegarde et sa restauration testée, les hôtes réels, la version de playbook, les résultats et l'acceptation du propriétaire.

## 3. Production — Sécurité

- Arrêter les exécutions suivantes dès qu'un échec ou une cible inattendue survient.
- Ne pas lancer un playbook de rollback non relu sur tout un groupe.
- Préserver les journaux utiles et les preuves; limiter l'accès aux sorties contenant des facts sensibles.
- Ne jamais supprimer inventaires ou dépôts de production pour « nettoyer » l'incident.

## Validation et retour arrière

- **Validation** : service fonctionnel, résultats conformes, hôtes impactés recensés, propriétaire informé.
- **Retour arrière** : suivre uniquement la restauration approuvée, confirmer l'état du service avant toute nouvelle exécution.

## Si le problème n'est pas résolu

- [Ansible — playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/index.html)
- [Ansible — Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html)
- [Guide complet Ansible Core Debian 13](/02-fiches-completes/debian/13/installation-deploiement/90-administration-ansible-core-debian-13#7-validation-sauvegarde-et-retour-arriere)