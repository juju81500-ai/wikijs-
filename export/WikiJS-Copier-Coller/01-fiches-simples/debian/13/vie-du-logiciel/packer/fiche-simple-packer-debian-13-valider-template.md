# Fiche simple — Initialiser et valider un template Packer

- **Environnement** : répertoire de template Packer avec connectivité aux dépôts de plugins approuvés
- **OS / Version** : Debian 13; Packer HCL2
- **Catégorie** : automatisation / validation

---

## Problème précis à résoudre

Initialiser les plugins déclarés et vérifier le format et la configuration sans construire d'image.

## 1. Hors-Production (Lab / Test / POC)

1. Initialiser (télécharge le plugin déclaré) :
   ```bash
   cd ~/packer-lab
   packer init .
   ```
   👉 Explication : crée `.packer.lock.hcl`, à conserver avec le template pour figer versions et empreintes des plugins.

2. Contrôler le format puis la configuration :
   ```bash
   packer fmt -check .
   packer validate .
   ```
   👉 Explication : `validate` vérifie la configuration mais ne prouve pas que le build réussira.

3. Examiner le fichier de verrouillage :
   ```bash
   cat .packer.lock.hcl
   ```
   👉 Explication : en cas d'erreur, ne pas lancer de build; corriger HCL, versions et dépendances, puis répéter.

## 2. Production — Contrôles

Pour une chaîne d’images de production, approuver le builder, les images de base immuables, les plugins verrouillés, les provisioners, le contrôle des secrets, les scans, la traçabilité et les approbations avant publication. Le pilote Docker local ne constitue pas une chaîne de production.

## 3. Production — Sécurité

- L’accès au socket Docker équivaut généralement à des privilèges root; réserver le pilote aux opérateurs autorisés.
- Ne jamais intégrer de secret dans HCL, les variables commitées, les journaux ou les couches d’image.
- Ne pas publier l’image vers un registre ni exécuter de build sur un démon partagé sans approbation.
- Verrouiller et réviser les plugins et sources; rejeter tout artefact dont la provenance ou le contenu est incertain.

## Validation et retour arrière

- **Validation** : initialisation réussie, lock file revu, format et validation sans erreur.
- **Retour arrière** : restaurer template et lock file depuis une révision connue; ne pas supprimer le verrou pour contourner un échec.

## Si le problème n'est pas résolu

- [HashiCorp — plugins Packer](https://developer.hashicorp.com/packer/docs/plugins/install)
- [HashiCorp — commande validate](https://developer.hashicorp.com/packer/docs/commands/validate)
- [Guide complet Packer Debian 13](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13#4-initialiser-et-valider-le-template-sans-construire)