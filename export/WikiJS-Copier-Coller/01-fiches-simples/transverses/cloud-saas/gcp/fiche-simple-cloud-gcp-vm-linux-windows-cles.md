# Fiche_Simple_-_Cloud_GCP_VM_Linux_Windows_Cles

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / vm linux et windows avec accès par clé

---

## Problème précis à résoudre

VM Linux et Windows avec accès par clé dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Compute Engine → VM instances → Create instance ; OS and storage → Boot disk ; Security and access ; Networking.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud compute instances create VM_LINUX --zone=ZONE --image-family=debian-12 --image-project=debian-cloud --metadata=enable-oslogin=TRUE
gcloud compute ssh VM_LINUX --zone=ZONE
   ```
   👉 Explication : OS Login et `gcloud compute ssh` fournissent un parcours Linux avec clés gérées. Windows n’accepte pas SSH par défaut : administrer via RDP/IAP/Bastion autorisé ou installer/configurer OpenSSH selon la documentation avant d’utiliser une clé.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Valider image et éditeur, taille, patching, chiffrement, rôle, sauvegarde, coût et réseau. Documenter la rotation/récupération des clés et l’accès de secours.

## 3. Production — Sécurité

Protéger la clé privée dans un coffre, désactiver les comptes/services inutiles, utiliser accès temporaire et MFA, ne pas inscrire de secrets dans user-data ou métadonnées.

## Validation et retour arrière

- **Validation** : Connexion Linux par clé testée et accès Windows conforme à la méthode retenue ; accès hors réseau autorisé refusé.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/compute/docs/instances/create-start-instance)
- [Référence et bonnes pratiques](https://cloud.google.com/compute/docs/connect/ssh-keys)
- [Fiche d’entrée Google Cloud Platform](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-google-cloud-platform)