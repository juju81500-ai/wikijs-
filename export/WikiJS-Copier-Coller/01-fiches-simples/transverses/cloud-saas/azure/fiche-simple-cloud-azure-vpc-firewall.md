# Fiche_Simple_-_Cloud_Azure_VPC_Firewall

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Azure CLI (az ; version publiée à vérifier)
- **Catégorie** : cloud public / vnet et pare-feu

---

## Problème précis à résoudre

VNet et pare-feu dans Microsoft Azure en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Virtual networks → Create ; Network security groups → Create ; Subnets → associer le NSG.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Azure CLI (az ; version publiée à vérifier)) :
   ```bash
   az network vnet create --resource-group GROUPE --name NOM_VNET --address-prefixes CIDR_VNET --subnet-name NOM_SUBNET --subnet-prefixes CIDR_SUBNET
az network nsg list --resource-group GROUPE
   ```
   👉 Explication : Valider le plan IP, les routes et les règles NSG avant attachement ; n’autoriser SSH/RDP que depuis IP_ADMIN/32 ou via Bastion/VPN.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Faire approuver CIDR, sous-réseaux, routes, flux entrants/sortants, DNS et accès d’administration. Vérifier qu’aucune règle SSH/RDP ne cible Internet entier.

## 3. Production — Sécurité

Appliquer le moindre privilège, filtrer IPv4 et IPv6, journaliser les flux sensibles et utiliser VPN/bastion/accès managé. Ne pas ouvrir de port d’administration au monde.

## Validation et retour arrière

- **Validation** : Connectivité autorisée vérifiée depuis la source prévue et flux non autorisé refusé ; règles enregistrées et propriétaires identifiés.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [Microsoft Azure — documentation officielle](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview)
- [Référence et bonnes pratiques](https://learn.microsoft.com/azure/virtual-network/network-security-groups-overview)
- [Fiche d’entrée Microsoft Azure](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-microsoft-azure)