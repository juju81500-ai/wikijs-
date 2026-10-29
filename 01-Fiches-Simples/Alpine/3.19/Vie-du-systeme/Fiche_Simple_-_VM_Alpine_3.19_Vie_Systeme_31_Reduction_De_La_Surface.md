# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Retirer ce qui n'est pas nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services actifs et les ports ouverts :
   ```sh
   rc-status
   ss -tulpn
   ```
   👉 Explication : identifie chaque service en écoute.

2. Retirer du démarrage un service inutile (remplacer `SERVICE`) :
   ```sh
   doas rc-service SERVICE stop
   doas rc-update del SERVICE default
   ```
   👉 Explication : arrête et retire le service de l'ordre de démarrage.

3. Supprimer un paquet inutile :
   ```sh
   doas apk del PAQUET
   apk list --installed | wc -l
   ```
   👉 Explication : supprime le paquet et ses dépendances orphelines.

## 2. Production — Contrôles

Documenter les services conservés et leur raison.

## 3. Production — Sécurité

Chaque port ouvert doit être justifié et filtré.

## Validation et retour arrière

- **Validation** : `ss -tulpn` ne montre que les ports attendus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](<../Vie-du-logiciel/OpenSSH/Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
