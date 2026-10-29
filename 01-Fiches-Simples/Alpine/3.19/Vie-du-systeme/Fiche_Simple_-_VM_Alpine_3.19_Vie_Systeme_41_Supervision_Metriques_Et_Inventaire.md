# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-41`

---

## Problème précis à résoudre

Superviser la machine avec Zabbix.

## 1. Hors-Production (Lab / Test / POC)

1. Installer l'agent (remplacer `SERVEUR_ZABBIX`) :
   ```sh
   doas apk add zabbix-agent
   doas sed -i 's/^Server=.*/Server=SERVEUR_ZABBIX/' /etc/zabbix/zabbix_agentd.conf
   ```
   👉 Explication : installe l'agent et l'autorise à répondre au serveur.

2. Activer et démarrer le service :
   ```sh
   doas rc-update add zabbix-agentd default
   doas rc-service zabbix-agentd start
   ```
   👉 Explication : le service `zabbix-agentd` démarre avec la machine.

3. Contrôler l'état :
   ```sh
   rc-service zabbix-agentd status
   ss -tlnp | grep 10050
   ```
   👉 Explication : l'agent écoute sur le port 10050; ouvrir ce port pour le serveur seul dans le pare-feu.

## 2. Production — Contrôles

Définir les déclencheurs (disque, mémoire, services, NTP).

## 3. Production — Sécurité

Limiter `Server=` au serveur Zabbix, ne pas autoriser `0.0.0.0/0`.

## Validation et retour arrière

- **Validation** : L'hôte apparaît en disponible dans la supervision.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Supervision Zabbix Agent](<../Vie-du-logiciel/Zabbix/Fiche_Simple_-_LXC_Alpine_3.19_Supervision_Zabbix_Agent.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
