# Kismet : détection sans fil passive et autorisée en laboratoire

- **OS / Version** : Linux avec adaptateur Wi-Fi compatible (mode moniteur)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Inventaire passif des points d'accès et des clients d'un environnement radio autorisé, détection de points d'accès non autorisés
- **Catégorie** : Sécurité sans fil
- **Tags** : `kismet`,`wifi`,`passif`,`rogue-ap`,`laboratoire`

## 1. Portée, hypothèses et licences

- Kismet est un outil de détection passive (écoute des trames, sans émission) sous licence GPL. L'usage couvre l'inventaire de **votre** environnement radio.
- Toute action décrite ici s'exécute uniquement sur des systèmes que vous possédez ou pour lesquels vous disposez d'une autorisation écrite (périmètre, dates, contacts). L'écoute de communications de tiers peut être pénalement sanctionnée (en France, atteinte au secret des correspondances et accès frauduleux : se référer au Code pénal). Aucune capture du contenu de communications n'est autorisée : on se limite aux métadonnées de gestion (SSID, BSSID, canal, chiffrement).
- Interdit : désauthentification, brouillage, attaques de mots de passe, déchiffrement de trafic, collecte dans un lieu public ou chez un tiers.
- Hypothèses : lab radio ou site de l'organisation, autorisation écrite précisant bâtiments, bandes et durée.

## 2. Prérequis

- Machine Linux dédiée ou [[Glossary:VM]] avec passage [[Glossary:USB]] d'un adaptateur Wi-Fi capable de mode moniteur (la compatibilité du pilote est à vérifier dans la documentation Kismet).
- Liste de référence des SSID/BSSID légitimes de l'organisation.
- Espace de stockage et procédure de purge des journaux.

## 3. Installation

1. Suivre la page d'installation Linux officielle de Kismet pour votre distribution (dépôts de paquets fournis par le projet ou paquet de la distribution), en vérifiant la source de signature.
2. Ajouter l'utilisateur d'exploitation au groupe prévu par le paquet pour accéder aux sources de capture sans exécuter l'interface en root (le nom du groupe et la procédure figurent dans la documentation ; l'installation propose un assistant pour les binaires privilégiés).
3. Contrôler :

```bash
kismet --version
ip link
```

## 4. Lancer une collecte passive autorisée

1. Identifier l'interface Wi-Fi (`ip link`). Kismet gère lui-même le mode moniteur à partir de la source de capture ; ne pas mélanger avec une autre application utilisant l'interface.
2. Démarrer la collecte :

```bash
kismet -c wlan0
```

3. Au premier lancement, créer les identifiants de l'interface web (la page par défaut écoute en local sur le port 2501) ; ne pas l'exposer hors de l'hôte et y accéder par tunnel [[Glossary:SSH]] si besoin.
4. Limiter les canaux ou bandes à ceux du périmètre autorisé dans les paramètres de la source.

## 5. Exploitation défensive

- Comparer les réseaux détectés à la liste de référence ; marquer les SSID inconnus, les SSID légitimes émis par un BSSID inconnu (point d'accès pirate potentiel) et les modes de chiffrement faibles (ouvert, WEP).
- Exporter l'inventaire (journaux au format Kismet, conversions proposées par les outils du projet) et le joindre au rapport.
- Toute découverte hors périmètre est consignée sans investigation supplémentaire et remontée au responsable.
- Purger les journaux selon la rétention validée.

## 6. Validation

- Kismet démarre sans émission (aucune association à un réseau) et détecte le point d'accès de lab connu.
- Le rapport liste exactement les équipements radio du périmètre, et les écarts ont un ticket.
- L'interface web n'est joignable que depuis l'hôte ou le tunnel.
- Aucun contenu applicatif n'est stocké.

## 7. Retour arrière

Arrêter Kismet (Ctrl+C dans le terminal ou arrêt du service), rendre l'interface à `NetworkManager` (redémarrage du service réseau ou de l'interface), supprimer les journaux et retirer l'utilisateur du groupe de capture. Restaurer le snapshot de la VM le cas échéant.

## Sources officielles

- [Kismet — documentation](https://www.kismetwireless.net/docs/)
- [Kismet — installation Linux](https://www.kismetwireless.net/docs/readme/installing/linux/)
- [Kismet — sources de capture](https://www.kismetwireless.net/docs/readme/datasources/datasources/)

Aucune capture radio n'a été effectuée pendant la rédaction ; l'adaptateur et le pilote doivent être validés dans le lab.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |
