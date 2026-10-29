# Fiche_Simple_-_VM_Debian_12_Borg_Restaurer_Isoler.md

- **Environnement** : Debian 12; dépôt Borg accessible et zone temporaire de restauration
- **OS / Version** : Debian 12 Bookworm
- **Catégorie** : sauvegarde / restauration Borg
- **Tags** : `debian12`, `borgbackup`, `restore`, `isolation`, `validation`

---

## Problème précis à résoudre

Restaurer un fichier ou un service sans écraser la production et prouver que les données récupérées sont utilisables.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les archives :
   ```bash
   borg list "$REPO"
   ```
   👉 Explication : repérer le nom de l'archive à restaurer.

2. Extraire dans un répertoire temporaire :
   ```bash
   mkdir -p /tmp/borg-restore-test
   cd /tmp/borg-restore-test
   borg extract "$REPO::NOM_ARCHIVE" etc/ssh/sshd_config
   ```
   👉 Explication : remplacer `NOM_ARCHIVE`; les chemins sont relatifs, la production n'est pas écrasée.

3. Comparer :
   ```bash
   ls -l etc/ssh/sshd_config
   diff etc/ssh/sshd_config /etc/ssh/sshd_config && echo "identique"
   ```
   👉 Explication : contrôler contenu, permissions et propriétaire.

4. Pour un service complet : restaurer sur une VM isolée, remettre les données (dump compris), démarrer et tester le parcours métier.
   👉 Explication : un fichier restauré n'est pas un service restauré.

## 2. Production — Contrôles

Faire approuver archive, chemins de restauration, responsable métier, fenêtre, RPO/RTO et vérification après reprise.

## 3. Production — Sécurité

- Ne jamais extraire directement sur les données actives pendant un test.
- Vérifier soigneusement l'archive et les chemins de destination.
- Protéger les données restaurées selon leur classification.
- Ne pas divulguer secret de dépôt ou phrase de passe dans les commandes journalisées.

## Validation et retour arrière

- **Validation** : fichiers vérifiés et service restauré en isolation fonctionnel.
- **Retour arrière** : conserver l'original; supprimer uniquement les données d'essai après confirmation du chemin.

## Si le problème n'est pas résolu

- [BorgBackup — extraire une archive](https://borgbackup.readthedocs.io/en/stable/usage/extract.html)
- [BorgBackup — documentation](https://borgbackup.readthedocs.io/en/stable/)
- [Guide complet BorgBackup Debian 12](../../../../../02-Fiches-Completes/Debian/12/Autres/19_Sauvegarde_Restauration_BorgBackup_Debian_12.md)
