# Liste de contrôle stricte — tests des fiches simples avant usage en production

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
| P0 | [VM Alpine 3.19 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Alpine 3.19 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Alpine 3.19 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Debian/12

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Debian 12 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Debian 12 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Debian/13

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Debian 13 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Debian 13 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-48-test-de-restauration-pra>) | | | | |

### OPNsense/Toutes-versions

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM OPNsense Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM OPNsense Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM OPNsense Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM OPNsense Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM OPNsense Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM OPNsense Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM OPNsense Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM OPNsense Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM OPNsense Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM OPNsense Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM OPNsense Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM OPNsense Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM OPNsense Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM OPNsense Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM OPNsense Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Proxmox/VE-8

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Proxmox VE 8 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Rocky-Linux/9

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky Linux 9 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-48-test-de-restauration-pra>) | | | | |

### TrueNAS/CORE-13.0

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-48-test-de-restauration-pra>) | | | | |

### TrueNAS/SCALE-25.10

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Ubuntu/24.04

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Ubuntu 24.04 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Ubuntu 24.04 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Ubuntu/26.04

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26.04 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Ubuntu 26.04 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Ubuntu 26.04 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-48-test-de-restauration-pra>) | | | | |

### VMware/ESXi-8

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM ESXi 8 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Windows/Client-10

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 10 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 19 Configuration Des Sources Logicielles](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-19-configuration-des-sources-logicielles>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 26 Authentification Forte Et Windows](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-26-authentification-forte-et-windows>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 30 Protection Contre Les Tentatives](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-30-protection-contre-les-tentatives>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Windows 10 Vie Systeme 39 Chiffrement Des Flux Et](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-39-chiffrement-des-flux-et>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Windows 10 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Windows/Client-11

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 19 Configuration Des Sources Logicielles](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-19-configuration-des-sources-logicielles>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 26 Authentification Forte Et Windows](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-26-authentification-forte-et-windows>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 30 Protection Contre Les Tentatives](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-30-protection-contre-les-tentatives>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Windows 11 Vie Systeme 39 Chiffrement Des Flux Et](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-39-chiffrement-des-flux-et>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Windows 11 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Windows/Server-2022

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 19 Configuration Des Sources De](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-19-configuration-des-sources-de>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 26 Authentification Forte Et Acces](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-26-authentification-forte-et-acces>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-48-test-de-restauration-pra>) | | | | |

### Windows/Server-2025

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2025 Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 19 Configuration Des Sources De](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-19-configuration-des-sources-de>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 26 Authentification Forte Et Acces](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-26-authentification-forte-et-acces>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-48-test-de-restauration-pra>) | | | | |

### pfSense/Toutes-versions

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM pfSense Vie Systeme 13 Partitionnement Et Systemes De](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-13-partitionnement-et-systemes-de>) | | | | |
| P0 | [VM pfSense Vie Systeme 16 Adressage Ip Fixe Definitif](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-16-adressage-ip-fixe-definitif>) | | | | |
| P1 | [VM pfSense Vie Systeme 19 Configuration Des Depots Logiciels](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-19-configuration-des-depots-logiciels>) | | | | |
| P1 | [VM pfSense Vie Systeme 20 Mise A Jour Initiale](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-20-mise-a-jour-initiale>) | | | | |
| P1 | [VM pfSense Vie Systeme 22 Synchronisation Horaire Ntp](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-22-synchronisation-horaire-ntp>) | | | | |
| P0 | [VM pfSense Vie Systeme 26 Authentification Par Cles Ssh](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-26-authentification-par-cles-ssh>) | | | | |
| P0 | [VM pfSense Vie Systeme 27 Durcissement De L Acces](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-27-durcissement-de-l-acces>) | | | | |
| P1 | [VM pfSense Vie Systeme 28 Gestion Fine Des Privileges](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-28-gestion-fine-des-privileges>) | | | | |
| P0 | [VM pfSense Vie Systeme 29 Pare Feu Hote](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-29-pare-feu-hote>) | | | | |
| P1 | [VM pfSense Vie Systeme 30 Protection Contre Le Brute](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-30-protection-contre-le-brute>) | | | | |
| P1 | [VM pfSense Vie Systeme 32 Automatisation Des Correctifs De](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-32-automatisation-des-correctifs-de>) | | | | |
| P1 | [VM pfSense Vie Systeme 39 Chiffrement Des Flux Pki](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-39-chiffrement-des-flux-pki>) | | | | |
| P0 | [VM pfSense Vie Systeme 40 Configuration Des Sauvegardes](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-40-configuration-des-sauvegardes>) | | | | |
| P0 | [VM pfSense Vie Systeme 46 Test De Persistance Au](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-46-test-de-persistance-au>) | | | | |
| P0 | [VM pfSense Vie Systeme 48 Test De Restauration Pra](</01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-48-test-de-restauration-pra>) | | | | |

## 6. P0 par logiciel (installation, sauvegarde, restauration, mise à jour)

Pour chaque logiciel : tester d'abord **Sauvegarde**, puis **Restauration** sur une machine vierge, puis **Mise à jour / retour arrière**. Une restauration jamais testée équivaut à une absence de sauvegarde.

### Alpine/3.19

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3.19 Securite Certbot TLS](</01-fiches-simples/alpine/3-19/vie-du-logiciel/certbot/fiche-simple-lxc-alpine-3-19-securite-certbot-tls>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3.19 Securite Fail2ban](</01-fiches-simples/alpine/3-19/vie-du-logiciel/fail2ban/fiche-simple-lxc-alpine-3-19-securite-fail2ban>) | | | | |

#### OpenSSH

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](</01-fiches-simples/alpine/3-19/vie-du-logiciel/openssh/fiche-simple-lxc-alpine-3-19-securite-openssh-cle-et-openrc>) | | | | |

### Debian/12

#### Ansible

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Installation Ansible](</01-fiches-simples/debian/12/vie-du-logiciel/ansible/fiche-simple-vm-debian-12-installation-ansible>) | | | | |

#### Bacula

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Bacula Prouver Restauration](</01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-prouver-restauration>) | | | | |
| P0 | [VM Debian 12 Bacula Valider Restauration](</01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-valider-restauration>) | | | | |
| P1 | [VM Debian 12 Bacula Valider Config Demarrer](</01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-valider-config-demarrer>) | | | | |

#### BorgBackup

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Borg Depanner Retour Arriere](</01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-depanner-retour-arriere>) | | | | |
| P0 | [VM Debian 12 Borg Restaurer Isoler](</01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-restaurer-isoler>) | | | | |
| P0 | [VM Debian 12 Sauvegarde Configuration BorgBackup](</01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-sauvegarde-configuration-borgbackup>) | | | | |
| P1 | [VM Debian 12 Borg Installer Initialiser](</01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-installer-initialiser>) | | | | |
| P1 | [VM Debian 12 Borg Securiser Verifier](</01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-securiser-verifier>) | | | | |

#### Cacti

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Cacti Installer Cacti](</01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-installer-cacti>) | | | | |
| P1 | [VM Debian 12 Cacti Installer Dependances](</01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-installer-dependances>) | | | | |
| P1 | [VM Debian 12 Cacti Securiser Exploiter](</01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-securiser-exploiter>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Securite Certbot SSL Nginx](</01-fiches-simples/debian/12/vie-du-logiciel/certbot/fiche-simple-vm-debian-12-securite-certbot-ssl-nginx>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Securite Configuration Fail2ban SSH](</01-fiches-simples/debian/12/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-12-securite-configuration-fail2ban-ssh>) | | | | |

#### FreePBX Asterisk

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 FreePBX Sauvegarder Maintenir](</01-fiches-simples/debian/12/vie-du-logiciel/freepbx-asterisk/fiche-simple-vm-debian-12-freepbx-sauvegarder-maintenir>) | | | | |
| P1 | [VM Debian 12 FreePBX Installer Methode Supportee](</01-fiches-simples/debian/12/vie-du-logiciel/freepbx-asterisk/fiche-simple-vm-debian-12-freepbx-installer-methode-supportee>) | | | | |

#### GLPI

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 GLPI Maintenir Restaurer](</01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-maintenir-restaurer>) | | | | |
| P1 | [LXC Debian 12 Installation GLPI Agent](</01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-lxc-debian-12-installation-glpi-agent>) | | | | |
| P1 | [VM Debian 12 GLPI Installer Application](</01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-installer-application>) | | | | |
| P1 | [VM Debian 12 GLPI Installer Recetter](</01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-installer-recetter>) | | | | |
| P1 | [VM Debian 12 Services Installation GLPI Serveur](</01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-services-installation-glpi-serveur>) | | | | |

