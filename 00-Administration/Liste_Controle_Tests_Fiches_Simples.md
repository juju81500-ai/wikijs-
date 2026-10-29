# Liste de contrôle stricte — tests des fiches simples avant usage en production

- **Tags** : `controle`, `tests`, `recette`, `production`, `checklist`

Aucune fiche du pack n'a été exécutée sur un système réel. Cette liste impose **dans quel ordre** les rejouer et **ce qui prouve** qu'une fiche est fiable. Une fiche non testée garde le statut « non éprouvée » et ne doit pas servir en production.

## 1. Règles strictes

1. **Environnement jetable obligatoire** : VM ou laboratoire isolé, snapshot avant chaque fiche, aucun accès au réseau de production, aucune donnée réelle.
2. **Version exacte** : tester sur la version d'OS et du logiciel indiquées dans la fiche. Noter la version réellement installée (`cat /etc/os-release`, `winver`, `Get-ComputerInfo`, version du logiciel).
3. **Exécution littérale** : copier les commandes telles quelles, dans l'ordre, sans correction silencieuse. Toute modification nécessaire est un **écart** à consigner.
4. **Chaque 👉 Explication est lue** : si l'explication ne correspond pas au résultat observé, la fiche est en échec.
5. **Validation puis retour arrière** : la section « Validation et retour arrière » doit être exécutée jusqu'au bout. Une fiche dont le retour arrière échoue est **KO**, même si l'installation réussit.
6. **Accès de secours** : avant toute fiche touchant SSH, pare-feu, réseau, comptes ou RDP, garder une console hyperviseur ouverte.
7. **Une fiche = un verdict** parmi : `OK`, `OK avec écarts` (corrigée dans le dépôt), `KO` (bloquante), `Non applicable`. Pas de verdict implicite.
8. **Revue par une seconde personne** pour toute fiche P0.
9. **Après correction d'une fiche**, la rejouer entièrement depuis un snapshot propre.
10. **Secrets** : jamais de mot de passe ou de clé réels dans une fiche, une capture ou un journal de test.

## 2. Priorités

| Priorité | Critère | Délai cible |
|---|---|---|
| **P0** | Risque de perte d'accès, de perte de données ou d'indisponibilité (partitionnement, IP fixe, SSH, pare-feu, sauvegarde, restauration, mise à jour, retour arrière, annuaire, stockage, hyperviseur) | avant toute mise en production |
| **P1** | Installation et sécurisation d'un service (dépôts, mises à jour, TLS, comptes de service) | avant mise en production du service concerné |
| **P2** | Configuration courante, supervision, documentation | selon l'usage |

## 3. Journal d'un test (à recopier pour chaque fiche)

| Champ | Valeur |
|---|---|
| Fiche | nom du fichier |
| Date / testeur / relecteur | |
| OS et version réels | |
| Logiciel et version réels | |
| Snapshot de départ | oui / non |
| Commandes exécutées sans modification | oui / non |
| Écarts constatés | liste |
| Retour arrière exécuté | oui / non |
| Verdict | OK / OK avec écarts / KO / Non applicable |

## 4. Points déjà identifiés comme incertains (à vérifier en premier)

| Sujet | Risque |
|---|---|
| Clés GPG Ubuntu (identifiants donnés de mémoire) | comparer à la page officielle avant import |
| Ubuntu 26.04 : sudo-rs, client NTP par défaut, trousseau `ubuntu.sources` | noms de paquets à confirmer |
| Rocky 9 : URL `CHECKSUM.sig`, paquet `fail2ban-firewalld` | téléchargement ou installation en échec |
| Windows Server : `PSWindowsUpdate`, `winget`, noms de groupes et règles localisés | commande absente ou nom différent |
| Debian 13 : MySQL et MongoDB (dépôts officiels), GitLab CE, FOG | paquets non disponibles pour trixie |
| winget : identifiants SSMS, MobaXterm et autres | identifiant inexistant |
| Traefik : placeholder `VERSION_TRAEFIK` | version à choisir |
| Redis Debian : prise en charge TLS du paquet | option inexistante |
| SQL Server : chemin de registre `MSSQL16` | chiffrement non appliqué |
| Exchange : procédures selon le cumulative update | commandes ou prérequis différents |
| Citrix, Horizon : menus et versions éditeur | libellés différents |
| Entra ID : licences, permissions Graph | fonction indisponible selon le tenant |
| VCSA, Schannel, adprep (Windows Server 2016/2019) | paramètres non vérifiés |
| OpenTofu : syntaxe `TF_ENCRYPTION` ; Bareos : URL du dépôt ; Dynatrace : jeton | syntaxe ou URL obsolètes |
| Pare-feu pfSense/OPNsense, ESXi, TrueNAS CORE : chemins d'interface | menus déplacés selon la version |
| Règle nftables d'exemple (table `inet filter`, chaîne `input`) | échec si la table n'existe pas |

## 5. P0 par système d'exploitation (étapes critiques de la vie du système)

Rejouer dans l'ordre du tableau. Colonnes à compléter : Verdict, Date, Testeur, Relecteur.

### Alpine/3.19

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Alpine 3.19 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Alpine/3.19/Vie-du-systeme/Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Debian/12

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Debian/13

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiche_Simple_-_VM_Debian_13_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### OPNsense/Toutes-versions

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM OPNsense Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM OPNsense Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM OPNsense Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM OPNsense Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM OPNsense Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM OPNsense Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM OPNsense Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM OPNsense Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM OPNsense Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM OPNsense Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM OPNsense Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM OPNsense Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM OPNsense Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM OPNsense Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM OPNsense Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_OPNsense_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Proxmox/VE-8

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Proxmox VE 8 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-systeme/Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Rocky-Linux/9

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky Linux 9 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-systeme/Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### TrueNAS/CORE-13.0

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/TrueNAS/CORE-13.0/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### TrueNAS/SCALE-25.10

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Ubuntu/24.04

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Ubuntu/26.04

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26.04 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-systeme/Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### VMware/ESXi-8

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM ESXi 8 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-systeme/Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Windows/Client-10

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 10 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 19 Configuration Des Sources Logicielles](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_19_Configuration_Des_Sources_Logicielles.md>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 26 Authentification Forte Et Windows](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_26_Authentification_Forte_Et_Windows.md>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 30 Protection Contre Les Tentatives](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_30_Protection_Contre_Les_Tentatives.md>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 39 Chiffrement Des Flux Et](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_39_Chiffrement_Des_Flux_Et.md>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Windows/Client-10/Vie-du-systeme/Fiche_Simple_-_VM_Windows_10_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Windows/Client-11

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 19 Configuration Des Sources Logicielles](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_19_Configuration_Des_Sources_Logicielles.md>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 26 Authentification Forte Et Windows](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_26_Authentification_Forte_Et_Windows.md>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 30 Protection Contre Les Tentatives](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_30_Protection_Contre_Les_Tentatives.md>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 39 Chiffrement Des Flux Et](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_39_Chiffrement_Des_Flux_Et.md>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Windows/Client-11/Vie-du-systeme/Fiche_Simple_-_VM_Windows_11_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Windows/Server-2022

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 19 Configuration Des Sources De](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_19_Configuration_Des_Sources_De.md>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 26 Authentification Forte Et Acces](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_26_Authentification_Forte_Et_Acces.md>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### Windows/Server-2025

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2025 Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 19 Configuration Des Sources De](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_19_Configuration_Des_Sources_De.md>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 26 Authentification Forte Et Acces](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_26_Authentification_Forte_Et_Acces.md>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

### pfSense/Toutes-versions

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM pfSense Vie Systeme 13 Partitionnement Et Systemes De](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md>) | | | | |
| P0 | [VM pfSense Vie Systeme 16 Adressage Ip Fixe Definitif](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md>) | | | | |
| P1 | [VM pfSense Vie Systeme 19 Configuration Des Depots Logiciels](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_19_Configuration_Des_Depots_Logiciels.md>) | | | | |
| P1 | [VM pfSense Vie Systeme 20 Mise A Jour Initiale](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_20_Mise_A_Jour_Initiale.md>) | | | | |
| P1 | [VM pfSense Vie Systeme 22 Synchronisation Horaire Ntp](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_22_Synchronisation_Horaire_Ntp.md>) | | | | |
| P0 | [VM pfSense Vie Systeme 26 Authentification Par Cles Ssh](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md>) | | | | |
| P0 | [VM pfSense Vie Systeme 27 Durcissement De L Acces](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_27_Durcissement_De_L_Acces.md>) | | | | |
| P1 | [VM pfSense Vie Systeme 28 Gestion Fine Des Privileges](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_28_Gestion_Fine_Des_Privileges.md>) | | | | |
| P0 | [VM pfSense Vie Systeme 29 Pare Feu Hote](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_29_Pare_Feu_Hote.md>) | | | | |
| P1 | [VM pfSense Vie Systeme 30 Protection Contre Le Brute](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_30_Protection_Contre_Le_Brute.md>) | | | | |
| P1 | [VM pfSense Vie Systeme 32 Automatisation Des Correctifs De](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_32_Automatisation_Des_Correctifs_De.md>) | | | | |
| P1 | [VM pfSense Vie Systeme 39 Chiffrement Des Flux Pki](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_39_Chiffrement_Des_Flux_Pki.md>) | | | | |
| P0 | [VM pfSense Vie Systeme 40 Configuration Des Sauvegardes](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_40_Configuration_Des_Sauvegardes.md>) | | | | |
| P0 | [VM pfSense Vie Systeme 46 Test De Persistance Au](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_46_Test_De_Persistance_Au.md>) | | | | |
| P0 | [VM pfSense Vie Systeme 48 Test De Restauration Pra](<../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiche_Simple_-_VM_pfSense_Vie_Systeme_48_Test_De_Restauration_Pra.md>) | | | | |

## 6. P0 par logiciel (installation, sauvegarde, restauration, mise à jour)

Pour chaque logiciel : tester d'abord **Sauvegarde**, puis **Restauration** sur une machine vierge, puis **Mise à jour / retour arrière**. Une restauration jamais testée équivaut à une absence de sauvegarde.

### Alpine/3.19

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3.19 Securite Certbot TLS](<../01-Fiches-Simples/Alpine/3.19/Vie-du-logiciel/Certbot/Fiche_Simple_-_LXC_Alpine_3.19_Securite_Certbot_TLS.md>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3.19 Securite Fail2ban](<../01-Fiches-Simples/Alpine/3.19/Vie-du-logiciel/Fail2ban/Fiche_Simple_-_LXC_Alpine_3.19_Securite_Fail2ban.md>) | | | | |

#### OpenSSH

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](<../01-Fiches-Simples/Alpine/3.19/Vie-du-logiciel/OpenSSH/Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC.md>) | | | | |

### Debian/12

#### Ansible

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Installation Ansible](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Ansible/Fiche_Simple_-_VM_Debian_12_Installation_Ansible.md>) | | | | |

#### Bacula

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Bacula Prouver Restauration](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Bacula/Fiche_Simple_-_VM_Debian_12_Bacula_Prouver_Restauration.md>) | | | | |
| P0 | [VM Debian 12 Bacula Valider Restauration](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Bacula/Fiche_Simple_-_VM_Debian_12_Bacula_Valider_Restauration.md>) | | | | |
| P1 | [VM Debian 12 Bacula Valider Config Demarrer](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Bacula/Fiche_Simple_-_VM_Debian_12_Bacula_Valider_Config_Demarrer.md>) | | | | |

