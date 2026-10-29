# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-01`

---

## Problème précis à résoudre

Dimensionner la machine avant de la créer.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources de la machine cible ou d'une machine comparable :
   ```sh
   nproc
   free -m
   lsblk -o NAME,SIZE,TYPE
   uname -m
   ```
   👉 Explication : nombre de vCPU, RAM en Mo, disques et architecture (`x86_64` ou `aarch64`) pour comparer au besoin.

2. Mesurer les entrées/sorties d'une machine comparable (sur Alpine) :
   ```sh
   doas apk add sysstat
   iostat -x 1 5
   ```
   👉 Explication : `%util` et `await` élevés indiquent un stockage à surdimensionner.

3. Noter vCPU, RAM, disque, IOPS, réseau et architecture dans le dossier du projet.
   👉 Explication : Alpine tient dans 512 Mo de RAM et 1 Go de disque pour un serveur minimal; ajouter la charge du service prévu (nginx, base de données, etc.).

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge, valider le dimensionnement avec le propriétaire du service.

## 3. Production — Sécurité

Prévoir un volume séparé pour `/var` ou les données si le service écrit beaucoup.

## Validation et retour arrière

- **Validation** : Tableau de sizing signé et conservé avec le dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
