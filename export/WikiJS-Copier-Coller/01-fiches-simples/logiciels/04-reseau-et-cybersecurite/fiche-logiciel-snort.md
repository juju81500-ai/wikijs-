# 📄 Snort

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Linux
- **Produit (matrice)** : Snort / Suricata / Zeek
- **Statut dans le pack** : Couvert

## 📚 Couverture dans le pack

Couvert — Snort IDS passif sur Debian 13, Ubuntu 24.04 et Rocky Linux 9 (Snort 3 compilé depuis les sources officielles sur Ubuntu/Rocky; disponibilité des paquets à vérifier). Le mode inline/IPS et le blocage ne sont pas couverts.

Fiches simples du guide : [prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-prerequis-limites), [installation](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-installer), [configuration](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-configurer), [sécurisation](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-securiser), [validation](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-valider), [sauvegarde/restauration](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-sauvegarder-restaurer), [mise à jour/retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-mise-a-jour-retour-arriere).

Fiches simples supplémentaires — Ubuntu 24.04 : [prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-prerequis-limites), [installation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-installer), [configuration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-configurer), [sécurisation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-securiser), [validation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-valider), [sauvegarde/restauration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-sauvegarder-restaurer), [mise à jour/retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-mise-a-jour-retour-arriere).

Fiches simples supplémentaires — Rocky Linux 9 : [prérequis et limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-prerequis-limites), [installation](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-installer), [configuration](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-configurer), [sécurisation](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-securiser), [validation](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-valider), [sauvegarde/restauration](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-sauvegarder-restaurer), [mise à jour/retour arrière](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-mise-a-jour-retour-arriere).

## 🧭 Périmètre

La matrice indique une couverture partielle: les fiches existantes documentent uniquement une supervision IDS passive en environnement autorisé. Cette fiche complète la gouvernance des règles, versions, alertes et journaux. Examiner les règles et leurs sources, effectuer leur revue en préproduction, protéger les journaux et transmettre les alertes via le processus SOC. Le mode IPS/inline et le blocage automatique ne sont pas documentés ici.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Valider que le capteur reste passif, que la configuration et les règles sont approuvées, que les événements arrivent au collecteur et que la procédure d’escalade est connue. Revenir aux règles et à la configuration précédemment validées si le volume d’alertes ou l’impact dérive; aucune procédure d’injection ou d’exploitation n’est incluse. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Cisco Snort documentation](https://www.snort.org/documents) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.