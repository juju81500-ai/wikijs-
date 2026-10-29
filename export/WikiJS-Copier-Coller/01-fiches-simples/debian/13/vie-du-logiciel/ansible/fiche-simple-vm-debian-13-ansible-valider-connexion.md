# Fiche_Simple_-_VM_Debian_13_Ansible_Valider_Connexion.md

- **Environnement** : nœud de contrôle Debian 13, un hôte Linux pilote
- **OS / Version** : Debian 13; Ansible Core
- **Catégorie** : automatisation / connectivité

---

## Problème précis à résoudre

Valider la communication Ansible et recueillir des facts sur un seul hôte sans modifier son état.

## 1. Hors-Production (Lab / Test / POC)

1. Afficher l'inventaire :
   ```bash
   cd ~/ansible-lab
   ansible-inventory -i inventory.ini --graph
   ```
   👉 Explication : le groupe `linux_lab` ne doit contenir que les hôtes autorisés.

2. Tester la connexion Ansible :
   ```bash
   ansible linux_lab -i inventory.ini -m ansible.builtin.ping
   ```
   👉 Explication : `ping` vérifie SSH et l'interpréteur Python; ce n'est pas un test ICMP. Réponse attendue : `pong`.

3. Collecter les faits sur un seul hôte :
   ```bash
   ansible linux_lab -i inventory.ini -m ansible.builtin.setup --limit serveur-test.example.net | head -30
   ```
   👉 Explication : limiter à un hôte avant d'élargir; `setup` ne modifie rien.

4. En cas d'échec, relancer avec plus de détails :
   ```bash
   ansible linux_lab -i inventory.ini -m ansible.builtin.ping -vvv
   ```
   👉 Explication : repérer l'erreur d'authentification, de clé d'hôte ou de Python manquant.

## 2. Production — Contrôles

Avant de cibler un groupe plus large, faire approuver la liste d'hôtes, le compte, le mode d'élévation, l'horaire et le volume de facts collectés.

## 3. Production — Sécurité

- Le module Ansible `ping` n'est pas une requête ICMP et ne justifie pas un changement réseau.
- La collecte de facts peut révéler système, interfaces et versions; limiter les destinataires et la conservation.
- Conserver `--limit` pour chaque test pilote; ne pas élargir automatiquement le groupe.
- En cas d'échec SSH, ne pas désactiver la validation de la clé d'hôte.

## Validation et retour arrière

- **Validation** : l'hôte attendu répond via Ansible, facts cohérents et aucun changement distant signalé.
- **Retour arrière** : aucune modification système n'étant prévue, arrêter la tâche et corriger la connectivité ou l'inventaire.

## Si le problème n'est pas résolu

- [Ansible — modules ad hoc](https://docs.ansible.com/projects/ansible/latest/command_guide/intro_adhoc.html)
- [Guide complet Ansible Core Debian 13](/02-fiches-completes/debian/13/installation-deploiement/90-administration-ansible-core-debian-13#4-verifier-la-connexion-sans-modifier-les-hotes)