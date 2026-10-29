# Fiche_Simple_-_VM_Debian_13_Ansible_Preparer_Inventaire.md

- **Environnement** : répertoire Ansible privé, hôte de laboratoire autorisé
- **OS / Version** : Debian 13; Ansible Core et OpenSSH
- **Catégorie** : automatisation / inventaire
- **Tags** : `debian13`, `ansible`, `inventory`, `ssh`, `known-hosts`

---

## Problème précis à résoudre

Préparer un inventaire minimal et vérifier l'identité SSH de l'hôte avant toute opération distante.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le dossier de travail restreint :
   ```bash
   install -d -m 0700 "$HOME/ansible-lab"
   cd "$HOME/ansible-lab"
   ```
   👉 Explication : ne pas versionner clés privées, mots de passe ni fichiers Vault non chiffrés.

2. Créer l'inventaire (remplacer par des systèmes autorisés) :
   ```bash
   cat > inventory.ini <<'EOF'
   [linux_lab]
   serveur-test.example.net ansible_user=admin_ansible
   EOF
   ```
   👉 Explication : un seul hôte de test au départ.

3. Vérifier l'empreinte SSH par un canal indépendant avant l'ajout :
   ```bash
   ssh-keyscan -t ed25519 serveur-test.example.net | ssh-keygen -lf -
   ```
   👉 Explication : comparer avec l'empreinte relevée sur l'hôte (`ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub`); ne jamais utiliser `StrictHostKeyChecking=no`.

4. Ajouter la clé validée à `known_hosts` puis tester sans privilèges élevés :
   ```bash
   ssh-keyscan -t ed25519 serveur-test.example.net >> ~/.ssh/known_hosts
   ssh -i ~/.ssh/id_ansible_lab admin_ansible@serveur-test.example.net 'whoami'
   ```
   👉 Explication : la connexion doit réussir sans `sudo`.

## 2. Production — Contrôles

Séparer les inventaires labo, préproduction et production; exiger revue des changements, propriétaire de groupe, limites de ciblage et méthode d'accès approuvée.

## 3. Production — Sécurité

- Exclure clés privées, fichiers de mots de passe et secrets non chiffrés du contrôle de version.
- Protéger la clé dédiée par phrase de passe et coffre approuvé.
- Ne pas utiliser un compte générique partagé ni ouvrir les accès SSH au-delà du périmètre autorisé.
- Vérifier les changements d'empreinte avant toute mise à jour de `known_hosts`.

## Validation et retour arrière

- **Validation** : inventaire affiche un unique hôte de test et la connexion SSH valide la clé attendue.
- **Retour arrière** : retirer uniquement l'entrée pilote ajoutée; ne pas remplacer globalement les clés d'hôte connues.

## Si le problème n'est pas résolu

- [Ansible — inventaire](https://docs.ansible.com/projects/ansible/latest/inventory_guide/index.html)
- [OpenSSH — ssh-keygen](https://man.openbsd.org/ssh-keygen)
- [Guide complet Ansible Core Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/90_Administration_Ansible_Core_Debian_13.md#3-preparer-un-inventaire-de-laboratoire)
