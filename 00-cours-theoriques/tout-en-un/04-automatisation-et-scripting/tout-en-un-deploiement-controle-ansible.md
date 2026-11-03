# Fiche_Simple_-_Tout-en-un_Deploiement_Controle_Ansible

- **Environnement** : laboratoire ou parc administré par Ansible
- **OS / Version** : contrôleur Linux ; hôtes selon inventaire et collections validés
- **Catégorie** : Tout-en-un / Automatisation et scripting
- **Tags** : `transverse`, `tout-en-un`, `ansible`, `automatisation`, `idempotence`

---

## Problème précis à résoudre

Prévisualiser puis appliquer un changement Ansible limité à un groupe autorisé, en contrôlant l'idempotence et le résultat sans exposer de secrets.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'identité, la version et l'inventaire du contrôleur :
   ```bash
   ansible --version
   ansible-inventory -i inventory.yml --graph
   ```
   👉 Explication : confirme le binaire et les groupes ciblés ; examiner l'inventaire avant tout playbook et n'utiliser qu'un groupe de laboratoire approuvé.

2. Vérifier la syntaxe du playbook :
   ```bash
   ansible-playbook -i inventory.yml playbook.yml --syntax-check
   ```
   👉 Explication : valide la syntaxe sans contacter les hôtes ni appliquer de tâche.

3. Simuler les changements sur un seul hôte de laboratoire :
   ```bash
   ansible-playbook -i inventory.yml playbook.yml --limit lab01 --check --diff
   ```
   👉 Explication : le mode check et le diff aident à examiner les changements ; certains modules ne simulent pas complètement leur comportement, donc ce résultat ne remplace pas un essai.

4. Appliquer le changement au laboratoire approuvé :
   ```bash
   ansible-playbook -i inventory.yml playbook.yml --limit lab01
   ```
   👉 Explication : ne retirer `--limit` qu'après revue du plan, des variables, des dépendances et de l'approbation.

5. Tester l'idempotence en rejouant le même playbook :
   ```bash
   ansible-playbook -i inventory.yml playbook.yml --limit lab01
   ```
   👉 Explication : une exécution sans changement inattendu est un indice d'idempotence ; confirmer également le résultat par un contrôle métier sur l'hôte.

## 2. Production — Contrôles

Exiger une revue du diff, des variables, des rôles et collections, un inventaire versionné, une approbation et un mécanisme de retour arrière propre au changement. Utiliser un compte de service à privilèges minimaux.

## 3. Production — Sécurité

Ne pas mettre de secret dans l'inventaire, les variables en clair, le dépôt ou la ligne de commande. Employer Ansible Vault ou un gestionnaire de secrets approuvé ; limiter les journaux et protéger les artefacts de CI.

## Validation et retour arrière

- **Validation** : syntaxe valide, portée vérifiée, changements attendus seulement, second passage sans modification imprévue et test applicatif concluant.
- **Retour arrière** : restaurer le fichier ou l'état antérieur par le rôle de rollback testé, ou restaurer le snapshot prévu ; ne pas lancer un playbook correctif non relu.

## Si le problème n'est pas résolu

- [Documentation Ansible — playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)
- [Documentation Ansible — mode check et diff](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html)

## Historique de vérification

| Vérifié le | OS / version | Logiciel / version | Testeur | Verdict | Sources |
|---|---|---|---|---|---|
| 2026-10-31 | Contrôleur Linux | Ansible — version à figer | — | Non testé sur plateforme cible | Documentation Ansible ci-dessus |
