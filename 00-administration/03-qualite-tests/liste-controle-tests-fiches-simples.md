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
| Ubuntu 26-04 : sudo-rs, client NTP par défaut, trousseau `ubuntu.sources` | noms de paquets à confirmer |
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

### Alpine/3-19

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Alpine 3-19 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Alpine 3-19 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Alpine 3-19 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM Alpine 3-19 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Alpine 3-19 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Alpine 3-19 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM Alpine 3-19 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Alpine 3-19 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Alpine 3-19 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Alpine 3-19 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Alpine 3-19 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Alpine 3-19 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Alpine 3-19 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Alpine 3-19 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Alpine 3-19 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/alpine/3-19/vie-du-systeme/fiche-simple-vm-alpine-3-19-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Debian/12

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-13-partitionnement-et-systemes-de.md) | OK avec écarts | 31/10/2026 | Agent IA | |
| P0 | [VM Debian 12 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-16-adressage-ip-fixe-definitif.md) | OK avec écarts | 31/10/2026 | Agent IA | |
| P1 | [VM Debian 12 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM Debian 12 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Debian 12 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Debian 12 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-26-authentification-par-cles-ssh.md) | OK avec écarts | 31/10/2026 | Agent IA | |
| P0 | [VM Debian 12 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-27-durcissement-de-l-acces.md) | OK | 31/10/2026 | Agent IA | |
| P1 | [VM Debian 12 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Debian 12 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-29-pare-feu-hote.md) | OK avec écarts | 31/10/2026 | Agent IA | |
| P1 | [VM Debian 12 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Debian 12 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Debian 12 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Debian 12 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-40-configuration-des-sauvegardes.md) | OK avec écarts | 31/10/2026 | Agent IA | |
| P0 | [VM Debian 12 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-46-test-de-persistance-au.md) | OK | 31/10/2026 | Agent IA | |
| P0 | [VM Debian 12 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/debian/12/vie-du-systeme/fiche-simple-vm-debian-12-vie-systeme-48-test-de-restauration-pra.md) | OK | 31/10/2026 | Agent IA | |

### Debian/13

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Debian 13 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Debian 13 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM Debian 13 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Debian 13 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Debian 13 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM Debian 13 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Debian 13 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Debian 13 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Debian 13 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Debian 13 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Debian 13 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Debian 13 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Debian 13 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Debian 13 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/debian/13/vie-du-systeme/fiche-simple-vm-debian-13-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### OPNsense/Toutes-versions

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM OPNsense Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM OPNsense Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM OPNsense Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM OPNsense Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM OPNsense Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM OPNsense Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM OPNsense Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM OPNsense Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM OPNsense Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM OPNsense Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM OPNsense Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM OPNsense Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM OPNsense Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM OPNsense Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM OPNsense Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiche-simple-vm-opnsense-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Proxmox/VE-8

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Proxmox VE 8 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Proxmox VE 8 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Proxmox VE 8 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/proxmox/ve-8/vie-du-systeme/fiche-simple-vm-proxmox-ve-8-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Rocky-Linux/9

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky Linux 9 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Rocky Linux 9 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Rocky Linux 9 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiche-simple-vm-rocky-linux-9-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### TrueNAS/core-13-0

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM TrueNAS CORE 13.0 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM TrueNAS CORE 13.0 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiche-simple-vm-truenas-core-13-0-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### TrueNAS/scale-25-10

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM TrueNAS SCALE 25.10 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM TrueNAS SCALE 25.10 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/truenas/scale-25-10/vie-du-systeme/fiche-simple-vm-truenas-scale-25-10-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Ubuntu/24-04

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Ubuntu 24-04 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Ubuntu 24-04 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM Ubuntu 24-04 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Ubuntu 24-04 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Ubuntu 24-04 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM Ubuntu 24-04 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Ubuntu 24-04 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Ubuntu 24-04 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Ubuntu 24-04 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Ubuntu 24-04 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Ubuntu 24-04 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Ubuntu 24-04 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Ubuntu 24-04 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Ubuntu 24-04 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiche-simple-vm-ubuntu-24-04-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Ubuntu/26-04

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26-04 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Ubuntu 26-04 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Ubuntu 26-04 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM Ubuntu 26-04 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Ubuntu 26-04 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Ubuntu 26-04 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM Ubuntu 26-04 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Ubuntu 26-04 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Ubuntu 26-04 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Ubuntu 26-04 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Ubuntu 26-04 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Ubuntu 26-04 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Ubuntu 26-04 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Ubuntu 26-04 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Ubuntu 26-04 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/ubuntu/26-04/vie-du-systeme/fiche-simple-vm-ubuntu-26-04-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### VMware/ESXi-8

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM ESXi 8 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM ESXi 8 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM ESXi 8 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiche-simple-vm-esxi-8-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Windows/Client-10

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 10 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Windows 10 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Windows 10 Vie Systeme 19 Configuration Des Sources Logicielles](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-19-configuration-des-sources-logicielles.md) | | | | |
| P1 | [VM Windows 10 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Windows 10 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Windows 10 Vie Systeme 26 Authentification Forte Et Windows](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-26-authentification-forte-et-windows.md) | | | | |
| P0 | [VM Windows 10 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Windows 10 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Windows 10 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Windows 10 Vie Systeme 30 Protection Contre Les Tentatives](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-30-protection-contre-les-tentatives.md) | | | | |
| P1 | [VM Windows 10 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Windows 10 Vie Systeme 39 Chiffrement Des Flux Et](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-39-chiffrement-des-flux-et.md) | | | | |
| P0 | [VM Windows 10 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Windows 10 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Windows 10 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/windows/client-10/vie-du-systeme/fiche-simple-vm-windows-10-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Windows/Client-11

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Windows 11 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Windows 11 Vie Systeme 19 Configuration Des Sources Logicielles](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-19-configuration-des-sources-logicielles.md) | | | | |
| P1 | [VM Windows 11 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Windows 11 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Windows 11 Vie Systeme 26 Authentification Forte Et Windows](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-26-authentification-forte-et-windows.md) | | | | |
| P0 | [VM Windows 11 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Windows 11 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Windows 11 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Windows 11 Vie Systeme 30 Protection Contre Les Tentatives](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-30-protection-contre-les-tentatives.md) | | | | |
| P1 | [VM Windows 11 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Windows 11 Vie Systeme 39 Chiffrement Des Flux Et](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-39-chiffrement-des-flux-et.md) | | | | |
| P0 | [VM Windows 11 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Windows 11 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Windows 11 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/windows/client-11/vie-du-systeme/fiche-simple-vm-windows-11-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Windows/Server-2022

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 19 Configuration Des Sources De](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-19-configuration-des-sources-de.md) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 26 Authentification Forte Et Acces](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-26-authentification-forte-et-acces.md) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Windows Server 2022 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Windows Server 2022 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiche-simple-vm-windows-server-2022-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### Windows/Server-2025

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2025 Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 19 Configuration Des Sources De](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-19-configuration-des-sources-de.md) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 26 Authentification Forte Et Acces](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-26-authentification-forte-et-acces.md) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM Windows Server 2025 Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM Windows Server 2025 Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/windows/server-2025/vie-du-systeme/fiche-simple-vm-windows-server-2025-vie-systeme-48-test-de-restauration-pra.md) | | | | |

### pfSense/Toutes-versions

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM pfSense Vie Systeme 13 Partitionnement Et Systemes De](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-13-partitionnement-et-systemes-de.md) | | | | |
| P0 | [VM pfSense Vie Systeme 16 Adressage Ip Fixe Definitif](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-16-adressage-ip-fixe-definitif.md) | | | | |
| P1 | [VM pfSense Vie Systeme 19 Configuration Des Depots Logiciels](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-19-configuration-des-depots-logiciels.md) | | | | |
| P1 | [VM pfSense Vie Systeme 20 Mise A Jour Initiale](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-20-mise-a-jour-initiale.md) | | | | |
| P1 | [VM pfSense Vie Systeme 22 Synchronisation Horaire Ntp](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-22-synchronisation-horaire-ntp.md) | | | | |
| P0 | [VM pfSense Vie Systeme 26 Authentification Par Cles Ssh](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-26-authentification-par-cles-ssh.md) | | | | |
| P0 | [VM pfSense Vie Systeme 27 Durcissement De L Acces](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-27-durcissement-de-l-acces.md) | | | | |
| P1 | [VM pfSense Vie Systeme 28 Gestion Fine Des Privileges](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-28-gestion-fine-des-privileges.md) | | | | |
| P0 | [VM pfSense Vie Systeme 29 Pare Feu Hote](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-29-pare-feu-hote.md) | | | | |
| P1 | [VM pfSense Vie Systeme 30 Protection Contre Le Brute](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-30-protection-contre-le-brute.md) | | | | |
| P1 | [VM pfSense Vie Systeme 32 Automatisation Des Correctifs De](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-32-automatisation-des-correctifs-de.md) | | | | |
| P1 | [VM pfSense Vie Systeme 39 Chiffrement Des Flux Pki](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-39-chiffrement-des-flux-pki.md) | | | | |
| P0 | [VM pfSense Vie Systeme 40 Configuration Des Sauvegardes](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-40-configuration-des-sauvegardes.md) | | | | |
| P0 | [VM pfSense Vie Systeme 46 Test De Persistance Au](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-46-test-de-persistance-au.md) | | | | |
| P0 | [VM pfSense Vie Systeme 48 Test De Restauration Pra](../../01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiche-simple-vm-pfsense-vie-systeme-48-test-de-restauration-pra.md) | | | | |

