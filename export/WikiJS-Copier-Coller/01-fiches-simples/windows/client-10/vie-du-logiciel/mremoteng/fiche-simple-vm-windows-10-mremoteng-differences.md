# Fiche_Simple_-_VM_Windows_10_mRemoteNG_Differences

- **Environnement** : Poste Windows Client-10 existant; application mRemoteNG
- **OS / Version** : Windows 10 — vérifier édition, version, LTSC ou statut ESU; la compatibilité produit dépend du build éditeur
- **Catégorie** : poste de travail / client d’administration distante

---

## Problème précis à résoudre

Décrire uniquement les différences liées à Windows Client-10 par rapport aux procédures mRemoteNG déjà disponibles pour Windows Client-11, sans dupliquer les étapes d’installation et d’exploitation.

## 1. Hors-Production (Lab / Test / POC)

mRemoteNG centralise des connexions distantes; la fiche Windows 11 existante décrit les étapes d’installation et de sauvegarde sans les reproduire ici. Sur Windows Client-10, il faut distinguer la compatibilité de l’application de celle de l’OS : Windows 10 Home/Pro 22H2 n’est plus supporté par Microsoft depuis le 14 octobre 2025, hors dispositifs LTSC/ESU à cycle distinct.

👉 Explication : la fin du support de l’OS est une différence propre au poste Windows 10; les procédures applicatives Client-11 ne remplacent ni les prérequis éditeur ni les mises à jour de sécurité Windows.

1. Vérifier le cycle de vie exact de l’édition Windows 10 concernée avant de l’utiliser pour l’administration.
   👉 Explication : Windows 10 Home/Pro et LTSC ne partagent pas nécessairement les mêmes dates de fin de support.
2. Vérifier les exigences publiées par l’éditeur pour le build applicatif à déployer.
   👉 Explication : ne pas déduire la prise en charge d’un OS d’une ancienne fiche ou d’une version précédente.
3. Pour les étapes communes au produit, utiliser uniquement les fiches Client-11 indiquées ci-dessous après validation de leur applicabilité à la version installée.
   👉 Explication : cette fiche reste une note de différence, pas une série Windows 10.

## 2. Production — Contrôles

Consigner l’édition/version de Windows, le statut de support (LTSC/ESU le cas échéant), le build mRemoteNG retenu et la décision de migration. Réduire l’exposition d’un poste qui ne reçoit plus de mises à jour de sécurité.

## 3. Production — Sécurité

- Ne pas utiliser un OS hors support pour l’administration de systèmes sensibles sans dérogation et mesure compensatoire approuvées.
- Ne pas inscrire d’identifiants, clés privées, mots de passe ou informations de connexion dans cette fiche.
- Migrer les données applicatives de manière contrôlée avant retrait ou réinstallation du poste.

## Validation et retour arrière

- **Validation** : cycle de vie de l’édition confirmé, build mRemoteNG autorisé par la documentation éditeur, et procédures Client-11 communes vérifiées avant usage.
- **Retour arrière** : revenir au poste précédent géré et supporté selon le plan de migration; ne pas restaurer une image Windows 10 hors support comme solution durable.

## Si le problème n’est pas résolu

- [Cycle de vie Windows 10 Home et Pro — Microsoft](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro)
- [mRemoteNG — Site officiel du projet](https://mremoteng.org/)
- [mRemoteNG — dépôt officiel du projet](https://github.com/mRemoteNG/mRemoteNG)
- [Prérequis mRemoteNG Windows Client-11](/01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-prerequis)
- [Fiche Windows Client-11 complémentaire](/01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-sauvegarde-restauration)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-mremoteng)