#### Nginx

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 ReverseProxy Installation Nginx Pro](</01-fiches-simples/debian/12/vie-du-logiciel/nginx/fiche-simple-vm-debian-12-reverseproxy-installation-nginx-pro>) | | | | |

#### QEMU

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Systeme Installation Qemu Guest Age](</01-fiches-simples/debian/12/vie-du-logiciel/qemu/fiche-simple-vm-debian-12-systeme-installation-qemu-guest-age>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Sauvegarde Restic Depot](</01-fiches-simples/debian/12/vie-du-logiciel/restic/fiche-simple-vm-debian-12-sauvegarde-restic-depot>) | | | | |

#### Splunk

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Splunk Installer Sans Root](</01-fiches-simples/debian/12/vie-du-logiciel/splunk/fiche-simple-vm-debian-12-splunk-installer-sans-root>) | | | | |
| P1 | [VM Debian 12 Splunk Securiser Premier Acces](</01-fiches-simples/debian/12/vie-du-logiciel/splunk/fiche-simple-vm-debian-12-splunk-securiser-premier-acces>) | | | | |

#### Wazuh

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Wazuh Sauvegarder Mettre A Jour](</01-fiches-simples/debian/12/vie-du-logiciel/wazuh/fiche-simple-vm-debian-12-wazuh-sauvegarder-mettre-a-jour>) | | | | |
| P1 | [VM Debian 12 Wazuh Installer Architecture](</01-fiches-simples/debian/12/vie-du-logiciel/wazuh/fiche-simple-vm-debian-12-wazuh-installer-architecture>) | | | | |

#### Zabbix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Zabbix Sauvegarder Mettre A Jour](</01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-sauvegarder-mettre-a-jour>) | | | | |
| P1 | [VM Debian 12 Supervision Installation Zabbix Age](</01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-supervision-installation-zabbix-age>) | | | | |
| P1 | [VM Debian 12 Supervision Installation Zabbix Ser](</01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-supervision-installation-zabbix-ser>) | | | | |
| P1 | [VM Debian 12 Zabbix Installer Configurer](</01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-installer-configurer>) | | | | |
| P1 | [VM Debian 12 Zabbix Valider Installation](</01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-valider-installation>) | | | | |

#### iTop

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 iTop Verifier Sauvegarder MAJ](</01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-verifier-sauvegarder-maj>) | | | | |
| P1 | [VM Debian 12 iTop Installer Apache PHP MariaDB](</01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-installer-apache-php-mariadb>) | | | | |
| P1 | [VM Debian 12 iTop Installer Paquet Officiel](</01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-installer-paquet-officiel>) | | | | |

### Debian/13

#### Ansible

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Ansible Production Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-production-retour-arriere>) | | | | |
| P1 | [VM Debian 13 Ansible Installer Core](</01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-installer-core>) | | | | |
| P1 | [VM Debian 13 Ansible Valider Connexion](</01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-valider-connexion>) | | | | |
| P1 | [VM Debian 13 Ansible Valider Playbook](</01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-valider-playbook>) | | | | |

#### Apache

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Apache Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Apache Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Apache Exploiter Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-exploiter-securiser>) | | | | |
| P1 | [VM Debian 13 Apache Installer Paquet](</01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-installer-paquet>) | | | | |
| P1 | [VM Debian 13 Apache Valider](</01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-valider>) | | | | |

#### BIND9

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 BIND9 Autoritatif Sauvegarde Retour](</01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-sauvegarde-retour>) | | | | |
| P1 | [VM Debian 13 BIND9 Autoritatif Installer](</01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-installer>) | | | | |
| P1 | [VM Debian 13 BIND9 Autoritatif Valider](</01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-valider>) | | | | |
| P1 | [VM Debian 13 Services Installation DNS BIND9](</01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-services-installation-dns-bind9>) | | | | |

#### Bareos

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Bareos Valider Restauration](</01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-valider-restauration>) | | | | |
| P1 | [VM Debian 13 Bareos Installer Paquets](</01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-installer-paquets>) | | | | |

#### Bash Shell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Bash Shell Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Bash Shell Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Bash Shell Installer](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-installer>) | | | | |
| P1 | [VM Debian 13 Bash Shell Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-securiser>) | | | | |
| P1 | [VM Debian 13 Bash Shell Valider](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-valider>) | | | | |

#### BlueMind

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 BlueMind Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 BlueMind Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 BlueMind Installer](</01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-installer>) | | | | |
| P1 | [VM Debian 13 BlueMind Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-securiser>) | | | | |
| P1 | [VM Debian 13 BlueMind Valider](</01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-valider>) | | | | |

#### Caddy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Caddy Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-retour-arriere>) | | | | |
| P1 | [VM Debian 13 Caddy Installer](</01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-installer>) | | | | |
| P1 | [VM Debian 13 Caddy Valider Service](</01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-valider-service>) | | | | |

#### Centreon

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Centreon Installer Central](</01-fiches-simples/debian/13/vie-du-logiciel/centreon/fiche-simple-vm-debian-13-centreon-installer-central>) | | | | |
| P1 | [VM Debian 13 Centreon Securiser Exploiter](</01-fiches-simples/debian/13/vie-du-logiciel/centreon/fiche-simple-vm-debian-13-centreon-securiser-exploiter>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Securite Certbot TLS](</01-fiches-simples/debian/13/vie-du-logiciel/certbot/fiche-simple-vm-debian-13-securite-certbot-tls>) | | | | |

#### DHCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Kea Installer](</01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-installer>) | | | | |
| P1 | [VM Debian 13 Kea Valider Demarrer](</01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-valider-demarrer>) | | | | |
| P1 | [VM Debian 13 Services Installation DHCP KEA](</01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-services-installation-dhcp-kea>) | | | | |

#### Docker

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Installation Docker Engine](</01-fiches-simples/debian/13/vie-du-logiciel/docker/fiche-simple-vm-debian-13-installation-docker-engine>) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Dovecot Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Dovecot Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Dovecot Installer](</01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-installer>) | | | | |
| P1 | [VM Debian 13 Dovecot Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-securiser>) | | | | |
| P1 | [VM Debian 13 Dovecot Valider](</01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-valider>) | | | | |

#### Elastic Stack

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Elastic Stack Installer Elasticsearch](</01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-installer-elasticsearch>) | | | | |
| P1 | [VM Debian 13 Elastic Stack Installer Kibana](</01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-installer-kibana>) | | | | |

#### FOG Project

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 FOG Project Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 FOG Project Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 FOG Project Installer](</01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-installer>) | | | | |
| P1 | [VM Debian 13 FOG Project Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-securiser>) | | | | |
| P1 | [VM Debian 13 FOG Project Valider](</01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-valider>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Securite Fail2ban](</01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban>) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 FreeIPA Client Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 FreeIPA Client Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Installer](</01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-installer>) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-securiser>) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Valider](</01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-valider>) | | | | |

#### GNS3

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 GNS3 Deploiement Sauvegarde MAJ](</01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-sauvegarde-maj>) | | | | |
| P1 | [VM Debian 13 GNS3 Deploiement Installer GUI Serveur](</01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-installer-gui-serveur>) | | | | |
| P1 | [VM Debian 13 GNS3 Valider Lab Isole](</01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-valider-lab-isole>) | | | | |

#### Git

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Git Installer](</01-fiches-simples/debian/13/vie-du-logiciel/git/fiche-simple-vm-debian-13-git-installer>) | | | | |

#### GitLab

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 GitLab CE Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 GitLab CE Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 GitLab CE Installer](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-installer>) | | | | |
| P1 | [VM Debian 13 GitLab CE Securiser TLS](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-securiser-tls>) | | | | |
| P1 | [VM Debian 13 GitLab CE Valider Recette](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-valider-recette>) | | | | |

#### Gitea

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Gitea Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Gitea Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Gitea Installer](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-installer>) | | | | |
| P1 | [VM Debian 13 Gitea Securiser TLS](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-securiser-tls>) | | | | |
| P1 | [VM Debian 13 Gitea Valider Recette](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-valider-recette>) | | | | |

