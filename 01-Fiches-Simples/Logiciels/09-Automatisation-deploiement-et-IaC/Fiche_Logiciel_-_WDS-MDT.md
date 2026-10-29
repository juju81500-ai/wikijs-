# 📄 WDS + MDT

- **Catégorie** : Automatisation, déploiement et IaC
- **Plateforme** : Windows / Linux
- **Produit (matrice)** : WDS + MDT / FOG Project
- **Statut dans le pack** : Couvert — Windows Server 2022 (7 fiches). Windows Server 2025 non couvert : limite WDS documentée par Microsoft (voir Couverture).
- **Tags** : `logiciel`, `09-Automatisation-deploiement-et-IaC`, `couvert`

## 📚 Couverture dans le pack

Série Windows Server 2022 en 7 fiches : prérequis, installation, configuration, sécurisation, recette PXE, sauvegarde et maintenance. La [procédure historique WDS/MDT](Fiche_Simple_-_WDS-MDT.md) reste disponible et n’est pas dupliquée. Windows Server 2025 : non couvert — Microsoft documente que le déploiement WDS depuis le `boot.wim` des médias Windows 11 et des versions futures de Windows Server est bloqué (PXE vers images personnalisées MDT/Configuration Manager non affecté) et recommande Configuration Manager ou MDT; aucune procédure 2025 n’est inventée ici. Le statut de support de MDT est à vérifier sur Microsoft Learn.

Fiches simples du guide : [prérequis et limites](../../Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Prerequis_Limites.md), [installation](../../Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Installer.md), [configuration](../../Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Configurer.md), [sécurisation](../../Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Securisation.md), [recette PXE](../../Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Recette.md), [sauvegarde et restauration](../../Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Sauvegarde_Restauration.md), [maintenance et retour arrière](../../Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Maintenance_Retour_arriere.md)

Procédure d’installation/configuration déjà existante : [WDS + MDT](Fiche_Simple_-_WDS-MDT.md).

## 🧭 Utilisation

Cette fiche est le point d'entrée du logiciel : elle indique si le pack contient une procédure et renvoie vers elle. Pour une procédure pas à pas, ouvrir le guide ou la fiche liée ci-dessus. Lorsque le statut est `Manquant`, aucune procédure dédiée n'existe encore dans le pack.

Procédure pas à pas du pack : [WDS + MDT](Fiche_Simple_-_WDS-MDT.md).
