---
title: "Cycle de vie 50 étapes : OPNsense"
description: "Cette checklist suit les 50 étapes du [cycle complet OPNsense](../../../../02-Fiches-Completes/OPNsense/Toutes-versions/Cycle-de-vie-50-etapes.md) et du [cycle de référence](../../../../00-Administration/Cycledevie50etapes.md). Utiliser la documentation officielle correspondant à la version déployée"
published: true
date: 2026-10-29T20:22:42Z
tags: ["cycle-de-vie", "opnsense", "pare-feu", "appliance", "installation", "production", "verification"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Cycle de vie 50 étapes : OPNsense

- **OS / Version** : OPNsense; relever la version exacte avant chaque opération, les options évoluent entre versions
- **Environnement** : Appliance physique ou VM dédiée; confirmer le support matériel et la topologie réseau
- **Catégorie** : Installation / exploitation / vérification
- **Tags** : `cycle-de-vie`, `opnsense`, `pare-feu`, `appliance`, `installation`, `production`, `verification`

Cette checklist suit les 50 étapes du [cycle complet OPNsense](/02-fiches-completes/opnsense/toutes-versions/cycle-de-vie-50-etapes) et du [cycle de référence](/00-administration/cycle-de-vie-50-etapes). Utiliser la documentation officielle correspondant à la version déployée.

## Périmètre et précautions

- OPNsense est une appliance basée sur FreeBSD. Gérer configuration, interfaces, mises à jour et extensions avec les mécanismes supportés par OPNsense; ne pas traiter l'appliance comme un serveur FreeBSD générique.
- Identifier précisément WAN, LAN, VLAN, accès console et règles de gestion avant de modifier les interfaces ou le pare-feu. Prévoir un accès local de secours.
- Sauvegarder la configuration et protéger le fichier exporté, qui peut contenir des éléments sensibles. Vérifier une restauration dans un environnement isolé.
- N'effectuer des tests réseau que sur des adresses et systèmes autorisés, avec une portée et une fenêtre définies.
- Les étapes de déploiement d'applications, d'agents et de services génériques ne s'appliquent pas toutes à une appliance pare-feu; limiter les services à ceux officiellement pris en charge.

## Checklist des 50 étapes

### Phase 1 — Préparation et prérequis (1 à 5)

1. Définir débit, interfaces, utilisateurs, flux, haute disponibilité et capacité.
2. Télécharger l'image OPNsense depuis une source officielle pour l'architecture cible.
3. Vérifier somme et signature selon la méthode publiée pour cette version.
4. Préparer média d'installation ou console hyperviseur sécurisée.
5. Vérifier NIC, stockage, firmware, compatibilité et accès console.

### Phase 2 — Installation de base (6 à 15)

6. Choisir langue et paramètres régionaux.
7. Choisir la disposition clavier.
8. Préparer temporairement le réseau d'installation si nécessaire.
9. Définir hostname et domaine selon le plan d'adressage.
10. Protéger le compte administrateur initial et renouveler les identifiants par défaut.
11. Créer des comptes d'administration individuels avec droits minimaux.
12. Configurer le fuseau horaire.
13. Choisir le disque, la redondance et le système de fichiers pris en charge.
14. Installer uniquement l'image officielle et les composants intégrés.
15. Vérifier le démarrage et le mode de console pris en charge.

### Phase 3 — Configuration post-installation (16 à 25)

16. Affecter et documenter les interfaces WAN/LAN et VLAN.
17. Configurer les résolveurs DNS et les domaines de recherche.
18. Vérifier hostname et résolution locale.
19. Contrôler les sources de mise à jour intégrées et les dépôts configurés.
20. Examiner les notes de version et planifier une mise à jour supportée.
21. Valider pilotes et interfaces réseau avec le matériel/virtualiseur cible.
22. Configurer NTP et vérifier l'heure système.
23. Activer uniquement les outils d'administration intégrés nécessaires.
24. Configurer les notifications et la bannière d'administration si nécessaire.
25. Exporter une configuration de référence et protéger sa copie.

### Phase 4 — Sécurisation et hardening (26 à 35)

26. Employer des comptes individuels et des secrets robustes; sécuriser les clés/certificats.
27. Limiter l'interface Web et SSH au réseau d'administration; vérifier l'accès de secours.
28. Appliquer rôles et privilèges minimaux; retirer les comptes inutilisés.
29. Construire les règles de pare-feu depuis une politique documentée; éviter les règles larges.
30. Configurer la protection contre les tentatives abusives selon le rôle et la version.
31. Désactiver les services non requis depuis l'interface supportée.
32. Définir un processus de mises à jour, notification, sauvegarde et retour arrière.
33. Protéger la configuration exportée, les certificats et les données de journalisation.
34. Ne modifier les réglages système qu'après vérification de leur compatibilité OPNsense.
35. Contrôler certificats, authentification, politiques d'accès et extensions installées.

### Phase 5 — Mise en production et services (36 à 42)

36. Intégrer l'appliance aux réseaux d'administration, DNS et services d'identité requis.
37. Configurer routage, NAT, VPN, DHCP ou autres services uniquement selon l'architecture validée.
38. Séparer comptes d'administration, comptes VPN et comptes de services.
39. Protéger les flux administratifs et VPN avec des certificats et protocoles pris en charge.
40. Mettre en place sauvegarde chiffrée, rétention et restauration testée.
41. Superviser état, interfaces, capacité, haute disponibilité et tunnels.
42. Centraliser journaux et alertes; protéger les données sensibles.

### Phase 6 — Vérification, tests et documentation (43 à 50)

43. Vérifier état des interfaces, routes, règles, services et ports en écoute.
44. Tester uniquement les flux explicitement autorisés, depuis des points approuvés.
45. Examiner journaux système, pare-feu, VPN, DNS et authentification.
46. Planifier un redémarrage contrôlé et confirmer accès, règles et services après reprise.
47. Tester bascule CARP/HA et alertes dans un laboratoire ou une fenêtre approuvée.
48. Restaurer la configuration sur une instance isolée et vérifier interfaces/règles avant usage.
49. Enregistrer l'appliance, interfaces, réseaux, règles et accès dans la CMDB/IPAM; conserver les secrets dans le coffre approuvé.
50. Documenter topologie, versions, flux, sauvegarde, mise à jour, procédure d'urgence et retour arrière.