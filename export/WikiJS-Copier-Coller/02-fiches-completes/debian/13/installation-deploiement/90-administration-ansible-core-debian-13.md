# Administrer des hôtes avec Ansible Core sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64 pour le nœud de contrôle; hôtes gérés Linux accessibles par SSH
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : installation de `ansible-core` depuis APT, inventaire contrôlé, vérification de connectivité et exécution d'un playbook sans changement
- **Catégorie** : automatisation / administration système

## 1. Périmètre et prérequis

Fiche simple : [cadrer le pilote Ansible](/01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-cadrer-pilote).

Ansible Core exécute les modules depuis un nœud de contrôle; les hôtes Linux gérés n'ont généralement besoin que de Python et d'un accès SSH. Cette fiche n'installe ni Ansible Automation Platform, AWX, collections tierces, ni agent sur les hôtes. Elle commence avec un test de lecture (`setup`) et ne modifie aucun hôte distant.

Utiliser une VM de contrôle dédiée, un compte utilisateur nominatif, une clé SSH dédiée protégée par phrase de passe et des hôtes de laboratoire explicitement autorisés. Ne pas utiliser root pour les opérations de contrôle ou de gestion, et ne pas accorder `become` avant d'avoir examiné les tâches.

## 2. Installer Ansible Core depuis Debian

Fiche simple : [installer Ansible Core](/01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-installer-core).

```bash
sudo apt update
apt-cache policy ansible-core
sudo apt install ansible-core openssh-client
ansible --version
```

La version provient des dépôts Debian configurés; relever version et origine via `apt-cache policy`. Pour une autre version, utiliser une méthode isolée officiellement documentée (par exemple environnement virtuel) plutôt que `pip` sur le Python système.

## 3. Préparer un inventaire de laboratoire

Fiche simple : [préparer l'inventaire pilote](/01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-preparer-inventaire).

Créer un dossier de travail avec accès limité et ne pas versionner clés privées, mots de passe ou fichiers Vault non chiffrés :

```bash
install -d -m 0700 "$HOME/ansible-lab"
cd "$HOME/ansible-lab"
```

Créer `inventory.ini`, en remplaçant les noms et comptes d'exemple par des systèmes autorisés :

```ini
[linux_lab]
serveur-test.example.net ansible_user=admin_ansible
```

Vérifier l'empreinte SSH de l'hôte par un canal indépendant avant l'ajout à `known_hosts`. Ne pas utiliser `StrictHostKeyChecking=no` et ne pas désactiver la validation de clé d'hôte. Tester la connexion SSH avec le compte prévu, sans privilèges élevés.

## 4. Vérifier la connexion sans modifier les hôtes

Fiche simple : [valider la connexion sans changement](/01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-valider-connexion).

```bash
ansible-inventory -i inventory.ini --graph
ansible linux_lab -i inventory.ini -m ansible.builtin.ping
ansible linux_lab -i inventory.ini -m ansible.builtin.setup --limit serveur-test.example.net
```

Le module `ping` vérifie la connexion Ansible et l'interpréteur Python; ce n'est pas un test ICMP. `setup` recueille des faits système. Limiter la commande à un seul hôte de test avant d'élargir le périmètre.

## 5. Écrire et valider un playbook sans changement

Fiche simple : [valider le playbook avant exécution](/01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-valider-playbook).

Créer `check.yml` :

```yaml
---
- name: Collecter les faits d'un hôte pilote
  hosts: linux_lab
  gather_facts: true
  tasks:
    - name: Afficher la distribution détectée
      ansible.builtin.debug:
        msg: "{{ ansible_facts.distribution }} {{ ansible_facts.distribution_version }}"
```

Valider la syntaxe, puis afficher les changements proposés :

```bash
ansible-playbook -i inventory.ini --syntax-check check.yml
ansible-playbook -i inventory.ini --list-hosts check.yml
ansible-playbook -i inventory.ini --check --diff --limit serveur-test.example.net check.yml
```

Ce playbook ne modifie pas l'hôte. Pour toute tâche de changement, relire les modules et variables, confirmer l'inventaire, sauvegarder la configuration distante et exécuter d'abord `--check --diff` sur un pilote. Le mode check est une simulation best-effort : certains modules ne le prennent pas en charge et il ne garantit pas l'absence de changement.

## 6. Identifiants, collections et exécution

Fiche simple : [protéger les secrets et contrôler les collections](/01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-secrets-collections).

- Préférer une clé SSH dédiée, gérée par l'agent ou le coffre de l'organisation; protéger `~/.ssh` et les fichiers de configuration.
- Ne pas inscrire de secret dans l'inventaire, les variables en clair, la ligne de commande ou les logs. Utiliser Ansible Vault avec une clé conservée séparément et tester la procédure de récupération.
- Installer seulement les collections nécessaires depuis des sources approuvées; figer leurs versions dans `requirements.yml` et inspecter les rôles avant exécution.
- Utiliser `become: true` uniquement sur les tâches qui le nécessitent. Les mots de passe sudo doivent être fournis via un mécanisme sûr, pas dans le dépôt.
- Limiter les cibles au groupe et au sous-ensemble explicitement approuvés (`--limit`); une erreur d'inventaire peut affecter de nombreux systèmes.

## 7. Validation, sauvegarde et retour arrière

Fiche simple : [valider l'exécution et préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-production-retour-arriere).

- Conserver l'inventaire et les playbooks dans un dépôt avec revue; exclure clés, états et données sensibles.
- Avant un playbook de changement, sauvegarder les fichiers ou données ciblés, consigner le résultat attendu et définir une procédure de restauration.
- Vérifier le code retour, les hôtes réellement ciblés et les journaux; exécuter un contrôle fonctionnel depuis l'application après chaque changement.
- En cas d'échec, arrêter les exécutions suivantes, restaurer uniquement les fichiers sauvegardés conformément au plan et confirmer l'état du service avant d'élargir à d'autres hôtes.
- Retirer l'installation via APT après archivage approuvé des playbooks et dépendances; ne jamais supprimer les inventaires ou dépôts de production sans validation.

## Sources

- [Ansible Community Documentation — Installation guide](https://docs.ansible.com/projects/ansible/latest/installation_guide/index.html)
- [Ansible Community Documentation — Debian installation](https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-debian)
- [Ansible Community Documentation — Inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/index.html)
- [Ansible Community Documentation — Check mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html)
- [Ansible Community Documentation — Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html)
- [Debian — paquet ansible-core pour Trixie](https://packages.debian.org/trixie/ansible-core)

Le contrôle de version, l'accès SSH et le playbook doivent être validés en laboratoire avant toute gestion de production. Cette fiche n'a pas été testée sur des hôtes cibles.