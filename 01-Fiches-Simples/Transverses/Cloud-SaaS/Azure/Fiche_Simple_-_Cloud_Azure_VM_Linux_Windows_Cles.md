# Fiche_Simple_-_Cloud_Azure_VM_Linux_Windows_Cles

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Azure CLI (az ; version publiée à vérifier)
- **Catégorie** : cloud public / vm linux et windows avec accès par clé
- **Tags** : `azure`, `vm_linux_windows_cles`, `securite`, `procedure`

---

## Problème précis à résoudre

VM Linux et Windows avec accès par clé dans Microsoft Azure en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Virtual machines → Create → Azure virtual machine ; Linux : Authentication type SSH public key ; Windows : identité et accès via Bastion.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Azure CLI (az ; version publiée à vérifier)) :
   ```bash
   az vm create --resource-group GROUPE --name VM_LINUX --image Ubuntu2404 --admin-username UTILISATEUR --authentication-type ssh --ssh-key-values ~/.ssh/id_ed25519.pub
az vm show --resource-group GROUPE --name VM_LINUX
   ```
   👉 Explication : Pour Linux, fournir une clé publique et tester SSH depuis le réseau autorisé. Windows n’utilise pas par défaut cette clé pour l’ouverture de session ; préférer Azure Bastion/Entra ou configurer OpenSSH et une clé séparément. Éviter les secrets de mot de passe dans la ligne de commande.
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

- [Microsoft Azure — documentation officielle](https://learn.microsoft.com/azure/virtual-machines/linux/quick-create-portal)
- [Référence et bonnes pratiques](https://learn.microsoft.com/azure/virtual-machines/linux/ssh-from-windows)
- [Fiche d’entrée Microsoft Azure](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Microsoft-Azure.md)
