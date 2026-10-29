# Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Creer_Valider_Lab

- **Environnement** : VM EVE-NG (appliance basée sur Ubuntu Server 24.04 LTS) hébergée sur un poste ou serveur de virtualisation
- **OS / Version** : EVE-NG 7.x (7.2.0-18 au contrôle du 29/10/2026), Ubuntu 24.04 LTS embarqué; Community 6.2.0-4 (Ubuntu 22.04) en fin de support juin 2026
- **Catégorie** : simulation réseau / validation

---

## Problème précis à résoudre

Créer un premier lab minimal et prouver que l'interface, les nœuds et les liens fonctionnent.

## 1. Hors-Production (Lab / Test / POC)

1. Se connecter à `https://IP_EVE/` avec un compte administrateur, puis dans le gestionnaire de fichiers cliquer sur **Add new lab**.
   👉 Explication : ouvre le formulaire de création de lab.

2. Renseigner **Name** = `LAB-VALIDATION` et **Version** = `1`, puis **Save**.
   👉 Explication : seuls le nom et la version sont obligatoires.

3. Dans le lab : clic droit sur une zone libre > **Node**, choisir le modèle **VPCS**, quantité `2`, **Save**. Si VPCS n'est pas proposé, utiliser une image déjà importée et autorisée.
   👉 Explication : les VPCS sont documentés comme illimités en Freemium et ne demandent pas d'image éditeur; ⚠️ la disponibilité du template dépend de la version installée.

4. Relier les deux nœuds en glissant le connecteur de `VPCS1` vers `VPCS2`.
   👉 Explication : crée un lien point à point isolé.

5. Cliquer sur **More actions > Start all nodes**, puis ouvrir la console de chaque nœud (clic sur l'icône).
   👉 Explication : démarre les nœuds et ouvre la console HTML5.

6. Dans `VPCS1` puis `VPCS2` :
   ```text
   ip 10.10.10.1/24   (sur VPCS1)
   ip 10.10.10.2/24   (sur VPCS2)
   ping 10.10.10.2    (sur VPCS1)
   ```
   👉 Explication : adresses privées d'exemple; la réponse du ping prouve que le lien est fonctionnel.

7. Cliquer sur **More actions > Stop all nodes**, puis **Wipe all nodes**.
   👉 Explication : remet le lab dans un état propre.

## 2. Production — Contrôles

- Surveiller CPU et RAM de la VM pendant le test (menu **System > System status**).
- Fermer le lab après usage pour libérer les ressources.
- Respecter la limite de nœuds de l'édition utilisée (7 nœuds en Freemium d'après les notes de version).

## 3. Production — Sécurité

- Ne pas utiliser le lab de validation pour tester des équipements avec des données de production.
- Verrouiller un lab partagé avec **Lock Lab** si besoin, en conservant le mot de passe : sa perte n'est pas récupérable sans le support éditeur.
- Ne pas connecter un nœud à un réseau réel (Cloud/Bridge) sans accord et isolation.

## Validation et retour arrière

- **Validation** : le ping entre `VPCS1` et `VPCS2` réussit et les nœuds s'arrêtent proprement.
- **Retour arrière** : dans le gestionnaire de fichiers, sélectionner `LAB-VALIDATION` puis **Delete**.

## Si le problème n'est pas résolu

- [EVE-NG — Professional Cookbook (PDF, chapitres 7 et 8)](https://www.eve-ng.net/wp-content/uploads/2026/09/EVE-PE-BOOK-7.9-2026.pdf)
- [EVE-NG — FAQ](https://www.eve-ng.net/index.php/faq/)
[EVE-NG — documentation officielle](https://www.eve-ng.net/index.php/documentation/)
- [Fiche logiciel EVE-NG](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-eve-ng)
- [Importer des images autorisées](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-importer-images-autorisees)
- [Sauvegarder et restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-sauvegarder-restaurer)