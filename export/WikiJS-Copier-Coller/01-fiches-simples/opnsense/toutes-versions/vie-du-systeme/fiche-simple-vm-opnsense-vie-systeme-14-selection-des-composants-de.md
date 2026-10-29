# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer uniquement ce qui est nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'installation (login `installer`, mot de passe `opnsense`) et valider la copie des fichiers sans option supplémentaire.
   👉 Explication : le système de base d'OPNsense est installé en une fois, sans choix de paquets.

2. Ajouter ensuite uniquement les plugins utiles dans Système > Micrologiciel > Plugins (ex. `os-qemu-guest-agent`). En shell :
   ```sh
   pkg info | grep -c .
   pkg info | grep '^os-'
   ```
   👉 Explication : compte les paquets et liste les plugins `os-*` installés.

## 2. Production — Contrôles

Tenir la liste des plugins autorisés et la déclarer à la CMDB.

## 3. Production — Sécurité

Chaque plugin ajoute de la surface d'attaque; ne pas installer de plugin non justifié.

## Validation et retour arrière

- **Validation** : La liste des plugins correspond au besoin.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)