#### HAProxy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 HAProxy Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 HAProxy Installer](</01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-installer>) | | | | |
| P1 | [VM Debian 13 HAProxy Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-securiser>) | | | | |
| P1 | [VM Debian 13 HAProxy Valider](</01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-valider>) | | | | |

#### HashiCorp Vault

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Debian 13 Hashicorp Vault Valider Politique](</01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-debian-13-hashicorp-vault-valider-politique>) | | | | |
| P1 | [VM Debian 13 Vault Installer](</01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-installer>) | | | | |

#### ISC DHCP Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 ISC-DHCP-Server Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 ISC-DHCP-Server Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Installer](</01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-installer>) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-securiser>) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Valider](</01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-valider>) | | | | |

#### InfluxDB3 Core

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [InfluxDB3 Core Debian 13 Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-retour-arriere>) | | | | |
| P0 | [InfluxDB3 Core Debian 13 Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-sauvegarder-restaurer>) | | | | |
| P1 | [InfluxDB3 Core Debian 13 Installer Depot](</01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-installer-depot>) | | | | |
| P1 | [InfluxDB3 Core Debian 13 Valider Ecriture](</01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-valider-ecriture>) | | | | |

#### KeePassXC

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 KeePassXC Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-sauvegarder-restaurer>) | | | | |
| P0 | [VM Debian 13 KeePassXC Verifier Mise A Jour](</01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-verifier-mise-a-jour>) | | | | |
| P1 | [VM Debian 13 KeePassXC Valider Coffre](</01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-valider-coffre>) | | | | |

#### Kubernetes K3s

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Kubeadm Sauvegarde Mise A Jour](</01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-sauvegarde-mise-a-jour>) | | | | |
| P0 | [VM Debian 13 Kubeadm Sauvegarder Preparer](</01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-sauvegarder-preparer>) | | | | |
| P1 | [VM Debian 13 K3s Installer Noeud Lab](</01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-installer-noeud-lab>) | | | | |
| P1 | [VM Debian 13 K3s Securiser Surveiller](</01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-securiser-surveiller>) | | | | |
| P1 | [VM Debian 13 Kubeadm Installer Paquets](</01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-installer-paquets>) | | | | |
| P1 | [VM Debian 13 Kubeadm Installer Runtime](</01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-installer-runtime>) | | | | |
| P1 | [VM Debian 13 Kubeadm Valider Cluster](</01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-valider-cluster>) | | | | |

#### LEMP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 LEMP Sauvegarder Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/lemp/fiche-simple-vm-debian-13-lemp-sauvegarder-retour-arriere>) | | | | |

#### MariaDB

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MariaDB Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Database Installation MariaDB 11](</01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-database-installation-mariadb-11>) | | | | |
| P1 | [VM Debian 13 LEMP Securiser MariaDB](</01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-lemp-securiser-mariadb>) | | | | |
| P1 | [VM Debian 13 MariaDB Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-securiser>) | | | | |
| P1 | [VM Debian 13 MariaDB Valider](</01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-valider>) | | | | |

#### Minikube

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Minikube Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Minikube Sauvegarde Prealable](</01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-sauvegarde-prealable>) | | | | |
| P1 | [VM Debian 13 Minikube Installer](</01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-installer>) | | | | |
| P1 | [VM Debian 13 Minikube Valider](</01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-valider>) | | | | |

#### MongoDB

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MongoDB Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 MongoDB Installer](</01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-installer>) | | | | |
| P1 | [VM Debian 13 MongoDB Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser>) | | | | |
| P1 | [VM Debian 13 MongoDB Valider](</01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-valider>) | | | | |

#### MySQL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MySQL Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 MySQL Installer](</01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-installer>) | | | | |
| P1 | [VM Debian 13 MySQL Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-securiser>) | | | | |
| P1 | [VM Debian 13 MySQL Valider](</01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-valider>) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Debian 13 Nakivo Transporter Mettre A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-mettre-a-jour-retour-arriere>) | | | | |
| P0 | [Debian 13 Nakivo Transporter Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-sauvegarder-restaurer>) | | | | |
| P1 | [Debian 13 Nakivo Transporter Installer](</01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-installer>) | | | | |
| P1 | [Debian 13 Nakivo Transporter Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-securiser>) | | | | |
| P1 | [Debian 13 Nakivo Transporter Valider Mettre A Jour](</01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-valider-mettre-a-jour>) | | | | |

#### NetBox

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 NetBox Sauvegarder Mettre A Jour](</01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-sauvegarder-mettre-a-jour>) | | | | |
| P1 | [VM Debian 13 NetBox Installer Release](</01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-installer-release>) | | | | |
| P1 | [VM Debian 13 NetBox Valider IPAM](</01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-valider-ipam>) | | | | |
| P1 | [VM Debian 13 NetBox Valider IPAM Pilote](</01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-valider-ipam-pilote>) | | | | |

#### Nextcloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Nextcloud Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Nextcloud Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Nextcloud Installer](</01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-installer>) | | | | |
| P1 | [VM Debian 13 Nextcloud Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-securiser>) | | | | |
| P1 | [VM Debian 13 Nextcloud Valider](</01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-valider>) | | | | |

#### Nginx

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Nginx Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Nginx Installer](</01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-installer>) | | | | |
| P1 | [VM Debian 13 Nginx Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-securiser>) | | | | |
| P1 | [VM Debian 13 Nginx Valider](</01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-valider>) | | | | |
| P1 | [VM Debian 13 Web Installation Nginx PHP8.4 FPM](</01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-web-installation-nginx-php8-4-fpm>) | | | | |

#### OCS Inventory

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OCS Inventory Sauvegarde](</01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-sauvegarde>) | | | | |
| P1 | [VM Debian 13 Installer Agent OCS Inventory](</01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-installer-agent-ocs-inventory>) | | | | |
| P1 | [VM Debian 13 OCS Inventory Installer Paquets](</01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-installer-paquets>) | | | | |

#### Observium

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Observium Sauvegarde Securite](</01-fiches-simples/debian/13/vie-du-logiciel/observium/fiche-simple-vm-debian-13-observium-sauvegarde-securite>) | | | | |

#### OpenLDAP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenLDAP Restaurer Test](</01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-restaurer-test>) | | | | |
| P0 | [VM Debian 13 OpenLDAP Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-retour-arriere>) | | | | |
| P0 | [VM Debian 13 OpenLDAP Sauvegarder](</01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-sauvegarder>) | | | | |
| P1 | [VM Debian 13 OpenLDAP Installer](</01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-installer>) | | | | |
| P1 | [VM Debian 13 OpenLDAP Valider](</01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-valider>) | | | | |

#### OpenMediaVault

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 OpenMediaVault Installer OMV](</01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-installer-omv>) | | | | |
| P1 | [VM Debian 13 Stockage Installation OpenMediaVault 8](</01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-stockage-installation-openmediavault-8>) | | | | |

#### OpenTofu

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenTofu Mise A Jour Rollback](</01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-mise-a-jour-rollback>) | | | | |
| P1 | [VM Debian 13 OpenTofu Installer](</01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-installer>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenVPN Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 OpenVPN Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 OpenVPN Installer](</01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-installer>) | | | | |
| P1 | [VM Debian 13 OpenVPN Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-securiser>) | | | | |
| P1 | [VM Debian 13 OpenVPN Valider](</01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-valider>) | | | | |

#### Packer

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Packer Debian 13 Nettoyer Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-nettoyer-retour-arriere>) | | | | |
| P1 | [Packer Debian 13 Installer](</01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-installer>) | | | | |
| P1 | [Packer Debian 13 Valider Template](</01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-valider-template>) | | | | |

#### Passbolt

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Passbolt Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Passbolt Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Passbolt Installer](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-installer>) | | | | |
| P1 | [VM Debian 13 Passbolt Securiser TLS](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-securiser-tls>) | | | | |
| P1 | [VM Debian 13 Passbolt Valider Recette](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-valider-recette>) | | | | |

#### Podman Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Podman Buildah Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Podman Buildah Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Podman Buildah Installer](</01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-installer>) | | | | |
| P1 | [VM Debian 13 Podman Buildah Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-securiser>) | | | | |
| P1 | [VM Debian 13 Podman Buildah Valider](</01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-valider>) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Postfix Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Postfix Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Postfix Installer](</01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-installer>) | | | | |
| P1 | [VM Debian 13 Postfix Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-securiser>) | | | | |
| P1 | [VM Debian 13 Postfix Valider](</01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-valider>) | | | | |

