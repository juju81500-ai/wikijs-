# Rapport de test réel — Debian 12 en laboratoire

- **Date** : 31 octobre 2026
- **Tags** : `test-reel`, `debian-12`, `laboratoire`, `qualite`
- **Périmètre** : fiches P0 Debian 12 listées ci-dessous uniquement ; ce rapport ne valide pas les autres fiches ni les autres OS.
- **Cible** : clone complet de laboratoire Debian 12, VM 124. Le test réseau est passé temporairement de `vmbr1`/DHCP à `vmbr0`/IP statique après autorisation explicite ; le modèle d'origine et les systèmes de production n'ont pas été modifiés.
- **Protection** : le snapshot `before-step16-vmbr0` a été restauré à la fin ; la VM courante est revenue sur `vmbr1`, DHCP `10.50.1.7/24`, SSH et QEMU Guest Agent actifs. Les snapshots de recette restent disponibles dans Proxmox.

## Résultats

| Étape | Fiche | Verdict | Résultat observé |
|---|---|---|---|
| 13 | [Partitionnement et systèmes de fichiers](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_13_Partitionnement_Et_Systemes_De.md) | OK avec écarts | `lsblk` et `df -hT` ont fonctionné. `vgs` et `lvs` ne sont pas installés et le clone n'a pas de volume LVM ; leur partie est non applicable. |
| 16 | [Adressage IP fixe](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif.md) | OK avec écarts | La fiche a été complétée avec une variante Netplan. Après confirmation de réservation de l'adresse et autorisation du bridge `vmbr0` avec NAT sortant, `netplan generate` a réussi ; au démarrage et après redémarrage, `ens18` a pris `10.40.1.88/16`, la route par défaut `10.40.0.1`, et la résolution de `deb.debian.org` ainsi qu'une requête HTTPS ont réussi. `netplan try` et la variante ifupdown n'ont pas été exécutés. |
| 26 | [Authentification SSH par clés](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_26_Authentification_Par_Cles_Ssh.md) | OK avec écarts | La connexion par clé du compte de test `admin01` a réussi. Le compte et la clé avaient été préparés hors de la procédure de copie de la fiche ; la commande de déploiement de clé elle-même n'est donc pas certifiée. |
| 27 | [Durcissement de l'accès SSH](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_27_Durcissement_De_L_Acces.md) | OK | `sshd -t` a validé la configuration. `sshd -T` a confirmé `permitrootlogin no`, `passwordauthentication no` et `maxauthtries 3`. La connexion par clé d'`admin01` restait fonctionnelle et l'accès root était refusé comme attendu. Le snapshot a ensuite été restauré. |
| 29 | [Pare-feu hôte](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_29_Pare_Feu_Hote.md) | OK avec écarts | nftables 1.0.6 a validé puis appliqué la politique approuvée : entrée bloquée par défaut, SSH depuis `10.40.0.1` uniquement, connexions établies, ICMP limité, journaux de refus limités, sorties autorisées. SSH est resté accessible ; une sonde TCP/8080 a été bloquée et le compteur de refus a augmenté. Le service est resté actif après redémarrage. Cette règle de laboratoire ne vaut pas politique de production. |
| 40 | [Configuration des sauvegardes](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_40_Configuration_Des_Sauvegardes.md) | OK avec écarts | Après autorisation du NAT de laboratoire, Borg 1.2.4 et rclone 1.60.1 ont été installés. Une archive Borg chiffrée locale de `/etc` et `/srv` a été créée et vérifiée avec `borg check --verify-data`. Le mode `rclone --dry-run` a confirmé qu'un fichier de test ne serait pas copié. Aucun dépôt distant rclone n'était configuré : le transfert hors site reste non testé. |
| 46 | [Test de persistance après redémarrage](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_46_Test_De_Persistance_Au.md) | OK | Le test initial sur DHCP a réussi. Après passage autorisé à l'IP statique, deux redémarrages ont confirmé `10.40.1.88/16`, la route `10.40.0.1`, SSH actif et, au second, nftables actif au démarrage. `findmnt --verify` n'a signalé aucune erreur ; aucun service n'était en échec. |
| 48 | [Test de restauration PRA](../../01-Fiches-Simples/Debian/12/Vie-du-systeme/Fiche_Simple_-_VM_Debian_12_Vie_Systeme_48_Test_De_Restauration_Pra.md) | OK | L'archive locale a été extraite dans `/srv/restore-test`. `diff` a confirmé que `etc/hostname` restauré était identique au fichier source. |

## Limites et suite nécessaire

- La copie rclone vers un dépôt distant reste non testée faute de remote configuré ; le test a utilisé un chemin local uniquement avec `--dry-run`.
- Le clone a été connecté uniquement au bridge de laboratoire `vmbr0` avec le NAT sortant explicitement autorisé ; ne pas le basculer vers un bridge non validé.
- Les étapes 13, 26, 27 et 46 ne sont validées que pour ce clone et les commandes consignées, pas pour toutes les variantes Debian ni pour l'ensemble du catalogue.
- Les statuts correspondants sont également inscrits dans la [liste de contrôle stricte](Liste_Controle_Tests_Fiches_Simples.md).
- Le contrôle distinct `verify_command_import.py` reste en échec : `TXT.txt` se termine au milieu du champ `command` de `cmd-344` (ligne 6289). Aucun contenu manquant n'a été reconstitué ; le fichier source doit être récupéré depuis une copie fiable avant de relancer ce contrôle.