#### BorgBackup

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Borg Depanner Retour Arriere](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Depanner_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 12 Borg Restaurer Isoler](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Restaurer_Isoler.md>) | | | | |
| P0 | [VM Debian 12 Sauvegarde Configuration BorgBackup](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Sauvegarde_Configuration_BorgBackup.md>) | | | | |
| P1 | [VM Debian 12 Borg Installer Initialiser](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Installer_Initialiser.md>) | | | | |
| P1 | [VM Debian 12 Borg Securiser Verifier](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Securiser_Verifier.md>) | | | | |

#### Cacti

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Cacti Installer Cacti](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Cacti/Fiche_Simple_-_VM_Debian_12_Cacti_Installer_Cacti.md>) | | | | |
| P1 | [VM Debian 12 Cacti Installer Dependances](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Cacti/Fiche_Simple_-_VM_Debian_12_Cacti_Installer_Dependances.md>) | | | | |
| P1 | [VM Debian 12 Cacti Securiser Exploiter](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Cacti/Fiche_Simple_-_VM_Debian_12_Cacti_Securiser_Exploiter.md>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Securite Certbot SSL Nginx](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Certbot/Fiche_Simple_-_VM_Debian_12_Securite_Certbot_SSL_Nginx.md>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Securite Configuration Fail2ban SSH](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Debian_12_Securite_Configuration_Fail2ban_SSH.md>) | | | | |

#### FreePBX Asterisk

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 FreePBX Sauvegarder Maintenir](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/FreePBX-Asterisk/Fiche_Simple_-_VM_Debian_12_FreePBX_Sauvegarder_Maintenir.md>) | | | | |
| P1 | [VM Debian 12 FreePBX Installer Methode Supportee](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/FreePBX-Asterisk/Fiche_Simple_-_VM_Debian_12_FreePBX_Installer_Methode_Supportee.md>) | | | | |

#### GLPI

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 GLPI Maintenir Restaurer](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/GLPI/Fiche_Simple_-_VM_Debian_12_GLPI_Maintenir_Restaurer.md>) | | | | |
| P1 | [LXC Debian 12 Installation GLPI Agent](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/GLPI/Fiche_Simple_-_LXC_Debian_12_Installation_GLPI_Agent.md>) | | | | |
| P1 | [VM Debian 12 GLPI Installer Application](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/GLPI/Fiche_Simple_-_VM_Debian_12_GLPI_Installer_Application.md>) | | | | |
| P1 | [VM Debian 12 GLPI Installer Recetter](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/GLPI/Fiche_Simple_-_VM_Debian_12_GLPI_Installer_Recetter.md>) | | | | |
| P1 | [VM Debian 12 Services Installation GLPI Serveur](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/GLPI/Fiche_Simple_-_VM_Debian_12_Services_Installation_GLPI_Serveur.md>) | | | | |

#### Nginx

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 ReverseProxy Installation Nginx Pro](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Nginx/Fiche_Simple_-_VM_Debian_12_ReverseProxy_Installation_Nginx_Pro.md>) | | | | |

#### QEMU

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Systeme Installation Qemu Guest Age](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/QEMU/Fiche_Simple_-_VM_Debian_12_Systeme_Installation_Qemu_Guest_Age.md>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Sauvegarde Restic Depot](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Restic/Fiche_Simple_-_VM_Debian_12_Sauvegarde_Restic_Depot.md>) | | | | |

#### Splunk

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Splunk Installer Sans Root](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Installer_Sans_Root.md>) | | | | |
| P1 | [VM Debian 12 Splunk Securiser Premier Acces](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Securiser_Premier_Acces.md>) | | | | |

#### Wazuh

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Wazuh Sauvegarder Mettre A Jour](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Wazuh/Fiche_Simple_-_VM_Debian_12_Wazuh_Sauvegarder_Mettre_A_Jour.md>) | | | | |
| P1 | [VM Debian 12 Wazuh Installer Architecture](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Wazuh/Fiche_Simple_-_VM_Debian_12_Wazuh_Installer_Architecture.md>) | | | | |

#### Zabbix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Zabbix Sauvegarder Mettre A Jour](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Zabbix/Fiche_Simple_-_VM_Debian_12_Zabbix_Sauvegarder_Mettre_A_Jour.md>) | | | | |
| P1 | [VM Debian 12 Supervision Installation Zabbix Age](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Zabbix/Fiche_Simple_-_VM_Debian_12_Supervision_Installation_Zabbix_Age.md>) | | | | |
| P1 | [VM Debian 12 Supervision Installation Zabbix Ser](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Zabbix/Fiche_Simple_-_VM_Debian_12_Supervision_Installation_Zabbix_Ser.md>) | | | | |
| P1 | [VM Debian 12 Zabbix Installer Configurer](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Zabbix/Fiche_Simple_-_VM_Debian_12_Zabbix_Installer_Configurer.md>) | | | | |
| P1 | [VM Debian 12 Zabbix Valider Installation](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Zabbix/Fiche_Simple_-_VM_Debian_12_Zabbix_Valider_Installation.md>) | | | | |

#### iTop

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 iTop Verifier Sauvegarder MAJ](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/iTop/Fiche_Simple_-_VM_Debian_12_iTop_Verifier_Sauvegarder_MAJ.md>) | | | | |
| P1 | [VM Debian 12 iTop Installer Apache PHP MariaDB](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/iTop/Fiche_Simple_-_VM_Debian_12_iTop_Installer_Apache_PHP_MariaDB.md>) | | | | |
| P1 | [VM Debian 12 iTop Installer Paquet Officiel](<../01-Fiches-Simples/Debian/12/Vie-du-logiciel/iTop/Fiche_Simple_-_VM_Debian_12_iTop_Installer_Paquet_Officiel.md>) | | | | |

### Debian/13

#### Ansible

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Ansible Production Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Ansible/Fiche_Simple_-_VM_Debian_13_Ansible_Production_Retour_Arriere.md>) | | | | |
| P1 | [VM Debian 13 Ansible Installer Core](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Ansible/Fiche_Simple_-_VM_Debian_13_Ansible_Installer_Core.md>) | | | | |
| P1 | [VM Debian 13 Ansible Valider Connexion](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Ansible/Fiche_Simple_-_VM_Debian_13_Ansible_Valider_Connexion.md>) | | | | |
| P1 | [VM Debian 13 Ansible Valider Playbook](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Ansible/Fiche_Simple_-_VM_Debian_13_Ansible_Valider_Playbook.md>) | | | | |

#### Apache

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Apache Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Apache/Fiche_Simple_-_VM_Debian_13_Apache_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Apache Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Apache/Fiche_Simple_-_VM_Debian_13_Apache_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Apache Exploiter Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Apache/Fiche_Simple_-_VM_Debian_13_Apache_Exploiter_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Apache Installer Paquet](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Apache/Fiche_Simple_-_VM_Debian_13_Apache_Installer_Paquet.md>) | | | | |
| P1 | [VM Debian 13 Apache Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Apache/Fiche_Simple_-_VM_Debian_13_Apache_Valider.md>) | | | | |

#### BIND9

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 BIND9 Autoritatif Sauvegarde Retour](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BIND9/Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Sauvegarde_Retour.md>) | | | | |
| P1 | [VM Debian 13 BIND9 Autoritatif Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BIND9/Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Installer.md>) | | | | |
| P1 | [VM Debian 13 BIND9 Autoritatif Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BIND9/Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Valider.md>) | | | | |
| P1 | [VM Debian 13 Services Installation DNS BIND9](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BIND9/Fiche_Simple_-_VM_Debian_13_Services_Installation_DNS_BIND9.md>) | | | | |

#### Bareos

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Bareos Valider Restauration](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Bareos/Fiche_Simple_-_VM_Debian_13_Bareos_Valider_Restauration.md>) | | | | |
| P1 | [VM Debian 13 Bareos Installer Paquets](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Bareos/Fiche_Simple_-_VM_Debian_13_Bareos_Installer_Paquets.md>) | | | | |

#### Bash Shell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Bash Shell Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Bash-Shell/Fiche_Simple_-_VM_Debian_13_Bash_Shell_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Bash Shell Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Bash-Shell/Fiche_Simple_-_VM_Debian_13_Bash_Shell_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Bash Shell Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Bash-Shell/Fiche_Simple_-_VM_Debian_13_Bash_Shell_Installer.md>) | | | | |
| P1 | [VM Debian 13 Bash Shell Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Bash-Shell/Fiche_Simple_-_VM_Debian_13_Bash_Shell_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Bash Shell Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Bash-Shell/Fiche_Simple_-_VM_Debian_13_Bash_Shell_Valider.md>) | | | | |

#### BlueMind

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 BlueMind Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Debian_13_BlueMind_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 BlueMind Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Debian_13_BlueMind_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 BlueMind Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Debian_13_BlueMind_Installer.md>) | | | | |
| P1 | [VM Debian 13 BlueMind Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Debian_13_BlueMind_Securiser.md>) | | | | |
| P1 | [VM Debian 13 BlueMind Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Debian_13_BlueMind_Valider.md>) | | | | |

#### Caddy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Caddy Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Caddy/Fiche_Simple_-_VM_Debian_13_Caddy_Retour_Arriere.md>) | | | | |
| P1 | [VM Debian 13 Caddy Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Caddy/Fiche_Simple_-_VM_Debian_13_Caddy_Installer.md>) | | | | |
| P1 | [VM Debian 13 Caddy Valider Service](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Caddy/Fiche_Simple_-_VM_Debian_13_Caddy_Valider_Service.md>) | | | | |

#### Centreon

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Centreon Installer Central](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Installer_Central.md>) | | | | |
| P1 | [VM Debian 13 Centreon Securiser Exploiter](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Centreon/Fiche_Simple_-_VM_Debian_13_Centreon_Securiser_Exploiter.md>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Securite Certbot TLS](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Certbot/Fiche_Simple_-_VM_Debian_13_Securite_Certbot_TLS.md>) | | | | |

#### DHCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Kea Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/DHCP/Fiche_Simple_-_VM_Debian_13_Kea_Installer.md>) | | | | |
| P1 | [VM Debian 13 Kea Valider Demarrer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/DHCP/Fiche_Simple_-_VM_Debian_13_Kea_Valider_Demarrer.md>) | | | | |
| P1 | [VM Debian 13 Services Installation DHCP KEA](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/DHCP/Fiche_Simple_-_VM_Debian_13_Services_Installation_DHCP_KEA.md>) | | | | |

#### Docker

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Installation Docker Engine](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Docker/Fiche_Simple_-_VM_Debian_13_Installation_Docker_Engine.md>) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Dovecot Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Debian_13_Dovecot_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Dovecot Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Debian_13_Dovecot_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Dovecot Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Debian_13_Dovecot_Installer.md>) | | | | |
| P1 | [VM Debian 13 Dovecot Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Debian_13_Dovecot_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Dovecot Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Debian_13_Dovecot_Valider.md>) | | | | |

#### Elastic Stack

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Elastic Stack Installer Elasticsearch](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Elastic-Stack/Fiche_Simple_-_VM_Debian_13_Elastic_Stack_Installer_Elasticsearch.md>) | | | | |
| P1 | [VM Debian 13 Elastic Stack Installer Kibana](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Elastic-Stack/Fiche_Simple_-_VM_Debian_13_Elastic_Stack_Installer_Kibana.md>) | | | | |

