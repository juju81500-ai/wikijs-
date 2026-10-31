# Politique de sécurité

## Règles pour le dépôt

Ne **jamais** committer :

- secrets : mots de passe, jetons API, clés privées (`*.pem`, `*.key`, `id_*`), certificats privés ;
- fichiers `.env*` et fichiers de configuration contenant des identifiants ;
- exports ou sauvegardes de données clients, dumps de bases, journaux contenant des données personnelles ;
- adresses, noms d'hôtes ou topologies réels d'un client ou d'un environnement de production.

Les fiches publiques ne contiennent **aucune donnée sensible** : utiliser des valeurs fictives (`192.0.2.0/24`, `exemple.local`, `<MOT_DE_PASSE>`).

## Gestion des secrets

- Les mots de passe et données sensibles sont conservés sur le serveur du mainteneur, dans un gestionnaire de secrets (coffre-fort type Vaultwarden/KeePassXC/Vault), pas dans Git.
- Accès selon le **principe du moindre privilège** : seules les personnes autorisées, avec les droits strictement nécessaires.
- Clés de déploiement (ex. stockage Git de Wiki.js) : lecture seule si possible, une clé par usage, rotation régulière.
- Le fichier `.gitignore` aide à éviter les erreurs, mais ne remplace pas la relecture du diff avant chaque commit.

## En cas de fuite accidentelle

1. **Révoquer/changer immédiatement** le secret exposé : supprimer le fichier du dépôt ne suffit pas, l'historique Git le conserve.
2. Prévenir le mainteneur par le canal non public ci-dessous.
3. Purger l'historique si nécessaire (`git filter-repo`) après révocation.

## Signaler une vulnérabilité ou une fuite

Merci de **ne pas ouvrir d'issue publique** ni de Pull Request publique pour un signalement de sécurité.

- Utiliser le signalement privé de GitHub : onglet **Security → Report a vulnerability** du dépôt (« private vulnerability reporting »), à activer par le mainteneur dans les paramètres du dépôt.
- À défaut, contacter le mainteneur par message privé via son profil GitHub.

Indiquer : la fiche ou le fichier concerné, la description, l'impact estimé et, si possible, une correction proposée. Un accusé de réception est envoyé dès que possible ; les détails sont rendus publics après correction.

## Contenu technique des fiches

Les commandes sont fournies à titre pédagogique : les tester d'abord en lab, appliquer les durcissements de manière progressive, et prévoir un retour arrière avant toute action en production.
