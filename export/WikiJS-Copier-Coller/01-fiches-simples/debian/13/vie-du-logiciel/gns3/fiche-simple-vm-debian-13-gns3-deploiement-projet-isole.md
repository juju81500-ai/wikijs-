# Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Projet_Isole.md

- **Environnement** : Poste Debian 13 graphique avec GNS3
- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Catégorie** : simulation reseau / projet

---

## Problème précis à résoudre

Lancer GNS3 avec un serveur local et un projet fermé.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'interface :
   ```bash
   gns3
   ```
   👉 Explication : l'assistant de premier démarrage s'ouvre.

2. Dans l'assistant, choisir **Run appliances on my local computer** et vérifier que l'adresse du serveur est `127.0.0.1`.
   👉 Explication : le serveur reste local, sans compute distant.

3. Créer le projet : **File > New blank project**, nom au choix, puis dessiner une topologie simple avec des éléments intégrés.
   👉 Explication : on teste sans image propriétaire.

4. Enregistrer puis rouvrir : **File > Save project**, fermer, puis **File > Open project**.
   👉 Explication : le projet doit se rouvrir sans fichier manquant.

5. Si une appliance QEMU est ajoutée, vérifier l'empreinte de l'image publiée par l'éditeur (remplacer `image.qcow2` par le fichier réel) :
   ```bash
   sha256sum image.qcow2
   ```
   👉 Explication : on compare le résultat avec l'empreinte officielle avant import.

## 2. Production — Contrôles

Définir qui valide les images, les licences et les ressources attribuées aux nœuds.

## 3. Production — Sécurité

- Ne pas relier le nœud Cloud à une interface physique ni ajouter de NAT pour un lab fermé.
- Ne pas télécharger d'images depuis des miroirs non autorisés.

## Validation et retour arrière

- **Validation** : Projet de test créé, enregistré et rouvert; aucun lien externe.
- **Retour arrière** : Fermer le projet et le supprimer depuis **File > Open project** après sauvegarde si nécessaire.

## Si le problème n'est pas résolu

- [GNS3 — installation Linux](https://docs.gns3.com/docs/getting-started/installation/linux)
- [GNS3 — Marketplace](https://www.gns3.com/marketplace/appliances)
- [Guide complet GNS3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13#5-configurer-le-serveur-local-et-lancer-un-projet-isole)