# Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Valider

- **Environnement** : Serveurs Windows Server 2022 (Connection Server), vCenter, UAG, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version Horizon à vérifier auprès de l'éditeur
- **Catégorie** : VDI / Horizon

---

## Problème précis à résoudre

Recetter Horizon : état des services, ouverture de session via UAG.

## 1. Hors-Production (Lab / Test / POC)

1. GUI **Monitor > Dashboard** : vérifier Connection Server, vCenter, pools et sessions en vert.
   👉 Explication : état global.

2. Contrôle PowerShell des services :
```powershell
Get-Service -DisplayName '*VMware Horizon*' | Where-Object Status -ne 'Running'
```
   👉 Explication : aucun résultat attendu.

3. Depuis un poste de test, ouvrir Horizon Client sur https://ADRESSE_UAG et lancer un bureau.
   👉 Explication : valide le chemin externe ; ADRESSE_UAG est à remplacer.

4. Vérifier dans **Monitor > Sessions** la session et le protocole.
   👉 Explication : confirme l'enregistrement de l'agent.

## 2. Production — Contrôles

- Consigner la recette.
- Mesurer le temps de connexion.

## 3. Production — Sécurité

- Compte de test à retirer ensuite.
- Contrôler qu'aucun accès direct au Connection Server n'est exposé.

## Validation et retour arrière

- **Validation** : Session ouverte via UAG, tableau de bord vert.
- **Retour arrière** : Corriger puis relancer, sinon revenir au snapshot.

## Si le problème n'est pas résolu

- [Documentation Horizon (Omnissa/VMware)](https://docs.omnissa.com/)
- [Broadcom TechDocs — Horizon](https://techdocs.broadcom.com/)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-vmware-horizon)