#### PostgreSQL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PostgreSQL Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Database Installation PostgreSQL 17](</01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-database-installation-postgresql-17>) | | | | |
| P1 | [VM Debian 13 NetBox Installer PostgreSQL Redis](</01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-netbox-installer-postgresql-redis>) | | | | |
| P1 | [VM Debian 13 PostgreSQL Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-securiser>) | | | | |
| P1 | [VM Debian 13 PostgreSQL Valider](</01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-valider>) | | | | |

#### Postman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Postman Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-mise-a-jour-retour-arriere>) | | | | |
| P1 | [VM Debian 13 Postman Installer](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-installer>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PowerShell Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 PowerShell Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 PowerShell Installer](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-installer>) | | | | |
| P1 | [VM Debian 13 PowerShell Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-securiser>) | | | | |
| P1 | [VM Debian 13 PowerShell Valider](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-valider>) | | | | |

#### Prometheus Grafana

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Prometheus Grafana Sauvegarder](</01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-sauvegarder>) | | | | |
| P1 | [VM Debian 13 Prometheus Grafana Installer Grafana](</01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-installer-grafana>) | | | | |
| P1 | [VM Debian 13 Prometheus Grafana Installer Prometheus](</01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-installer-prometheus>) | | | | |

#### PuTTY

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PuTTY Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 PuTTY Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 PuTTY Installer](</01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-installer>) | | | | |
| P1 | [VM Debian 13 PuTTY Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-securiser>) | | | | |
| P1 | [VM Debian 13 PuTTY Valider](</01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-valider>) | | | | |

#### Python

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Python Installer Outils](</01-fiches-simples/debian/13/vie-du-logiciel/python/fiche-simple-vm-debian-13-python-installer-outils>) | | | | |
| P1 | [VM Debian 13 Python Valider Venv Pipx](</01-fiches-simples/debian/13/vie-du-logiciel/python/fiche-simple-vm-debian-13-python-valider-venv-pipx>) | | | | |

#### QGIS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 QGIS Maj Sauvegarde](</01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-maj-sauvegarde>) | | | | |
| P1 | [VM Debian 13 QGIS Installer QGIS](</01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-installer-qgis>) | | | | |
| P1 | [VM Debian 13 QGIS Valider Chaine](</01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-valider-chaine>) | | | | |
| P1 | [VM Debian 13 QGIS Valider Projet](</01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-valider-projet>) | | | | |

#### Redis

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Redis Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Redis Installer](</01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-installer>) | | | | |
| P1 | [VM Debian 13 Redis Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-securiser>) | | | | |
| P1 | [VM Debian 13 Redis Valider](</01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-valider>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Sauvegarde Restic Depot](</01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot>) | | | | |

#### Samba AD DC

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Samba AD DC Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Samba AD DC Sauvegarde](</01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-sauvegarde>) | | | | |
| P1 | [VM Debian 13 Samba AD DC Reseau Securite](</01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-reseau-securite>) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Snort Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Snort Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Snort Installer](</01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-installer>) | | | | |
| P1 | [VM Debian 13 Snort Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-securiser>) | | | | |
| P1 | [VM Debian 13 Snort Valider](</01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-valider>) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Suricata IDS Installer](</01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-installer>) | | | | |
| P1 | [VM Debian 13 Suricata Valider Capteur IDS](</01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-valider-capteur-ids>) | | | | |

#### Terraform

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Terraform Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 Terraform Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Terraform Installer](</01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-installer>) | | | | |
| P1 | [VM Debian 13 Terraform Securiser Etat](</01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-securiser-etat>) | | | | |
| P1 | [VM Debian 13 Terraform Valider Recette](</01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-valider-recette>) | | | | |

#### Traefik

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Traefik Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 Traefik Installer](</01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-installer>) | | | | |
| P1 | [VM Debian 13 Traefik Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-securiser>) | | | | |
| P1 | [VM Debian 13 Traefik Valider](</01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-valider>) | | | | |

#### VS Code

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 VSCode Mise a jour](</01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-mise-a-jour>) | | | | |
| P1 | [VM Debian 13 VSCode Installer](</01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-installer>) | | | | |
| P1 | [VM Debian 13 VSCode Valider Installation](</01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-valider-installation>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 WireGuard Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 WireGuard Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 WireGuard Installer](</01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-installer>) | | | | |
| P1 | [VM Debian 13 WireGuard Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-securiser>) | | | | |
| P1 | [VM Debian 13 WireGuard Valider](</01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-valider>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Wireshark Analyse Installer](</01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer>) | | | | |
| P1 | [VM Debian 13 Wireshark Valider Capture Locale](</01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-valider-capture-locale>) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Zeek Depot Installer](</01-fiches-simples/debian/13/vie-du-logiciel/zeek/fiche-simple-vm-debian-13-zeek-depot-installer>) | | | | |
| P1 | [VM Debian 13 Zeek Valider Capteur](</01-fiches-simples/debian/13/vie-du-logiciel/zeek/fiche-simple-vm-debian-13-zeek-valider-capteur>) | | | | |
| P1 | [VM Debian 13 Zeek Valider Logs](</01-fiches-simples/debian/13/vie-du-logiciel/zeek/fiche-simple-vm-debian-13-zeek-valider-logs>) | | | | |

#### cURL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 cURL Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 cURL Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 cURL Installer](</01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-installer>) | | | | |
| P1 | [VM Debian 13 cURL Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-securiser>) | | | | |
| P1 | [VM Debian 13 cURL Valider](</01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-valider>) | | | | |

#### draw.io

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 draw io Installer](</01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-installer>) | | | | |
| P1 | [VM Debian 13 draw io Valider Diagramme](</01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-valider-diagramme>) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 ownCloud Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 ownCloud Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 ownCloud Installer](</01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-installer>) | | | | |
| P1 | [VM Debian 13 ownCloud Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-securiser>) | | | | |
| P1 | [VM Debian 13 ownCloud Valider](</01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-valider>) | | | | |

#### phpIPAM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 phpIPAM Sauvegarder](</01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-sauvegarder>) | | | | |
| P1 | [VM Debian 13 phpIPAM Valider IPAM](</01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-valider-ipam>) | | | | |

#### rsync

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 rsync Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-retour-arriere>) | | | | |
| P0 | [VM Debian 13 rsync Valider Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-valider-restaurer>) | | | | |
| P1 | [VM Debian 13 rsync Installer Preparer](</01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-installer-preparer>) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 tcpdump Mise A Jour Retour Arriere](</01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Debian 13 tcpdump Sauvegarder Restaurer](</01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-sauvegarder-restaurer>) | | | | |
| P1 | [VM Debian 13 tcpdump Installer](</01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-installer>) | | | | |
| P1 | [VM Debian 13 tcpdump Securiser](</01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-securiser>) | | | | |
| P1 | [VM Debian 13 tcpdump Valider](</01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-valider>) | | | | |

### OPNsense/Toutes-versions

#### CARP pfsync HA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Appliance OPNsense CARP pfsync Exploitation Retour Arriere](</01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/carp-pfsync-ha/fiche-simple-appliance-opnsense-carp-pfsync-exploitation-retour-arriere>) | | | | |

### Proxmox/Toutes-versions

#### Cluster Stockage VM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Proxmox VE Diagnostic Restaurer](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-restaurer>) | | | | |

#### Proxmox Backup Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Proxmox Backup Server Tester Restauration](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-tester-restauration>) | | | | |
| P1 | [Hote Proxmox Backup Server Installer Datastore](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-installer-datastore>) | | | | |

### Proxmox/VE-8

#### Cluster Corosync

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Proxmox VE 8 Cluster Securiser](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-securiser>) | | | | |
| P1 | [Hote Proxmox VE 8 Cluster Valider](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-valider>) | | | | |

#### Proxmox OpenStack

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Mise A Jour Retour Arriere](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-nettoyer-retour-arriere>) | | | | |
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-sauvegarder-restaurer-lab>) | | | | |
| P1 | [VM Proxmox VE 8 Proxmox OpenStack Securiser Valider Lab](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-securiser-valider-lab>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenStack DevStack Installer Lab](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/openstack/ubuntu-24-04-lts/fiche-simple-vm-ubuntu-24-04-openstack-devstack-installer-lab>) | | | | |

### Rocky-Linux/9

#### Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Buildah Publier Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-publier-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 Buildah Sauvegarder Etat Initial](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-sauvegarder-etat-initial>) | | | | |
| P1 | [VM Rocky 9 Buildah Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-installer>) | | | | |
| P1 | [VM Rocky 9 Buildah Valider Image](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-valider-image>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Rocky 9 Securite Certbot TLS](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/certbot/fiche-simple-vm-rocky-9-securite-certbot-tls>) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Dovecot Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 Dovecot Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 Dovecot Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-installer>) | | | | |
| P1 | [VM Rocky 9 Dovecot Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-securiser>) | | | | |
| P1 | [VM Rocky 9 Dovecot Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-valider>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Rocky 9 Securite Fail2ban](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/fail2ban/fiche-simple-vm-rocky-9-securite-fail2ban>) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 FreeIPA Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-restaurer>) | | | | |
| P0 | [VM Rocky 9 FreeIPA Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 FreeIPA Sauvegarder](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-sauvegarder>) | | | | |
| P1 | [VM Rocky 9 FreeIPA Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-installer>) | | | | |
| P1 | [VM Rocky 9 FreeIPA Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-valider>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 OpenVPN Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 OpenVPN Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 OpenVPN Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-installer>) | | | | |
| P1 | [VM Rocky 9 OpenVPN Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-securiser>) | | | | |
| P1 | [VM Rocky 9 OpenVPN Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-valider>) | | | | |

#### Pile Web

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Pile Web Sauvegarder Retour](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/pile-web/fiche-simple-vm-rocky-9-pile-web-sauvegarder-retour>) | | | | |
| P1 | [VM Rocky 9 Pile Web Installer Paquets](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/pile-web/fiche-simple-vm-rocky-9-pile-web-installer-paquets>) | | | | |
| P1 | [VM Rocky 9 Pile Web Securiser MariaDB](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/pile-web/fiche-simple-vm-rocky-9-pile-web-securiser-mariadb>) | | | | |

#### Podman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Podman Quadlet Mise A Jour Reprise](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-mise-a-jour-reprise>) | | | | |
| P1 | [VM Rocky 9 Podman Quadlet Valider Image](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-valider-image>) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Postfix Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 Postfix Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 Postfix Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-installer>) | | | | |
| P1 | [VM Rocky 9 Postfix Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-securiser>) | | | | |
| P1 | [VM Rocky 9 Postfix Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-valider>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 PowerShell Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 PowerShell Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 PowerShell Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-installer>) | | | | |
| P1 | [VM Rocky 9 PowerShell Securiser Signature](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-securiser-signature>) | | | | |
| P1 | [VM Rocky 9 PowerShell Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-valider>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Sauvegarde Restic Depot](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/restic/fiche-simple-vm-rocky-9-sauvegarde-restic-depot>) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Snort Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 Snort Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 Snort Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-installer>) | | | | |
| P1 | [VM Rocky 9 Snort Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-securiser>) | | | | |
| P1 | [VM Rocky 9 Snort Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-valider>) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Suricata Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 Suricata Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 Suricata Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-installer>) | | | | |
| P1 | [VM Rocky 9 Suricata Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-securiser>) | | | | |
| P1 | [VM Rocky 9 Suricata Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-valider>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 WireGuard Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 WireGuard Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 WireGuard Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-installer>) | | | | |
| P1 | [VM Rocky 9 WireGuard Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-securiser>) | | | | |
| P1 | [VM Rocky 9 WireGuard Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-valider>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Wireshark Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 Wireshark Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 Wireshark Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-installer>) | | | | |
| P1 | [VM Rocky 9 Wireshark Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-securiser>) | | | | |
| P1 | [VM Rocky 9 Wireshark Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-valider>) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Zeek Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 Zeek Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 Zeek Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-installer>) | | | | |
| P1 | [VM Rocky 9 Zeek Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-securiser>) | | | | |
| P1 | [VM Rocky 9 Zeek Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-valider>) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 ownCloud Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 ownCloud Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 ownCloud Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-installer>) | | | | |
| P1 | [VM Rocky 9 ownCloud Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-securiser>) | | | | |
| P1 | [VM Rocky 9 ownCloud Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-valider>) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 tcpdump Mise A Jour Retour Arriere](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Rocky 9 tcpdump Sauvegarder Restaurer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-sauvegarder-restaurer>) | | | | |
| P1 | [VM Rocky 9 tcpdump Installer](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-installer>) | | | | |
| P1 | [VM Rocky 9 tcpdump Securiser](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-securiser>) | | | | |
| P1 | [VM Rocky 9 tcpdump Valider](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-valider>) | | | | |

### Transverses/Cloud-SaaS

#### AWS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud AWS Nettoyage Retour Arriere](</01-fiches-simples/transverses/cloud-saas/aws/fiche-simple-cloud-aws-nettoyage-retour-arriere>) | | | | |
| P0 | [Cloud AWS Sauvegardes Snapshots](</01-fiches-simples/transverses/cloud-saas/aws/fiche-simple-cloud-aws-sauvegardes-snapshots>) | | | | |

#### Azure

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Azure Nettoyage Retour Arriere](</01-fiches-simples/transverses/cloud-saas/azure/fiche-simple-cloud-azure-nettoyage-retour-arriere>) | | | | |
| P0 | [Cloud Azure Sauvegardes Snapshots](</01-fiches-simples/transverses/cloud-saas/azure/fiche-simple-cloud-azure-sauvegardes-snapshots>) | | | | |

#### Datadog

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Datadog Retour Arriere](</01-fiches-simples/transverses/cloud-saas/datadog/fiche-simple-cloud-datadog-retour-arriere>) | | | | |
| P1 | [Cloud Datadog Installer Agent Linux Pilote](</01-fiches-simples/transverses/cloud-saas/datadog/fiche-simple-cloud-datadog-installer-agent-linux-pilote>) | | | | |
| P1 | [Cloud Datadog Securite Maintenance](</01-fiches-simples/transverses/cloud-saas/datadog/fiche-simple-cloud-datadog-securite-maintenance>) | | | | |

#### Dynatrace

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Dynatrace OneAgent Securite MaJ Retour](</01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-securite-maj-retour>) | | | | |
| P1 | [Cloud Dynatrace OneAgent Generer Installateur](</01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-generer-installateur>) | | | | |
| P1 | [Cloud Dynatrace OneAgent Installer Pilote](</01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-installer-pilote>) | | | | |
| P1 | [Cloud Dynatrace OneAgent Installer Pilote Linux](</01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-installer-pilote-linux>) | | | | |

#### Entra ID

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Entra ID Connect Retour Arriere](</01-fiches-simples/transverses/cloud-saas/entra-id/fiche-simple-cloud-entra-id-connect-retour-arriere>) | | | | |

#### Exchange Online

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Cloud Exchange Online Valider Recette](</01-fiches-simples/transverses/cloud-saas/exchange-online/fiche-simple-cloud-exchange-online-valider-recette>) | | | | |

#### GCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud GCP Nettoyage Retour Arriere](</01-fiches-simples/transverses/cloud-saas/gcp/fiche-simple-cloud-gcp-nettoyage-retour-arriere>) | | | | |
| P0 | [Cloud GCP Sauvegardes Snapshots](</01-fiches-simples/transverses/cloud-saas/gcp/fiche-simple-cloud-gcp-sauvegardes-snapshots>) | | | | |

#### Google Workspace

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Cloud Google Workspace Valider Recette](</01-fiches-simples/transverses/cloud-saas/google-workspace/fiche-simple-cloud-google-workspace-valider-recette>) | | | | |

### Transverses/Docker

#### Bitwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Bitwarden Self Hosted Deploiement Sauvegardes Mises A Jour Reprise](</01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-sauvegardes-mises-a-jour-reprise>) | | | | |
| P0 | [Bitwarden Self Hosted Verifier Backup Restauration](</01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-verifier-backup-restauration>) | | | | |
| P1 | [Bitwarden Self Hosted Deploiement Telecharger Installer](</01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-telecharger-installer>) | | | | |

#### Guacamole

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Docker Guacamole Mise A Jour Retour Arriere](</01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Hote Docker Guacamole Sauvegarde Restauration](</01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-sauvegarde-restauration>) | | | | |
| P1 | [Hote Docker Guacamole Valider Controle Acces](</01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-valider-controle-acces>) | | | | |

#### Installation systeme

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Docker Installation Engine et Compose](</01-fiches-simples/transverses/docker/installation-systeme/fiche-simple-hote-docker-installation-engine-et-compose>) | | | | |

#### Nextcloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Nextcloud29 Migration Retour Arriere](</01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-retour-arriere>) | | | | |
| P0 | [Docker Nextcloud29 Migration Sauvegarder Tester Restauration](</01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-sauvegarder-tester-restauration>) | | | | |

#### Sauvegarde restauration

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Sauvegarder Restaurer Volume](</01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-docker-sauvegarder-restaurer-volume>) | | | | |
| P0 | [Docker Sauvegarder Stack Compose Base Donnees](</01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-docker-sauvegarder-stack-compose-base-donnees>) | | | | |
| P0 | [Hote Docker Stack Restaurer](</01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-hote-docker-stack-restaurer>) | | | | |
| P0 | [Hote Docker Stack Verifier Sauvegarde](</01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-hote-docker-stack-verifier-sauvegarde>) | | | | |

#### Securite

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Docker Securite Activer Mode Rootless](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-activer-mode-rootless>) | | | | |
| P1 | [Hote Docker Securite Hardening Images Mises A Jour](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-images-mises-a-jour>) | | | | |
| P1 | [Hote Docker Securite Hardening Inventaire Plan Controle](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-inventaire-plan-controle>) | | | | |
| P1 | [Hote Docker Securite Hardening Reduire Privileges](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-reduire-privileges>) | | | | |
| P1 | [Hote Docker Securite Hardening Reponse Incident](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-reponse-incident>) | | | | |
| P1 | [Hote Docker Securite Hardening Ressources Journaux](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-ressources-journaux>) | | | | |
| P1 | [Hote Docker Securite Hardening Segmentation Donnees](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-segmentation-donnees>) | | | | |
| P1 | [Hote Docker Securite Hardening Verifier Exploiter](</01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-verifier-exploiter>) | | | | |

#### Snipe IT

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Snipe-IT Mise A Jour Retour](</01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-mise-a-jour-retour>) | | | | |
| P0 | [Docker Snipe-IT Sauvegarde Restauration](</01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-sauvegarde-restauration>) | | | | |
| P1 | [Docker Snipe-IT Valider Demarrer](</01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-valider-demarrer>) | | | | |

#### Traefik

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Conteneur Traefik Mise A Jour Retour](</01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-mise-a-jour-retour>) | | | | |

#### Validation

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Production Mise A Jour Rollback Compose](</01-fiches-simples/transverses/docker/validation/fiche-simple-docker-production-mise-a-jour-rollback-compose>) | | | | |
| P0 | [Docker Production Reconstruire Hote Restaurer Stacks](</01-fiches-simples/transverses/docker/validation/fiche-simple-docker-production-reconstruire-hote-restaurer-stacks>) | | | | |

#### Vaultwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Docker Vaultwarden Restaurer](</01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-restaurer>) | | | | |
| P0 | [Hote Docker Vaultwarden Retour Arriere](</01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-retour-arriere>) | | | | |
| P0 | [Hote Docker Vaultwarden Sauvegarder](</01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-sauvegarder>) | | | | |
| P1 | [Hote Docker Vaultwarden Validation](</01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-validation>) | | | | |

#### WikiJS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker WikiJS Mise A Jour Retour Arriere](</01-fiches-simples/transverses/docker/wikijs/fiche-simple-docker-wikijs-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Docker WikiJS Sauvegarder Restaurer](</01-fiches-simples/transverses/docker/wikijs/fiche-simple-docker-wikijs-sauvegarder-restaurer>) | | | | |
| P1 | [Docker WikiJS Valider Demarrer](</01-fiches-simples/transverses/docker/wikijs/fiche-simple-docker-wikijs-valider-demarrer>) | | | | |

### Transverses/Multi-OS

#### Diagnostic Reseau

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Multi-OS Reseau Diagnostic Validation Retour Arriere](</01-fiches-simples/transverses/multi-os/diagnostic-reseau/fiche-simple-vm-multi-os-reseau-diagnostic-validation-retour-arriere>) | | | | |
| P1 | [VM Multi-OS Reseau Diagnostic Securiser Diagnostic](</01-fiches-simples/transverses/multi-os/diagnostic-reseau/fiche-simple-vm-multi-os-reseau-diagnostic-securiser-diagnostic>) | | | | |

#### Keepalived HAProxy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Linux Keepalived HAProxy Securite Retour Arriere](</01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-securite-retour-arriere>) | | | | |
| P1 | [VM Linux Keepalived HAProxy Installer Valider HAProxy](</01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy>) | | | | |

### Ubuntu/24.04

#### BlueMind

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 BlueMind Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 BlueMind Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 BlueMind Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 BlueMind Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 BlueMind Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-valider>) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 24.04 Securite Certbot TLS](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/certbot/fiche-simple-vm-ubuntu-24-04-securite-certbot-tls>) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Dovecot Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 Dovecot Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 Dovecot Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 Dovecot Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 Dovecot Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-valider>) | | | | |

#### EVE NG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 EVE-NG Mettre A Jour Retour](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-mettre-a-jour-retour>) | | | | |
| P0 | [VM Ubuntu 24.04 EVE-NG Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 EVE-NG Creer Valider Lab](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-creer-valider-lab>) | | | | |
| P1 | [VM Ubuntu 24.04 EVE-NG Installer ISO VM](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-installer-iso-vm>) | | | | |
| P1 | [VM Ubuntu 24.04 EVE-NG Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-securiser>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 24.04 Securite Fail2ban](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/fail2ban/fiche-simple-vm-ubuntu-24-04-securite-fail2ban>) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 FreeIPA Client Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 FreeIPA Client Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 FreeIPA Client Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 FreeIPA Client Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 FreeIPA Client Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-valider>) | | | | |

#### Graylog

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Graylog Verifier Exploiter Sauvegarder](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-verifier-exploiter-sauvegarder>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Installer Data Node](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-data-node>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Installer MongoDB](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-mongodb>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Installer Server](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-server>) | | | | |
| P1 | [VM Ubuntu 24.04 Graylog Valider Input Syslog Pilote](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-valider-input-syslog-pilote>) | | | | |

#### LEMP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 LEMP Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 LEMP Valider Sauvegarder Exploiter](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-valider-sauvegarder-exploiter>) | | | | |
| P1 | [VM Ubuntu 24.04 LEMP Installer Pile](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-installer-pile>) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Ubuntu 24.04 Nakivo Transporter Mettre A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-mettre-a-jour-retour-arriere>) | | | | |
| P0 | [Ubuntu 24.04 Nakivo Transporter Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-sauvegarder-restaurer>) | | | | |
| P1 | [Ubuntu 24.04 Nakivo Transporter Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-installer>) | | | | |
| P1 | [Ubuntu 24.04 Nakivo Transporter Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-securiser>) | | | | |
| P1 | [Ubuntu 24.04 Nakivo Transporter Valider Mettre A Jour](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-valider-mettre-a-jour>) | | | | |

#### OpenLDAP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 OpenLDAP Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 OpenLDAP Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenLDAP Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenLDAP Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenLDAP Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-valider>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 OpenVPN Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 OpenVPN Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenVPN Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenVPN Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 OpenVPN Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-valider>) | | | | |

#### Packet Tracer

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Packet Tracer Sauvegarder Maintenir](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-sauvegarder-maintenir>) | | | | |
| P1 | [VM Ubuntu 24.04 Packet Tracer Installer Paquet](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-installer-paquet>) | | | | |
| P1 | [VM Ubuntu 24.04 Packet Tracer Valider Simulation](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-valider-simulation>) | | | | |

#### Podman Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Podman Buildah Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 Podman Buildah Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 Podman Buildah Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 Podman Buildah Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 Podman Buildah Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-valider>) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Postfix Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 Postfix Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 Postfix Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 Postfix Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 Postfix Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-valider>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 PowerShell Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 PowerShell Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 PowerShell Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 PowerShell Securiser Signature](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-securiser-signature>) | | | | |
| P1 | [VM Ubuntu 24.04 PowerShell Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-valider>) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Snort Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 Snort Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 Snort Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 Snort Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 Snort Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-valider>) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Suricata Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 Suricata Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 Suricata Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 Suricata Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 Suricata Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-valider>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 WireGuard Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 WireGuard Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 WireGuard Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 WireGuard Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 WireGuard Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-valider>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Wireshark Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 Wireshark Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 Wireshark Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 Wireshark Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 Wireshark Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-valider>) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 Zeek Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 Zeek Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 Zeek Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 Zeek Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 Zeek Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-valider>) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 ownCloud Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 ownCloud Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 ownCloud Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 ownCloud Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 ownCloud Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-valider>) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24.04 tcpdump Mise A Jour Retour Arriere](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Ubuntu 24.04 tcpdump Sauvegarder Restaurer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-sauvegarder-restaurer>) | | | | |
| P1 | [VM Ubuntu 24.04 tcpdump Installer](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-installer>) | | | | |
| P1 | [VM Ubuntu 24.04 tcpdump Securiser](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-securiser>) | | | | |
| P1 | [VM Ubuntu 24.04 tcpdump Valider](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-valider>) | | | | |

