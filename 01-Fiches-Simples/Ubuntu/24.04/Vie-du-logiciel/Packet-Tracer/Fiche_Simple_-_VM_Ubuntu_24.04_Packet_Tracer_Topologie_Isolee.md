# Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Topologie_Isolee.md

- **Environnement** : Poste Ubuntu Desktop 24.04 (VM) pour la simulation réseau pédagogique
- **OS / Version** : Ubuntu Desktop 24.04 LTS amd64; Cisco Packet Tracer 9.0.1
- **Catégorie** : simulation réseau / recette
- **Tags** : `ubuntu24.04`, `cisco`, `packet-tracer`, `netacad`, `topologie`, `simulation`

---

## Problème précis à résoudre

Valider l'outil avec deux postes et un commutateur.

## 1. Hors-Production (Lab / Test / POC)

1. **Nouveau fichier > Dispositifs terminaux > PC** ×2, puis **Commutateurs > Switch**
   👉 Explication : crée la maquette.

2. Relier les deux PC au commutateur avec des câbles.
   👉 Explication : les liens sont purement simulés, sans carte physique ni réseau externe.

3. Saisir les adresses IP dans **PC > Desktop > IP Configuration** (adresses de documentation, par exemple 192.0.2.10 et 192.0.2.11 en /24) :
   👉 Explication : paramètres réservés à la documentation, jamais celles d'un réseau réel.

4. Tester par **Simulation > Add Simple PDU** entre les deux PC puis lire les événements :
   👉 Explication : la connectivité simulée doit réussir.

5. Enregistrer, fermer et rouvrir le fichier : **Fichier > Enregistrer**
   👉 Explication : équipements, liens et paramètres doivent être conservés.

## 2. Production — Contrôles

Ce test prouve uniquement la maquette pédagogique; confirmer la configuration d'un équipement réel avec sa documentation.

## 3. Production — Sécurité

- Utiliser uniquement des adresses de documentation ou de cours.

## Validation et retour arrière

- **Validation** : ping simulé réussi et fichier relu correctement.
- **Retour arrière** : supprimer le fichier de test.

## Si le problème n'est pas résolu

- [Cisco Networking Academy — téléchargements Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco — instructions de téléchargement et d'installation](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf)
- [Guide complet Packet Tracer Ubuntu 24.04](../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/78_Deploiement_Cisco_Packet_Tracer_9.0.1_Ubuntu_24.04.md#5-verifier-une-topologie-de-cours-isolee)
