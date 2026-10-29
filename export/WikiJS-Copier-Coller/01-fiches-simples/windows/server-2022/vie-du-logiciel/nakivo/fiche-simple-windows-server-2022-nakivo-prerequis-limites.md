# Fiche_Simple_-_Windows_Server_2022_Nakivo_Prerequis_Limites

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `sauvegarde / restauration / NAKIVO`

---

## Problème précis à résoudre

Valider qu'un serveur Windows Server 2022 peut accueillir NAKIVO Director et Transporter. Périmètre : NAKIVO Backup & Replication Director et Transporter, un job de sauvegarde, restauration via l'interface web. Altaro/Hornetsecurity n'est pas couvert.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier Windows. PowerShell :
```powershell
Get-ComputerInfo -Property OsName,OsVersion
```
   👉 Explication : on confirme Windows Server 2022.

2. Vérifier l'espace libre pour le dépôt de sauvegarde. PowerShell :
```powershell
Get-Volume | Format-Table DriveLetter,FileSystemLabel,SizeRemaining,Size
```
   👉 Explication : le dépôt (repository) doit résider sur un volume dédié et suffisamment grand.

3. Lire la page System Requirements du Help Center NAKIVO (lien en bas) et vérifier la compatibilité de Windows Server 2022 et des plateformes à protéger avec la version courante du produit.
   👉 Explication : les exigences changent selon la version ; elles ne sont pas recopiées.

4. Prévoir les ports d'échange Director/Transporter et d'accès web, à relever dans la documentation officielle de la version.
   👉 Explication : les flux doivent être autorisés avant l'installation.

5. Noter les limites : Altaro/Hornetsecurity n'est pas couvert ; seule l'interface web est utilisée, aucun script n'est supposé.
   👉 Explication : le périmètre exact évite toute fausse impression de couverture.

## 2. Production — Contrôles

- Documenter les charges à protéger, la rétention et l'espace de stockage.
- Prévoir la licence ou l'essai auprès de NAKIVO.

## 3. Production — Sécurité

- Dépôt de sauvegarde séparé de la production sauvegardée.
- Pas de secret dans la fiche.

## Validation et retour arrière

- **Validation** : Version Windows, espace disque et exigences éditeur relevés.
- **Retour arrière** : Rien n'est modifié : aucun retour arrière.

## Si le problème n'est pas résolu

- [NAKIVO — Help Center officiel](https://helpcenter.nakivo.com/)
- [NAKIVO — System Requirements](https://helpcenter.nakivo.com/display/NH/System+Requirements)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)