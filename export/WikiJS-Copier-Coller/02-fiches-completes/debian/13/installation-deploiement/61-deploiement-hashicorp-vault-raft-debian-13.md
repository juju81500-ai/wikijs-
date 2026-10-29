# Déployer HashiCorp Vault avec stockage intégré Raft

- **OS / Version** : Debian 13 Trixie x86-64; édition et version Vault fixées selon le canal validé
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Cluster de trois nœuds Raft pour services et équipes autorisés
- **Catégorie** : Coffre de secrets / PKI / tokens

## 1. Choisir l'architecture

Fiche simple : [cadrer l'architecture Vault Raft](/01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-architecture).

Valider si Vault Community ou Enterprise répond au besoin et à la licence. Pour la production, prévoir idéalement trois nœuds Vault dans des domaines de panne distincts, stockage Raft persistant, DNS stable, NTP, certificats TLS par nœud, supervision et sauvegarde des snapshots. Une instance unique est un lab, pas un service HA.

Définir les propriétaires, méthodes d'authentification, engines, politiques d'accès, rotation/TTL, audit, limites de requêtes et plan de reprise avant le premier secret.

## 2. Installer Vault

Fiche simple : [installer Vault](/01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-installer).

Installer une version officiellement supportée depuis le dépôt signé HashiCorp pour Debian/Ubuntu, ou télécharger le binaire et vérifier checksum/signature selon la procédure éditeur. Épingler la version validée pour le déploiement; ne pas suivre aveuglément `latest`.

Le paquet officiel crée un utilisateur système dédié et une unité systemd. Vérifier propriétaire et permissions des répertoires de configuration, données, certificats et logs. Ne pas exécuter Vault comme root.

## 3. Configurer TLS et stockage

Fiche simple : [configurer TLS et stockage Raft](/01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-tls-raft).

Utiliser des certificats émis par l'autorité approuvée avec SAN correspondant au DNS du nœud et chiffrer API (`8200`) et cluster (`8201`). Établir la chaîne de confiance client avant d'ouvrir l'accès. Dans `/etc/vault.d/vault.hcl`, configurer `api_addr`, `cluster_addr`, listener TCP TLS et backend `storage "raft"` avec `path` persistant et `node_id` unique par nœud.

Ne pas copier une configuration de développement. Le service doit être seul sur son hôte autant que possible; restreindre le pare-feu, désactiver les core dumps, évaluer swap/mlock selon le backend et les recommandations actuelles, protéger stockage et sauvegardes.

## 4. Démarrer, initialiser et joindre Raft

Fiche simple : [initialiser et joindre le cluster Raft](/01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-initialiser).

Vérifier la syntaxe de la configuration et l'unité avant activation. Démarrer les nœuds, confirmer TLS via CA vérifiée, puis initialiser le cluster une seule fois. La cérémonie d'initialisation produit des clés de déverrouillage et un token root initial : générer les seuils/parts selon le plan, remettre les parts à des détenteurs séparés, sauvegarder selon procédure et ne jamais conserver les valeurs en clair dans shell history, Wiki ou tickets.

Joindre les autres nœuds via `retry_join` et l'identité TLS; contrôler quorum, leader et santé avant de continuer. Si l'auto-unseal est utilisé, configurer une intégration KMS/HSM supportée et une identité machine, jamais une credential permanente en clair dans `vault.hcl`.

## 5. Créer les accès et audit

Fiche simple : [créer les accès et activer l'audit](/01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-acces-audit).

Utiliser le token root uniquement pour le bootstrap initial : activer une méthode d'authentification d'entreprise, créer des politiques explicites à moindre privilège et des tokens courts pour les workloads. Activer au moins un audit device avant usage opérationnel; expédier les audits vers un stockage central protégé.

Tester un secret synthétique avec un rôle de service dédié, vérifier refus d'accès hors politique, TTL/renouvellement et révocation. L'interface Web est une option d'administration, pas un substitut à IAM ou audit.

## 6. Vérifier et exploiter

Fiche simple : [vérifier et exploiter Vault](/01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-verifier-exploiter).

```bash
sudo systemctl --no-pager status vault
sudo journalctl -u vault -b --no-pager
vault status
```

Utiliser `VAULT_ADDR` en HTTPS et `VAULT_CACERT` vers la CA approuvée; ne pas employer `VAULT_SKIP_VERIFY`. Surveiller quorum, latence, intégrité des snapshots, espace, certificats, audit, erreurs d'authentification et versions.

Créer des snapshots Raft chiffrés/stockés en lieu séparé suivant la procédure HashiCorp et tester une restauration dans un environnement isolé. Sauvegarder aussi la configuration et les éléments de seal/recovery nécessaires, séparément des données Vault. Revoir les plans d'accès et révoquer les identifiants des comptes sortants.

## Sources

- [HashiCorp — Installer Vault](https://developer.hashicorp.com/vault/install)
- [HashiCorp — Déployer Vault avec Integrated Storage/Raft](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-deployment-guide)
- [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [HashiCorp — Configuration Integrated Storage](https://developer.hashicorp.com/vault/docs/configuration/storage/raft)