## 6. P0 par logiciel (installation, sauvegarde, restauration, mise à jour)

Pour chaque logiciel : tester d'abord **Sauvegarde**, puis **Restauration** sur une machine vierge, puis **Mise à jour / retour arrière**. Une restauration jamais testée équivaut à une absence de sauvegarde.

### Alpine/3-19

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3-19 Securite Certbot TLS](../../01-fiches-simples/alpine/3-19/vie-du-logiciel/certbot/fiche-simple-lxc-alpine-3-19-securite-certbot-tls.md) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3-19 Securite Fail2ban](../../01-fiches-simples/alpine/3-19/vie-du-logiciel/fail2ban/fiche-simple-lxc-alpine-3-19-securite-fail2ban.md) | | | | |

#### OpenSSH

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [LXC Alpine 3-19 Securite OpenSSH Cle Et OpenRC](../../01-fiches-simples/alpine/3-19/vie-du-logiciel/openssh/fiche-simple-lxc-alpine-3-19-securite-openssh-cle-et-openrc.md) | | | | |

### Debian/12

#### Ansible

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Installation Ansible](../../01-fiches-simples/debian/12/vie-du-logiciel/ansible/fiche-simple-vm-debian-12-installation-ansible.md) | | | | |

#### Bacula

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Bacula Prouver Restauration](../../01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-prouver-restauration.md) | | | | |
| P0 | [VM Debian 12 Bacula Valider Restauration](../../01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-valider-restauration.md) | | | | |
| P1 | [VM Debian 12 Bacula Valider Config Demarrer](../../01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-valider-config-demarrer.md) | | | | |

#### BorgBackup

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Borg Depanner Retour Arriere](../../01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-depanner-retour-arriere.md) | | | | |
| P0 | [VM Debian 12 Borg Restaurer Isoler](../../01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-restaurer-isoler.md) | | | | |
| P0 | [VM Debian 12 Sauvegarde Configuration BorgBackup](../../01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-sauvegarde-configuration-borgbackup.md) | | | | |
| P1 | [VM Debian 12 Borg Installer Initialiser](../../01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-installer-initialiser.md) | | | | |
| P1 | [VM Debian 12 Borg Securiser Verifier](../../01-fiches-simples/debian/12/vie-du-logiciel/borgbackup/fiche-simple-vm-debian-12-borg-securiser-verifier.md) | | | | |

#### Cacti

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Cacti Installer Cacti](../../01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-installer-cacti.md) | | | | |
| P1 | [VM Debian 12 Cacti Installer Dependances](../../01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-installer-dependances.md) | | | | |
| P1 | [VM Debian 12 Cacti Securiser Exploiter](../../01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-securiser-exploiter.md) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Securite Certbot SSL Nginx](../../01-fiches-simples/debian/12/vie-du-logiciel/certbot/fiche-simple-vm-debian-12-securite-certbot-ssl-nginx.md) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Securite Configuration Fail2ban SSH](../../01-fiches-simples/debian/12/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-12-securite-configuration-fail2ban-ssh.md) | | | | |

#### FreePBX Asterisk

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 FreePBX Sauvegarder Maintenir](../../01-fiches-simples/debian/12/vie-du-logiciel/freepbx-asterisk/fiche-simple-vm-debian-12-freepbx-sauvegarder-maintenir.md) | | | | |
| P1 | [VM Debian 12 FreePBX Installer Methode Supportee](../../01-fiches-simples/debian/12/vie-du-logiciel/freepbx-asterisk/fiche-simple-vm-debian-12-freepbx-installer-methode-supportee.md) | | | | |

#### GLPI

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 GLPI Maintenir Restaurer](../../01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-maintenir-restaurer.md) | | | | |
| P1 | [LXC Debian 12 Installation GLPI Agent](../../01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-lxc-debian-12-installation-glpi-agent.md) | | | | |
| P1 | [VM Debian 12 GLPI Installer Application](../../01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-installer-application.md) | | | | |
| P1 | [VM Debian 12 GLPI Installer Recetter](../../01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-installer-recetter.md) | | | | |
| P1 | [VM Debian 12 Services Installation GLPI Serveur](../../01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-services-installation-glpi-serveur.md) | | | | |

#### Nginx

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 ReverseProxy Installation Nginx Pro](../../01-fiches-simples/debian/12/vie-du-logiciel/nginx/fiche-simple-vm-debian-12-reverseproxy-installation-nginx-pro.md) | | | | |

#### QEMU

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Systeme Installation Qemu Guest Age](../../01-fiches-simples/debian/12/vie-du-logiciel/qemu/fiche-simple-vm-debian-12-systeme-installation-qemu-guest-age.md) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Sauvegarde Restic Depot](../../01-fiches-simples/debian/12/vie-du-logiciel/restic/fiche-simple-vm-debian-12-sauvegarde-restic-depot.md) | | | | |

#### Splunk

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 12 Splunk Installer Sans Root](../../01-fiches-simples/debian/12/vie-du-logiciel/splunk/fiche-simple-vm-debian-12-splunk-installer-sans-root.md) | | | | |
| P1 | [VM Debian 12 Splunk Securiser Premier Acces](../../01-fiches-simples/debian/12/vie-du-logiciel/splunk/fiche-simple-vm-debian-12-splunk-securiser-premier-acces.md) | | | | |

#### Wazuh

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Wazuh Sauvegarder Mettre A Jour](../../01-fiches-simples/debian/12/vie-du-logiciel/wazuh/fiche-simple-vm-debian-12-wazuh-sauvegarder-mettre-a-jour.md) | | | | |
| P1 | [VM Debian 12 Wazuh Installer Architecture](../../01-fiches-simples/debian/12/vie-du-logiciel/wazuh/fiche-simple-vm-debian-12-wazuh-installer-architecture.md) | | | | |

#### Zabbix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 Zabbix Sauvegarder Mettre A Jour](../../01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-sauvegarder-mettre-a-jour.md) | | | | |
| P1 | [VM Debian 12 Supervision Installation Zabbix Age](../../01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-supervision-installation-zabbix-age.md) | | | | |
| P1 | [VM Debian 12 Supervision Installation Zabbix Ser](../../01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-supervision-installation-zabbix-ser.md) | | | | |
| P1 | [VM Debian 12 Zabbix Installer Configurer](../../01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-installer-configurer.md) | | | | |
| P1 | [VM Debian 12 Zabbix Valider Installation](../../01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-valider-installation.md) | | | | |

#### iTop

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 12 iTop Verifier Sauvegarder MAJ](../../01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-verifier-sauvegarder-maj.md) | | | | |
| P1 | [VM Debian 12 iTop Installer Apache PHP MariaDB](../../01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-installer-apache-php-mariadb.md) | | | | |
| P1 | [VM Debian 12 iTop Installer Paquet Officiel](../../01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-installer-paquet-officiel.md) | | | | |

### Debian/13

#### Ansible

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Ansible Production Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-production-retour-arriere.md) | | | | |
| P1 | [VM Debian 13 Ansible Installer Core](../../01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-installer-core.md) | | | | |
| P1 | [VM Debian 13 Ansible Valider Connexion](../../01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-valider-connexion.md) | | | | |
| P1 | [VM Debian 13 Ansible Valider Playbook](../../01-fiches-simples/debian/13/vie-du-logiciel/ansible/fiche-simple-vm-debian-13-ansible-valider-playbook.md) | | | | |

#### Apache

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Apache Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Apache Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Apache Exploiter Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-exploiter-securiser.md) | | | | |
| P1 | [VM Debian 13 Apache Installer Paquet](../../01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-installer-paquet.md) | | | | |
| P1 | [VM Debian 13 Apache Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-valider.md) | | | | |

#### BIND9

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 BIND9 Autoritatif Sauvegarde Retour](../../01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-sauvegarde-retour.md) | | | | |
| P1 | [VM Debian 13 BIND9 Autoritatif Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-installer.md) | | | | |
| P1 | [VM Debian 13 BIND9 Autoritatif Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-valider.md) | | | | |
| P1 | [VM Debian 13 Services Installation DNS BIND9](../../01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-services-installation-dns-bind9.md) | | | | |

#### Bareos

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Bareos Valider Restauration](../../01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-valider-restauration.md) | | | | |
| P1 | [VM Debian 13 Bareos Installer Paquets](../../01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-installer-paquets.md) | | | | |

#### Bash Shell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Bash Shell Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Bash Shell Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Bash Shell Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-installer.md) | | | | |
| P1 | [VM Debian 13 Bash Shell Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-securiser.md) | | | | |
| P1 | [VM Debian 13 Bash Shell Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-valider.md) | | | | |

#### BlueMind

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 BlueMind Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 BlueMind Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 BlueMind Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-installer.md) | | | | |
| P1 | [VM Debian 13 BlueMind Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-securiser.md) | | | | |
| P1 | [VM Debian 13 BlueMind Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-valider.md) | | | | |

#### Caddy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Caddy Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-retour-arriere.md) | | | | |
| P1 | [VM Debian 13 Caddy Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-installer.md) | | | | |
| P1 | [VM Debian 13 Caddy Valider Service](../../01-fiches-simples/debian/13/vie-du-logiciel/caddy/fiche-simple-vm-debian-13-caddy-valider-service.md) | | | | |

