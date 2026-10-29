# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Prouver que la sauvegarde restaure.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer dans un dossier isolé (exemple Borg) :
   ```bash
   mkdir -p /srv/restore-test && cd /srv/restore-test
   borg list
   borg extract ::NOM_ARCHIVE etc/hostname
   ```
   👉 Explication : remplacer `NOM_ARCHIVE`; extrait un fichier de contrôle.

2. Comparer :
   ```bash
   diff /srv/restore-test/etc/hostname /etc/hostname && echo IDENTIQUE
   ```
   👉 Explication : confirme l'intégrité des données.

## 2. Production — Contrôles

Restaurer en VM isolée pour un test complet; ne pas réintroduire sur le réseau de production.

## 3. Production — Sécurité

Supprimer les données restaurées après le test.

## Validation et retour arrière

- **Validation** : Procédure de restauration chronométrée et consignée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)