#### FOG Project

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 FOG Project Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FOG-Project/Fiche_Simple_-_VM_Debian_13_FOG_Project_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 FOG Project Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FOG-Project/Fiche_Simple_-_VM_Debian_13_FOG_Project_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 FOG Project Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FOG-Project/Fiche_Simple_-_VM_Debian_13_FOG_Project_Installer.md>) | | | | |
| P1 | [VM Debian 13 FOG Project Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FOG-Project/Fiche_Simple_-_VM_Debian_13_FOG_Project_Securiser.md>) | | | | |
| P1 | [VM Debian 13 FOG Project Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FOG-Project/Fiche_Simple_-_VM_Debian_13_FOG_Project_Valider.md>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Securite Fail2ban](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Debian_13_Securite_Fail2ban.md>) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 FreeIPA Client Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 FreeIPA Client Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Installer.md>) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Securiser.md>) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Valider.md>) | | | | |

#### GNS3

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 GNS3 Deploiement Sauvegarde MAJ](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GNS3/Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Sauvegarde_MAJ.md>) | | | | |
| P1 | [VM Debian 13 GNS3 Deploiement Installer GUI Serveur](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GNS3/Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Installer_GUI_Serveur.md>) | | | | |
| P1 | [VM Debian 13 GNS3 Valider Lab Isole](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GNS3/Fiche_Simple_-_VM_Debian_13_GNS3_Valider_Lab_Isole.md>) | | | | |

#### Git

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Git Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Installer.md>) | | | | |

#### GitLab

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 GitLab CE Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GitLab/Fiche_Simple_-_VM_Debian_13_GitLab_CE_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 GitLab CE Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GitLab/Fiche_Simple_-_VM_Debian_13_GitLab_CE_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 GitLab CE Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GitLab/Fiche_Simple_-_VM_Debian_13_GitLab_CE_Installer.md>) | | | | |
| P1 | [VM Debian 13 GitLab CE Securiser TLS](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GitLab/Fiche_Simple_-_VM_Debian_13_GitLab_CE_Securiser_TLS.md>) | | | | |
| P1 | [VM Debian 13 GitLab CE Valider Recette](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GitLab/Fiche_Simple_-_VM_Debian_13_GitLab_CE_Valider_Recette.md>) | | | | |

#### Gitea

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Gitea Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Gitea/Fiche_Simple_-_VM_Debian_13_Gitea_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Gitea Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Gitea/Fiche_Simple_-_VM_Debian_13_Gitea_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Gitea Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Gitea/Fiche_Simple_-_VM_Debian_13_Gitea_Installer.md>) | | | | |
| P1 | [VM Debian 13 Gitea Securiser TLS](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Gitea/Fiche_Simple_-_VM_Debian_13_Gitea_Securiser_TLS.md>) | | | | |
| P1 | [VM Debian 13 Gitea Valider Recette](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Gitea/Fiche_Simple_-_VM_Debian_13_Gitea_Valider_Recette.md>) | | | | |

#### HAProxy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 HAProxy Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/HAProxy/Fiche_Simple_-_VM_Debian_13_HAProxy_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 HAProxy Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/HAProxy/Fiche_Simple_-_VM_Debian_13_HAProxy_Installer.md>) | | | | |
| P1 | [VM Debian 13 HAProxy Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/HAProxy/Fiche_Simple_-_VM_Debian_13_HAProxy_Securiser.md>) | | | | |
| P1 | [VM Debian 13 HAProxy Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/HAProxy/Fiche_Simple_-_VM_Debian_13_HAProxy_Valider.md>) | | | | |

#### HashiCorp Vault

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Debian 13 Hashicorp Vault Valider Politique](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/HashiCorp-Vault/Fiche_Simple_-_Debian_13_Hashicorp_Vault_Valider_Politique.md>) | | | | |
| P1 | [VM Debian 13 Vault Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/HashiCorp-Vault/Fiche_Simple_-_VM_Debian_13_Vault_Installer.md>) | | | | |

#### ISC DHCP Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 ISC-DHCP-Server Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ISC-DHCP-Server/Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 ISC-DHCP-Server Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ISC-DHCP-Server/Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ISC-DHCP-Server/Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Installer.md>) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ISC-DHCP-Server/Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Securiser.md>) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ISC-DHCP-Server/Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider.md>) | | | | |

#### InfluxDB3 Core

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [InfluxDB3 Core Debian 13 Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/InfluxDB3-Core/Fiche_Simple_-_InfluxDB3_Core_Debian_13_Retour_Arriere.md>) | | | | |
| P0 | [InfluxDB3 Core Debian 13 Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/InfluxDB3-Core/Fiche_Simple_-_InfluxDB3_Core_Debian_13_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [InfluxDB3 Core Debian 13 Installer Depot](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/InfluxDB3-Core/Fiche_Simple_-_InfluxDB3_Core_Debian_13_Installer_Depot.md>) | | | | |
| P1 | [InfluxDB3 Core Debian 13 Valider Ecriture](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/InfluxDB3-Core/Fiche_Simple_-_InfluxDB3_Core_Debian_13_Valider_Ecriture.md>) | | | | |

#### KeePassXC

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 KeePassXC Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Sauvegarder_Restaurer.md>) | | | | |
| P0 | [VM Debian 13 KeePassXC Verifier Mise A Jour](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Verifier_Mise_A_Jour.md>) | | | | |
| P1 | [VM Debian 13 KeePassXC Valider Coffre](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Valider_Coffre.md>) | | | | |

#### Kubernetes K3s

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Kubeadm Sauvegarde Mise A Jour](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Sauvegarde_Mise_A_Jour.md>) | | | | |
| P0 | [VM Debian 13 Kubeadm Sauvegarder Preparer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Sauvegarder_Preparer.md>) | | | | |
| P1 | [VM Debian 13 K3s Installer Noeud Lab](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_K3s_Installer_Noeud_Lab.md>) | | | | |
| P1 | [VM Debian 13 K3s Securiser Surveiller](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_K3s_Securiser_Surveiller.md>) | | | | |
| P1 | [VM Debian 13 Kubeadm Installer Paquets](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Installer_Paquets.md>) | | | | |
| P1 | [VM Debian 13 Kubeadm Installer Runtime](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Installer_Runtime.md>) | | | | |
| P1 | [VM Debian 13 Kubeadm Valider Cluster](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Valider_Cluster.md>) | | | | |

#### LEMP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 LEMP Sauvegarder Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/LEMP/Fiche_Simple_-_VM_Debian_13_LEMP_Sauvegarder_Retour_Arriere.md>) | | | | |

#### MariaDB

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MariaDB Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MariaDB/Fiche_Simple_-_VM_Debian_13_MariaDB_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Database Installation MariaDB 11](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MariaDB/Fiche_Simple_-_VM_Debian_13_Database_Installation_MariaDB_11.md>) | | | | |
| P1 | [VM Debian 13 LEMP Securiser MariaDB](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MariaDB/Fiche_Simple_-_VM_Debian_13_LEMP_Securiser_MariaDB.md>) | | | | |
| P1 | [VM Debian 13 MariaDB Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MariaDB/Fiche_Simple_-_VM_Debian_13_MariaDB_Securiser.md>) | | | | |
| P1 | [VM Debian 13 MariaDB Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MariaDB/Fiche_Simple_-_VM_Debian_13_MariaDB_Valider.md>) | | | | |

#### Minikube

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Minikube Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Minikube Sauvegarde Prealable](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Sauvegarde_Prealable.md>) | | | | |
| P1 | [VM Debian 13 Minikube Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Installer.md>) | | | | |
| P1 | [VM Debian 13 Minikube Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Valider.md>) | | | | |

#### MongoDB

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MongoDB Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MongoDB/Fiche_Simple_-_VM_Debian_13_MongoDB_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 MongoDB Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MongoDB/Fiche_Simple_-_VM_Debian_13_MongoDB_Installer.md>) | | | | |
| P1 | [VM Debian 13 MongoDB Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MongoDB/Fiche_Simple_-_VM_Debian_13_MongoDB_Securiser.md>) | | | | |
| P1 | [VM Debian 13 MongoDB Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MongoDB/Fiche_Simple_-_VM_Debian_13_MongoDB_Valider.md>) | | | | |

#### MySQL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MySQL Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MySQL/Fiche_Simple_-_VM_Debian_13_MySQL_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 MySQL Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MySQL/Fiche_Simple_-_VM_Debian_13_MySQL_Installer.md>) | | | | |
| P1 | [VM Debian 13 MySQL Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MySQL/Fiche_Simple_-_VM_Debian_13_MySQL_Securiser.md>) | | | | |
| P1 | [VM Debian 13 MySQL Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/MySQL/Fiche_Simple_-_VM_Debian_13_MySQL_Valider.md>) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Debian 13 Nakivo Transporter Mettre A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Mettre_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Debian 13 Nakivo Transporter Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Debian 13 Nakivo Transporter Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Installer.md>) | | | | |
| P1 | [Debian 13 Nakivo Transporter Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Securiser.md>) | | | | |
| P1 | [Debian 13 Nakivo Transporter Valider Mettre A Jour](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Valider_Mettre_A_Jour.md>) | | | | |

#### NetBox

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 NetBox Sauvegarder Mettre A Jour](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/NetBox/Fiche_Simple_-_VM_Debian_13_NetBox_Sauvegarder_Mettre_A_Jour.md>) | | | | |
| P1 | [VM Debian 13 NetBox Installer Release](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/NetBox/Fiche_Simple_-_VM_Debian_13_NetBox_Installer_Release.md>) | | | | |
| P1 | [VM Debian 13 NetBox Valider IPAM](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/NetBox/Fiche_Simple_-_VM_Debian_13_NetBox_Valider_IPAM.md>) | | | | |
| P1 | [VM Debian 13 NetBox Valider IPAM Pilote](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/NetBox/Fiche_Simple_-_VM_Debian_13_NetBox_Valider_IPAM_Pilote.md>) | | | | |

#### Nextcloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Nextcloud Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nextcloud/Fiche_Simple_-_VM_Debian_13_Nextcloud_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Nextcloud Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nextcloud/Fiche_Simple_-_VM_Debian_13_Nextcloud_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Nextcloud Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nextcloud/Fiche_Simple_-_VM_Debian_13_Nextcloud_Installer.md>) | | | | |
| P1 | [VM Debian 13 Nextcloud Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nextcloud/Fiche_Simple_-_VM_Debian_13_Nextcloud_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Nextcloud Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nextcloud/Fiche_Simple_-_VM_Debian_13_Nextcloud_Valider.md>) | | | | |

#### Nginx

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Nginx Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nginx/Fiche_Simple_-_VM_Debian_13_Nginx_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Nginx Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nginx/Fiche_Simple_-_VM_Debian_13_Nginx_Installer.md>) | | | | |
| P1 | [VM Debian 13 Nginx Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nginx/Fiche_Simple_-_VM_Debian_13_Nginx_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Nginx Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nginx/Fiche_Simple_-_VM_Debian_13_Nginx_Valider.md>) | | | | |
| P1 | [VM Debian 13 Web Installation Nginx PHP8.4 FPM](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Nginx/Fiche_Simple_-_VM_Debian_13_Web_Installation_Nginx_PHP8.4_FPM.md>) | | | | |

#### OCS Inventory

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OCS Inventory Sauvegarde](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OCS-Inventory/Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Sauvegarde.md>) | | | | |
| P1 | [VM Debian 13 Installer Agent OCS Inventory](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OCS-Inventory/Fiche_Simple_-_VM_Debian_13_Installer_Agent_OCS_Inventory.md>) | | | | |
| P1 | [VM Debian 13 OCS Inventory Installer Paquets](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OCS-Inventory/Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Installer_Paquets.md>) | | | | |

