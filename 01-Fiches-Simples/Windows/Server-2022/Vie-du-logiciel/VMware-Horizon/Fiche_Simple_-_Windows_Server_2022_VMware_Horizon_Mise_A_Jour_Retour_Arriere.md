# Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Mise_A_Jour_Retour_Arriere

- **Environnement** : Serveurs Windows Server 2022 (Connection Server), vCenter, UAG, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version Horizon à vérifier auprès de l'éditeur
- **Catégorie** : VDI / Horizon
- **Tags** : `vmware-horizon`, `horizon`, `windows-server`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour Horizon et revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes de version et l'ordre de mise à niveau officiel (Connection Servers, puis agents, puis clients, UAG à vérifier).
   👉 Explication : respecter la compatibilité.

2. Sauvegarder (fiche dédiée) et faire un snapshot de CS1_HORIZON.
   👉 Explication : point de retour.

3. Sur chaque Connection Server, exécuter l'installeur de la nouvelle version VERSION_HORIZON_CIBLE en administrateur.
   👉 Explication : mise à niveau sur place ; faire un serveur à la fois.

4. Mettre à jour l'agent dans VM_MODELE, créer un nouveau snapshot et pousser le pool : GUI **Inventory > Desktops > NOM_POOL > Maintain > Schedule/Push Image**.
   👉 Explication : libellé à vérifier.

5. Mettre à jour l'UAG en redéployant la nouvelle OVA avec le fichier INI.
   👉 Explication : UAG se remplace plutôt que de se mettre à jour sur place.

## 2. Production — Contrôles

- Fenêtre de maintenance.
- Versions avant/après notées.

## 3. Production — Sécurité

- Médias issus du portail éditeur uniquement.

## Validation et retour arrière

- **Validation** : Version attendue, tableau de bord vert, session OK.
- **Retour arrière** : Restaurer le snapshot et la configuration exportée ; redéployer l'ancien UAG.

## Si le problème n'est pas résolu

- [Documentation Horizon (Omnissa/VMware)](https://docs.omnissa.com/)
- [Broadcom TechDocs — Horizon](https://techdocs.broadcom.com/)
- [Fiche d'entrée du logiciel](../../../../Logiciels/13-Poste-de-travail-et-VDI/Fiche_Logiciel_-_VMware-Horizon.md)