#### Centreon

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Centreon Installer Central](../../01-fiches-simples/debian/13/vie-du-logiciel/centreon/fiche-simple-vm-debian-13-centreon-installer-central.md) | | | | |
| P1 | [VM Debian 13 Centreon Securiser Exploiter](../../01-fiches-simples/debian/13/vie-du-logiciel/centreon/fiche-simple-vm-debian-13-centreon-securiser-exploiter.md) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Securite Certbot TLS](../../01-fiches-simples/debian/13/vie-du-logiciel/certbot/fiche-simple-vm-debian-13-securite-certbot-tls.md) | | | | |

#### DHCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Kea Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-installer.md) | | | | |
| P1 | [VM Debian 13 Kea Valider Demarrer](../../01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-valider-demarrer.md) | | | | |
| P1 | [VM Debian 13 Services Installation DHCP KEA](../../01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-services-installation-dhcp-kea.md) | | | | |

#### Docker

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Installation Docker Engine](../../01-fiches-simples/debian/13/vie-du-logiciel/docker/fiche-simple-vm-debian-13-installation-docker-engine.md) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Dovecot Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Dovecot Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Dovecot Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-installer.md) | | | | |
| P1 | [VM Debian 13 Dovecot Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-securiser.md) | | | | |
| P1 | [VM Debian 13 Dovecot Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-valider.md) | | | | |

#### Elastic Stack

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Elastic Stack Installer Elasticsearch](../../01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-installer-elasticsearch.md) | | | | |
| P1 | [VM Debian 13 Elastic Stack Installer Kibana](../../01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-installer-kibana.md) | | | | |

#### FOG Project

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 FOG Project Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 FOG Project Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 FOG Project Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-installer.md) | | | | |
| P1 | [VM Debian 13 FOG Project Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-securiser.md) | | | | |
| P1 | [VM Debian 13 FOG Project Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-valider.md) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Securite Fail2ban](../../01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban.md) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 FreeIPA Client Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 FreeIPA Client Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-installer.md) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-securiser.md) | | | | |
| P1 | [VM Debian 13 FreeIPA Client Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-valider.md) | | | | |

#### GNS3

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 GNS3 Deploiement Sauvegarde MAJ](../../01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-sauvegarde-maj.md) | | | | |
| P1 | [VM Debian 13 GNS3 Deploiement Installer GUI Serveur](../../01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-deploiement-installer-gui-serveur.md) | | | | |
| P1 | [VM Debian 13 GNS3 Valider Lab Isole](../../01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-valider-lab-isole.md) | | | | |

#### Git

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Git Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/git/fiche-simple-vm-debian-13-git-installer.md) | | | | |

#### GitLab

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 GitLab CE Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 GitLab CE Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 GitLab CE Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-installer.md) | | | | |
| P1 | [VM Debian 13 GitLab CE Securiser TLS](../../01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-securiser-tls.md) | | | | |
| P1 | [VM Debian 13 GitLab CE Valider Recette](../../01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-valider-recette.md) | | | | |

#### Gitea

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Gitea Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Gitea Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Gitea Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-installer.md) | | | | |
| P1 | [VM Debian 13 Gitea Securiser TLS](../../01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-securiser-tls.md) | | | | |
| P1 | [VM Debian 13 Gitea Valider Recette](../../01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-valider-recette.md) | | | | |

#### HAProxy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 HAProxy Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 HAProxy Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-installer.md) | | | | |
| P1 | [VM Debian 13 HAProxy Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-securiser.md) | | | | |
| P1 | [VM Debian 13 HAProxy Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-valider.md) | | | | |

#### HashiCorp Vault

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Debian 13 Hashicorp Vault Valider Politique](../../01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-debian-13-hashicorp-vault-valider-politique.md) | | | | |
| P1 | [VM Debian 13 Vault Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/hashicorp-vault/fiche-simple-vm-debian-13-vault-installer.md) | | | | |

#### ISC DHCP Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 ISC-DHCP-Server Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 ISC-DHCP-Server Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-installer.md) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-securiser.md) | | | | |
| P1 | [VM Debian 13 ISC-DHCP-Server Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-valider.md) | | | | |

#### InfluxDB3 Core

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [InfluxDB3 Core Debian 13 Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-retour-arriere.md) | | | | |
| P0 | [InfluxDB3 Core Debian 13 Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-sauvegarder-restaurer.md) | | | | |
| P1 | [InfluxDB3 Core Debian 13 Installer Depot](../../01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-installer-depot.md) | | | | |
| P1 | [InfluxDB3 Core Debian 13 Valider Ecriture](../../01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-valider-ecriture.md) | | | | |

#### KeePassXC

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 KeePassXC Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-sauvegarder-restaurer.md) | | | | |
| P0 | [VM Debian 13 KeePassXC Verifier Mise A Jour](../../01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-verifier-mise-a-jour.md) | | | | |
| P1 | [VM Debian 13 KeePassXC Valider Coffre](../../01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-valider-coffre.md) | | | | |

#### Kubernetes K3s

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Kubeadm Sauvegarde Mise A Jour](../../01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-sauvegarde-mise-a-jour.md) | | | | |
| P0 | [VM Debian 13 Kubeadm Sauvegarder Preparer](../../01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-sauvegarder-preparer.md) | | | | |
| P1 | [VM Debian 13 K3s Installer Noeud Lab](../../01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-installer-noeud-lab.md) | | | | |
| P1 | [VM Debian 13 K3s Securiser Surveiller](../../01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-securiser-surveiller.md) | | | | |
| P1 | [VM Debian 13 Kubeadm Installer Paquets](../../01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-installer-paquets.md) | | | | |
| P1 | [VM Debian 13 Kubeadm Installer Runtime](../../01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-installer-runtime.md) | | | | |
| P1 | [VM Debian 13 Kubeadm Valider Cluster](../../01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-kubeadm-valider-cluster.md) | | | | |

#### LEMP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 LEMP Sauvegarder Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/lemp/fiche-simple-vm-debian-13-lemp-sauvegarder-retour-arriere.md) | | | | |

#### MariaDB

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MariaDB Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Database Installation MariaDB 11](../../01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-database-installation-mariadb-11.md) | | | | |
| P1 | [VM Debian 13 LEMP Securiser MariaDB](../../01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-lemp-securiser-mariadb.md) | | | | |
| P1 | [VM Debian 13 MariaDB Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-securiser.md) | | | | |
| P1 | [VM Debian 13 MariaDB Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-valider.md) | | | | |

#### Minikube

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Minikube Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Minikube Sauvegarde Prealable](../../01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-sauvegarde-prealable.md) | | | | |
| P1 | [VM Debian 13 Minikube Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-installer.md) | | | | |
| P1 | [VM Debian 13 Minikube Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/minikube/fiche-simple-vm-debian-13-minikube-valider.md) | | | | |

#### MongoDB

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MongoDB Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 MongoDB Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-installer.md) | | | | |
| P1 | [VM Debian 13 MongoDB Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser.md) | | | | |
| P1 | [VM Debian 13 MongoDB Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-valider.md) | | | | |

#### MySQL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 MySQL Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 MySQL Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-installer.md) | | | | |
| P1 | [VM Debian 13 MySQL Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-securiser.md) | | | | |
| P1 | [VM Debian 13 MySQL Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-valider.md) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Debian 13 Nakivo Transporter Mettre A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-mettre-a-jour-retour-arriere.md) | | | | |
| P0 | [Debian 13 Nakivo Transporter Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-sauvegarder-restaurer.md) | | | | |
| P1 | [Debian 13 Nakivo Transporter Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-installer.md) | | | | |
| P1 | [Debian 13 Nakivo Transporter Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-securiser.md) | | | | |
| P1 | [Debian 13 Nakivo Transporter Valider Mettre A Jour](../../01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-valider-mettre-a-jour.md) | | | | |

#### NetBox

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 NetBox Sauvegarder Mettre A Jour](../../01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-sauvegarder-mettre-a-jour.md) | | | | |
| P1 | [VM Debian 13 NetBox Installer Release](../../01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-installer-release.md) | | | | |
| P1 | [VM Debian 13 NetBox Valider IPAM](../../01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-valider-ipam.md) | | | | |
| P1 | [VM Debian 13 NetBox Valider IPAM Pilote](../../01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-valider-ipam-pilote.md) | | | | |

#### Nextcloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Nextcloud Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Nextcloud Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Nextcloud Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-installer.md) | | | | |
| P1 | [VM Debian 13 Nextcloud Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-securiser.md) | | | | |
| P1 | [VM Debian 13 Nextcloud Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-valider.md) | | | | |

#### Nginx

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Nginx Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Nginx Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-installer.md) | | | | |
| P1 | [VM Debian 13 Nginx Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-securiser.md) | | | | |
| P1 | [VM Debian 13 Nginx Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-valider.md) | | | | |
| P1 | [VM Debian 13 Web Installation Nginx PHP8.4 FPM](../../01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-web-installation-nginx-php8-4-fpm.md) | | | | |

#### OCS Inventory

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OCS Inventory Sauvegarde](../../01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-sauvegarde.md) | | | | |
| P1 | [VM Debian 13 Installer Agent OCS Inventory](../../01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-installer-agent-ocs-inventory.md) | | | | |
| P1 | [VM Debian 13 OCS Inventory Installer Paquets](../../01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-installer-paquets.md) | | | | |

#### Observium

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Observium Sauvegarde Securite](../../01-fiches-simples/debian/13/vie-du-logiciel/observium/fiche-simple-vm-debian-13-observium-sauvegarde-securite.md) | | | | |