#### Observium

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Observium Sauvegarde Securite](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Sauvegarde_Securite.md>) | | | | |

#### OpenLDAP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenLDAP Restaurer Test](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Restaurer_Test.md>) | | | | |
| P0 | [VM Debian 13 OpenLDAP Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 OpenLDAP Sauvegarder](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Sauvegarder.md>) | | | | |
| P1 | [VM Debian 13 OpenLDAP Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Installer.md>) | | | | |
| P1 | [VM Debian 13 OpenLDAP Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Valider.md>) | | | | |

#### OpenMediaVault

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 OpenMediaVault Installer OMV](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenMediaVault/Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Installer_OMV.md>) | | | | |
| P1 | [VM Debian 13 Stockage Installation OpenMediaVault 8](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenMediaVault/Fiche_Simple_-_VM_Debian_13_Stockage_Installation_OpenMediaVault_8.md>) | | | | |

#### OpenTofu

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenTofu Mise A Jour Rollback](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenTofu/Fiche_Simple_-_VM_Debian_13_OpenTofu_Mise_A_Jour_Rollback.md>) | | | | |
| P1 | [VM Debian 13 OpenTofu Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenTofu/Fiche_Simple_-_VM_Debian_13_OpenTofu_Installer.md>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenVPN Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 OpenVPN Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 OpenVPN Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Installer.md>) | | | | |
| P1 | [VM Debian 13 OpenVPN Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Securiser.md>) | | | | |
| P1 | [VM Debian 13 OpenVPN Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Debian_13_OpenVPN_Valider.md>) | | | | |

#### Packer

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Packer Debian 13 Nettoyer Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Packer/Fiche_Simple_-_Packer_Debian_13_Nettoyer_Retour_Arriere.md>) | | | | |
| P1 | [Packer Debian 13 Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Packer/Fiche_Simple_-_Packer_Debian_13_Installer.md>) | | | | |
| P1 | [Packer Debian 13 Valider Template](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Packer/Fiche_Simple_-_Packer_Debian_13_Valider_Template.md>) | | | | |

#### Passbolt

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Passbolt Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Passbolt/Fiche_Simple_-_VM_Debian_13_Passbolt_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Passbolt Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Passbolt/Fiche_Simple_-_VM_Debian_13_Passbolt_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Passbolt Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Passbolt/Fiche_Simple_-_VM_Debian_13_Passbolt_Installer.md>) | | | | |
| P1 | [VM Debian 13 Passbolt Securiser TLS](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Passbolt/Fiche_Simple_-_VM_Debian_13_Passbolt_Securiser_TLS.md>) | | | | |
| P1 | [VM Debian 13 Passbolt Valider Recette](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Passbolt/Fiche_Simple_-_VM_Debian_13_Passbolt_Valider_Recette.md>) | | | | |

#### Podman Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Podman Buildah Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Podman Buildah Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Podman Buildah Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Installer.md>) | | | | |
| P1 | [VM Debian 13 Podman Buildah Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Podman Buildah Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Valider.md>) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Postfix Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Debian_13_Postfix_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Postfix Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Debian_13_Postfix_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Postfix Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Debian_13_Postfix_Installer.md>) | | | | |
| P1 | [VM Debian 13 Postfix Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Debian_13_Postfix_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Postfix Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Debian_13_Postfix_Valider.md>) | | | | |

#### PostgreSQL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PostgreSQL Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PostgreSQL/Fiche_Simple_-_VM_Debian_13_PostgreSQL_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Database Installation PostgreSQL 17](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PostgreSQL/Fiche_Simple_-_VM_Debian_13_Database_Installation_PostgreSQL_17.md>) | | | | |
| P1 | [VM Debian 13 NetBox Installer PostgreSQL Redis](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PostgreSQL/Fiche_Simple_-_VM_Debian_13_NetBox_Installer_PostgreSQL_Redis.md>) | | | | |
| P1 | [VM Debian 13 PostgreSQL Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PostgreSQL/Fiche_Simple_-_VM_Debian_13_PostgreSQL_Securiser.md>) | | | | |
| P1 | [VM Debian 13 PostgreSQL Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PostgreSQL/Fiche_Simple_-_VM_Debian_13_PostgreSQL_Valider.md>) | | | | |

#### Postman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Postman Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Postman/Fiche_Simple_-_VM_Debian_13_Postman_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P1 | [VM Debian 13 Postman Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Postman/Fiche_Simple_-_VM_Debian_13_Postman_Installer.md>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PowerShell Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Debian_13_PowerShell_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 PowerShell Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Debian_13_PowerShell_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 PowerShell Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Debian_13_PowerShell_Installer.md>) | | | | |
| P1 | [VM Debian 13 PowerShell Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Debian_13_PowerShell_Securiser.md>) | | | | |
| P1 | [VM Debian 13 PowerShell Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Debian_13_PowerShell_Valider.md>) | | | | |

#### Prometheus Grafana

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Prometheus Grafana Sauvegarder](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Prometheus-Grafana/Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Sauvegarder.md>) | | | | |
| P1 | [VM Debian 13 Prometheus Grafana Installer Grafana](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Prometheus-Grafana/Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Installer_Grafana.md>) | | | | |
| P1 | [VM Debian 13 Prometheus Grafana Installer Prometheus](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Prometheus-Grafana/Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Installer_Prometheus.md>) | | | | |

#### PuTTY

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PuTTY Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Debian_13_PuTTY_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 PuTTY Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Debian_13_PuTTY_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 PuTTY Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Debian_13_PuTTY_Installer.md>) | | | | |
| P1 | [VM Debian 13 PuTTY Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Debian_13_PuTTY_Securiser.md>) | | | | |
| P1 | [VM Debian 13 PuTTY Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Debian_13_PuTTY_Valider.md>) | | | | |

#### Python

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Python Installer Outils](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Installer_Outils.md>) | | | | |
| P1 | [VM Debian 13 Python Valider Venv Pipx](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Valider_Venv_Pipx.md>) | | | | |

#### QGIS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 QGIS Maj Sauvegarde](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/QGIS/Fiche_Simple_-_VM_Debian_13_QGIS_Maj_Sauvegarde.md>) | | | | |
| P1 | [VM Debian 13 QGIS Installer QGIS](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/QGIS/Fiche_Simple_-_VM_Debian_13_QGIS_Installer_QGIS.md>) | | | | |
| P1 | [VM Debian 13 QGIS Valider Chaine](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/QGIS/Fiche_Simple_-_VM_Debian_13_QGIS_Valider_Chaine.md>) | | | | |
| P1 | [VM Debian 13 QGIS Valider Projet](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/QGIS/Fiche_Simple_-_VM_Debian_13_QGIS_Valider_Projet.md>) | | | | |

#### Redis

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Redis Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Redis/Fiche_Simple_-_VM_Debian_13_Redis_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Redis Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Redis/Fiche_Simple_-_VM_Debian_13_Redis_Installer.md>) | | | | |
| P1 | [VM Debian 13 Redis Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Redis/Fiche_Simple_-_VM_Debian_13_Redis_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Redis Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Redis/Fiche_Simple_-_VM_Debian_13_Redis_Valider.md>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Sauvegarde Restic Depot](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Restic/Fiche_Simple_-_VM_Debian_13_Sauvegarde_Restic_Depot.md>) | | | | |

#### Samba AD DC

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Samba AD DC Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Samba-AD-DC/Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Samba AD DC Sauvegarde](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Samba-AD-DC/Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Sauvegarde.md>) | | | | |
| P1 | [VM Debian 13 Samba AD DC Reseau Securite](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Samba-AD-DC/Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Reseau_Securite.md>) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Snort Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Debian_13_Snort_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Snort Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Debian_13_Snort_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Snort Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Debian_13_Snort_Installer.md>) | | | | |
| P1 | [VM Debian 13 Snort Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Debian_13_Snort_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Snort Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Debian_13_Snort_Valider.md>) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Suricata IDS Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Debian_13_Suricata_IDS_Installer.md>) | | | | |
| P1 | [VM Debian 13 Suricata Valider Capteur IDS](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Debian_13_Suricata_Valider_Capteur_IDS.md>) | | | | |

#### Terraform

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Terraform Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Terraform/Fiche_Simple_-_VM_Debian_13_Terraform_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 Terraform Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Terraform/Fiche_Simple_-_VM_Debian_13_Terraform_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Terraform Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Terraform/Fiche_Simple_-_VM_Debian_13_Terraform_Installer.md>) | | | | |
| P1 | [VM Debian 13 Terraform Securiser Etat](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Terraform/Fiche_Simple_-_VM_Debian_13_Terraform_Securiser_Etat.md>) | | | | |
| P1 | [VM Debian 13 Terraform Valider Recette](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Terraform/Fiche_Simple_-_VM_Debian_13_Terraform_Valider_Recette.md>) | | | | |

#### Traefik

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Traefik Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Traefik/Fiche_Simple_-_VM_Debian_13_Traefik_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 Traefik Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Traefik/Fiche_Simple_-_VM_Debian_13_Traefik_Installer.md>) | | | | |
| P1 | [VM Debian 13 Traefik Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Traefik/Fiche_Simple_-_VM_Debian_13_Traefik_Securiser.md>) | | | | |
| P1 | [VM Debian 13 Traefik Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Traefik/Fiche_Simple_-_VM_Debian_13_Traefik_Valider.md>) | | | | |

#### VS Code

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 VSCode Mise a jour](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/VS-Code/Fiche_Simple_-_VM_Debian_13_VSCode_Mise_a_jour.md>) | | | | |
| P1 | [VM Debian 13 VSCode Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/VS-Code/Fiche_Simple_-_VM_Debian_13_VSCode_Installer.md>) | | | | |
| P1 | [VM Debian 13 VSCode Valider Installation](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/VS-Code/Fiche_Simple_-_VM_Debian_13_VSCode_Valider_Installation.md>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 WireGuard Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Debian_13_WireGuard_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 WireGuard Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Debian_13_WireGuard_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 WireGuard Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Debian_13_WireGuard_Installer.md>) | | | | |
| P1 | [VM Debian 13 WireGuard Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Debian_13_WireGuard_Securiser.md>) | | | | |
| P1 | [VM Debian 13 WireGuard Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Debian_13_WireGuard_Valider.md>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Wireshark Analyse Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Installer.md>) | | | | |
| P1 | [VM Debian 13 Wireshark Valider Capture Locale](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Debian_13_Wireshark_Valider_Capture_Locale.md>) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Zeek Depot Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Depot_Installer.md>) | | | | |
| P1 | [VM Debian 13 Zeek Valider Capteur](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Valider_Capteur.md>) | | | | |
| P1 | [VM Debian 13 Zeek Valider Logs](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Valider_Logs.md>) | | | | |

#### cURL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 cURL Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/cURL/Fiche_Simple_-_VM_Debian_13_cURL_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 cURL Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/cURL/Fiche_Simple_-_VM_Debian_13_cURL_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 cURL Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/cURL/Fiche_Simple_-_VM_Debian_13_cURL_Installer.md>) | | | | |
| P1 | [VM Debian 13 cURL Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/cURL/Fiche_Simple_-_VM_Debian_13_cURL_Securiser.md>) | | | | |
| P1 | [VM Debian 13 cURL Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/cURL/Fiche_Simple_-_VM_Debian_13_cURL_Valider.md>) | | | | |

