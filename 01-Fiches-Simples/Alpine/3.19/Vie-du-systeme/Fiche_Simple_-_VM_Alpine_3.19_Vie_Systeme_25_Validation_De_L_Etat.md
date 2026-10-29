# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-25`

---

## Problème précis à résoudre

Photographier l'état de référence avant la mise en production.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version et les paquets :
   ```sh
   cat /etc/alpine-release
   uname -a
   apk info -v | sort > /root/baseline-paquets.txt
   wc -l /root/baseline-paquets.txt
   ```
   👉 Explication : enregistre la version d'Alpine, le noyau et la liste des paquets installés.

2. Relever services, ports et disques :
   ```sh
   rc-status -a
   ss -tulpn
   df -hT
   ```
   👉 Explication : documente les services actifs, les ports en écoute et l'occupation.

3. Lister les fichiers de configuration modifiés (référence pour les audits) :
   ```sh
   apk audit --system | head -30
   ```
   👉 Explication : montre les fichiers modifiés par rapport aux paquets; en mode diskless ou data, finir par `doas lbu commit`.

## 2. Production — Contrôles

Archiver la baseline avec la fiche de la machine.

## 3. Production — Sécurité

Aucun mot de passe ne figure dans les fichiers de baseline.

## Validation et retour arrière

- **Validation** : Baseline archivée et relue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
