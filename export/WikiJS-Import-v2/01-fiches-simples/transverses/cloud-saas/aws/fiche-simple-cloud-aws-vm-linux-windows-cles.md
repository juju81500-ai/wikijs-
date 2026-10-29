---
title: "Fiche Simple - Cloud AWS VM Linux Windows Cles"
description: "VM Linux et Windows avec accès par clé dans AWS en limitant les risques de sécurité, de disponibilité et de coût."
published: true
date: 2026-10-29T21:00:44Z
tags: ["aws", "vm_linux_windows_cles", "securite", "procedure"]
editor: markdown
dateCreated: 2026-10-29T21:00:44Z
dateModified: 2026-10-29T21:00:44Z
---

# Fiche_Simple_-_Cloud_AWS_VM_Linux_Windows_Cles

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / vm linux et windows avec accès par clé
- **Tags** : `aws`, `vm_linux_windows_cles`, `securite`, `procedure`

---

## Problème précis à résoudre

VM Linux et Windows avec accès par clé dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : EC2 → Key Pairs → Create key pair ; EC2 → Instances → Launch instances ; Connect → SSH client.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws ec2 run-instances --image-id AMI_VERIFIEE --instance-type TYPE_INSTANCE --key-name NOM_CLE --subnet-id ID_SUBNET --security-group-ids ID_SG --count 1
aws ec2 describe-instances --instance-ids ID_INSTANCE
   ```
   👉 Explication : La clé EC2 sert à SSH Linux ; sur Windows, elle permet généralement de déchiffrer le mot de passe Administrateur et n’active pas SSH. Utiliser Session Manager/Bastion ou configurer OpenSSH Windows explicitement. Ne jamais exposer la clé privée.
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

- [AWS — documentation officielle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)