# Fiche_Simple_-_Cloud_AWS_VPC_Firewall

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / vpc et pare-feu

---

## Problème précis à résoudre

VPC et pare-feu dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : VPC → Your VPCs → Create VPC ; Subnets → Create subnet ; Security Groups → Create security group.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws ec2 create-vpc --cidr-block CIDR_VPC
aws ec2 describe-security-groups --filters Name=vpc-id,Values=ID_VPC
   ```
   👉 Explication : Créer un adressage non chevauchant et des règles minimales ; limiter SSH/RDP à IP_ADMIN/32 ou préférer un bastion/SSM.
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

- [AWS — documentation officielle](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)