#### OpenLDAP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenLDAP Restaurer Test](../../01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-restaurer-test.md) | | | | |
| P0 | [VM Debian 13 OpenLDAP Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 OpenLDAP Sauvegarder](../../01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-sauvegarder.md) | | | | |
| P1 | [VM Debian 13 OpenLDAP Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-installer.md) | | | | |
| P1 | [VM Debian 13 OpenLDAP Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-valider.md) | | | | |

#### OpenMediaVault

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 OpenMediaVault Installer OMV](../../01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-openmediavault-installer-omv.md) | | | | |
| P1 | [VM Debian 13 Stockage Installation OpenMediaVault 8](../../01-fiches-simples/debian/13/vie-du-logiciel/openmediavault/fiche-simple-vm-debian-13-stockage-installation-openmediavault-8.md) | | | | |

#### OpenTofu

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenTofu Mise A Jour Rollback](../../01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-mise-a-jour-rollback.md) | | | | |
| P1 | [VM Debian 13 OpenTofu Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-installer.md) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 OpenVPN Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 OpenVPN Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 OpenVPN Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-installer.md) | | | | |
| P1 | [VM Debian 13 OpenVPN Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-securiser.md) | | | | |
| P1 | [VM Debian 13 OpenVPN Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-valider.md) | | | | |

#### Packer

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Packer Debian 13 Nettoyer Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-nettoyer-retour-arriere.md) | | | | |
| P1 | [Packer Debian 13 Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-installer.md) | | | | |
| P1 | [Packer Debian 13 Valider Template](../../01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-valider-template.md) | | | | |

#### Passbolt

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Passbolt Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Passbolt Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Passbolt Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-installer.md) | | | | |
| P1 | [VM Debian 13 Passbolt Securiser TLS](../../01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-securiser-tls.md) | | | | |
| P1 | [VM Debian 13 Passbolt Valider Recette](../../01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-valider-recette.md) | | | | |

#### Podman Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Podman Buildah Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Podman Buildah Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Podman Buildah Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-installer.md) | | | | |
| P1 | [VM Debian 13 Podman Buildah Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-securiser.md) | | | | |
| P1 | [VM Debian 13 Podman Buildah Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-valider.md) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Postfix Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Postfix Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Postfix Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-installer.md) | | | | |
| P1 | [VM Debian 13 Postfix Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-securiser.md) | | | | |
| P1 | [VM Debian 13 Postfix Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-valider.md) | | | | |

#### PostgreSQL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PostgreSQL Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Database Installation PostgreSQL 17](../../01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-database-installation-postgresql-17.md) | | | | |
| P1 | [VM Debian 13 NetBox Installer PostgreSQL Redis](../../01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-netbox-installer-postgresql-redis.md) | | | | |
| P1 | [VM Debian 13 PostgreSQL Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-securiser.md) | | | | |
| P1 | [VM Debian 13 PostgreSQL Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-valider.md) | | | | |

#### Postman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Postman Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-mise-a-jour-retour-arriere.md) | | | | |
| P1 | [VM Debian 13 Postman Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-installer.md) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PowerShell Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 PowerShell Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 PowerShell Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-installer.md) | | | | |
| P1 | [VM Debian 13 PowerShell Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-securiser.md) | | | | |
| P1 | [VM Debian 13 PowerShell Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-valider.md) | | | | |

#### Prometheus Grafana

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Prometheus Grafana Sauvegarder](../../01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-sauvegarder.md) | | | | |
| P1 | [VM Debian 13 Prometheus Grafana Installer Grafana](../../01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-installer-grafana.md) | | | | |
| P1 | [VM Debian 13 Prometheus Grafana Installer Prometheus](../../01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-installer-prometheus.md) | | | | |

#### PuTTY

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 PuTTY Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 PuTTY Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 PuTTY Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-installer.md) | | | | |
| P1 | [VM Debian 13 PuTTY Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-securiser.md) | | | | |
| P1 | [VM Debian 13 PuTTY Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/putty/fiche-simple-vm-debian-13-putty-valider.md) | | | | |

#### Python

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Python Installer Outils](../../01-fiches-simples/debian/13/vie-du-logiciel/python/fiche-simple-vm-debian-13-python-installer-outils.md) | | | | |
| P1 | [VM Debian 13 Python Valider Venv Pipx](../../01-fiches-simples/debian/13/vie-du-logiciel/python/fiche-simple-vm-debian-13-python-valider-venv-pipx.md) | | | | |

#### QGIS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 QGIS Maj Sauvegarde](../../01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-maj-sauvegarde.md) | | | | |
| P1 | [VM Debian 13 QGIS Installer QGIS](../../01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-installer-qgis.md) | | | | |
| P1 | [VM Debian 13 QGIS Valider Chaine](../../01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-valider-chaine.md) | | | | |
| P1 | [VM Debian 13 QGIS Valider Projet](../../01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-valider-projet.md) | | | | |

#### Redis

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Redis Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Redis Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-installer.md) | | | | |
| P1 | [VM Debian 13 Redis Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-securiser.md) | | | | |
| P1 | [VM Debian 13 Redis Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-valider.md) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Sauvegarde Restic Depot](../../01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot.md) | | | | |

#### Samba AD DC

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Samba AD DC Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Samba AD DC Sauvegarde](../../01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-sauvegarde.md) | | | | |
| P1 | [VM Debian 13 Samba AD DC Reseau Securite](../../01-fiches-simples/debian/13/vie-du-logiciel/samba-ad-dc/fiche-simple-vm-debian-13-samba-ad-dc-reseau-securite.md) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Snort Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Snort Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Snort Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-installer.md) | | | | |
| P1 | [VM Debian 13 Snort Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-securiser.md) | | | | |
| P1 | [VM Debian 13 Snort Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-valider.md) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Suricata IDS Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-installer.md) | | | | |
| P1 | [VM Debian 13 Suricata Valider Capteur IDS](../../01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-valider-capteur-ids.md) | | | | |

#### Terraform

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Terraform Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 Terraform Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Terraform Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-installer.md) | | | | |
| P1 | [VM Debian 13 Terraform Securiser Etat](../../01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-securiser-etat.md) | | | | |
| P1 | [VM Debian 13 Terraform Valider Recette](../../01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-valider-recette.md) | | | | |

#### Traefik

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 Traefik Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 Traefik Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-installer.md) | | | | |
| P1 | [VM Debian 13 Traefik Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-securiser.md) | | | | |
| P1 | [VM Debian 13 Traefik Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-valider.md) | | | | |

#### VS Code

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 VSCode Mise a jour](../../01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-mise-a-jour.md) | | | | |
| P1 | [VM Debian 13 VSCode Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-installer.md) | | | | |
| P1 | [VM Debian 13 VSCode Valider Installation](../../01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-valider-installation.md) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 WireGuard Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 WireGuard Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 WireGuard Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-installer.md) | | | | |
| P1 | [VM Debian 13 WireGuard Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-securiser.md) | | | | |
| P1 | [VM Debian 13 WireGuard Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-valider.md) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Wireshark Analyse Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer.md) | | | | |
| P1 | [VM Debian 13 Wireshark Valider Capture Locale](../../01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-valider-capture-locale.md) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 Zeek Depot Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/zeek/fiche-simple-vm-debian-13-zeek-depot-installer.md) | | | | |
| P1 | [VM Debian 13 Zeek Valider Capteur](../../01-fiches-simples/debian/13/vie-du-logiciel/zeek/fiche-simple-vm-debian-13-zeek-valider-capteur.md) | | | | |
| P1 | [VM Debian 13 Zeek Valider Logs](../../01-fiches-simples/debian/13/vie-du-logiciel/zeek/fiche-simple-vm-debian-13-zeek-valider-logs.md) | | | | |

#### cURL

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 cURL Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 cURL Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 cURL Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-installer.md) | | | | |
| P1 | [VM Debian 13 cURL Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-securiser.md) | | | | |
| P1 | [VM Debian 13 cURL Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/curl/fiche-simple-vm-debian-13-curl-valider.md) | | | | |

#### draw-io

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Debian 13 draw io Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-installer.md) | | | | |
| P1 | [VM Debian 13 draw io Valider Diagramme](../../01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-valider-diagramme.md) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 ownCloud Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 ownCloud Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 ownCloud Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-installer.md) | | | | |
| P1 | [VM Debian 13 ownCloud Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-securiser.md) | | | | |
| P1 | [VM Debian 13 ownCloud Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-valider.md) | | | | |

#### phpIPAM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 phpIPAM Sauvegarder](../../01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-sauvegarder.md) | | | | |
| P1 | [VM Debian 13 phpIPAM Valider IPAM](../../01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-valider-ipam.md) | | | | |

#### rsync

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 rsync Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 rsync Valider Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-valider-restaurer.md) | | | | |
| P1 | [VM Debian 13 rsync Installer Preparer](../../01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-installer-preparer.md) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Debian 13 tcpdump Mise A Jour Retour Arriere](../../01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Debian 13 tcpdump Sauvegarder Restaurer](../../01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Debian 13 tcpdump Installer](../../01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-installer.md) | | | | |
| P1 | [VM Debian 13 tcpdump Securiser](../../01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-securiser.md) | | | | |
| P1 | [VM Debian 13 tcpdump Valider](../../01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-valider.md) | | | | |

### OPNsense/Toutes-versions

#### CARP pfsync HA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Appliance OPNsense CARP pfsync Exploitation Retour Arriere](../../01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/carp-pfsync-ha/fiche-simple-appliance-opnsense-carp-pfsync-exploitation-retour-arriere.md) | | | | |