### Ubuntu/26.04

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 26.04 Securite Certbot TLS](</01-fiches-simples/ubuntu/26-04/vie-du-logiciel/certbot/fiche-simple-vm-ubuntu-26-04-securite-certbot-tls>) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 26.04 Securite Fail2ban](</01-fiches-simples/ubuntu/26-04/vie-du-logiciel/fail2ban/fiche-simple-vm-ubuntu-26-04-securite-fail2ban>) | | | | |

#### LibreNMS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26.04 LibreNMS Sauvegarde Mises A Jour](</01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-sauvegarde-mises-a-jour>) | | | | |
| P1 | [VM Ubuntu 26.04 LibreNMS Installer Paquets](</01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-installer-paquets>) | | | | |

#### Pile Web

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26.04 Pile Web Validation Sauvegarde Retour](</01-fiches-simples/ubuntu/26-04/vie-du-logiciel/pile-web/fiche-simple-vm-ubuntu-26-04-pile-web-validation-sauvegarde-retour>) | | | | |
| P1 | [VM Ubuntu 26.04 Pile Web Installer Nginx PHP PostgreSQL](</01-fiches-simples/ubuntu/26-04/vie-du-logiciel/pile-web/fiche-simple-vm-ubuntu-26-04-pile-web-installer-nginx-php-postgresql>) | | | | |

### Ubuntu/Toutes-versions

#### Ceph

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu Ceph Sauvegarde Upgrade Retrait](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-sauvegarde-upgrade-retrait>) | | | | |
| P1 | [VM Ubuntu Ceph Installer Cephadm Bootstrap](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-installer-cephadm-bootstrap>) | | | | |
| P1 | [VM Ubuntu Ceph Limites Validation](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-limites-validation>) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu Restic Effectuer Sauvegarde](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-effectuer-sauvegarde>) | | | | |
| P0 | [VM Ubuntu Restic Restaurer Sans Ecraser](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-restaurer-sans-ecraser>) | | | | |
| P1 | [VM Ubuntu Restic Installer Proteger Secret](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-installer-proteger-secret>) | | | | |

### VMware/ESXi-8

#### vSphere

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM ESXi 8 VMware vSphere VCSA Sauvegarde Restauration VAMI](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-sauvegarde-restauration-vami>) | | | | |
| P1 | [VM ESXi 8 VMware vSphere VCSA Installer](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-installer>) | | | | |

### Windows/Client-11

#### Bitwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Bitwarden Mise A Jour Retour Arriere](</01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Windows 11 Bitwarden Sauvegarder Restaurer](</01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-sauvegarder-restaurer>) | | | | |
| P1 | [VM Windows 11 Bitwarden Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-installer>) | | | | |
| P1 | [VM Windows 11 Bitwarden Securiser](</01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-securiser>) | | | | |
| P1 | [VM Windows 11 Bitwarden Valider](</01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-valider>) | | | | |

#### Microsoft Visio

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Visio Mise A Jour Retour Arriere](</01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Windows 11 Visio Sauvegarder Restaurer](</01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-sauvegarder-restaurer>) | | | | |
| P1 | [VM Windows 11 Visio Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-installer>) | | | | |
| P1 | [VM Windows 11 Visio Securiser](</01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-securiser>) | | | | |
| P1 | [VM Windows 11 Visio Valider](</01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-valider>) | | | | |

#### MobaXterm

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 MobaXterm Mise A Jour Rollback](</01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-mise-a-jour-rollback>) | | | | |
| P0 | [VM Windows 11 MobaXterm Sauvegarde Restauration](</01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-sauvegarde-restauration>) | | | | |
| P1 | [VM Windows 11 MobaXterm Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-installer>) | | | | |
| P1 | [VM Windows 11 MobaXterm Securisation](</01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-securisation>) | | | | |
| P1 | [VM Windows 11 MobaXterm Validation](</01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-validation>) | | | | |

#### OpenSSH

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows 11 Administration Installer OpenSSH Cle](</01-fiches-simples/windows/client-11/vie-du-logiciel/openssh/fiche-simple-vm-windows-11-administration-installer-openssh-cle>) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Client 11 OpenVPN Mise A Jour Retour Arriere](</01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Client 11 OpenVPN Sauvegarder Restaurer](</01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Client 11 OpenVPN Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-installer>) | | | | |
| P1 | [Windows Client 11 OpenVPN Securiser](</01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-securiser>) | | | | |
| P1 | [Windows Client 11 OpenVPN Valider](</01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-valider>) | | | | |

#### Postman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Postman Mise A Jour Retour Arriere](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-mise-a-jour-retour-arriere>) | | | | |
| P1 | [VM Windows 11 Postman Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-installer>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 PowerShell7 Mise A Jour Validation](</01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-mise-a-jour-validation>) | | | | |
| P1 | [VM Windows 11 PowerShell7 Installer Version Stable](</01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-installer-version-stable>) | | | | |
| P1 | [VM Windows 11 PowerShell Valider Shell Admin](</01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell-valider-shell-admin>) | | | | |

#### PuTTY

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 PuTTY Mise A Jour Reception](</01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-mise-a-jour-reception>) | | | | |
| P1 | [VM Windows 11 PuTTY Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-installer>) | | | | |
| P1 | [VM Windows 11 PuTTY Valider SSH HostKey](</01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-valider-ssh-hostkey>) | | | | |

#### Royal TS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Royal TS Mise A Jour](</01-fiches-simples/windows/client-11/vie-du-logiciel/royal-ts/fiche-simple-vm-windows-11-royal-ts-mise-a-jour>) | | | | |
| P0 | [VM Windows 11 Royal TS Sauvegarde Config](</01-fiches-simples/windows/client-11/vie-du-logiciel/royal-ts/fiche-simple-vm-windows-11-royal-ts-sauvegarde-config>) | | | | |
| P1 | [VM Windows 11 Royal TS Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/royal-ts/fiche-simple-vm-windows-11-royal-ts-installer>) | | | | |

#### Sysinternals

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Sysinternals Retour Arriere Limites](</01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-retour-arriere-limites>) | | | | |
| P1 | [VM Windows 11 Sysinternals Collecte Validation](</01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-collecte-validation>) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Client 11 WireGuard Mise A Jour Retour Arriere](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Client 11 WireGuard Sauvegarder Restaurer](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Client 11 WireGuard Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-installer>) | | | | |
| P1 | [Windows Client 11 WireGuard Securiser](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-securiser>) | | | | |
| P1 | [Windows Client 11 WireGuard Valider](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-valider>) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Wireshark Mise A Jour Retour Arriere](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-mise-a-jour-retour-arriere>) | | | | |
| P0 | [VM Windows 11 Wireshark Sauvegarder Restaurer](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-sauvegarder-restaurer>) | | | | |
| P1 | [VM Windows 11 Wireshark Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-installer>) | | | | |
| P1 | [VM Windows 11 Wireshark Securiser Droits Captures](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-securiser-droits-captures>) | | | | |
| P1 | [VM Windows 11 Wireshark Valider Recette](</01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-valider-recette>) | | | | |

#### mRemoteNG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 mRemoteNG Mise A Jour Rollback](</01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-mise-a-jour-rollback>) | | | | |
| P0 | [VM Windows 11 mRemoteNG Sauvegarde Restauration](</01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-sauvegarde-restauration>) | | | | |
| P1 | [VM Windows 11 mRemoteNG Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-installer>) | | | | |
| P1 | [VM Windows 11 mRemoteNG Securisation](</01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-securisation>) | | | | |
| P1 | [VM Windows 11 mRemoteNG Validation](</01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-validation>) | | | | |

### Windows/Server-2022