#### draw.io

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 draw io Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Installer.md>) | | | | |
| P1 | [VM Debian 13 draw io Valider Diagramme](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Valider_Diagramme.md>) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 ownCloud Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Debian_13_ownCloud_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 ownCloud Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Debian_13_ownCloud_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 ownCloud Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Debian_13_ownCloud_Installer.md>) | | | | |
| P1 | [VM Debian 13 ownCloud Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Debian_13_ownCloud_Securiser.md>) | | | | |
| P1 | [VM Debian 13 ownCloud Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Debian_13_ownCloud_Valider.md>) | | | | |

#### phpIPAM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 phpIPAM Sauvegarder](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/phpIPAM/Fiche_Simple_-_VM_Debian_13_phpIPAM_Sauvegarder.md>) | | | | |
| P1 | [VM Debian 13 phpIPAM Valider IPAM](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/phpIPAM/Fiche_Simple_-_VM_Debian_13_phpIPAM_Valider_IPAM.md>) | | | | |

#### rsync

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 rsync Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/rsync/Fiche_Simple_-_VM_Debian_13_rsync_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 rsync Valider Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/rsync/Fiche_Simple_-_VM_Debian_13_rsync_Valider_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 rsync Installer Preparer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/rsync/Fiche_Simple_-_VM_Debian_13_rsync_Installer_Preparer.md>) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 tcpdump Mise A Jour Retour Arriere](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Debian_13_tcpdump_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Debian 13 tcpdump Sauvegarder Restaurer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Debian_13_tcpdump_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Debian 13 tcpdump Installer](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Debian_13_tcpdump_Installer.md>) | | | | |
| P1 | [VM Debian 13 tcpdump Securiser](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Debian_13_tcpdump_Securiser.md>) | | | | |
| P1 | [VM Debian 13 tcpdump Valider](<../01-Fiches-Simples/Debian/13/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Debian_13_tcpdump_Valider.md>) | | | | |

### OPNsense/Toutes-versions

#### CARP pfsync HA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Appliance OPNsense CARP pfsync Exploitation Retour Arriere](<../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-logiciel/CARP-pfsync-HA/Fiche_Simple_-_Appliance_OPNsense_CARP_pfsync_Exploitation_Retour_Arriere.md>) | | | | |

### Proxmox/Toutes-versions

#### Cluster Stockage VM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Proxmox VE Diagnostic Restaurer](<../01-Fiches-Simples/Proxmox/Toutes-versions/Vie-du-logiciel/Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Restaurer.md>) | | | | |

#### Proxmox Backup Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Proxmox Backup Server Tester Restauration](<../01-Fiches-Simples/Proxmox/Toutes-versions/Vie-du-logiciel/Proxmox-Backup-Server/Fiche_Simple_-_Hote_Proxmox_Backup_Server_Tester_Restauration.md>) | | | | |
| P1 | [Hote Proxmox Backup Server Installer Datastore](<../01-Fiches-Simples/Proxmox/Toutes-versions/Vie-du-logiciel/Proxmox-Backup-Server/Fiche_Simple_-_Hote_Proxmox_Backup_Server_Installer_Datastore.md>) | | | | |

### Proxmox/VE-8

#### Cluster Corosync

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Proxmox VE 8 Cluster Securiser](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Securiser.md>) | | | | |
| P1 | [Hote Proxmox VE 8 Cluster Valider](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Valider.md>) | | | | |

#### Proxmox OpenStack

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Mise A Jour Retour Arriere](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Nettoyer_Retour_Arriere.md>) | | | | |
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Sauvegarder_Restaurer_Lab.md>) | | | | |
| P1 | [VM Proxmox VE 8 Proxmox OpenStack Securiser Valider Lab](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Securiser_Valider_Lab.md>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenStack DevStack Installer Lab](<../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Proxmox-OpenStack/OpenStack/Ubuntu-24.04-LTS/Fiche_Simple_-_VM_Ubuntu_24.04_OpenStack_DevStack_Installer_Lab.md>) | | | | |

### Rocky-Linux/9

#### Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Buildah Publier Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Publier_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 Buildah Sauvegarder Etat Initial](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Sauvegarder_Etat_Initial.md>) | | | | |
| P1 | [VM Rocky 9 Buildah Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Installer.md>) | | | | |
| P1 | [VM Rocky 9 Buildah Valider Image](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Valider_Image.md>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Rocky 9 Securite Certbot TLS](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Certbot/Fiche_Simple_-_VM_Rocky_9_Securite_Certbot_TLS.md>) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Dovecot Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Rocky_9_Dovecot_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 Dovecot Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Rocky_9_Dovecot_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 Dovecot Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Rocky_9_Dovecot_Installer.md>) | | | | |
| P1 | [VM Rocky 9 Dovecot Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Rocky_9_Dovecot_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 Dovecot Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Rocky_9_Dovecot_Valider.md>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Rocky 9 Securite Fail2ban](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Rocky_9_Securite_Fail2ban.md>) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 FreeIPA Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Rocky_9_FreeIPA_Restaurer.md>) | | | | |
| P0 | [VM Rocky 9 FreeIPA Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Rocky_9_FreeIPA_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 FreeIPA Sauvegarder](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Rocky_9_FreeIPA_Sauvegarder.md>) | | | | |
| P1 | [VM Rocky 9 FreeIPA Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Rocky_9_FreeIPA_Installer.md>) | | | | |
| P1 | [VM Rocky 9 FreeIPA Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Rocky_9_FreeIPA_Valider.md>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 OpenVPN Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 OpenVPN Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 OpenVPN Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Installer.md>) | | | | |
| P1 | [VM Rocky 9 OpenVPN Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 OpenVPN Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Rocky_9_OpenVPN_Valider.md>) | | | | |

#### Pile Web

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Pile Web Sauvegarder Retour](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Sauvegarder_Retour.md>) | | | | |
| P1 | [VM Rocky 9 Pile Web Installer Paquets](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Installer_Paquets.md>) | | | | |
| P1 | [VM Rocky 9 Pile Web Securiser MariaDB](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Securiser_MariaDB.md>) | | | | |

#### Podman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Podman Quadlet Mise A Jour Reprise](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Podman/Fiche_Simple_-_VM_Rocky_9_Podman_Quadlet_Mise_A_Jour_Reprise.md>) | | | | |
| P1 | [VM Rocky 9 Podman Quadlet Valider Image](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Podman/Fiche_Simple_-_VM_Rocky_9_Podman_Quadlet_Valider_Image.md>) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Postfix Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Rocky_9_Postfix_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 Postfix Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Rocky_9_Postfix_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 Postfix Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Rocky_9_Postfix_Installer.md>) | | | | |
| P1 | [VM Rocky 9 Postfix Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Rocky_9_Postfix_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 Postfix Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Rocky_9_Postfix_Valider.md>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 PowerShell Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Rocky_9_PowerShell_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 PowerShell Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Rocky_9_PowerShell_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 PowerShell Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Rocky_9_PowerShell_Installer.md>) | | | | |
| P1 | [VM Rocky 9 PowerShell Securiser Signature](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Rocky_9_PowerShell_Securiser_Signature.md>) | | | | |
| P1 | [VM Rocky 9 PowerShell Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Rocky_9_PowerShell_Valider.md>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Sauvegarde Restic Depot](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Restic/Fiche_Simple_-_VM_Rocky_9_Sauvegarde_Restic_Depot.md>) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Snort Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Rocky_9_Snort_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 Snort Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Rocky_9_Snort_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 Snort Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Rocky_9_Snort_Installer.md>) | | | | |
| P1 | [VM Rocky 9 Snort Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Rocky_9_Snort_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 Snort Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Rocky_9_Snort_Valider.md>) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Suricata Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Rocky_9_Suricata_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 Suricata Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Rocky_9_Suricata_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 Suricata Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Rocky_9_Suricata_Installer.md>) | | | | |
| P1 | [VM Rocky 9 Suricata Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Rocky_9_Suricata_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 Suricata Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Rocky_9_Suricata_Valider.md>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 WireGuard Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Rocky_9_WireGuard_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 WireGuard Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Rocky_9_WireGuard_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 WireGuard Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Rocky_9_WireGuard_Installer.md>) | | | | |
| P1 | [VM Rocky 9 WireGuard Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Rocky_9_WireGuard_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 WireGuard Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Rocky_9_WireGuard_Valider.md>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Wireshark Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Rocky_9_Wireshark_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 Wireshark Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Rocky_9_Wireshark_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 Wireshark Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Rocky_9_Wireshark_Installer.md>) | | | | |
| P1 | [VM Rocky 9 Wireshark Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Rocky_9_Wireshark_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 Wireshark Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Rocky_9_Wireshark_Valider.md>) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Zeek Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Rocky_9_Zeek_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 Zeek Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Rocky_9_Zeek_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 Zeek Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Rocky_9_Zeek_Installer.md>) | | | | |
| P1 | [VM Rocky 9 Zeek Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Rocky_9_Zeek_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 Zeek Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Rocky_9_Zeek_Valider.md>) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 ownCloud Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Rocky_9_ownCloud_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 ownCloud Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Rocky_9_ownCloud_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 ownCloud Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Rocky_9_ownCloud_Installer.md>) | | | | |
| P1 | [VM Rocky 9 ownCloud Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Rocky_9_ownCloud_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 ownCloud Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Rocky_9_ownCloud_Valider.md>) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 tcpdump Mise A Jour Retour Arriere](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Rocky_9_tcpdump_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Rocky 9 tcpdump Sauvegarder Restaurer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Rocky_9_tcpdump_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Rocky 9 tcpdump Installer](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Rocky_9_tcpdump_Installer.md>) | | | | |
| P1 | [VM Rocky 9 tcpdump Securiser](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Rocky_9_tcpdump_Securiser.md>) | | | | |
| P1 | [VM Rocky 9 tcpdump Valider](<../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Rocky_9_tcpdump_Valider.md>) | | | | |

### Transverses/Cloud-SaaS

#### AWS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud AWS Nettoyage Retour Arriere](<../01-Fiches-Simples/Transverses/Cloud-SaaS/AWS/Fiche_Simple_-_Cloud_AWS_Nettoyage_Retour_Arriere.md>) | | | | |
| P0 | [Cloud AWS Sauvegardes Snapshots](<../01-Fiches-Simples/Transverses/Cloud-SaaS/AWS/Fiche_Simple_-_Cloud_AWS_Sauvegardes_Snapshots.md>) | | | | |

#### Azure

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Azure Nettoyage Retour Arriere](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Azure/Fiche_Simple_-_Cloud_Azure_Nettoyage_Retour_Arriere.md>) | | | | |
| P0 | [Cloud Azure Sauvegardes Snapshots](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Azure/Fiche_Simple_-_Cloud_Azure_Sauvegardes_Snapshots.md>) | | | | |

#### Datadog

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Datadog Retour Arriere](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Retour_Arriere.md>) | | | | |
| P1 | [Cloud Datadog Installer Agent Linux Pilote](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Installer_Agent_Linux_Pilote.md>) | | | | |
| P1 | [Cloud Datadog Securite Maintenance](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Securite_Maintenance.md>) | | | | |

#### Dynatrace

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Dynatrace OneAgent Securite MaJ Retour](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Dynatrace/Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Securite_MaJ_Retour.md>) | | | | |
| P1 | [Cloud Dynatrace OneAgent Generer Installateur](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Dynatrace/Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Generer_Installateur.md>) | | | | |
| P1 | [Cloud Dynatrace OneAgent Installer Pilote](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Dynatrace/Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Installer_Pilote.md>) | | | | |
| P1 | [Cloud Dynatrace OneAgent Installer Pilote Linux](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Dynatrace/Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Installer_Pilote_Linux.md>) | | | | |