### Proxmox/Toutes-versions

#### Cluster Stockage VM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Proxmox VE Diagnostic Restaurer](../../01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-restaurer.md) | | | | |

#### Proxmox Backup Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Proxmox Backup Server Tester Restauration](../../01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-tester-restauration.md) | | | | |
| P1 | [Hote Proxmox Backup Server Installer Datastore](../../01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-installer-datastore.md) | | | | |

### Proxmox/VE-8

#### Cluster Corosync

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Proxmox VE 8 Cluster Securiser](../../01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-securiser.md) | | | | |
| P1 | [Hote Proxmox VE 8 Cluster Valider](../../01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-valider.md) | | | | |

#### Proxmox OpenStack

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Mise A Jour Retour Arriere](../../01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere](../../01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-nettoyer-retour-arriere.md) | | | | |
| P0 | [VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab](../../01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-sauvegarder-restaurer-lab.md) | | | | |
| P1 | [VM Proxmox VE 8 Proxmox OpenStack Securiser Valider Lab](../../01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-securiser-valider-lab.md) | | | | |
| P1 | [VM Ubuntu 24-04 OpenStack DevStack Installer Lab](../../01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/openstack/ubuntu-24-04-lts/fiche-simple-vm-ubuntu-24-04-openstack-devstack-installer-lab.md) | | | | |

### Rocky-Linux/9

#### Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Buildah Publier Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-publier-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 Buildah Sauvegarder Etat Initial](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-sauvegarder-etat-initial.md) | | | | |
| P1 | [VM Rocky 9 Buildah Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-installer.md) | | | | |
| P1 | [VM Rocky 9 Buildah Valider Image](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/buildah/fiche-simple-vm-rocky-9-buildah-valider-image.md) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Rocky 9 Securite Certbot TLS](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/certbot/fiche-simple-vm-rocky-9-securite-certbot-tls.md) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Dovecot Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 Dovecot Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 Dovecot Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-installer.md) | | | | |
| P1 | [VM Rocky 9 Dovecot Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-securiser.md) | | | | |
| P1 | [VM Rocky 9 Dovecot Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/dovecot/fiche-simple-vm-rocky-9-dovecot-valider.md) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Rocky 9 Securite Fail2ban](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/fail2ban/fiche-simple-vm-rocky-9-securite-fail2ban.md) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 FreeIPA Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-restaurer.md) | | | | |
| P0 | [VM Rocky 9 FreeIPA Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 FreeIPA Sauvegarder](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-sauvegarder.md) | | | | |
| P1 | [VM Rocky 9 FreeIPA Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-installer.md) | | | | |
| P1 | [VM Rocky 9 FreeIPA Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-valider.md) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 OpenVPN Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 OpenVPN Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 OpenVPN Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-installer.md) | | | | |
| P1 | [VM Rocky 9 OpenVPN Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-securiser.md) | | | | |
| P1 | [VM Rocky 9 OpenVPN Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-valider.md) | | | | |

#### Pile Web

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Pile Web Sauvegarder Retour](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/pile-web/fiche-simple-vm-rocky-9-pile-web-sauvegarder-retour.md) | | | | |
| P1 | [VM Rocky 9 Pile Web Installer Paquets](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/pile-web/fiche-simple-vm-rocky-9-pile-web-installer-paquets.md) | | | | |
| P1 | [VM Rocky 9 Pile Web Securiser MariaDB](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/pile-web/fiche-simple-vm-rocky-9-pile-web-securiser-mariadb.md) | | | | |

#### Podman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Podman Quadlet Mise A Jour Reprise](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-mise-a-jour-reprise.md) | | | | |
| P1 | [VM Rocky 9 Podman Quadlet Valider Image](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-valider-image.md) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Postfix Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 Postfix Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 Postfix Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-installer.md) | | | | |
| P1 | [VM Rocky 9 Postfix Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-securiser.md) | | | | |
| P1 | [VM Rocky 9 Postfix Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-valider.md) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 PowerShell Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 PowerShell Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 PowerShell Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-installer.md) | | | | |
| P1 | [VM Rocky 9 PowerShell Securiser Signature](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-securiser-signature.md) | | | | |
| P1 | [VM Rocky 9 PowerShell Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-valider.md) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Sauvegarde Restic Depot](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/restic/fiche-simple-vm-rocky-9-sauvegarde-restic-depot.md) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Snort Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 Snort Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 Snort Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-installer.md) | | | | |
| P1 | [VM Rocky 9 Snort Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-securiser.md) | | | | |
| P1 | [VM Rocky 9 Snort Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-valider.md) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Suricata Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 Suricata Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 Suricata Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-installer.md) | | | | |
| P1 | [VM Rocky 9 Suricata Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-securiser.md) | | | | |
| P1 | [VM Rocky 9 Suricata Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-valider.md) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 WireGuard Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 WireGuard Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 WireGuard Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-installer.md) | | | | |
| P1 | [VM Rocky 9 WireGuard Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-securiser.md) | | | | |
| P1 | [VM Rocky 9 WireGuard Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-valider.md) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Wireshark Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 Wireshark Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 Wireshark Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-installer.md) | | | | |
| P1 | [VM Rocky 9 Wireshark Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-securiser.md) | | | | |
| P1 | [VM Rocky 9 Wireshark Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-valider.md) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 Zeek Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 Zeek Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 Zeek Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-installer.md) | | | | |
| P1 | [VM Rocky 9 Zeek Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-securiser.md) | | | | |
| P1 | [VM Rocky 9 Zeek Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-valider.md) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 ownCloud Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 ownCloud Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 ownCloud Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-installer.md) | | | | |
| P1 | [VM Rocky 9 ownCloud Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-securiser.md) | | | | |
| P1 | [VM Rocky 9 ownCloud Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-valider.md) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Rocky 9 tcpdump Mise A Jour Retour Arriere](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Rocky 9 tcpdump Sauvegarder Restaurer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Rocky 9 tcpdump Installer](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-installer.md) | | | | |
| P1 | [VM Rocky 9 tcpdump Securiser](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-securiser.md) | | | | |
| P1 | [VM Rocky 9 tcpdump Valider](../../01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-valider.md) | | | | |

### Transverses/Cloud-SaaS

#### AWS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud AWS Nettoyage Retour Arriere](../../01-fiches-simples/transverses/cloud-saas/aws/fiche-simple-cloud-aws-nettoyage-retour-arriere.md) | | | | |
| P0 | [Cloud AWS Sauvegardes Snapshots](../../01-fiches-simples/transverses/cloud-saas/aws/fiche-simple-cloud-aws-sauvegardes-snapshots.md) | | | | |

#### Azure

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Azure Nettoyage Retour Arriere](../../01-fiches-simples/transverses/cloud-saas/azure/fiche-simple-cloud-azure-nettoyage-retour-arriere.md) | | | | |
| P0 | [Cloud Azure Sauvegardes Snapshots](../../01-fiches-simples/transverses/cloud-saas/azure/fiche-simple-cloud-azure-sauvegardes-snapshots.md) | | | | |

#### Datadog

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Datadog Retour Arriere](../../01-fiches-simples/transverses/cloud-saas/datadog/fiche-simple-cloud-datadog-retour-arriere.md) | | | | |
| P1 | [Cloud Datadog Installer Agent Linux Pilote](../../01-fiches-simples/transverses/cloud-saas/datadog/fiche-simple-cloud-datadog-installer-agent-linux-pilote.md) | | | | |
| P1 | [Cloud Datadog Securite Maintenance](../../01-fiches-simples/transverses/cloud-saas/datadog/fiche-simple-cloud-datadog-securite-maintenance.md) | | | | |

#### Dynatrace

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Dynatrace OneAgent Securite MaJ Retour](../../01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-securite-maj-retour.md) | | | | |
| P1 | [Cloud Dynatrace OneAgent Generer Installateur](../../01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-generer-installateur.md) | | | | |
| P1 | [Cloud Dynatrace OneAgent Installer Pilote](../../01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-installer-pilote.md) | | | | |
| P1 | [Cloud Dynatrace OneAgent Installer Pilote Linux](../../01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-installer-pilote-linux.md) | | | | |

#### Entra ID

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud Entra ID Connect Retour Arriere](../../01-fiches-simples/transverses/cloud-saas/entra-id/fiche-simple-cloud-entra-id-connect-retour-arriere.md) | | | | |

#### Exchange Online

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Cloud Exchange Online Valider Recette](../../01-fiches-simples/transverses/cloud-saas/exchange-online/fiche-simple-cloud-exchange-online-valider-recette.md) | | | | |

#### GCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Cloud GCP Nettoyage Retour Arriere](../../01-fiches-simples/transverses/cloud-saas/gcp/fiche-simple-cloud-gcp-nettoyage-retour-arriere.md) | | | | |
| P0 | [Cloud GCP Sauvegardes Snapshots](../../01-fiches-simples/transverses/cloud-saas/gcp/fiche-simple-cloud-gcp-sauvegardes-snapshots.md) | | | | |

#### Google Workspace

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Cloud Google Workspace Valider Recette](../../01-fiches-simples/transverses/cloud-saas/google-workspace/fiche-simple-cloud-google-workspace-valider-recette.md) | | | | |

### Transverses/Docker

#### Bitwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Bitwarden Self Hosted Deploiement Sauvegardes Mises A Jour Reprise](../../01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-sauvegardes-mises-a-jour-reprise.md) | | | | |
| P0 | [Bitwarden Self Hosted Verifier Backup Restauration](../../01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-verifier-backup-restauration.md) | | | | |
| P1 | [Bitwarden Self Hosted Deploiement Telecharger Installer](../../01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-telecharger-installer.md) | | | | |

#### Guacamole

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Docker Guacamole Mise A Jour Retour Arriere](../../01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Hote Docker Guacamole Sauvegarde Restauration](../../01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-sauvegarde-restauration.md) | | | | |
| P1 | [Hote Docker Guacamole Valider Controle Acces](../../01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-valider-controle-acces.md) | | | | |

#### Installation systeme

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Docker Installation Engine et Compose](../../01-fiches-simples/transverses/docker/installation-systeme/fiche-simple-hote-docker-installation-engine-et-compose.md) | | | | |

#### Nextcloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Nextcloud29 Migration Retour Arriere](../../01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-retour-arriere.md) | | | | |
| P0 | [Docker Nextcloud29 Migration Sauvegarder Tester Restauration](../../01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-sauvegarder-tester-restauration.md) | | | | |

#### Sauvegarde restauration

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Sauvegarder Restaurer Volume](../../01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-docker-sauvegarder-restaurer-volume.md) | | | | |
| P0 | [Docker Sauvegarder Stack Compose Base Donnees](../../01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-docker-sauvegarder-stack-compose-base-donnees.md) | | | | |
| P0 | [Hote Docker Stack Restaurer](../../01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-hote-docker-stack-restaurer.md) | | | | |
| P0 | [Hote Docker Stack Verifier Sauvegarde](../../01-fiches-simples/transverses/docker/sauvegarde-restauration/fiche-simple-hote-docker-stack-verifier-sauvegarde.md) | | | | |

#### Securite

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [Hote Docker Securite Activer Mode Rootless](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-activer-mode-rootless.md) | | | | |
| P1 | [Hote Docker Securite Hardening Images Mises A Jour](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-images-mises-a-jour.md) | | | | |
| P1 | [Hote Docker Securite Hardening Inventaire Plan Controle](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-inventaire-plan-controle.md) | | | | |
| P1 | [Hote Docker Securite Hardening Reduire Privileges](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-reduire-privileges.md) | | | | |
| P1 | [Hote Docker Securite Hardening Reponse Incident](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-reponse-incident.md) | | | | |
| P1 | [Hote Docker Securite Hardening Ressources Journaux](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-ressources-journaux.md) | | | | |
| P1 | [Hote Docker Securite Hardening Segmentation Donnees](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-segmentation-donnees.md) | | | | |
| P1 | [Hote Docker Securite Hardening Verifier Exploiter](../../01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-verifier-exploiter.md) | | | | |

#### Snipe IT

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Snipe-IT Mise A Jour Retour](../../01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-mise-a-jour-retour.md) | | | | |
| P0 | [Docker Snipe-IT Sauvegarde Restauration](../../01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-sauvegarde-restauration.md) | | | | |
| P1 | [Docker Snipe-IT Valider Demarrer](../../01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-valider-demarrer.md) | | | | |

#### Traefik

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Conteneur Traefik Mise A Jour Retour](../../01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-mise-a-jour-retour.md) | | | | |

#### Validation

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker Production Mise A Jour Rollback Compose](../../01-fiches-simples/transverses/docker/validation/fiche-simple-docker-production-mise-a-jour-rollback-compose.md) | | | | |
| P0 | [Docker Production Reconstruire Hote Restaurer Stacks](../../01-fiches-simples/transverses/docker/validation/fiche-simple-docker-production-reconstruire-hote-restaurer-stacks.md) | | | | |

#### Vaultwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Hote Docker Vaultwarden Restaurer](../../01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-restaurer.md) | | | | |
| P0 | [Hote Docker Vaultwarden Retour Arriere](../../01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-retour-arriere.md) | | | | |
| P0 | [Hote Docker Vaultwarden Sauvegarder](../../01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-sauvegarder.md) | | | | |
| P1 | [Hote Docker Vaultwarden Validation](../../01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-validation.md) | | | | |

#### WikiJS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Docker WikiJS Mise A Jour Retour Arriere](../../01-fiches-simples/transverses/docker/wikijs/fiche-simple-docker-wikijs-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Docker WikiJS Sauvegarder Restaurer](../../01-fiches-simples/transverses/docker/wikijs/fiche-simple-docker-wikijs-sauvegarder-restaurer.md) | | | | |
| P1 | [Docker WikiJS Valider Demarrer](../../01-fiches-simples/transverses/docker/wikijs/fiche-simple-docker-wikijs-valider-demarrer.md) | | | | |

### Transverses/Multi-OS

#### Diagnostic Reseau

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Multi-OS Reseau Diagnostic Validation Retour Arriere](../../01-fiches-simples/transverses/multi-os/diagnostic-reseau/fiche-simple-vm-multi-os-reseau-diagnostic-validation-retour-arriere.md) | | | | |
| P1 | [VM Multi-OS Reseau Diagnostic Securiser Diagnostic](../../01-fiches-simples/transverses/multi-os/diagnostic-reseau/fiche-simple-vm-multi-os-reseau-diagnostic-securiser-diagnostic.md) | | | | |

#### Keepalived HAProxy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Linux Keepalived HAProxy Securite Retour Arriere](../../01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-securite-retour-arriere.md) | | | | |
| P1 | [VM Linux Keepalived HAProxy Installer Valider HAProxy](../../01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy.md) | | | | |

### Ubuntu/24-04

#### BlueMind

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 BlueMind Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 BlueMind Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 BlueMind Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 BlueMind Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 BlueMind Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-valider.md) | | | | |

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 24-04 Securite Certbot TLS](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/certbot/fiche-simple-vm-ubuntu-24-04-securite-certbot-tls.md) | | | | |

#### Dovecot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Dovecot Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 Dovecot Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Dovecot Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Dovecot Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 Dovecot Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-valider.md) | | | | |

#### EVE NG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 EVE-NG Mettre A Jour Retour](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-mettre-a-jour-retour.md) | | | | |
| P0 | [VM Ubuntu 24-04 EVE-NG Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 EVE-NG Creer Valider Lab](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-creer-valider-lab.md) | | | | |
| P1 | [VM Ubuntu 24-04 EVE-NG Installer ISO VM](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-installer-iso-vm.md) | | | | |
| P1 | [VM Ubuntu 24-04 EVE-NG Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-securiser.md) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 24-04 Securite Fail2ban](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/fail2ban/fiche-simple-vm-ubuntu-24-04-securite-fail2ban.md) | | | | |

#### FreeIPA

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 FreeIPA Client Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 FreeIPA Client Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 FreeIPA Client Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 FreeIPA Client Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 FreeIPA Client Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-valider.md) | | | | |

#### Graylog

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Graylog Verifier Exploiter Sauvegarder](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-verifier-exploiter-sauvegarder.md) | | | | |
| P1 | [VM Ubuntu 24-04 Graylog Installer Data Node](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-data-node.md) | | | | |
| P1 | [VM Ubuntu 24-04 Graylog Installer MongoDB](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-mongodb.md) | | | | |
| P1 | [VM Ubuntu 24-04 Graylog Installer Server](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-server.md) | | | | |
| P1 | [VM Ubuntu 24-04 Graylog Valider Input Syslog Pilote](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-valider-input-syslog-pilote.md) | | | | |

#### LEMP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 LEMP Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 LEMP Valider Sauvegarder Exploiter](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-valider-sauvegarder-exploiter.md) | | | | |
| P1 | [VM Ubuntu 24-04 LEMP Installer Pile](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-installer-pile.md) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Ubuntu 24-04 Nakivo Transporter Mettre A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-mettre-a-jour-retour-arriere.md) | | | | |
| P0 | [Ubuntu 24-04 Nakivo Transporter Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-sauvegarder-restaurer.md) | | | | |
| P1 | [Ubuntu 24-04 Nakivo Transporter Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-installer.md) | | | | |
| P1 | [Ubuntu 24-04 Nakivo Transporter Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-securiser.md) | | | | |
| P1 | [Ubuntu 24-04 Nakivo Transporter Valider Mettre A Jour](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-valider-mettre-a-jour.md) | | | | |

#### OpenLDAP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 OpenLDAP Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 OpenLDAP Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 OpenLDAP Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 OpenLDAP Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 OpenLDAP Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-valider.md) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 OpenVPN Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 OpenVPN Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 OpenVPN Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 OpenVPN Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 OpenVPN Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-valider.md) | | | | |

#### Packet Tracer

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Packet Tracer Sauvegarder Maintenir](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-sauvegarder-maintenir.md) | | | | |
| P1 | [VM Ubuntu 24-04 Packet Tracer Installer Paquet](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-installer-paquet.md) | | | | |
| P1 | [VM Ubuntu 24-04 Packet Tracer Valider Simulation](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-valider-simulation.md) | | | | |

#### Podman Buildah

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Podman Buildah Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 Podman Buildah Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Podman Buildah Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Podman Buildah Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 Podman Buildah Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-valider.md) | | | | |

#### Postfix

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Postfix Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 Postfix Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Postfix Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Postfix Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 Postfix Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-valider.md) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 PowerShell Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 PowerShell Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 PowerShell Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 PowerShell Securiser Signature](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-securiser-signature.md) | | | | |
| P1 | [VM Ubuntu 24-04 PowerShell Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-valider.md) | | | | |

#### Snort

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Snort Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 Snort Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Snort Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Snort Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 Snort Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-valider.md) | | | | |

