# Déployer une plateforme Wazuh 4.x sur Debian 12

- **Environnement** : Lab ou plateforme de sécurité dimensionnée, idéalement composants séparés à l'échelle
- **Composants** : Manager, indexer et dashboard ; agents sur les systèmes supervisés
- **Tags** : `wazuh`, `siem`, `xdr`, `debian12`, `logs`, `securite`

## 1. Dimensionnement et prérequis

Fiche simple : [dimensionner et préparer la plateforme](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Wazuh/Fiche_Simple_-_VM_Debian_12_Wazuh_Dimensionner_Preparer.md).

Choisir une version Wazuh 4.x encore maintenue et vérifier la matrice officielle pour OS, versions Java/OpenSearch embarquées, tailles de nœuds et limites d'index. Dimensionner CPU, RAM, stockage rapide et rétention à partir du débit réel de logs. Un nœud unique convient à un lab, pas à une architecture HA.

Définir DNS, synchronisation horaire, certificats, réseau d'administration, sources de journaux et durée de conservation. Ne jamais collecter des secrets non nécessaires.

## 2. Déployer selon l'architecture officielle

Fiche simple : [déployer l'architecture Wazuh](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Wazuh/Fiche_Simple_-_VM_Debian_12_Wazuh_Installer_Architecture.md).

Télécharger le dépôt ou l'assistant d'installation correspondant exactement à la version retenue depuis le projet officiel Wazuh. Vérifier les sommes/signatures publiées, lire le script avant exécution et épingler la version. Ne pas exécuter un script distant non vérifié avec privilèges root.

Pour un lab, suivre le guide officiel d'installation all-in-one. Pour la production, utiliser les procédures multi-nœuds et certificats dédiés ; ne pas convertir un lab en HA par simple clonage.

Protéger les certificats, clés et mots de passe générés pendant l'installation. Les conserver dans un coffre sécurisé, pas dans les logs ni dans le dépôt documentaire.

## 3. Connecter les agents

Fiche simple : [enrôler les agents pilotes](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Wazuh/Fiche_Simple_-_VM_Debian_12_Wazuh_Enroler_Agents.md).

Autoriser les ports d'enrôlement, d'événements et d'administration uniquement entre les réseaux et hôtes concernés, selon la version Wazuh. Installer un agent depuis le dépôt signé correspondant à l'OS, l'enrôler avec la méthode officielle puis tester sur un hôte pilote avant déploiement massif.

Vérifier qu'une modification de configuration produit un événement attendu et qu'un agent hors ligne déclenche une alerte.

## 4. Contrôles opérationnels

Fiche simple : [valider les contrôles opérationnels](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Wazuh/Fiche_Simple_-_VM_Debian_12_Wazuh_Controles_Operationnels.md).

- Vérifier l'état des composants, la santé du cluster et l'espace d'index.
- Configurer TLS pour l'interface et les communications inter-composants.
- Limiter les comptes du dashboard selon le principe du moindre privilège.
- Superviser la file d'ingestion, les certificats, les expirations et l'heure système.

## 5. Sauvegarde et mises à jour

Fiche simple : [sauvegarder et mettre à jour](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Wazuh/Fiche_Simple_-_VM_Debian_12_Wazuh_Sauvegarder_Mettre_A_Jour.md).

Sauvegarder configuration, certificats et index selon une procédure compatible avec la version déployée. Tester une restauration sur un environnement séparé. Mettre à niveau les composants selon l'ordre et les chemins supportés par Wazuh ; ne pas mettre à jour un seul nœud hors séquence. En incident, préserver les journaux et l'état des index avant toute réinstallation.
