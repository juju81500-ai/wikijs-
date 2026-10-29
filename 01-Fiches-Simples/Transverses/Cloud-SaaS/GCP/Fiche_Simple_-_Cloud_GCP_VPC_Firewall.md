# Fiche_Simple_-_Cloud_GCP_VPC_Firewall

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / vpc et pare-feu
- **Tags** : `gcp`, `vpc_firewall`, `securite`, `procedure`

---

## Problème précis à résoudre

VPC et pare-feu dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : VPC network → VPC networks → Create VPC network ; Firewall → Create firewall rule.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud compute networks create NOM_VPC --subnet-mode=custom
gcloud compute firewall-rules create REGLE_SSH --network=NOM_VPC --direction=INGRESS --action=ALLOW --rules=tcp:22 --source-ranges=IP_ADMIN/32
   ```
   👉 Explication : Créer des sous-réseaux non chevauchants ; ne jamais autoriser SSH/RDP depuis 0.0.0.0/0. Vérifier les règles effectives et les tags/comptes de service ciblés.
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

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/vpc/docs/vpc)
- [Référence et bonnes pratiques](https://cloud.google.com/firewall/docs/firewalls)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
