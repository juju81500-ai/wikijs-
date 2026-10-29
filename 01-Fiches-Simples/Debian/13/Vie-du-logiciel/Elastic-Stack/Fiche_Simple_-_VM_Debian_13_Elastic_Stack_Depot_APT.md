# Fiche_Simple_-_VM_Debian_13_Elastic_Stack_Depot_APT.md

- **Environnement** : Elasticsearch et Kibana sur Debian 13, nœud unique
- **OS / Version** : Debian 13; Elasticsearch et Kibana 9.5.x
- **Catégorie** : journalisation / dépôt APT
- **Tags** : `debian13`, `elastic`, `apt`, `gpg`, `depot`

---

## Problème précis à résoudre

Ajouter le dépôt APT officiel Elastic 9.x avec une clé dédiée, sans clé globale.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils nécessaires :
   ```bash
   sudo apt-get update
   sudo apt-get install -y ca-certificates wget gpg
   ```
   👉 Explication : Fournit le téléchargement HTTPS et la conversion de clé.

2. Installer la clé Elastic dans un keyring dédié (vérifier d'abord son empreinte via une source officielle indépendante) :
   ```bash
   wget -qO- https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor --yes -o /usr/share/keyrings/elasticsearch-keyring.gpg
   ```
   👉 Explication : La clé ne servira qu'au dépôt qui la référence avec `signed-by`.

3. Déclarer le dépôt 9.x :
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list
   sudo apt-get update
   ```
   👉 Explication : Crée la source APT et rafraîchit l'index.

4. Vérifier qu'un seul dépôt 9.x est actif :
   ```bash
   grep -r 'artifacts.elastic.co' /etc/apt/sources.list /etc/apt/sources.list.d/
   ```
   👉 Explication : Un seul résultat 9.x évite les mélanges de versions.

## 2. Production — Contrôles

Pour un déploiement reproductible, épingler une version 9.5.x validée pour les deux paquets; passer par un miroir interne si la politique le demande.

## 3. Production — Sécurité

- Contrôler l'empreinte de la clé avant de l'enregistrer.
- Ne pas mélanger plusieurs versions Elastic Stack.

## Validation et retour arrière

- **Validation** : `apt-cache policy elasticsearch` affiche un candidat 9.5.x depuis artifacts.elastic.co.
- **Retour arrière** : supprimer `/etc/apt/sources.list.d/elastic-9.x.list` et le keyring, puis `sudo apt-get update`.

## Si le problème n'est pas résolu

- [Elastic — paquet Debian Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package)
- [Elastic — paquet Debian Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-debian-package)
- [Guide complet Elastic_Stack Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/50_Deploiement_Elastic_Stack_9.5_Debian_13.md#2-ajouter-le-depot-elastic-signe)
