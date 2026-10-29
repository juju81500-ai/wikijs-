# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Diagnostic_Journalctl_Erreurs

- **Environnement** : VM ou serveur Ubuntu en incident ou après une mise à jour
- **OS / Version** : Ubuntu Server 26.04 LTS (systemd 259)
- **Catégorie** : Diagnostic / Journaux systemd et noyau
- **Tags** : `ubuntu2604`, `journalctl`, `dmesg`, `systemd`, `diagnostic`, `erreurs`

---

## 🎯 Problème précis à résoudre

Identifier rapidement les erreurs critiques d'un serveur Ubuntu 26.04 (services en échec, erreurs du noyau, erreurs de disque) à partir du journal systemd et des messages du noyau, avant de corriger la cause.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Lister les unités en échec :
```bash
systemctl --failed --no-pager
```
👉 Explication : Donne le point de départ : chaque unité listée a échoué ou a atteint sa limite de redémarrage.

2. Afficher les erreurs du démarrage courant :
```bash
sudo journalctl -p err -b --no-pager
```
👉 Explication : `-p err` ne garde que les niveaux `err` et plus graves ; `-b` limite la recherche au démarrage en cours.

3. Analyser un service précis :
```bash
sudo journalctl -u <nom_du_service> -n 200 --no-pager
```
👉 Explication : Affiche les 200 dernières entrées du service. Remplacer `<nom_du_service>` par l'unité en échec (sans le suffixe `.service`).

## ⚡ 2. Production — Façon Simplifiée

1. Consulter le démarrage précédent après un redémarrage imprévu :
```bash
sudo journalctl --list-boots
sudo journalctl -b -1 -p err --no-pager
```
👉 Explication : `--list-boots` liste les démarrages enregistrés. `-b -1` cible le démarrage précédent, utile pour expliquer une coupure. Si la liste ne montre qu'un démarrage, le journal n'est pas persistant (voir la fiche journald).

2. Lire les erreurs du noyau :
```bash
sudo dmesg --level=err,crit,alert,emerg --ctime
```
👉 Explication : Affiche les erreurs matérielles et pilotes avec une date lisible. Une erreur de disque (`I/O error`, `ata`, `nvme`) prime sur les autres causes.

3. Mesurer le temps de démarrage par unité :
```bash
systemd-analyze blame | head -n 15
```
👉 Explication : Montre les unités les plus lentes ; un service bloqué au démarrage ralentit toute la séquence.

## 🔒 3. Production — Façon Sécurisée

1. Filtrer les événements de sécurité liés à l'authentification :
```bash
sudo journalctl _COMM=sshd --since "1 hour ago" --no-pager
```
👉 Explication : Montre les connexions et échecs SSH de l'heure écoulée. Des échecs répétés depuis une même IP justifient la vérification de Fail2ban.

2. Vérifier l'intégrité des journaux persistants :
```bash
sudo journalctl --verify
```
👉 Explication : Contrôle la cohérence des fichiers journal. Une erreur peut signaler une altération ou un disque défaillant ; à escalader avant toute correction.

3. Exporter le diagnostic pour analyse ou dossier d'incident :
```bash
sudo journalctl -b -p warning --no-pager > /tmp/diagnostic-$(hostname)-$(date +%F).log
```
👉 Explication : Conserve une copie horodatée du diagnostic, sans modifier le journal source. Déplacer ensuite le fichier hors du serveur.

## ✅ Validation et retour arrière

- **Précontrôles** : heure de l'incident notée, accès en lecture aux journaux (`sudo`), espace disque libre pour l'export.
- **Validation** : la cause est identifiée (unité, message précis) ; `systemctl --failed` ne liste plus l'unité après correction ; `journalctl -p err -b` ne répète plus l'erreur.
- **Retour arrière** : cette fiche est en lecture seule. Les corrections appliquées après diagnostic doivent suivre leur propre fiche avec retour arrière.