#### Entra ID

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Entra ID Connect Retour Arriere](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Entra-ID/Fiche_Simple_-_Cloud_Entra_ID_Connect_Retour_Arriere.md>) | | | | |

#### Exchange Online

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Cloud Exchange Online Valider Recette](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Exchange-Online/Fiche_Simple_-_Cloud_Exchange_Online_Valider_Recette.md>) | | | | |

#### GCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud GCP Nettoyage Retour Arriere](<../01-Fiches-Simples/Transverses/Cloud-SaaS/GCP/Fiche_Simple_-_Cloud_GCP_Nettoyage_Retour_Arriere.md>) | | | | |
| P0 | [Cloud GCP Sauvegardes Snapshots](<../01-Fiches-Simples/Transverses/Cloud-SaaS/GCP/Fiche_Simple_-_Cloud_GCP_Sauvegardes_Snapshots.md>) | | | | |

#### Google Workspace

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Cloud Google Workspace Valider Recette](<../01-Fiches-Simples/Transverses/Cloud-SaaS/Google-Workspace/Fiche_Simple_-_Cloud_Google_Workspace_Valider_Recette.md>) | | | | |

### Transverses/Docker

#### Bitwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Bitwarden Self Hosted Deploiement Sauvegardes Mises A Jour Reprise](<../01-Fiches-Simples/Transverses/Docker/Bitwarden/Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Sauvegardes_Mises_A_Jour_Reprise.md>) | | | | |
| P0 | [Bitwarden Self Hosted Verifier Backup Restauration](<../01-Fiches-Simples/Transverses/Docker/Bitwarden/Fiche_Simple_-_Bitwarden_Self_Hosted_Verifier_Backup_Restauration.md>) | | | | |
| P1 | [Bitwarden Self Hosted Deploiement Telecharger Installer](<../01-Fiches-Simples/Transverses/Docker/Bitwarden/Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Telecharger_Installer.md>) | | | | |

#### Guacamole

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Docker Guacamole Mise A Jour Retour Arriere](<../01-Fiches-Simples/Transverses/Docker/Guacamole/Fiche_Simple_-_Hote_Docker_Guacamole_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Hote Docker Guacamole Sauvegarde Restauration](<../01-Fiches-Simples/Transverses/Docker/Guacamole/Fiche_Simple_-_Hote_Docker_Guacamole_Sauvegarde_Restauration.md>) | | | | |
| P1 | [Hote Docker Guacamole Valider Controle Acces](<../01-Fiches-Simples/Transverses/Docker/Guacamole/Fiche_Simple_-_Hote_Docker_Guacamole_Valider_Controle_Acces.md>) | | | | |

#### Installation systeme

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Docker Installation Engine et Compose](<../01-Fiches-Simples/Transverses/Docker/Installation-systeme/Fiche_Simple_-_Hote_Docker_Installation_Engine_et_Compose.md>) | | | | |

#### Nextcloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Nextcloud29 Migration Retour Arriere](<../01-Fiches-Simples/Transverses/Docker/Nextcloud/Fiche_Simple_-_Docker_Nextcloud29_Migration_Retour_Arriere.md>) | | | | |
| P0 | [Docker Nextcloud29 Migration Sauvegarder Tester Restauration](<../01-Fiches-Simples/Transverses/Docker/Nextcloud/Fiche_Simple_-_Docker_Nextcloud29_Migration_Sauvegarder_Tester_Restauration.md>) | | | | |

#### Sauvegarde restauration

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Sauvegarder Restaurer Volume](<../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Docker_Sauvegarder_Restaurer_Volume.md>) | | | | |
| P0 | [Docker Sauvegarder Stack Compose Base Donnees](<../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Docker_Sauvegarder_Stack_Compose_Base_Donnees.md>) | | | | |
| P0 | [Hote Docker Stack Restaurer](<../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Restaurer.md>) | | | | |
| P0 | [Hote Docker Stack Verifier Sauvegarde](<../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Verifier_Sauvegarde.md>) | | | | |

#### Securite

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Docker Securite Activer Mode Rootless](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Activer_Mode_Rootless.md>) | | | | |
| P1 | [Hote Docker Securite Hardening Images Mises A Jour](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Hardening_Images_Mises_A_Jour.md>) | | | | |
| P1 | [Hote Docker Securite Hardening Inventaire Plan Controle](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Hardening_Inventaire_Plan_Controle.md>) | | | | |
| P1 | [Hote Docker Securite Hardening Reduire Privileges](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Hardening_Reduire_Privileges.md>) | | | | |
| P1 | [Hote Docker Securite Hardening Reponse Incident](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Hardening_Reponse_Incident.md>) | | | | |
| P1 | [Hote Docker Securite Hardening Ressources Journaux](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Hardening_Ressources_Journaux.md>) | | | | |
| P1 | [Hote Docker Securite Hardening Segmentation Donnees](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Hardening_Segmentation_Donnees.md>) | | | | |
| P1 | [Hote Docker Securite Hardening Verifier Exploiter](<../01-Fiches-Simples/Transverses/Docker/Securite/Fiche_Simple_-_Hote_Docker_Securite_Hardening_Verifier_Exploiter.md>) | | | | |

#### Snipe IT

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Snipe-IT Mise A Jour Retour](<../01-Fiches-Simples/Transverses/Docker/Snipe-IT/Fiche_Simple_-_Docker_Snipe-IT_Mise_A_Jour_Retour.md>) | | | | |
| P0 | [Docker Snipe-IT Sauvegarde Restauration](<../01-Fiches-Simples/Transverses/Docker/Snipe-IT/Fiche_Simple_-_Docker_Snipe-IT_Sauvegarde_Restauration.md>) | | | | |
| P1 | [Docker Snipe-IT Valider Demarrer](<../01-Fiches-Simples/Transverses/Docker/Snipe-IT/Fiche_Simple_-_Docker_Snipe-IT_Valider_Demarrer.md>) | | | | |

#### Traefik

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Conteneur Traefik Mise A Jour Retour](<../01-Fiches-Simples/Transverses/Docker/Traefik/Fiche_Simple_-_Docker_Conteneur_Traefik_Mise_A_Jour_Retour.md>) | | | | |

#### Validation

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Production Mise A Jour Rollback Compose](<../01-Fiches-Simples/Transverses/Docker/Validation/Fiche_Simple_-_Docker_Production_Mise_A_Jour_Rollback_Compose.md>) | | | | |
| P0 | [Docker Production Reconstruire Hote Restaurer Stacks](<../01-Fiches-Simples/Transverses/Docker/Validation/Fiche_Simple_-_Docker_Production_Reconstruire_Hote_Restaurer_Stacks.md>) | | | | |

#### Vaultwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Docker Vaultwarden Restaurer](<../01-Fiches-Simples/Transverses/Docker/Vaultwarden/Fiche_Simple_-_Hote_Docker_Vaultwarden_Restaurer.md>) | | | | |
| P0 | [Hote Docker Vaultwarden Retour Arriere](<../01-Fiches-Simples/Transverses/Docker/Vaultwarden/Fiche_Simple_-_Hote_Docker_Vaultwarden_Retour_Arriere.md>) | | | | |
| P0 | [Hote Docker Vaultwarden Sauvegarder](<../01-Fiches-Simples/Transverses/Docker/Vaultwarden/Fiche_Simple_-_Hote_Docker_Vaultwarden_Sauvegarder.md>) | | | | |
| P1 | [Hote Docker Vaultwarden Validation](<../01-Fiches-Simples/Transverses/Docker/Vaultwarden/Fiche_Simple_-_Hote_Docker_Vaultwarden_Validation.md>) | | | | |

#### WikiJS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker WikiJS Mise A Jour Retour Arriere](<../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Docker WikiJS Sauvegarder Restaurer](<../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Docker WikiJS Valider Demarrer](<../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Valider_Demarrer.md>) | | | | |

### Transverses/Multi-OS

#### Diagnostic Reseau

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Multi-OS Reseau Diagnostic Validation Retour Arriere](<../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Validation_Retour_Arriere.md>) | | | | |
| P1 | [VM Multi-OS Reseau Diagnostic Securiser Diagnostic](<../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Securiser_Diagnostic.md>) | | | | |

#### Keepalived HAProxy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Linux Keepalived HAProxy Securite Retour Arriere](<../01-Fiches-Simples/Transverses/Multi-OS/Keepalived-HAProxy/Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Securite_Retour_Arriere.md>) | | | | |
| P1 | [VM Linux Keepalived HAProxy Installer Valider HAProxy](<../01-Fiches-Simples/Transverses/Multi-OS/Keepalived-HAProxy/Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Installer_Valider_HAProxy.md>) | | | | |

### Ubuntu/24.04

#### BlueMind

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 BlueMind Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Ubuntu_24.04_BlueMind_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 BlueMind Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Ubuntu_24.04_BlueMind_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 BlueMind Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Ubuntu_24.04_BlueMind_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 BlueMind Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Ubuntu_24.04_BlueMind_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 BlueMind Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/BlueMind/Fiche_Simple_-_VM_Ubuntu_24.04_BlueMind_Valider.md>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 24.04 Securite Certbot TLS](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Certbot/Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Certbot_TLS.md>) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Dovecot Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Dovecot Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Dovecot Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Dovecot Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Dovecot Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Dovecot/Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Valider.md>) | | | | |

#### EVE NG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 EVE-NG Mettre A Jour Retour](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/EVE-NG/Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Mettre_A_Jour_Retour.md>) | | | | |
| P0 | [VM Ubuntu 24.04 EVE-NG Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/EVE-NG/Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 EVE-NG Creer Valider Lab](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/EVE-NG/Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Creer_Valider_Lab.md>) | | | | |
| P1 | [VM Ubuntu 24.04 EVE-NG Installer ISO VM](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/EVE-NG/Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Installer_ISO_VM.md>) | | | | |
| P1 | [VM Ubuntu 24.04 EVE-NG Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/EVE-NG/Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Securiser.md>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 24.04 Securite Fail2ban](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Fail2ban.md>) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 FreeIPA Client Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 FreeIPA Client Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 FreeIPA Client Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 FreeIPA Client Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 FreeIPA Client Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Valider.md>) | | | | |

#### Graylog

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Graylog Verifier Exploiter Sauvegarder](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Graylog/Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Verifier_Exploiter_Sauvegarder.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Installer Data Node](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Graylog/Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Installer_Data_Node.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Installer MongoDB](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Graylog/Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Installer_MongoDB.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Installer Server](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Graylog/Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Installer_Server.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Valider Input Syslog Pilote](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Graylog/Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Valider_Input_Syslog_Pilote.md>) | | | | |

#### LEMP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 LEMP Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/LEMP/Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 LEMP Valider Sauvegarder Exploiter](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/LEMP/Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Valider_Sauvegarder_Exploiter.md>) | | | | |
| P1 | [VM Ubuntu 24.04 LEMP Installer Pile](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/LEMP/Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Installer_Pile.md>) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Ubuntu 24.04 Nakivo Transporter Mettre A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Mettre_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Ubuntu 24.04 Nakivo Transporter Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Ubuntu 24.04 Nakivo Transporter Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Installer.md>) | | | | |
| P1 | [Ubuntu 24.04 Nakivo Transporter Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Securiser.md>) | | | | |
| P1 | [Ubuntu 24.04 Nakivo Transporter Valider Mettre A Jour](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Valider_Mettre_A_Jour.md>) | | | | |

