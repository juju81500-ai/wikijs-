# Déployer PRTG Network Monitor sur Windows Server

- **OS / Version** : Windows Server 2022 ou 2025 en Desktop Experience; PRTG Network Monitor version maintenue
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Serveur Windows dédié ou VM, accès d'administration restreint
- **Machine ciblée** : Serveur de supervision réseau
- **Catégorie** : Supervision / SNMP / WMI

## 1. Dimensionner et préparer

Fiche simple : [dimensionner et préparer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-dimensionner).

Dimensionner selon le nombre de capteurs, intervalles, protocoles et rétention; suivre les tableaux officiels Paessler plutôt que le nombre d'équipements seul. Prévoir un volume de données dédié, sauvegarde, DNS, adresse fixe et fenêtre d'installation.

Le Core Server et les sondes Windows nécessitent une version de Windows prise en charge et .NET Framework 4.7.2 minimum (4.8 recommandé). Ne pas installer sur Windows Server Core. Pour des domaines ou réseaux distants, prévoir des Remote Probes ou Multi-Platform Probe selon la matrice officielle.

## 2. Télécharger et installer

Fiche simple : [télécharger et installer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-installer).

1. Obtenir l'installateur depuis le site officiel Paessler et vérifier son éditeur/signature avant exécution.
2. Exécuter avec un compte administrateur local dédié et utiliser l'assistant d'installation.
3. Choisir le mode personnalisé pour définir les répertoires programme et données et **ignorer l'auto-discovery initiale**; éviter tout scan global par défaut.
4. Terminer l'installation, configurer la licence/activation et ouvrir l'interface Web via HTTPS ou le binding/TLS approuvé.
5. Définir mot de passe administrateur robuste, notifications système et fuseau horaire.

## 3. Définir le modèle d'accès

Fiche simple : [définir le modèle d'accès](/01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-acces).

- Créer des comptes nominatifs et groupes séparés pour administrateurs et opérateurs lecture seule.
- Restreindre l'interface Web aux réseaux d'administration et activer l'authentification centralisée/MFA lorsque disponible.
- Documenter les droits d'accès aux équipements; utiliser des comptes de lecture seule pour WMI/Windows et SNMPv3 authPriv en lecture seule pour les équipements réseau.
- Ne pas utiliser les comptes Domain Admin ni la communauté SNMP `public` pour les scans.

## 4. Ajouter un périmètre pilote

Fiche simple : [ajouter un périmètre pilote](/01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-pilote).

Commencer avec un équipement ou une petite liste d'actifs appartenant à l'organisation et explicitement autorisés. Ajouter d'abord Ping/HTTP, puis SNMP ou WMI selon le protocole et les permissions approuvées. Régler intervalle, seuils et notifications avant d'augmenter la couverture.

Vérifier la matrice de ports officielle et ouvrir uniquement les flux requis entre Core/Probe et les appareils sélectionnés. Les capteurs WMI/flow/sniffer ont un coût supérieur; mesurer la charge avant généralisation.

## 5. Recette

Fiche simple : [recette](/01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-recette).

- Confirmer état du service Core et de la sonde, accès Web et certificat.
- Vérifier qu'un appareil pilote et ses capteurs attendus sont `Up`.
- Tester une alerte de seuil sur un capteur de test, son destinataire et sa résolution.
- Examiner CPU/RAM/disque, durée des scans et journaux système.
- Valider permissions avec un compte opérateur non administrateur.

## 6. Exploitation et restauration

Fiche simple : [exploitation et restauration](/01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-exploitation).

Documenter licence, répertoires programme/données, comptes, cibles, capteurs, intervalles, sondes et ports. Sauvegarder via les fonctions officielles avant mise à jour ou changement important; restaurer d'abord dans un environnement isolé.

Avant upgrade, consulter les notes de version et tester un pilote. Ne pas supprimer la base ou les données de supervision pour résoudre un simple problème de connectivité.

## Sources

- [Paessler — Exigences système PRTG](https://www.paessler.com/manuals/prtg/system_requirements)
- [Paessler — Installer le Core Server](https://www.paessler.com/manuals/prtg/install_a_prtg_core_server)
- [Paessler — Guide de démarrage](https://www.paessler.com/manuals/prtg/quick_start_guide)
- [Paessler — Installation logicielle](https://www.paessler.com/manuals/prtg/installing_the_software)
- [Paessler — Appareils et capteurs](https://www.paessler.com/manuals/prtg/device_and_sensor_setup)