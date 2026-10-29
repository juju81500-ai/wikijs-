# Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Reseau_Secrets.md

- **Environnement** : Ubuntu Server 24.04: nœud Graylog + MongoDB et Data Node (laboratoire)
- **OS / Version** : Ubuntu Server 24.04 LTS; Graylog 7.2; MongoDB 8.0
- **Catégorie** : journaux / sécurité
- **Tags** : `ubuntu2404`, `graylog`, `datanode`, `mongodb`, `secrets`, `pare-feu`

---

## Problème précis à résoudre

Limiter les flux et préparer les secrets partagés.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les ports en écoute :
   ```bash
   sudo ss -tlnp | grep -E ':(27017|9000|9200)\b' || echo 'rien en écoute'
   ```
   👉 Explication : MongoDB 27017 et l'interface de recherche du Data Node ne doivent pas être joignables par le réseau utilisateur.

2. Générer un secret `password_secret` aléatoire (à placer dans le coffre, jamais dans un ticket) :
   ```bash
   openssl rand -hex 48
   ```
   👉 Explication : ce secret doit être identique sur Graylog Server et Data Node.

3. Limiter les règles du pare-feu aux adresses des composants et postes d'administration (UFW; adresses d'exemple à remplacer) :
   ```bash
   sudo ufw allow from 192.0.2.0/24 to any port 9000 proto tcp
   sudo ufw status numbered
   ```
   👉 Explication : n'ouvrir que les ports réellement activés.

## 2. Production — Contrôles

Documenter chaque port, protocole et source de journaux prévue.

## 3. Production — Sécurité

- Ne pas utiliser les valeurs de démonstration ni recopier de secrets dans la fiche.

## Validation et retour arrière

- **Validation** : ports internes non exposés, secrets en coffre.
- **Retour arrière** : `sudo ufw delete NUMERO` (numéro relevé dans `ufw status numbered`).

## Si le problème n'est pas résolu

- [Graylog 7.2 — installation Ubuntu](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm)
- [Graylog — sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)
- [Guide complet Graylog Ubuntu 24.04](../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/49_Deploiement_Graylog_7.2_Ubuntu_24.04.md#2-reseau-et-secrets)
