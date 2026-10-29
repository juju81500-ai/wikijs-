# Vie du système : TrueNAS SCALE 25.10 en 50 étapes

Chaque étape ci-dessous ouvre une fiche simple avec les commandes TrueNAS SCALE 25.10 et une explication pour chaque action. Cycle commun à tous les OS : [Vie du système](/00-administration/vie-du-systeme).

## Phase : Préparation et prérequis (étapes 1 à 5)

1. [Définition des besoins (sizing)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-01-definition-des-besoins-sizing>)
2. [Récupération de l'image système](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-02-recuperation-de-l-image>)
3. [Vérification d'intégrité et d'authenticité](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-03-verification-d-integrite-et>)
4. [Préparation du support d'amorçage](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-04-preparation-du-support-d>)
5. [Configuration matérielle / firmware](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-05-configuration-materielle-firmware>)

## Phase : Installation de base (étapes 6 à 15)

6. [Langue et localisation (locales)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-06-langue-et-localisation-locales>)
7. [Disposition du clavier (keymap)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-07-disposition-du-clavier-keymap>)
8. [Configuration réseau d'installation](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-08-configuration-reseau-d-installation>)
9. [Identité de la machine (hostname / FQDN)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-09-identite-de-la-machine>)
10. [Compte super-administrateur](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-10-compte-super-administrateur>)
11. [Compte d'administration délégué](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-11-compte-d-administration-delegue>)
12. [Fuseau horaire](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-12-fuseau-horaire>)
13. [Partitionnement et systèmes de fichiers](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-13-partitionnement-et-systemes-de>)
14. [Sélection des composants de base](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-14-selection-des-composants-de>)
15. [Chargeur d'amorçage](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-15-chargeur-d-amorcage>)

## Phase : Configuration post-installation (étapes 16 à 25)

16. [Adressage IP fixe définitif](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-16-adressage-ip-fixe-definitif>)
17. [Résolution de noms (client DNS)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-17-resolution-de-noms-client>)
18. [Table d'hôtes locale](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-18-table-d-hotes-locale>)
19. [Configuration des dépôts logiciels](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-19-configuration-des-depots-logiciels>)
20. [Mise à jour initiale complète](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-20-mise-a-jour-initiale>)
21. [Pilotes et agents de virtualisation](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-21-pilotes-et-agents-de>)
22. [Synchronisation horaire (NTP)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-22-synchronisation-horaire-ntp>)
23. [Outils d'administration fondamentaux](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-23-outils-d-administration-fondamentaux>)
24. [Personnalisation et bannières](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-24-personnalisation-et-bannieres>)
25. [Validation de l'état initial (baseline)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-25-validation-de-l-etat>)

## Phase : Sécurisation et durcissement (étapes 26 à 35)

26. [Authentification par clés (SSH)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-26-authentification-par-cles-ssh>)
27. [Durcissement de l'accès distant](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-27-durcissement-de-l-acces>)
28. [Gestion fine des privilèges (sudo)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-28-gestion-fine-des-privileges>)
29. [Pare-feu hôte](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-29-pare-feu-hote>)
30. [Protection contre le brute-force](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-30-protection-contre-le-brute>)
31. [Réduction de la surface d'attaque](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-31-reduction-de-la-surface>)
32. [Automatisation des correctifs de sécurité](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-32-automatisation-des-correctifs-de>)
33. [Sécurisation des systèmes de fichiers](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-33-securisation-des-systemes-de>)
34. [Durcissement du noyau et du réseau](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-34-durcissement-du-noyau-et>)
35. [Contrôle d'accès obligatoire (SELinux)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-35-controle-d-acces-obligatoire>)

## Phase : Mise en production et services (étapes 36 à 42)

36. [Intégration à l'annuaire ou au réseau d'administration](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-36-integration-a-l-annuaire>)
37. [Déploiement des rôles métiers](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-37-deploiement-des-roles-metiers>)
38. [Isolation des comptes de service](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-38-isolation-des-comptes-de>)
39. [Chiffrement des flux (PKI / TLS)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-39-chiffrement-des-flux-pki>)
40. [Configuration des sauvegardes](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-40-configuration-des-sauvegardes>)
41. [Supervision, métriques et inventaire](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-41-supervision-metriques-et-inventaire>)
42. [Journaux : rotation et centralisation](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-42-journaux-rotation-et-centralisation>)

## Phase : Vérification, tests et documentation (étapes 43 à 50)

43. [Contrôle des services et des ports](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-43-controle-des-services-et>)
44. [Audit d'exposition réseau externe](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-44-audit-d-exposition-reseau>)
45. [Analyse des journaux d'erreurs](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-45-analyse-des-journaux-d>)
46. [Test de persistance au redémarrage](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-46-test-de-persistance-au>)
47. [Test de résilience et d'alerte](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-47-test-de-resilience-et>)
48. [Test de restauration (PRA/DRP)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-48-test-de-restauration-pra>)
49. [Enregistrement CMDB et gestion des accès](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-49-enregistrement-cmdb-et-gestion>)
50. [Documentation d'exploitation (runbook)](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-50-documentation-d-exploitation-runbook>)