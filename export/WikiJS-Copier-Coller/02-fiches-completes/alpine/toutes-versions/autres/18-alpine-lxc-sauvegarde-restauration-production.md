# Sauvegarder et restaurer un LXC Alpine en production

- **Type de fiche** : Autres — sauvegarde / reprise
- **Environnement** : Proxmox VE avec CT Alpine et Proxmox Backup Server ou stockage de sauvegarde dédié
- **OS / Version** : Alpine Linux, version maintenue choisie pour le service
- **Rôle** : Définir la sauvegarde, le test de restauration et la bascule de reprise

## 1. Concevoir la protection

Fiche simple : [cadrer la protection](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-lxc-alpine-sauvegarde-cadrer-protection).

Inventorier données persistantes, fichiers de configuration, secrets, montages, tâches planifiées, identifiant CT, hostname, IP, bridge/VLAN et dépendances. Distinguer une sauvegarde du CT d'une sauvegarde applicative cohérente : les bases de données peuvent nécessiter un dump natif ou l'arrêt propre des écritures.

Choisir une cible distincte du nœud protégé, une rétention, un chiffrement si requis et les responsables de récupération. Un snapshot local ne remplace pas une copie indépendante.

## 2. Préparer Proxmox Backup Server

Fiche simple : [configurer PBS pour le CT](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-lxc-alpine-sauvegarde-configurer-pbs).

Depuis PVE, ajouter le datastore PBS avec certificat/empreinte validés et compte/token dédié aux droits minimaux. Créer une tâche de sauvegarde pour le CT et vérifier mode, planification, rétention, chiffrement et notifications selon le stockage et la politique de l'organisation.

Pour un test manuel ponctuel sur le nœud PVE :

```bash
vzdump <CTID> --storage <STOCKAGE_PBS> --mode snapshot
```

Le mode doit être pris en charge par le stockage; choisir une fenêtre d'arrêt si l'application ne tolère pas un snapshot à chaud.

## 3. Vérifier le résultat de sauvegarde

Fiche simple : [vérifier le résultat de sauvegarde](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-lxc-alpine-sauvegarde-verifier-resultat).

- Contrôler le journal du job dans PVE/PBS, la date, la durée et les données incluses.
- Vérifier l'espace, la rétention et l'intégrité de la cible PBS.
- Sauvegarder les clés de chiffrement et secrets hors du CT, dans le coffre prévu.
- Conserver le fichier de configuration CT et la liste des montages réseau/hôte.

## 4. Tester une restauration isolée

Fiche simple : [restaurer le CT en isolation](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-lxc-alpine-sauvegarde-restaurer-isoler).

Dans PVE/PBS, sélectionner un point de sauvegarde validé et restaurer vers un **ID CT temporaire**. Connecter le CT restauré à un bridge/VLAN isolé ou lui donner une IP de test distincte avant démarrage.

Vérifier dans Alpine :

```sh
cat /etc/alpine-release
ip -br addr
ip route
rc-status
```

Puis contrôler volumes, propriétaires, secrets, logs et fonction applicative. Pour les bases, effectuer aussi une restauration applicative cohérente et un test de lecture/écriture métier.

## 5. Reprise en production

Fiche simple : [reprendre le service en production](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-lxc-alpine-sauvegarde-reprise-production).

1. Déclarer l'incident et geler les écritures sur l'ancien service si possible.
2. Choisir le point de sauvegarde; noter l'ID source et la destination.
3. Restaurer en environnement isolé et valider avant la bascule.
4. Éteindre l'ancien CT ou isoler son réseau avant de réutiliser IP, DNS ou tâches planifiées.
5. Basculer l'adresse/DNS/VIP selon le plan, tester les clients, puis surveiller.

## 6. Retour arrière et conservation

Fiche simple : [gérer le retour arrière et la conservation](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-lxc-alpine-sauvegarde-retour-arriere-conservation).

Si le test échoue, garder le CT restauré isolé et remettre l'ancien service en fonctionnement après confirmation qu'il n'y a pas d'écritures concurrentes. Ne jamais démarrer simultanément deux CT portant la même IP ou exécutant les mêmes traitements.

Conserver l'ancienne instance et le point de sauvegarde jusqu'à la période d'acceptation; documenter le RPO/RTO réellement mesuré.

## Sources

- [Proxmox VE — vzdump](https://pve.proxmox.com/pve-docs/vzdump.1.html)
- [Proxmox Backup Server — Documentation](https://pbs.proxmox.com/docs/)
- [Proxmox Backup Server — Vérification d'intégrité](https://pbs.proxmox.com/docs/maintenance.html)