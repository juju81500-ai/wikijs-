# Fiche_Simple_-_VM_Debian_13_Elastic_Stack_Ingestion.md

- **Environnement** : Elasticsearch et Kibana sur Debian 13, nœud unique
- **OS / Version** : Debian 13; Elasticsearch et Kibana 9.5.x
- **Catégorie** : journalisation / ingestion
- **Tags** : `debian13`, `elastic`, `ingestion`, `index`, `health`

---

## Problème précis à résoudre

Valider la santé du nœud et préparer une ingestion pilote.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la santé du cluster :
   ```bash
   curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic https://localhost:9200/_cluster/health?pretty
   ```
   👉 Explication : Un nœud unique est généralement `green` ou `yellow` selon les réplicas demandés.

2. Créer un document de test dans un index pilote :
   ```bash
   curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic -X POST https://localhost:9200/test-pilote/_doc -H 'Content-Type: application/json' -d '{"message":"test"}'
   ```
   👉 Explication : Valide l'écriture; vérifier ensuite l'index dans **Kibana > Discover** (champs, fuseau horaire, droits).

3. Lister les index :
   ```bash
   curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic 'https://localhost:9200/_cat/indices?v'
   ```
   👉 Explication : Confirme la présence de l'index de test.

## 2. Production — Contrôles

Choisir Elastic Agent/Fleet ou un shipper conforme à l'architecture; valider d'abord un hôte pilote avec certificat CA.

## 3. Production — Sécurité

- Utiliser des credentials à privilèges limités pour la collecte.
- Ne pas activer de listener réseau générique sans filtrage par source.

## Validation et retour arrière

- **Validation** : l'API est saine et le document de test est visible dans Kibana.
- **Retour arrière** : supprimer l'index de test : `curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic -X DELETE https://localhost:9200/test-pilote`.

## Si le problème n'est pas résolu

- [Elastic — paquet Debian Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package)
- [Elastic — paquet Debian Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-debian-package)
- [Guide complet Elastic_Stack Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/50_Deploiement_Elastic_Stack_9.5_Debian_13.md#5-verifier-et-definir-lingestion)
