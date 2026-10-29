---
title: "Fiche Simple - Windows Server 2022 VMware Horizon Prerequis Limites"
description: "Cadrer prérequis, licences et limites avant de déployer VMware Horizon (Connection Server, agent, pools, UAG) sur Windows Server 2022."
published: true
date: 2026-10-29T20:56:41Z
tags: ["vmware-horizon", "horizon", "windows-server", "prerequis"]
editor: markdown
dateCreated: 2026-10-29T20:56:41Z
dateModified: 2026-10-29T20:56:41Z
---

# Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Prerequis_Limites

- **Environnement** : Serveurs Windows Server 2022 (Connection Server), vCenter, UAG, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version Horizon à vérifier auprès de l'éditeur
- **Catégorie** : VDI / Horizon
- **Tags** : `vmware-horizon`, `horizon`, `windows-server`, `prerequis`

---

## Problème précis à résoudre

Cadrer prérequis, licences et limites avant de déployer VMware Horizon (Connection Server, agent, pools, UAG) sur Windows Server 2022.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier dans la matrice d'interopérabilité officielle que Windows Server 2022 est pris en charge pour la version VERSION_HORIZON (à remplacer) pour le Connection Server et l'Horizon Agent, et noter l'éditeur actuel du produit (renommage possible Omnissa) : vérifier la version publiée.
   👉 Explication : le support dépend de la version ; ne pas supposer.

2. Lister les éléments : CS1_HORIZON (Connection Server), VCENTER_FQDN (vCenter), VM_MODELE (image parente), UAG1_HORIZON (Unified Access Gateway), DOMAINE_AD.
   👉 Explication : placeholders à remplacer par vos noms DNS.

3. Contrôler le réseau et le DNS depuis CS1_HORIZON. PowerShell :
```powershell
Resolve-DnsName VCENTER_FQDN
Test-NetConnection VCENTER_FQDN -Port 443
Get-ComputerInfo -Property CsDomain,OsName
```
   👉 Explication : 443 vers vCenter est indispensable ; CsDomain doit être le domaine cible.

4. Cadrer les licences : clé de licence Horizon (édition selon contrat) à saisir dans la console, plus licences Windows Server/Client adaptées aux postes virtuels.
   👉 Explication : la clé ne doit jamais figurer dans une fiche.

5. Prévoir un compte de service vCenter à privilèges minimaux pour Horizon, nommé COMPTE_HORIZON_VC (à remplacer).
   👉 Explication : respecte le moindre privilège ; liste des privilèges dans la doc officielle.

## 2. Production — Contrôles

- Matrice d'interopérabilité validée.
- Lab d'abord.

## 3. Production — Sécurité

- Pas de mot de passe dans la fiche.
- Pas d'exposition Internet directe du Connection Server : passer par UAG.

## Validation et retour arrière

- **Validation** : Prérequis documentés et réseau validé.
- **Retour arrière** : Aucune installation à ce stade.

## Si le problème n'est pas résolu

- [Documentation Horizon (Omnissa/VMware)](https://docs.omnissa.com/)
- [Broadcom TechDocs — Horizon](https://techdocs.broadcom.com/)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-vmware-horizon)