#### OpenLDAP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 OpenLDAP Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 OpenLDAP Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenLDAP Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenLDAP Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenLDAP Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Valider.md>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 OpenVPN Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 OpenVPN Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenVPN Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenVPN Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenVPN Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Valider.md>) | | | | |

#### Packet Tracer

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Packet Tracer Sauvegarder Maintenir](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Packet-Tracer/Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Sauvegarder_Maintenir.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Packet Tracer Installer Paquet](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Packet-Tracer/Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Installer_Paquet.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Packet Tracer Valider Simulation](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Packet-Tracer/Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Valider_Simulation.md>) | | | | |

#### Podman Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Podman Buildah Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Podman Buildah Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Podman Buildah Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Podman Buildah Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Podman Buildah Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Podman-Buildah/Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Valider.md>) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Postfix Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Postfix Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Postfix Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Postfix Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Postfix Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Postfix/Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Valider.md>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 PowerShell Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 PowerShell Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 PowerShell Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 PowerShell Securiser Signature](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Securiser_Signature.md>) | | | | |
| P1 | [VM Ubuntu 24.04 PowerShell Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Valider.md>) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Snort Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Snort Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Snort Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Snort Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Snort Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Snort/Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Valider.md>) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Suricata Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Suricata Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Suricata Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Suricata Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Suricata Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Suricata/Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Valider.md>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 WireGuard Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 WireGuard Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 WireGuard Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 WireGuard Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 WireGuard Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/WireGuard/Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Valider.md>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Wireshark Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Wireshark Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Wireshark Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Wireshark Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Wireshark Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Valider.md>) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Zeek Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 Zeek Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Zeek Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Zeek Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 Zeek Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Valider.md>) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 ownCloud Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 ownCloud Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 ownCloud Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 ownCloud Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 ownCloud Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/ownCloud/Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Valider.md>) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 tcpdump Mise A Jour Retour Arriere](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Ubuntu 24.04 tcpdump Sauvegarder Restaurer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 tcpdump Installer](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Installer.md>) | | | | |
| P1 | [VM Ubuntu 24.04 tcpdump Securiser](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Securiser.md>) | | | | |
| P1 | [VM Ubuntu 24.04 tcpdump Valider](<../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/tcpdump/Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Valider.md>) | | | | |

### Ubuntu/26.04

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 26.04 Securite Certbot TLS](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Certbot/Fiche_Simple_-_VM_Ubuntu_26.04_Securite_Certbot_TLS.md>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 26.04 Securite Fail2ban](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Fail2ban/Fiche_Simple_-_VM_Ubuntu_26.04_Securite_Fail2ban.md>) | | | | |

#### LibreNMS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26.04 LibreNMS Sauvegarde Mises A Jour](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/LibreNMS/Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Sauvegarde_Mises_A_Jour.md>) | | | | |
| P1 | [VM Ubuntu 26.04 LibreNMS Installer Paquets](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/LibreNMS/Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Installer_Paquets.md>) | | | | |

#### Pile Web

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26.04 Pile Web Validation Sauvegarde Retour](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Validation_Sauvegarde_Retour.md>) | | | | |
| P1 | [VM Ubuntu 26.04 Pile Web Installer Nginx PHP PostgreSQL](<../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Installer_Nginx_PHP_PostgreSQL.md>) | | | | |

### Ubuntu/Toutes-versions

#### Ceph

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu Ceph Sauvegarde Upgrade Retrait](<../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Ceph/Fiche_Simple_-_VM_Ubuntu_Ceph_Sauvegarde_Upgrade_Retrait.md>) | | | | |
| P1 | [VM Ubuntu Ceph Installer Cephadm Bootstrap](<../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Ceph/Fiche_Simple_-_VM_Ubuntu_Ceph_Installer_Cephadm_Bootstrap.md>) | | | | |
| P1 | [VM Ubuntu Ceph Limites Validation](<../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Ceph/Fiche_Simple_-_VM_Ubuntu_Ceph_Limites_Validation.md>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu Restic Effectuer Sauvegarde](<../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Restic/Fiche_Simple_-_VM_Ubuntu_Restic_Effectuer_Sauvegarde.md>) | | | | |
| P0 | [VM Ubuntu Restic Restaurer Sans Ecraser](<../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Restic/Fiche_Simple_-_VM_Ubuntu_Restic_Restaurer_Sans_Ecraser.md>) | | | | |
| P1 | [VM Ubuntu Restic Installer Proteger Secret](<../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Restic/Fiche_Simple_-_VM_Ubuntu_Restic_Installer_Proteger_Secret.md>) | | | | |

### VMware/ESXi-8

#### vSphere

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM ESXi 8 VMware vSphere VCSA Sauvegarde Restauration VAMI](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-logiciel/vSphere/Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_VCSA_Sauvegarde_Restauration_VAMI.md>) | | | | |
| P1 | [VM ESXi 8 VMware vSphere VCSA Installer](<../01-Fiches-Simples/VMware/ESXi-8/Vie-du-logiciel/vSphere/Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_VCSA_Installer.md>) | | | | |

### Windows/Client-11

#### Bitwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Bitwarden Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Bitwarden/Fiche_Simple_-_VM_Windows_11_Bitwarden_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Windows 11 Bitwarden Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Bitwarden/Fiche_Simple_-_VM_Windows_11_Bitwarden_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Windows 11 Bitwarden Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Bitwarden/Fiche_Simple_-_VM_Windows_11_Bitwarden_Installer.md>) | | | | |
| P1 | [VM Windows 11 Bitwarden Securiser](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Bitwarden/Fiche_Simple_-_VM_Windows_11_Bitwarden_Securiser.md>) | | | | |
| P1 | [VM Windows 11 Bitwarden Valider](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Bitwarden/Fiche_Simple_-_VM_Windows_11_Bitwarden_Valider.md>) | | | | |

#### Microsoft Visio

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Visio Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Microsoft-Visio/Fiche_Simple_-_VM_Windows_11_Visio_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Windows 11 Visio Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Microsoft-Visio/Fiche_Simple_-_VM_Windows_11_Visio_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Windows 11 Visio Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Microsoft-Visio/Fiche_Simple_-_VM_Windows_11_Visio_Installer.md>) | | | | |
| P1 | [VM Windows 11 Visio Securiser](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Microsoft-Visio/Fiche_Simple_-_VM_Windows_11_Visio_Securiser.md>) | | | | |
| P1 | [VM Windows 11 Visio Valider](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Microsoft-Visio/Fiche_Simple_-_VM_Windows_11_Visio_Valider.md>) | | | | |

#### MobaXterm

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 MobaXterm Mise A Jour Rollback](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/MobaXterm/Fiche_Simple_-_VM_Windows_11_MobaXterm_Mise_A_Jour_Rollback.md>) | | | | |
| P0 | [VM Windows 11 MobaXterm Sauvegarde Restauration](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/MobaXterm/Fiche_Simple_-_VM_Windows_11_MobaXterm_Sauvegarde_Restauration.md>) | | | | |
| P1 | [VM Windows 11 MobaXterm Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/MobaXterm/Fiche_Simple_-_VM_Windows_11_MobaXterm_Installer.md>) | | | | |
| P1 | [VM Windows 11 MobaXterm Securisation](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/MobaXterm/Fiche_Simple_-_VM_Windows_11_MobaXterm_Securisation.md>) | | | | |
| P1 | [VM Windows 11 MobaXterm Validation](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/MobaXterm/Fiche_Simple_-_VM_Windows_11_MobaXterm_Validation.md>) | | | | |

#### OpenSSH

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows 11 Administration Installer OpenSSH Cle](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/OpenSSH/Fiche_Simple_-_VM_Windows_11_Administration_Installer_OpenSSH_Cle.md>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Client 11 OpenVPN Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Client 11 OpenVPN Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Client 11 OpenVPN Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Installer.md>) | | | | |
| P1 | [Windows Client 11 OpenVPN Securiser](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Securiser.md>) | | | | |
| P1 | [Windows Client 11 OpenVPN Valider](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/OpenVPN/Fiche_Simple_-_Windows_Client_11_OpenVPN_Valider.md>) | | | | |

#### Postman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Postman Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Postman/Fiche_Simple_-_VM_Windows_11_Postman_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P1 | [VM Windows 11 Postman Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Postman/Fiche_Simple_-_VM_Windows_11_Postman_Installer.md>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 PowerShell7 Mise A Jour Validation](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Windows_11_PowerShell7_Mise_A_Jour_Validation.md>) | | | | |
| P1 | [VM Windows 11 PowerShell7 Installer Version Stable](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Windows_11_PowerShell7_Installer_Version_Stable.md>) | | | | |
| P1 | [VM Windows 11 PowerShell Valider Shell Admin](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Windows_11_PowerShell_Valider_Shell_Admin.md>) | | | | |

#### PuTTY

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 PuTTY Mise A Jour Reception](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Mise_A_Jour_Reception.md>) | | | | |
| P1 | [VM Windows 11 PuTTY Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Installer.md>) | | | | |
| P1 | [VM Windows 11 PuTTY Valider SSH HostKey](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Valider_SSH_HostKey.md>) | | | | |

#### Royal TS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Royal TS Mise A Jour](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Royal-TS/Fiche_Simple_-_VM_Windows_11_Royal_TS_Mise_A_Jour.md>) | | | | |
| P0 | [VM Windows 11 Royal TS Sauvegarde Config](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Royal-TS/Fiche_Simple_-_VM_Windows_11_Royal_TS_Sauvegarde_Config.md>) | | | | |
| P1 | [VM Windows 11 Royal TS Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Royal-TS/Fiche_Simple_-_VM_Windows_11_Royal_TS_Installer.md>) | | | | |