#### Suricata

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Suricata Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 Suricata Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Suricata Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Suricata Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 Suricata Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/suricata/fiche-simple-vm-ubuntu-24-04-suricata-valider.md) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 WireGuard Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 WireGuard Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 WireGuard Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 WireGuard Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 WireGuard Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-valider.md) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Wireshark Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 Wireshark Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Wireshark Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Wireshark Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 Wireshark Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-valider.md) | | | | |

#### Zeek

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 Zeek Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 Zeek Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Zeek Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 Zeek Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 Zeek Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-valider.md) | | | | |

#### ownCloud

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 ownCloud Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 ownCloud Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 ownCloud Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 ownCloud Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 ownCloud Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-valider.md) | | | | |

#### tcpdump

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 24-04 tcpdump Mise A Jour Retour Arriere](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Ubuntu 24-04 tcpdump Sauvegarder Restaurer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Ubuntu 24-04 tcpdump Installer](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-installer.md) | | | | |
| P1 | [VM Ubuntu 24-04 tcpdump Securiser](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-securiser.md) | | | | |
| P1 | [VM Ubuntu 24-04 tcpdump Valider](../../01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-valider.md) | | | | |

### Ubuntu/26-04

#### Certbot

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 26-04 Securite Certbot TLS](../../01-fiches-simples/ubuntu/26-04/vie-du-logiciel/certbot/fiche-simple-vm-ubuntu-26-04-securite-certbot-tls.md) | | | | |

#### Fail2ban

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Ubuntu 26-04 Securite Fail2ban](../../01-fiches-simples/ubuntu/26-04/vie-du-logiciel/fail2ban/fiche-simple-vm-ubuntu-26-04-securite-fail2ban.md) | | | | |

#### LibreNMS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26-04 LibreNMS Sauvegarde Mises A Jour](../../01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-sauvegarde-mises-a-jour.md) | | | | |
| P1 | [VM Ubuntu 26-04 LibreNMS Installer Paquets](../../01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-installer-paquets.md) | | | | |

#### Pile Web

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu 26-04 Pile Web Validation Sauvegarde Retour](../../01-fiches-simples/ubuntu/26-04/vie-du-logiciel/pile-web/fiche-simple-vm-ubuntu-26-04-pile-web-validation-sauvegarde-retour.md) | | | | |
| P1 | [VM Ubuntu 26-04 Pile Web Installer Nginx PHP PostgreSQL](../../01-fiches-simples/ubuntu/26-04/vie-du-logiciel/pile-web/fiche-simple-vm-ubuntu-26-04-pile-web-installer-nginx-php-postgresql.md) | | | | |

### Ubuntu/Toutes-versions

#### Ceph

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu Ceph Sauvegarde Upgrade Retrait](../../01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-sauvegarde-upgrade-retrait.md) | | | | |
| P1 | [VM Ubuntu Ceph Installer Cephadm Bootstrap](../../01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-installer-cephadm-bootstrap.md) | | | | |
| P1 | [VM Ubuntu Ceph Limites Validation](../../01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-limites-validation.md) | | | | |

#### Restic

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Ubuntu Restic Effectuer Sauvegarde](../../01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-effectuer-sauvegarde.md) | | | | |
| P0 | [VM Ubuntu Restic Restaurer Sans Ecraser](../../01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-restaurer-sans-ecraser.md) | | | | |
| P1 | [VM Ubuntu Restic Installer Proteger Secret](../../01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-installer-proteger-secret.md) | | | | |

### VMware/ESXi-8

#### vSphere

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM ESXi 8 VMware vSphere VCSA Sauvegarde Restauration VAMI](../../01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-sauvegarde-restauration-vami.md) | | | | |
| P1 | [VM ESXi 8 VMware vSphere VCSA Installer](../../01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-installer.md) | | | | |

### Windows/Client-11

#### Bitwarden

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Bitwarden Mise A Jour Retour Arriere](../../01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Windows 11 Bitwarden Sauvegarder Restaurer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Windows 11 Bitwarden Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-installer.md) | | | | |
| P1 | [VM Windows 11 Bitwarden Securiser](../../01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-securiser.md) | | | | |
| P1 | [VM Windows 11 Bitwarden Valider](../../01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-valider.md) | | | | |

#### Microsoft Visio

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Visio Mise A Jour Retour Arriere](../../01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Windows 11 Visio Sauvegarder Restaurer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Windows 11 Visio Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-installer.md) | | | | |
| P1 | [VM Windows 11 Visio Securiser](../../01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-securiser.md) | | | | |
| P1 | [VM Windows 11 Visio Valider](../../01-fiches-simples/windows/client-11/vie-du-logiciel/microsoft-visio/fiche-simple-vm-windows-11-visio-valider.md) | | | | |

#### MobaXterm

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 MobaXterm Mise A Jour Rollback](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-mise-a-jour-rollback.md) | | | | |
| P0 | [VM Windows 11 MobaXterm Sauvegarde Restauration](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-sauvegarde-restauration.md) | | | | |
| P1 | [VM Windows 11 MobaXterm Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-installer.md) | | | | |
| P1 | [VM Windows 11 MobaXterm Securisation](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-securisation.md) | | | | |
| P1 | [VM Windows 11 MobaXterm Validation](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mobaxterm/fiche-simple-vm-windows-11-mobaxterm-validation.md) | | | | |

#### OpenSSH

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows 11 Administration Installer OpenSSH Cle](../../01-fiches-simples/windows/client-11/vie-du-logiciel/openssh/fiche-simple-vm-windows-11-administration-installer-openssh-cle.md) | | | | |

#### OpenVPN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Client 11 OpenVPN Mise A Jour Retour Arriere](../../01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Client 11 OpenVPN Sauvegarder Restaurer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Client 11 OpenVPN Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-installer.md) | | | | |
| P1 | [Windows Client 11 OpenVPN Securiser](../../01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-securiser.md) | | | | |
| P1 | [Windows Client 11 OpenVPN Valider](../../01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-valider.md) | | | | |

#### Postman

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Postman Mise A Jour Retour Arriere](../../01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-mise-a-jour-retour-arriere.md) | | | | |
| P1 | [VM Windows 11 Postman Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-installer.md) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 PowerShell7 Mise A Jour Validation](../../01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-mise-a-jour-validation.md) | | | | |
| P1 | [VM Windows 11 PowerShell7 Installer Version Stable](../../01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-installer-version-stable.md) | | | | |
| P1 | [VM Windows 11 PowerShell Valider Shell Admin](../../01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell-valider-shell-admin.md) | | | | |

#### PuTTY

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 PuTTY Mise A Jour Reception](../../01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-mise-a-jour-reception.md) | | | | |
| P1 | [VM Windows 11 PuTTY Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-installer.md) | | | | |
| P1 | [VM Windows 11 PuTTY Valider SSH HostKey](../../01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-valider-ssh-hostkey.md) | | | | |

#### Royal TS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Royal TS Mise A Jour](../../01-fiches-simples/windows/client-11/vie-du-logiciel/royal-ts/fiche-simple-vm-windows-11-royal-ts-mise-a-jour.md) | | | | |
| P0 | [VM Windows 11 Royal TS Sauvegarde Config](../../01-fiches-simples/windows/client-11/vie-du-logiciel/royal-ts/fiche-simple-vm-windows-11-royal-ts-sauvegarde-config.md) | | | | |
| P1 | [VM Windows 11 Royal TS Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/royal-ts/fiche-simple-vm-windows-11-royal-ts-installer.md) | | | | |

#### Sysinternals

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Sysinternals Retour Arriere Limites](../../01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-retour-arriere-limites.md) | | | | |
| P1 | [VM Windows 11 Sysinternals Collecte Validation](../../01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-collecte-validation.md) | | | | |

#### WireGuard

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Client 11 WireGuard Mise A Jour Retour Arriere](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Client 11 WireGuard Sauvegarder Restaurer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Client 11 WireGuard Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-installer.md) | | | | |
| P1 | [Windows Client 11 WireGuard Securiser](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-securiser.md) | | | | |
| P1 | [Windows Client 11 WireGuard Valider](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-valider.md) | | | | |

#### Wireshark

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 Wireshark Mise A Jour Retour Arriere](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [VM Windows 11 Wireshark Sauvegarder Restaurer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-sauvegarder-restaurer.md) | | | | |
| P1 | [VM Windows 11 Wireshark Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-installer.md) | | | | |
| P1 | [VM Windows 11 Wireshark Securiser Droits Captures](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-securiser-droits-captures.md) | | | | |
| P1 | [VM Windows 11 Wireshark Valider Recette](../../01-fiches-simples/windows/client-11/vie-du-logiciel/wireshark/fiche-simple-vm-windows-11-wireshark-valider-recette.md) | | | | |

#### mRemoteNG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows 11 mRemoteNG Mise A Jour Rollback](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-mise-a-jour-rollback.md) | | | | |
| P0 | [VM Windows 11 mRemoteNG Sauvegarde Restauration](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-sauvegarde-restauration.md) | | | | |
| P1 | [VM Windows 11 mRemoteNG Installer](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-installer.md) | | | | |
| P1 | [VM Windows 11 mRemoteNG Securisation](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-securisation.md) | | | | |
| P1 | [VM Windows 11 mRemoteNG Validation](../../01-fiches-simples/windows/client-11/vie-du-logiciel/mremoteng/fiche-simple-vm-windows-11-mremoteng-validation.md) | | | | |

### Windows/Server-2022

#### Active Directory

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 ADDS DNS DHCP Sauvegarde Securite Retour](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-adds-dns-dhcp-sauvegarde-securite-retour.md) | | | | |
| P0 | [VM Windows Server 2022 Reprise Foret AD DS Preparer Sauvegardes](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-preparer-sauvegardes.md) | | | | |
| P0 | [VM Windows Server 2022 Reprise Foret AD DS Restaurer Premiers DC](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-restaurer-premiers-dc.md) | | | | |
| P1 | [VM Windows Server 2022 ADDS DNS DHCP Valider ADDS DNS](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-adds-dns-dhcp-valider-adds-dns.md) | | | | |
| P1 | [VM Windows Server 2022 Reprise Foret AD DS Risques Identite Securite](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-risques-identite-securite.md) | | | | |
| P1 | [VM Windows Server 2022 Reprise Foret AD DS Valider Avant Production](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/active-directory/fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-valider-avant-production.md) | | | | |

