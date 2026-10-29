# 📄 Fiche_Simple_-_VM_Debian_13_Elastic_Verifier_Sante_TLS.md

- **Environnement** : Elasticsearch 9.5.x et Kibana 9.5.x auto-hébergés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Journaux / exploitation
- **Tags** : `debian13`, `elasticsearch`, `kibana`, `tls`, `logs`, `diagnostic`

---

## 🎯 Problème précis à résoudre

Vérifier l'état des services et l'accès TLS à Elasticsearch/Kibana après l'installation.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Contrôler les services et leurs journaux :
   ```bash
   sudo systemctl --no-pager status elasticsearch kibana
   sudo journalctl -u elasticsearch -b --no-pager | tail -30
   sudo journalctl -u kibana -b --no-pager | tail -30
   ```
   👉 Explication : les deux services doivent être `active (running)`.

2. Tester l'API en HTTPS avec la CA du cluster (le secret est saisi, pas écrit) :
   ```bash
   read -rsp "Mot de passe du compte de contrôle : " EPW; echo
   curl --cacert /etc/elasticsearch/certs/http_ca.crt -u COMPTE_CONTROLE:"$EPW" https://127.0.0.1:9200/_cluster/health?pretty
   unset EPW
   ```
   👉 Explication : jamais `curl -k`; utiliser un compte dédié et non `elastic`; le statut attendu est `green` (ou `yellow` en lab mono-nœud).


## ⚡ 2. Production — Façon Simplifiée

1. Contrôler l'espace disque et les ports :
   ```bash
   df -h /var/lib/elasticsearch
   sudo ss -ltnp | grep -E ':(9200|9300|5601)\b'
   ```
   👉 Explication : 9200/9300 réservés aux composants, 5601 aux administrateurs ou au proxy TLS.

2. Dans Kibana : **Stack Management > Index Management** (santé des index) et **Stack Management > Snapshot and Restore** (dernière sauvegarde).
   👉 Explication : vérifier aussi que les versions Elasticsearch et Kibana sont identiques.


## 🔒 3. Production — Façon Sécurisée

- Garder ports 9200/9300 sur les réseaux de composants; limiter 5601 aux administrateurs ou au proxy TLS.
- Utiliser rôles dédiés et API keys à privilèges minimaux; ne pas effectuer le contrôle courant avec `elastic`.
- Ne pas copier CA, enrollment token, API key ou mot de passe dans le wiki ou un ticket.

## ✅ Validation et retour arrière

- **Validation** : services actifs, API répondant en TLS vérifié, Kibana joignable et cluster en état attendu.
- **Retour arrière** : si une modification de config a provoqué une panne, restaurer le fichier sauvegardé, valider YAML et redémarrer uniquement le service concerné.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : consulter la documentation officielle Elastic ci-dessous.
- [Elastic — Vérifier Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package)