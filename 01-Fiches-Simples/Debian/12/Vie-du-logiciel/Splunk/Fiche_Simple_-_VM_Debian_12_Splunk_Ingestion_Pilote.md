# Fiche_Simple_-_VM_Debian_12_Splunk_Ingestion_Pilote.md

- **Environnement** : VM Debian 12 dédiée à Splunk Enterprise autonome (laboratoire)
- **OS / Version** : Debian 12 Bookworm; Splunk Enterprise 10.2
- **Catégorie** : journaux / ingestion
- **Tags** : `debian12`, `splunk`, `logs`, `input`, `index`

---

## Problème précis à résoudre

Ingérer une source de test dans un index à rétention limitée.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'index et l'input pilote : **Settings > Indexes > New Index** puis **Settings > Data inputs > Add new**
   👉 Explication : index à rétention limitée; ne pas écouter sur les interfaces globales par défaut.

2. Créer un événement synthétique connu (fichier d'exemple à adapter) :
   ```bash
   printf 'splunk-pilote test 1\n' | sudo tee -a /var/tmp/splunk-pilote.log
   ```
   👉 Explication : donnée de test sans secret ni donnée personnelle.

3. Lancer la recherche de validation : **Search & Reporting > index=pilote "splunk-pilote"**
   👉 Explication : confirmer source, sourcetype, index, horodatage et timezone.

## 2. Production — Contrôles

Pour des sources distribuées, utiliser un Universal Forwarder ou un transport approuvé, TLS vérifié; contrôler volumes d'ingestion, CPU et disque avant extension.

## 3. Production — Sécurité

- Ne pas indexer de journaux contenant mots de passe, tokens ou données personnelles non autorisées.

## Validation et retour arrière

- **Validation** : l'événement pilote est retrouvé avec les bons champs.
- **Retour arrière** : supprimer l'input et l'index pilote depuis **Settings**, après export des données utiles.

## Si le problème n'est pas résolu

- [Splunk 10.2 — installer sur Linux](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/install-on-linux)
- [Guide complet Splunk Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/54_Deploiement_Splunk_Enterprise_10.2_Debian_12.md#5-configurer-lingestion-pilote)
