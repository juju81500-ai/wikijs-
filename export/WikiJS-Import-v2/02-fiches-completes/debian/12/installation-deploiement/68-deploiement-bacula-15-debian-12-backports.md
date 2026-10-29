---
title: "Déployer Bacula Community 15.0.3 sur Debian 12"
description: "Fiche simple : [cadrer le périmètre Bacula](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Bacula/FicheSimple-VMDebian12BaculaCadrerPerimetre.md)."
published: true
date: 2026-10-29T19:55:10Z
tags: ["bacula", "debian12", "backports", "postgresql", "backup", "restore"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Déployer Bacula Community 15.0.3 sur Debian 12

- **OS / Version** : Debian 12 Bookworm, paquets Debian Backports `15.0.3-3~bpo12+1`
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Director, Storage Daemon, File Daemon et catalogue PostgreSQL sur un serveur de laboratoire
- **Catégorie** : Sauvegarde réseau et restauration granulaire
- **Tags** : `bacula`, `debian12`, `backports`, `postgresql`, `backup`, `restore`

## 1. Périmètre et architecture

Fiche simple : [cadrer le périmètre Bacula](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-cadrer-perimetre).

Bacula sépare le Director (planification et catalogue), le Storage Daemon (volumes), et un File Daemon par machine sauvegardée. PostgreSQL héberge le catalogue qui indexe jobs, fichiers et volumes; il ne contient pas les données de sauvegarde elles-mêmes.

Cette procédure vise un laboratoire à serveur unique Debian 12 avec stockage disque et un jeu de fichiers fictifs. Bacula Community 15.0.3 est disponible dans les backports Debian Bookworm; les paquets Bookworm standard sont d'une génération antérieure. Le guide ne vise ni Debian 13, ni une architecture de production, ni les paquets upstream Bacula qui nécessitent une inscription et une clé d'accès.

En production, séparer les rôles selon les besoins, protéger le stockage contre l'effacement ou le chiffrement depuis le serveur sauvegardé, conserver une copie hors site, définir RPO/RTO et éprouver les restaurations. Une copie de volumes sur le même serveur n'est pas une stratégie de reprise.

## 2. Préparer Debian 12 et vérifier la version

Fiche simple : [préparer Debian 12 et vérifier la version](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-preparer-debian12-version).

Configurer le dépôt officiel `bookworm-backports` selon la documentation Debian, puis contrôler la version candidate avant toute installation :

```bash
sudo apt update
apt-cache policy bacula-director-pgsql bacula-sd bacula-client bacula-console
```

Le candidat doit provenir de Bookworm Backports et correspondre à Bacula 15.0.3 (`15.0.3-3~bpo12+1` pour la révision référencée ici). Si ce n'est pas le cas, arrêter et revoir les sources APT au lieu de mélanger les versions.

Installer explicitement les composants du serveur et PostgreSQL :

```bash
sudo apt install -t bookworm-backports postgresql bacula-director-pgsql bacula-sd bacula-client bacula-console
```

Lors des questions d'installation, choisir le catalogue PostgreSQL et conserver la configuration générée par les paquets. Ne pas remplacer les fichiers `.conf` par des exemples provenant d'une autre distribution. Confirmer ensuite les paquets et versions installés :

```bash
dpkg-query -W 'bacula*' postgresql
systemctl --no-pager status postgresql
```

Si l'assistant n'a pas initialisé le catalogue, suivre la documentation du paquet Bacula Debian pour créer les tables et le compte PostgreSQL; ne pas lancer des scripts de schéma tirés d'une version différente.

## 3. Examiner les ressources et le stockage

Fiche simple : [examiner les ressources et le stockage](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-examiner-ressources-stockage).

Les configurations sont généralement sous `/etc/bacula/`. Examiner les directives `@` du fichier Director pour identifier les fragments inclus, puis les ressources déjà définies dans le Director, le Storage Daemon et le File Daemon :

```bash
grep -n '^[[:space:]]*@' /etc/bacula/bacula-dir.conf
grep -nE '^[[:space:]]*(Name|Address|Device|Archive Device|Pool|FileSet|Storage)[[:space:]]*=' /etc/bacula/bacula-dir.conf /etc/bacula/bacula-sd.conf /etc/bacula/bacula-fd.conf
```

Repérer les noms exacts du Director, du client local, du Storage, du Device, du Pool et du FileSet. Ce sont des ressources liées entre fichiers; leurs noms et mots de passe doivent correspondre. Ne pas copier les secrets dans un ticket, un dépôt Git ou cette fiche.

Confirmer que le `Archive Device` du Storage Daemon pointe vers un répertoire disque existant, accessible en écriture au compte réel du service et disposant d'assez d'espace. Pour les essais seulement, le stockage fourni par le paquet peut convenir. En exploitation, préférer un volume séparé, surveillé et protégé contre l'accès depuis les clients.

## 4. Ajouter un job pilote manuel

Fiche simple : [ajouter un job pilote manuel](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-ajouter-job-pilote).

Créer un répertoire et un fichier de test non sensibles sur le client :

```bash
sudo install -d -m 0750 /var/tmp/bacula-pilote
printf 'Bacula restore validation\n' | sudo tee /var/tmp/bacula-pilote/controle.txt
sudo sha256sum /var/tmp/bacula-pilote/controle.txt
```

Dans un fichier de ressources Director déjà inclus, ajouter un FileSet dédié et un Job sans `Schedule` afin qu'il ne démarre que manuellement. Remplacer les valeurs entre chevrons par les noms réellement définis dans les fichiers installés; ne pas conserver les chevrons dans la configuration :

```text
FileSet {
  Name = "FichiersPilote"
  Include {
    Options {
      signature = SHA256
      aclsupport = yes
      xattrsupport = yes
    }
    File = "/var/tmp/bacula-pilote"
  }
}

Job {
  Name = "BackupPilote"
  Type = Backup
  Level = Full
  Client = "<client-fd-existant>"
  FileSet = "FichiersPilote"
  Storage = "<storage-existant>"
  Pool = "<pool-existant>"
  Messages = Standard
}
```

Si le nom du message standard diffère, reprendre le nom défini dans la configuration. Sauvegarder une copie des fichiers modifiés et leurs permissions avant de poursuivre.

## 5. Valider la configuration et démarrer les services

Fiche simple : [valider la configuration et démarrer les services](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-valider-config-demarrer).

Tester chaque configuration avec le binaire correspondant avant tout redémarrage :

```bash
sudo bacula-dir -t
sudo bacula-sd -t
sudo bacula-fd -t
```

Ne pas continuer si une commande signale une ressource absente, un secret incohérent, un fichier inaccessible ou une erreur de syntaxe. Repérer les unités réellement installées, puis activer celles du Director, du Storage Daemon et du File Daemon :

```bash
systemctl list-unit-files 'bacula*'
```

Sur les paquets Debian, les unités sont habituellement `bacula-director`, `bacula-sd` et `bacula-fd`; confirmer leurs noms avant d'exécuter :

```bash
sudo systemctl enable --now bacula-director.service bacula-sd.service bacula-fd.service
sudo systemctl --no-pager --full status bacula-director.service bacula-sd.service bacula-fd.service
```

Si les unités portent d'autres noms sur le système, employer ceux trouvés à l'étape précédente. Contrôler aussi les journaux systemd. Limiter le pare-feu aux flux requis entre les composants : console vers Director (TCP 9101 par défaut), Director vers File Daemon (9102) et Director/File Daemon vers Storage Daemon (9103). Ne jamais exposer ces ports à Internet.

## 6. Exécuter le job et étiqueter un volume

Fiche simple : [exécuter le job et étiqueter un volume](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-executer-job-etiqueter-volume).

Ouvrir la console et contrôler l'état des composants :

```bash
sudo bconsole
```

Dans `bconsole`, utiliser `status dir`, `status client` et `status storage`. Lancer ensuite `run` et sélectionner `BackupPilote`. Vérifier le client, le FileSet, le Storage, le Pool et le niveau `Full` avant de confirmer.

Si le Pool ne contient aucun volume inscriptible, utiliser la commande interactive `label` et créer un nom de volume unique dans le Pool et le Storage attendus. Ne pas relabeler ou purger un volume existant pour débloquer un essai. Après le job, relever son JobId, son statut, le nombre de fichiers, les erreurs, le volume utilisé et les messages du Director/Storage/File Daemon. Le résultat attendu est `Backup OK` avec un seul fichier pilote.

## 7. Prouver la restauration

Fiche simple : [prouver la restauration](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-prouver-restauration).

Dans `bconsole`, lancer `restore`, sélectionner le client et le JobId du pilote, puis marquer uniquement `controle.txt`. Avant de démarrer, vérifier le Storage, le client cible et le champ `Where`. Utiliser le répertoire temporaire prévu par le modèle `RestoreFiles` (souvent `/tmp/bacula-restores`) ou définir un autre emplacement isolé. Ne jamais choisir `/` ou un répertoire de données actif pour ce premier test.

Après la fin du job Restore, trouver le fichier restauré, comparer son SHA-256 à la valeur relevée avant la sauvegarde, puis vérifier propriétaire et permissions. Consigner le JobId et le résultat. Ne supprimer que les données de test du répertoire temporaire après contrôle.

Un job de sauvegarde `OK` ne prouve pas qu'une restauration est possible. Répéter périodiquement les tests depuis des volumes réellement conservés et tester séparément la restauration du catalogue et du bootstrap.

## 8. Secrets, TLS et exploitation

Fiche simple : [secrets, TLS et exploitation](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-secrets-tls-exploitation).

- Utiliser des mots de passe aléatoires, uniques par relation Director/Storage/File Daemon et protégés dans les configurations avec les permissions minimales nécessaires.
- Configurer TLS et exiger le chiffrement de bout en bout entre les composants, en vérifiant les certificats et noms d'hôtes. La documentation Bacula 15 indique qu'une authentification TLS seule (`TLS Authenticate = yes`) désactive ensuite le chiffrement du flux; ne pas confondre authentification et chiffrement.
- Restreindre les accès à `bconsole`, au catalogue PostgreSQL, aux volumes, aux configurations et aux clés privées.
- Vérifier que le job de sauvegarde du catalogue est planifié après les autres jobs; protéger ses exports, les fichiers bootstrap, les configurations et les certificats sur une cible indépendante.
- Définir les rétentions Fichiers, Jobs et Volumes après calcul de capacité. Le pruning du catalogue supprime des index, pas les volumes; le recyclage d'un volume réutilise ses données et doit respecter la politique de rétention.
- Surveiller les jobs en erreur, l'espace disque, la croissance PostgreSQL, l'âge des volumes, les certificats et les sauvegardes hors site. Tester les mises à niveau en laboratoire avant de les appliquer.

## Sources

- [Bacula Community 15.0.3 — annonce de version et plateformes binaires](https://www.bacula.org/bacula-community-15-0-3-released/)
- [Bacula Community — paquets binaires, accès et limites de support](https://www.bacula.org/bacula-binary-package-download/)
- [Debian Backports — manpage bacula-dir 15.0.3](https://manpages.debian.org/bookworm-backports/bacula-director/bacula-dir.8.en.html)
- [Debian Backports — manpage bacula-sd 15.0.3](https://manpages.debian.org/bookworm-backports/bacula-sd/bacula-sd.8.en.html)
- [Debian Backports — manpage bacula-fd 15.0.3](https://manpages.debian.org/bookworm-backports/bacula-fd/bacula-fd.8.en.html)
- [Bacula 15.0.x — configuration du Director](https://www.bacula.org/15.0.x-manuals/en/main/Configuring_Director.html)
- [Bacula 15.0.x — chiffrement TLS](https://www.bacula.org/15.0.x-manuals/en/main/Bacula_TLS_Communications_E.html)
- [Bacula 15.0.x — maintenance et sauvegarde du catalogue](https://www.bacula.org/15.0.x-manuals/en/main/Catalog_Maintenance.html)

Les chapitres de configuration/TLS/catalogue sont publiés dans le manuel Bacula 15.0.x de Bacula Systems; vérifier les particularités de la Community et de l'intégration Debian avant production. Aucun déploiement ni test de restauration réel n'est consigné par cette fiche.