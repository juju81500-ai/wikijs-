# Vie du système : Debian 12 en 50 étapes

- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `sommaire`

Chaque étape ci-dessous ouvre une fiche simple avec les commandes Debian 12 et une explication pour chaque action. Cycle commun à tous les OS : [Vie du système](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md).

## Phase : Préparation et prérequis (étapes 1 à 5)

1. [Définition des besoins (sizing)](./fiche-simple-vm-debian-12-vie-systeme-01-definition-des-besoins-sizing.md)
2. [Récupération de l'image système](./fiche-simple-vm-debian-12-vie-systeme-02-recuperation-de-l-image.md)
3. [Vérification d'intégrité et d'authenticité](./fiche-simple-vm-debian-12-vie-systeme-03-verification-d-integrite-et.md)
4. [Préparation du support d'amorçage](./fiche-simple-vm-debian-12-vie-systeme-04-preparation-du-support-d.md)
5. [Configuration matérielle / firmware](./fiche-simple-vm-debian-12-vie-systeme-05-configuration-materielle-firmware.md)

## Phase : Installation de base (étapes 6 à 15)

6. [Langue et localisation (locales)](./fiche-simple-vm-debian-12-vie-systeme-06-langue-et-localisation-locales.md)
7. [Disposition du clavier (keymap)](./fiche-simple-vm-debian-12-vie-systeme-07-disposition-du-clavier-keymap.md)
8. [Configuration réseau d'installation](./fiche-simple-vm-debian-12-vie-systeme-08-configuration-reseau-d-installation.md)
9. [Identité de la machine (hostname / FQDN)](./fiche-simple-vm-debian-12-vie-systeme-09-identite-de-la-machine.md)
10. [Compte super-administrateur](./fiche-simple-vm-debian-12-vie-systeme-10-compte-super-administrateur.md)
11. [Compte d'administration délégué](./fiche-simple-vm-debian-12-vie-systeme-11-compte-d-administration-delegue.md)
12. [Fuseau horaire](./fiche-simple-vm-debian-12-vie-systeme-12-fuseau-horaire.md)
13. [Partitionnement et systèmes de fichiers](./fiche-simple-vm-debian-12-vie-systeme-13-partitionnement-et-systemes-de.md)
14. [Sélection des composants de base](./fiche-simple-vm-debian-12-vie-systeme-14-selection-des-composants-de.md)
15. [Chargeur d'amorçage](./fiche-simple-vm-debian-12-vie-systeme-15-chargeur-d-amorcage.md)

## Phase : Configuration post-installation (étapes 16 à 25)

16. [Adressage IP fixe définitif](./fiche-simple-vm-debian-12-vie-systeme-16-adressage-ip-fixe-definitif.md)
17. [Résolution de noms (client DNS)](./fiche-simple-vm-debian-12-vie-systeme-17-resolution-de-noms-client.md)
18. [Table d'hôtes locale](./fiche-simple-vm-debian-12-vie-systeme-18-table-d-hotes-locale.md)
19. [Configuration des dépôts logiciels](./fiche-simple-vm-debian-12-vie-systeme-19-configuration-des-depots-logiciels.md)
20. [Mise à jour initiale complète](./fiche-simple-vm-debian-12-vie-systeme-20-mise-a-jour-initiale.md)
21. [Pilotes et agents de virtualisation](./fiche-simple-vm-debian-12-vie-systeme-21-pilotes-et-agents-de.md)
22. [Synchronisation horaire (NTP)](./fiche-simple-vm-debian-12-vie-systeme-22-synchronisation-horaire-ntp.md)
23. [Outils d'administration fondamentaux](./fiche-simple-vm-debian-12-vie-systeme-23-outils-d-administration-fondamentaux.md)
24. [Personnalisation et bannières](./fiche-simple-vm-debian-12-vie-systeme-24-personnalisation-et-bannieres.md)
25. [Validation de l'état initial (baseline)](./fiche-simple-vm-debian-12-vie-systeme-25-validation-de-l-etat.md)

## Phase : Sécurisation et durcissement (étapes 26 à 35)

26. [Authentification par clés (SSH)](./fiche-simple-vm-debian-12-vie-systeme-26-authentification-par-cles-ssh.md)
27. [Durcissement de l'accès distant](./fiche-simple-vm-debian-12-vie-systeme-27-durcissement-de-l-acces.md)
28. [Gestion fine des privilèges (sudo)](./fiche-simple-vm-debian-12-vie-systeme-28-gestion-fine-des-privileges.md)
29. [Pare-feu hôte](./fiche-simple-vm-debian-12-vie-systeme-29-pare-feu-hote.md)
30. [Protection contre le brute-force](./fiche-simple-vm-debian-12-vie-systeme-30-protection-contre-le-brute.md)
31. [Réduction de la surface d'attaque](./fiche-simple-vm-debian-12-vie-systeme-31-reduction-de-la-surface.md)
32. [Automatisation des correctifs de sécurité](./fiche-simple-vm-debian-12-vie-systeme-32-automatisation-des-correctifs-de.md)
33. [Sécurisation des systèmes de fichiers](./fiche-simple-vm-debian-12-vie-systeme-33-securisation-des-systemes-de.md)
34. [Durcissement du noyau et du réseau](./fiche-simple-vm-debian-12-vie-systeme-34-durcissement-du-noyau-et.md)
35. [Contrôle d'accès obligatoire (AppArmor)](./fiche-simple-vm-debian-12-vie-systeme-35-controle-d-acces-obligatoire.md)

## Phase : Mise en production et services (étapes 36 à 42)

36. [Intégration à l'annuaire ou au réseau d'administration](./fiche-simple-vm-debian-12-vie-systeme-36-integration-a-l-annuaire.md)
37. [Déploiement des rôles métiers](./fiche-simple-vm-debian-12-vie-systeme-37-deploiement-des-roles-metiers.md)
38. [Isolation des comptes de service](./fiche-simple-vm-debian-12-vie-systeme-38-isolation-des-comptes-de.md)
39. [Chiffrement des flux (PKI / TLS)](./fiche-simple-vm-debian-12-vie-systeme-39-chiffrement-des-flux-pki.md)
40. [Configuration des sauvegardes](./fiche-simple-vm-debian-12-vie-systeme-40-configuration-des-sauvegardes.md)
41. [Supervision, métriques et inventaire](./fiche-simple-vm-debian-12-vie-systeme-41-supervision-metriques-et-inventaire.md)
42. [Journaux : rotation et centralisation](./fiche-simple-vm-debian-12-vie-systeme-42-journaux-rotation-et-centralisation.md)

## Phase : Vérification, tests et documentation (étapes 43 à 50)

43. [Contrôle des services et des ports](./fiche-simple-vm-debian-12-vie-systeme-43-controle-des-services-et.md)
44. [Audit d'exposition réseau externe](./fiche-simple-vm-debian-12-vie-systeme-44-audit-d-exposition-reseau.md)
45. [Analyse des journaux d'erreurs](./fiche-simple-vm-debian-12-vie-systeme-45-analyse-des-journaux-d.md)
46. [Test de persistance au redémarrage](./fiche-simple-vm-debian-12-vie-systeme-46-test-de-persistance-au.md)
47. [Test de résilience et d'alerte](./fiche-simple-vm-debian-12-vie-systeme-47-test-de-resilience-et.md)
48. [Test de restauration (PRA/DRP)](./fiche-simple-vm-debian-12-vie-systeme-48-test-de-restauration-pra.md)
49. [Enregistrement CMDB et gestion des accès](./fiche-simple-vm-debian-12-vie-systeme-49-enregistrement-cmdb-et-gestion.md)
50. [Documentation d'exploitation (runbook)](./fiche-simple-vm-debian-12-vie-systeme-50-documentation-d-exploitation-runbook.md)