#### Citrix Virtual Apps and Desktops

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Citrix CVAD Mise A Jour Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 Citrix CVAD Sauvegarder Restaurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-installer.md) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Securiser](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-securiser.md) | | | | |
| P1 | [Windows Server 2022 Citrix CVAD Valider](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/citrix-virtual-apps-and-desktops/fiche-simple-windows-server-2022-citrix-cvad-valider.md) | | | | |

#### DHCP

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows Server 2022 Installation DHCP et Eten](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/dhcp/fiche-simple-vm-windows-server-2022-installation-dhcp-et-eten.md) | | | | |

#### Differences 2016 2019

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Differences 2016 2019 Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/differences-2016-2019/fiche-simple-windows-server-2022-differences-2016-2019-retour-arriere.md) | | | | |

#### Exchange Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Exchange Server DAG Sauvegarde](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-dag-sauvegarde.md) | | | | |
| P0 | [Windows Server 2022 Exchange Server Mise A Jour CU](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-mise-a-jour-cu.md) | | | | |
| P1 | [Windows Server 2022 Exchange Server Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-installer.md) | | | | |
| P1 | [Windows Server 2022 Exchange Server Securiser Certificats](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-securiser-certificats.md) | | | | |
| P1 | [Windows Server 2022 Exchange Server Valider Recette](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2022-exchange-server-valider-recette.md) | | | | |

#### Hyper V

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Hyper V Durcissement Retour](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/hyper-v/fiche-simple-vm-windows-server-2022-hyper-v-durcissement-retour.md) | | | | |
| P1 | [VM Windows Server 2022 Hyper V Installer Role](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/hyper-v/fiche-simple-vm-windows-server-2022-hyper-v-installer-role.md) | | | | |

#### IIS

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 IIS Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-retour-arriere.md) | | | | |
| P0 | [VM Windows Server 2022 IIS Securite Sauvegarde Maintenance](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-securite-sauvegarde-maintenance.md) | | | | |
| P1 | [VM Windows Server 2022 IIS Installer Role Web Server](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-installer-role-web-server.md) | | | | |

#### MECM SCCM

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 MECM Mise a jour Retour arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 MECM Sauvegarde Restauration](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-sauvegarde-restauration.md) | | | | |
| P1 | [Windows Server 2022 MECM Installation](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-installation.md) | | | | |
| P1 | [Windows Server 2022 MECM Securisation](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-securisation.md) | | | | |

#### Nakivo

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 Nakivo Job Sauvegarde](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-job-sauvegarde.md) | | | | |
| P0 | [Windows Server 2022 Nakivo Mettre A Jour Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-mettre-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 Nakivo Restaurer Interface](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-restaurer-interface.md) | | | | |
| P1 | [Windows Server 2022 Nakivo Installer Director Transporter](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-installer-director-transporter.md) | | | | |
| P1 | [Windows Server 2022 Nakivo Securiser](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-securiser.md) | | | | |

#### PRTG

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P1 | [VM Windows Server 2022 PRTG Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-installer.md) | | | | |

#### PowerShell

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 PowerShell Mise A Jour Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 PowerShell Sauvegarder Restaurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Server 2022 PowerShell Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-installer.md) | | | | |
| P1 | [Windows Server 2022 PowerShell Securiser Signature](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-securiser-signature.md) | | | | |
| P1 | [Windows Server 2022 PowerShell Valider](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-valider.md) | | | | |

#### Remote Desktop Services

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 RDS Mise A Jour Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 RDS Sauvegarder Restaurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Server 2022 RDS Installer Configurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-installer-configurer.md) | | | | |
| P1 | [Windows Server 2022 RDS Securiser Acces](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-securiser-acces.md) | | | | |
| P1 | [Windows Server 2022 RDS Valider Recette](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-valider-recette.md) | | | | |

#### Robocopy

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Robocopy Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-retour-arriere.md) | | | | |
| P0 | [VM Windows Server 2022 Robocopy Valider Restaurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-valider-restaurer.md) | | | | |

#### SQL Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 SQL-Server Sauvegarder Restaurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Server 2022 SQL-Server Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-installer.md) | | | | |
| P1 | [Windows Server 2022 SQL-Server Securiser](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-securiser.md) | | | | |
| P1 | [Windows Server 2022 SQL-Server Valider](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-valider.md) | | | | |

#### StarWind Virtual SAN

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 StarWind Virtual SAN Mettre A Jour Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-mettre-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 StarWind Virtual SAN Sauvegarder Restaurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-installer.md) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Securiser](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-securiser.md) | | | | |
| P1 | [Windows Server 2022 StarWind Virtual SAN Valider](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/starwind-virtual-san/fiche-simple-windows-server-2022-starwind-virtual-san-valider.md) | | | | |

#### VMware Horizon

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 VMware Horizon Mise A Jour Retour Arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 VMware Horizon Sauvegarder Restaurer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-installer.md) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Securiser](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-securiser.md) | | | | |
| P1 | [Windows Server 2022 VMware Horizon Valider](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/vmware-horizon/fiche-simple-windows-server-2022-vmware-horizon-valider.md) | | | | |

#### Veeam

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server 2022 Veeam Ajouter Depot Sauvegarde](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-ajouter-depot-sauvegarde.md) | | | | |
| P1 | [VM Windows Server 2022 Veeam Installer Serveur Sauvegarde](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-installer-serveur-sauvegarde.md) | | | | |

#### WDS MDT

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2022 WDS MDT Maintenance Retour arriere](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-maintenance-retour-arriere.md) | | | | |
| P0 | [Windows Server 2022 WDS MDT Sauvegarde Restauration](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-sauvegarde-restauration.md) | | | | |
| P1 | [Windows Server 2022 WDS MDT Installer](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-installer.md) | | | | |
| P1 | [Windows Server 2022 WDS MDT Securisation](../../01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-securisation.md) | | | | |

### Windows/Server-2025

#### Exchange Server

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2025 Exchange Server DAG Sauvegarde](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-dag-sauvegarde.md) | | | | |
| P0 | [Windows Server 2025 Exchange Server Mise A Jour CU](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-mise-a-jour-cu.md) | | | | |
| P1 | [Windows Server 2025 Exchange Server Installer](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-installer.md) | | | | |
| P1 | [Windows Server 2025 Exchange Server Securiser Certificats](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-securiser-certificats.md) | | | | |
| P1 | [Windows Server 2025 Exchange Server Valider Recette](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/exchange-server/fiche-simple-windows-server-2025-exchange-server-valider-recette.md) | | | | |

#### Remote Desktop Services

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [Windows Server 2025 RDS Mise A Jour Retour Arriere](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-mise-a-jour-retour-arriere.md) | | | | |
| P0 | [Windows Server 2025 RDS Sauvegarder Restaurer](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-sauvegarder-restaurer.md) | | | | |
| P1 | [Windows Server 2025 RDS Installer Configurer](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-installer-configurer.md) | | | | |
| P1 | [Windows Server 2025 RDS Securiser TLS Comptes Pare-feu](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-securiser-tls-comptes-pare-feu.md) | | | | |
| P1 | [Windows Server 2025 RDS Valider Recette](../../01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-valider-recette.md) | | | | |

### Windows/Toutes-versions

#### Lansweeper

| Prio | Fiche | Verdict | Date | Testeur | Relecteur |
|---|---|---|---|---|---|
| P0 | [VM Windows Server Lansweeper Sauvegarde Maintenance](../../01-fiches-simples/windows/toutes-versions/vie-du-logiciel/lansweeper/fiche-simple-vm-windows-server-lansweeper-sauvegarde-maintenance.md) | | | | |
| P1 | [VM Windows Server Lansweeper Installer Serveur](../../01-fiches-simples/windows/toutes-versions/vie-du-logiciel/lansweeper/fiche-simple-vm-windows-server-lansweeper-installer-serveur.md) | | | | |

## 7. Critères de sortie

- 100 % des fiches P0 d'un OS en `OK` ou `OK avec écarts` (corrigés) avant de déclarer cet OS utilisable en production.
- 100 % des fiches Sauvegarde et Restauration d'un logiciel en `OK` avant sa mise en production.
- Aucune fiche `KO` ouverte sur le périmètre déployé.
- Chaque écart corrigé est rejoué depuis un snapshot propre.
- Après les corrections, relancer `verify-wiki.py` puis régénérer les exports Wiki.js.

_Volumétrie : 391 lignes P0 et 513 lignes P1._
