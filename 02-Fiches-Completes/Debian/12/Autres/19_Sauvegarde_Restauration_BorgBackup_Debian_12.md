# Sauvegarde et restauration BorgBackup sur Debian 12

- **Type de fiche** : Autres — sauvegarde / reprise
- **Environnement** : VM ou serveur Debian 12 Bookworm, dépôt Borg distant ou disque dédié
- **OS / Version** : Debian 12 (Bookworm) avec BorgBackup
- **Rôle** : Sauvegarder configurations/données et tester une restauration isolée
- **Tags** : `debian12`, `bookworm`, `borgbackup`, `sauvegarde`, `restauration`, `chiffrement`

## 1. Concevoir la sauvegarde

Fiche simple : [cadrer le besoin Borg](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Cadrer_Besoin.md).

Définir les données, fréquence, rétention, RPO/RTO, destination indépendante et accès aux clés. Pour les bases actives, compléter l'archive fichier par un dump ou une méthode cohérente au moteur; une copie des fichiers de base en cours d'écriture n'est pas forcément restaurable.

## 2. Installer Borg et préparer un dépôt

Fiche simple : [installer Borg et initialiser le dépôt](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Installer_Initialiser.md).

```bash
sudo apt update
sudo apt install borgbackup
borg --version
```

Créer le compte dédié et préparer la destination selon le modèle d'accès choisi (SSH vers un dépôt distant ou volume monté réservé aux sauvegardes). Garder la clé et la phrase de passe hors du serveur protégé.

Initialiser une seule fois un dépôt chiffré, sur la destination réelle :

```bash
borg init --encryption=repokey-blake2 <DEPOT_BORG>
```

Conserver l'empreinte du dépôt et exporter la clé avec protection stricte; une clé perdue rend les archives chiffrées irrécupérables.

## 3. Créer une archive cohérente

Fiche simple : [créer une archive cohérente](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Creer_Archive.md).

Avant la première archive de production, valider chemins, exclusions et système de fichiers monté :

```bash
findmnt
sudo borg create --stats --progress --compression zstd,3 \
  <DEPOT_BORG>::'{hostname}-{now:%Y-%m-%d_%H:%M}' \
  /etc /home /var/www
sudo borg list <DEPOT_BORG>
```

Adapter les chemins au serveur; exclure caches/répertoires temporaires seulement après revue. Utiliser un fichier de configuration/environnement lisible par le compte de sauvegarde, sans placer le secret dans la ligne de commande.

## 4. Automatiser et conserver

Fiche simple : [automatiser et appliquer la rétention](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Automatiser_Retention.md).

Planifier une unité/timer systemd ou un ordonnanceur sous compte dédié. Vérifier code retour, logs, espace dépôt et alertes. Simuler la rétention avant suppression :

```bash
sudo borg prune --dry-run --list --keep-daily=7 --keep-weekly=4 --keep-monthly=12 <DEPOT_BORG>
```

Retirer `--dry-run` uniquement après validation des archives conservées/supprimées et présence d'une copie indépendante.

## 5. Restaurer un fichier ou un service

Fiche simple : [restaurer en isolation](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Restaurer_Isoler.md).

Lister puis extraire dans un répertoire temporaire, sans écraser la production :

```bash
borg list <DEPOT_BORG>
mkdir -p /tmp/borg-restore-test
cd /tmp/borg-restore-test
borg extract <DEPOT_BORG>::<NOM_ARCHIVE> etc/ssh/sshd_config
```

Comparer le fichier, ses permissions et son propriétaire; pour un service complet, restaurer sur VM isolée, remettre les données, puis tester le démarrage et le parcours métier.

## 6. Sécuriser et vérifier

Fiche simple : [sécuriser et vérifier le dépôt](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Securiser_Verifier.md).

- Protéger dépôt, accès SSH et clé de chiffrement indépendamment du serveur.
- Exécuter `borg check` selon une fréquence planifiée, en surveillant l'impact I/O.
- Conserver une copie hors site/hors ligne; la déduplication n'est ni une réplication ni une sauvegarde indépendante.
- Tester régulièrement une restauration complète et consigner sa durée réelle.

## 7. Retour arrière et dépannage

Fiche simple : [dépanner et préparer le retour arrière](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/BorgBackup/Fiche_Simple_-_VM_Debian_12_Borg_Depanner_Retour_Arriere.md).

En cas d'erreur, ne pas lancer `prune` ni `delete` avant inventaire. Conserver les archives et la clé, vérifier accès, espace et logs, puis restaurer vers une destination de test. Pour annuler une unité/timer, la désactiver et conserver les anciens scripts jusqu'à validation de la nouvelle méthode.

## Sources

- [BorgBackup — documentation](https://borgbackup.readthedocs.io/en/stable/)
- [Debian 12 — notes de version](https://www.debian.org/releases/bookworm/)