#### Sysinternals

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Sysinternals Retour Arriere Limites](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Sysinternals/Fiche_Simple_-_VM_Windows_11_Sysinternals_Retour_Arriere_Limites.md>) | | | | |
| P1 | [VM Windows 11 Sysinternals Collecte Validation](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Sysinternals/Fiche_Simple_-_VM_Windows_11_Sysinternals_Collecte_Validation.md>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Client 11 WireGuard Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/WireGuard/Fiche_Simple_-_Windows_Client_11_WireGuard_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Client 11 WireGuard Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/WireGuard/Fiche_Simple_-_Windows_Client_11_WireGuard_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Client 11 WireGuard Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/WireGuard/Fiche_Simple_-_Windows_Client_11_WireGuard_Installer.md>) | | | | |
| P1 | [Windows Client 11 WireGuard Securiser](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/WireGuard/Fiche_Simple_-_Windows_Client_11_WireGuard_Securiser.md>) | | | | |
| P1 | [Windows Client 11 WireGuard Valider](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/WireGuard/Fiche_Simple_-_Windows_Client_11_WireGuard_Valider.md>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Wireshark Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Windows_11_Wireshark_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [VM Windows 11 Wireshark Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Windows_11_Wireshark_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [VM Windows 11 Wireshark Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Windows_11_Wireshark_Installer.md>) | | | | |
| P1 | [VM Windows 11 Wireshark Securiser Droits Captures](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Windows_11_Wireshark_Securiser_Droits_Captures.md>) | | | | |
| P1 | [VM Windows 11 Wireshark Valider Recette](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Wireshark/Fiche_Simple_-_VM_Windows_11_Wireshark_Valider_Recette.md>) | | | | |

#### mRemoteNG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 mRemoteNG Mise A Jour Rollback](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/mRemoteNG/Fiche_Simple_-_VM_Windows_11_mRemoteNG_Mise_A_Jour_Rollback.md>) | | | | |
| P0 | [VM Windows 11 mRemoteNG Sauvegarde Restauration](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/mRemoteNG/Fiche_Simple_-_VM_Windows_11_mRemoteNG_Sauvegarde_Restauration.md>) | | | | |
| P1 | [VM Windows 11 mRemoteNG Installer](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/mRemoteNG/Fiche_Simple_-_VM_Windows_11_mRemoteNG_Installer.md>) | | | | |
| P1 | [VM Windows 11 mRemoteNG Securisation](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/mRemoteNG/Fiche_Simple_-_VM_Windows_11_mRemoteNG_Securisation.md>) | | | | |
| P1 | [VM Windows 11 mRemoteNG Validation](<../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/mRemoteNG/Fiche_Simple_-_VM_Windows_11_mRemoteNG_Validation.md>) | | | | |

### Windows/Server-2022

#### Active Directory

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 ADDS DNS DHCP Sauvegarde Securite Retour](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Sauvegarde_Securite_Retour.md>) | | | | |
| P0 | [VM Windows Server 2022 Reprise Foret AD DS Preparer Sauvegardes](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Preparer_Sauvegardes.md>) | | | | |
| P0 | [VM Windows Server 2022 Reprise Foret AD DS Restaurer Premiers DC](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Restaurer_Premiers_DC.md>) | | | | |
| P1 | [VM Windows Server 2022 ADDS DNS DHCP Valider ADDS DNS](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Valider_ADDS_DNS.md>) | | | | |
| P1 | [VM Windows Server 2022 Reprise Foret AD DS Risques Identite Securite](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Risques_Identite_Securite.md>) | | | | |
| P1 | [VM Windows Server 2022 Reprise Foret AD DS Valider Avant Production](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Valider_Avant_Production.md>) | | | | |

#### Citrix Virtual Apps and Desktops

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Citrix CVAD Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Citrix-Virtual-Apps-and-Desktops/Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Server 2022 Citrix CVAD Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Citrix-Virtual-Apps-and-Desktops/Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Citrix-Virtual-Apps-and-Desktops/Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Installer.md>) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Securiser](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Citrix-Virtual-Apps-and-Desktops/Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Securiser.md>) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Valider](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Citrix-Virtual-Apps-and-Desktops/Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Valider.md>) | | | | |

#### DHCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows Server 2022 Installation DHCP et Eten](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/DHCP/Fiche_Simple_-_VM_Windows_Server_2022_Installation_DHCP_et_Eten.md>) | | | | |

#### Differences 2016 2019

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Differences 2016 2019 Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Differences-2016-2019/Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_Retour_Arriere.md>) | | | | |

#### Exchange Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Exchange Server DAG Sauvegarde](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2022_Exchange_Server_DAG_Sauvegarde.md>) | | | | |
| P0 | [Windows Server 2022 Exchange Server Mise A Jour CU](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Mise_A_Jour_CU.md>) | | | | |
| P1 | [Windows Server 2022 Exchange Server Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Installer.md>) | | | | |
| P1 | [Windows Server 2022 Exchange Server Securiser Certificats](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Securiser_Certificats.md>) | | | | |
| P1 | [Windows Server 2022 Exchange Server Valider Recette](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Valider_Recette.md>) | | | | |

#### Hyper V

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Hyper V Durcissement Retour](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Durcissement_Retour.md>) | | | | |
| P1 | [VM Windows Server 2022 Hyper V Installer Role](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Installer_Role.md>) | | | | |

#### IIS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 IIS Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/IIS/Fiche_Simple_-_VM_Windows_Server_2022_IIS_Retour_Arriere.md>) | | | | |
| P0 | [VM Windows Server 2022 IIS Securite Sauvegarde Maintenance](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/IIS/Fiche_Simple_-_VM_Windows_Server_2022_IIS_Securite_Sauvegarde_Maintenance.md>) | | | | |
| P1 | [VM Windows Server 2022 IIS Installer Role Web Server](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/IIS/Fiche_Simple_-_VM_Windows_Server_2022_IIS_Installer_Role_Web_Server.md>) | | | | |

#### MECM SCCM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 MECM Mise a jour Retour arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/MECM-SCCM/Fiche_Simple_-_Windows_Server_2022_MECM_Mise_a_jour_Retour_arriere.md>) | | | | |
| P0 | [Windows Server 2022 MECM Sauvegarde Restauration](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/MECM-SCCM/Fiche_Simple_-_Windows_Server_2022_MECM_Sauvegarde_Restauration.md>) | | | | |
| P1 | [Windows Server 2022 MECM Installation](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/MECM-SCCM/Fiche_Simple_-_Windows_Server_2022_MECM_Installation.md>) | | | | |
| P1 | [Windows Server 2022 MECM Securisation](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/MECM-SCCM/Fiche_Simple_-_Windows_Server_2022_MECM_Securisation.md>) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Nakivo Job Sauvegarde](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Job_Sauvegarde.md>) | | | | |
| P0 | [Windows Server 2022 Nakivo Mettre A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Mettre_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Server 2022 Nakivo Restaurer Interface](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Restaurer_Interface.md>) | | | | |
| P1 | [Windows Server 2022 Nakivo Installer Director Transporter](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Installer_Director_Transporter.md>) | | | | |
| P1 | [Windows Server 2022 Nakivo Securiser](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Securiser.md>) | | | | |

#### PRTG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows Server 2022 PRTG Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/PRTG/Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Installer.md>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 PowerShell Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/PowerShell/Fiche_Simple_-_Windows_Server_2022_PowerShell_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Server 2022 PowerShell Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/PowerShell/Fiche_Simple_-_Windows_Server_2022_PowerShell_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Server 2022 PowerShell Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/PowerShell/Fiche_Simple_-_Windows_Server_2022_PowerShell_Installer.md>) | | | | |
| P1 | [Windows Server 2022 PowerShell Securiser Signature](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/PowerShell/Fiche_Simple_-_Windows_Server_2022_PowerShell_Securiser_Signature.md>) | | | | |
| P1 | [Windows Server 2022 PowerShell Valider](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/PowerShell/Fiche_Simple_-_Windows_Server_2022_PowerShell_Valider.md>) | | | | |

#### Remote Desktop Services

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 RDS Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2022_RDS_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Server 2022 RDS Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2022_RDS_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Server 2022 RDS Installer Configurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2022_RDS_Installer_Configurer.md>) | | | | |
| P1 | [Windows Server 2022 RDS Securiser Acces](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2022_RDS_Securiser_Acces.md>) | | | | |
| P1 | [Windows Server 2022 RDS Valider Recette](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2022_RDS_Valider_Recette.md>) | | | | |

#### Robocopy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Robocopy Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Robocopy/Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Retour_Arriere.md>) | | | | |
| P0 | [VM Windows Server 2022 Robocopy Valider Restaurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Robocopy/Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Valider_Restaurer.md>) | | | | |

#### SQL Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 SQL-Server Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/SQL-Server/Fiche_Simple_-_Windows_Server_2022_SQL-Server_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Server 2022 SQL-Server Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/SQL-Server/Fiche_Simple_-_Windows_Server_2022_SQL-Server_Installer.md>) | | | | |
| P1 | [Windows Server 2022 SQL-Server Securiser](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/SQL-Server/Fiche_Simple_-_Windows_Server_2022_SQL-Server_Securiser.md>) | | | | |
| P1 | [Windows Server 2022 SQL-Server Valider](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/SQL-Server/Fiche_Simple_-_Windows_Server_2022_SQL-Server_Valider.md>) | | | | |

#### StarWind Virtual SAN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 StarWind Virtual SAN Mettre A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/StarWind-Virtual-SAN/Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Mettre_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Server 2022 StarWind Virtual SAN Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/StarWind-Virtual-SAN/Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/StarWind-Virtual-SAN/Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Installer.md>) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Securiser](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/StarWind-Virtual-SAN/Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Securiser.md>) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Valider](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/StarWind-Virtual-SAN/Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Valider.md>) | | | | |

#### VMware Horizon

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 VMware Horizon Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/VMware-Horizon/Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Server 2022 VMware Horizon Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/VMware-Horizon/Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/VMware-Horizon/Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Installer.md>) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Securiser](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/VMware-Horizon/Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Securiser.md>) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Valider](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/VMware-Horizon/Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Valider.md>) | | | | |

#### Veeam

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Veeam Ajouter Depot Sauvegarde](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Veeam/Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Ajouter_Depot_Sauvegarde.md>) | | | | |
| P1 | [VM Windows Server 2022 Veeam Installer Serveur Sauvegarde](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Veeam/Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Installer_Serveur_Sauvegarde.md>) | | | | |

#### WDS MDT

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 WDS MDT Maintenance Retour arriere](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Maintenance_Retour_arriere.md>) | | | | |
| P0 | [Windows Server 2022 WDS MDT Sauvegarde Restauration](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Sauvegarde_Restauration.md>) | | | | |
| P1 | [Windows Server 2022 WDS MDT Installer](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Installer.md>) | | | | |
| P1 | [Windows Server 2022 WDS MDT Securisation](<../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/WDS-MDT/Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Securisation.md>) | | | | |

### Windows/Server-2025

#### Exchange Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2025 Exchange Server DAG Sauvegarde](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2025_Exchange_Server_DAG_Sauvegarde.md>) | | | | |
| P0 | [Windows Server 2025 Exchange Server Mise A Jour CU](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Mise_A_Jour_CU.md>) | | | | |
| P1 | [Windows Server 2025 Exchange Server Installer](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Installer.md>) | | | | |
| P1 | [Windows Server 2025 Exchange Server Securiser Certificats](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Securiser_Certificats.md>) | | | | |
| P1 | [Windows Server 2025 Exchange Server Valider Recette](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Exchange-Server/Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Valider_Recette.md>) | | | | |

#### Remote Desktop Services

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2025 RDS Mise A Jour Retour Arriere](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2025_RDS_Mise_A_Jour_Retour_Arriere.md>) | | | | |
| P0 | [Windows Server 2025 RDS Sauvegarder Restaurer](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2025_RDS_Sauvegarder_Restaurer.md>) | | | | |
| P1 | [Windows Server 2025 RDS Installer Configurer](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2025_RDS_Installer_Configurer.md>) | | | | |
| P1 | [Windows Server 2025 RDS Securiser TLS Comptes Pare-feu](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2025_RDS_Securiser_TLS_Comptes_Pare-feu.md>) | | | | |
| P1 | [Windows Server 2025 RDS Valider Recette](<../01-Fiches-Simples/Windows/Server-2025/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2025_RDS_Valider_Recette.md>) | | | | |

### Windows/Toutes-versions

#### Lansweeper

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server Lansweeper Sauvegarde Maintenance](<../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Sauvegarde_Maintenance.md>) | | | | |
| P1 | [VM Windows Server Lansweeper Installer Serveur](<../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Installer_Serveur.md>) | | | | |

## 7. Critères de sortie

- 100 % des fiches P0 d'un OS en `OK` ou `OK avec écarts` (corrigés) avant de déclarer cet OS utilisable en production.
- 100 % des fiches Sauvegarde et Restauration d'un logiciel en `OK` avant sa mise en production.
- Aucune fiche `KO` ouverte sur le périmètre déployé.
- Chaque écart corrigé est rejoué depuis un snapshot propre.
- Après les corrections, relancer `verify_wiki.py` puis régénérer les exports Wiki.js.

_Volumétrie : 391 lignes P0 et 513 lignes P1._
