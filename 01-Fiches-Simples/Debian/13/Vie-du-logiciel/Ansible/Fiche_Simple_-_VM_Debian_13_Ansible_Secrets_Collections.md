# Fiche_Simple_-_VM_Debian_13_Ansible_Secrets_Collections.md

- **Environnement** : dépôt Ansible privé avec collections approuvées
- **OS / Version** : Debian 13; Ansible Core
- **Catégorie** : automatisation / secrets et extensions
- **Tags** : `debian13`, `ansible`, `vault`, `collections`, `secrets`

---

## Problème précis à résoudre

Protéger les identifiants Ansible et contrôler les collections avant leur exécution.

## 1. Hors-Production (Lab / Test / POC)

1. Protéger les clés SSH :
   ```bash
   chmod 0700 ~/.ssh
   chmod 0600 ~/.ssh/id_ansible_lab
   ls -l ~/.ssh
   ```
   👉 Explication : la clé privée n'est lisible que par son propriétaire.

2. Chiffrer un fichier de variables avec Ansible Vault :
   ```bash
   cd ~/ansible-lab
   ansible-vault create group_vars/linux_lab/vault.yml
   ```
   👉 Explication : le mot de passe Vault est saisi à l'invite et conservé séparément; tester la procédure de récupération.

3. Rechercher des secrets en clair :
   ```bash
   grep -rEn '(password|passwd|secret|token)\s*[:=]' . --include='*.ini' --include='*.yml' | grep -v vault || echo "aucun secret en clair"
   ```
   👉 Explication : l'inventaire, les variables et les logs ne doivent contenir aucun secret.

4. Figer les collections nécessaires :
   ```bash
   cat > requirements.yml <<'EOF'
   collections:
     - name: ansible.posix
       version: "X.Y.Z"
   EOF
   ansible-galaxy collection install -r requirements.yml
   ```
   👉 Explication : remplacer nom et version par ceux approuvés; inspecter les rôles avant exécution.

5. Limiter toujours les cibles :
   ```bash
   ansible-playbook -i inventory.ini --limit serveur-test.example.net --list-hosts check.yml
   ```
   👉 Explication : utiliser `become: true` seulement pour les tâches qui l'exigent.

## 2. Production — Contrôles

Définir propriétaires de secrets, rotation, accès au coffre, récupération, versions approuvées de collections et procédure de revue des dépendances.

## 3. Production — Sécurité

- Ne jamais commiter clé privée, mot de passe ou fichier Vault non chiffré.
- Ne pas fournir de mot de passe dans la ligne de commande ou les logs; utiliser un mécanisme sûr.
- Limiter `become` aux tâches qui en ont besoin; fournir les secrets sudo depuis un coffre.
- Refuser toute collection de source ou version non vérifiée.

## Validation et retour arrière

- **Validation** : aucun secret en clair dans le dépôt; versions de collections verrouillées et contenu revu.
- **Incident** : considérer un secret commité comme compromis, le révoquer/renouveler et analyser les copies, sans se limiter à supprimer le fichier.

## Si le problème n'est pas résolu

- [Ansible — Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html)
- [Ansible — collections](https://docs.ansible.com/projects/ansible/latest/collections_guide/index.html)
- [Guide complet Ansible Core Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/90_Administration_Ansible_Core_Debian_13.md#6-identifiants-collections-et-execution)