#### Active Directory

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 ADDS DNS DHCP Sauvegarde Securite Retour](</01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-adds-dns-dhcp-sauvegarde-securite-retour>) | | | | |
| P0 | [VM Windows Server 2022 Reprise Foret AD DS Preparer Sauvegardes](</01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-preparer-sauvegardes>) | | | | |
| P0 | [VM Windows Server 2022 Reprise Foret AD DS Restaurer Premiers DC](</01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-restaurer-premiers-dc>) | | | | |
| P1 | [VM Windows Server 2022 ADDS DNS DHCP Valider ADDS DNS](</01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-adds-dns-dhcp-valider-adds-dns>) | | | | |
| P1 | [VM Windows Server 2022 Reprise Foret AD DS Risques Identite Securite](</01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-risques-identite-securite>) | | | | |
| P1 | [VM Windows Server 2022 Reprise Foret AD DS Valider Avant Production](</01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-valider-avant-production>) | | | | |

#### Citrix Virtual Apps and Desktops

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Citrix CVAD Mise A Jour Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 Citrix CVAD Sauvegarder Restaurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-installer>) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Securiser](</01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-securiser>) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Valider](</01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-valider>) | | | | |

#### DHCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows Server 2022 Installation DHCP et Eten](</01-fiches-simples/windows/server-2022/vie-du-logiciel/dhcp/fiche-simple-vm-windows-server-2022-installation-dhcp-et-eten>) | | | | |

#### Differences 2016 2019

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Differences 2016 2019 Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/differences-2016-2019/fiche-simple-windows-server-2022-differences-2016-2019-retour-arriere>) | | | | |

#### Exchange Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Exchange Server DAG Sauvegarde](</01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-dag-sauvegarde>) | | | | |
| P0 | [Windows Server 2022 Exchange Server Mise A Jour CU](</01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-mise-a-jour-cu>) | | | | |
| P1 | [Windows Server 2022 Exchange Server Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-installer>) | | | | |
| P1 | [Windows Server 2022 Exchange Server Securiser Certificats](</01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-securiser-certificats>) | | | | |
| P1 | [Windows Server 2022 Exchange Server Valider Recette](</01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-valider-recette>) | | | | |

#### Hyper V

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Hyper V Durcissement Retour](</01-fiches-simples/windows/server-2022/vie-du-logiciel/hyper-v/fiche-simple-vm-windows-server-2022-hyper-v-durcissement-retour>) | | | | |
| P1 | [VM Windows Server 2022 Hyper V Installer Role](</01-fiches-simples/windows/server-2022/vie-du-logiciel/hyper-v/fiche-simple-vm-windows-server-2022-hyper-v-installer-role>) | | | | |

#### IIS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 IIS Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-retour-arriere>) | | | | |
| P0 | [VM Windows Server 2022 IIS Securite Sauvegarde Maintenance](</01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-securite-sauvegarde-maintenance>) | | | | |
| P1 | [VM Windows Server 2022 IIS Installer Role Web Server](</01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-installer-role-web-server>) | | | | |

#### MECM SCCM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 MECM Mise a jour Retour arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 MECM Sauvegarde Restauration](</01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-sauvegarde-restauration>) | | | | |
| P1 | [Windows Server 2022 MECM Installation](</01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-installation>) | | | | |
| P1 | [Windows Server 2022 MECM Securisation](</01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-securisation>) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Nakivo Job Sauvegarde](</01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-job-sauvegarde>) | | | | |
| P0 | [Windows Server 2022 Nakivo Mettre A Jour Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-mettre-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 Nakivo Restaurer Interface](</01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-restaurer-interface>) | | | | |
| P1 | [Windows Server 2022 Nakivo Installer Director Transporter](</01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-installer-director-transporter>) | | | | |
| P1 | [Windows Server 2022 Nakivo Securiser](</01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-securiser>) | | | | |

#### PRTG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows Server 2022 PRTG Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-installer>) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 PowerShell Mise A Jour Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 PowerShell Sauvegarder Restaurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Server 2022 PowerShell Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-installer>) | | | | |
| P1 | [Windows Server 2022 PowerShell Securiser Signature](</01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-securiser-signature>) | | | | |
| P1 | [Windows Server 2022 PowerShell Valider](</01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-valider>) | | | | |

#### Remote Desktop Services

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 RDS Mise A Jour Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 RDS Sauvegarder Restaurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Server 2022 RDS Installer Configurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-installer-configurer>) | | | | |
| P1 | [Windows Server 2022 RDS Securiser Acces](</01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-securiser-acces>) | | | | |
| P1 | [Windows Server 2022 RDS Valider Recette](</01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-valider-recette>) | | | | |

#### Robocopy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Robocopy Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-retour-arriere>) | | | | |
| P0 | [VM Windows Server 2022 Robocopy Valider Restaurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-valider-restaurer>) | | | | |

#### SQL Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 SQL-Server Sauvegarder Restaurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Server 2022 SQL-Server Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-installer>) | | | | |
| P1 | [Windows Server 2022 SQL-Server Securiser](</01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-securiser>) | | | | |
| P1 | [Windows Server 2022 SQL-Server Valider](</01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-valider>) | | | | |

#### StarWind Virtual SAN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 StarWind Virtual SAN Mettre A Jour Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-mettre-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 StarWind Virtual SAN Sauvegarder Restaurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-installer>) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Securiser](</01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-securiser>) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Valider](</01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-valider>) | | | | |

#### VMware Horizon

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 VMware Horizon Mise A Jour Retour Arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 VMware Horizon Sauvegarder Restaurer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-installer>) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Securiser](</01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-securiser>) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Valider](</01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-valider>) | | | | |

#### Veeam

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Veeam Ajouter Depot Sauvegarde](</01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-ajouter-depot-sauvegarde>) | | | | |
| P1 | [VM Windows Server 2022 Veeam Installer Serveur Sauvegarde](</01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-installer-serveur-sauvegarde>) | | | | |

#### WDS MDT

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 WDS MDT Maintenance Retour arriere](</01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-maintenance-retour-arriere>) | | | | |
| P0 | [Windows Server 2022 WDS MDT Sauvegarde Restauration](</01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-sauvegarde-restauration>) | | | | |
| P1 | [Windows Server 2022 WDS MDT Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-installer>) | | | | |
| P1 | [Windows Server 2022 WDS MDT Securisation](</01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-securisation>) | | | | |

### Windows/Server-2025

#### Exchange Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2025 Exchange Server DAG Sauvegarde](</01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-dag-sauvegarde>) | | | | |
| P0 | [Windows Server 2025 Exchange Server Mise A Jour CU](</01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-mise-a-jour-cu>) | | | | |
| P1 | [Windows Server 2025 Exchange Server Installer](</01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-installer>) | | | | |
| P1 | [Windows Server 2025 Exchange Server Securiser Certificats](</01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-securiser-certificats>) | | | | |
| P1 | [Windows Server 2025 Exchange Server Valider Recette](</01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-valider-recette>) | | | | |

#### Remote Desktop Services

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2025 RDS Mise A Jour Retour Arriere](</01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-mise-a-jour-retour-arriere>) | | | | |
| P0 | [Windows Server 2025 RDS Sauvegarder Restaurer](</01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-sauvegarder-restaurer>) | | | | |
| P1 | [Windows Server 2025 RDS Installer Configurer](</01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-installer-configurer>) | | | | |
| P1 | [Windows Server 2025 RDS Securiser TLS Comptes Pare-feu](</01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-securiser-tls-comptes-pare-feu>) | | | | |
| P1 | [Windows Server 2025 RDS Valider Recette](</01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-valider-recette>) | | | | |

### Windows/Toutes-versions

#### Lansweeper

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server Lansweeper Sauvegarde Maintenance](</01-fiches-simples/windows/toutes-versions/vie-du-logiciel/lansweeper/fiche-simple-vm-windows-server-lansweeper-sauvegarde-maintenance>) | | | | |
| P1 | [VM Windows Server Lansweeper Installer Serveur](</01-fiches-simples/windows/toutes-versions/vie-du-logiciel/lansweeper/fiche-simple-vm-windows-server-lansweeper-installer-serveur>) | | | | |

## 7. Critères de sortie

- 100 % des fiches P0 d'un OS en `OK` ou `OK avec écarts` (corrigés) avant de déclarer cet OS utilisable en production.
- 100 % des fiches Sauvegarde et Restauration d'un logiciel en `OK` avant sa mise en production.
- Aucune fiche `KO` ouverte sur le périmètre déployé.
- Chaque écart corrigé est rejoué depuis un snapshot propre.
- Après les corrections, relancer `verify_wiki.py` puis régénérer les exports Wiki.js.

_Volumétrie : 391 lignes P0 et 513 lignes P1._