# Fiche_Simple_-_VM_Debian_12_Wazuh_Dimensionner_Preparer.md

- **Environnement** : plateforme Wazuh de test ou production dimensionnée; sources de logs autorisées
- **OS / Version** : version Wazuh 4.x maintenue, compatibilité Debian 12 à confirmer
- **Catégorie** : SIEM/XDR / cadrage
- **Tags** : `debian12`, `wazuh`, `siem`, `xdr`, `capacity`, `logs`

---

## Problème précis à résoudre

Préparer une plateforme Wazuh adaptée au volume réel et au niveau de disponibilité requis sans collecter de données superflues.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources de la VM :
   ```bash
   nproc; free -h; df -h /var/lib
   ```
   👉 Explication : comparer à la matrice officielle de la version retenue (CPU, RAM, stockage selon le nombre d'agents et la rétention).

2. Contrôler l'heure et le DNS :
   ```bash
   timedatectl | grep synchronized
   getent hosts wazuh.example.net
   ```
   👉 Explication : l'horloge conditionne les certificats et la corrélation des événements.

3. Consigner : version Wazuh 4.x maintenue, réseau d'administration, sources de journaux, durée de conservation.
   👉 Explication : ne jamais collecter de secrets non nécessaires.

## 2. Production — Contrôles

Faire approuver dimensions, rétention, disponibilité, sources, propriétaire métier, accès, sauvegarde et capacité d'évolution.

## 3. Production — Sécurité

- Ne pas considérer un nœud unique de lab comme une architecture HA.
- Ne pas collecter des secrets ou données hors périmètre.
- Limiter l'administration de la plateforme au réseau prévu.
- Ne pas déployer une version dont le support ou la compatibilité n'est pas confirmé.

## Validation et retour arrière

- **Validation** : version et architecture confirmées, débit estimé, réseau et périmètre de collecte approuvés.
- **Arrêt** : ne pas installer si les ressources, responsabilités ou sources de logs ne sont pas établies.

## Si le problème n'est pas résolu

- [Wazuh — documentation](https://documentation.wazuh.com/current/)
- [Wazuh — guide de déploiement](https://documentation.wazuh.com/current/deployment-options/index.html)
- [Guide complet Wazuh Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/11_SIEM_XDR_Centralise_Wazuh_4x_Debian_12.md)
