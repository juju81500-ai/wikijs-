# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Nommer la machine de façon unique et cohérente.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le nom court (remplacer `NOM_MACHINE`, par exemple `srv-alp01`) :
   ```sh
   setup-hostname NOM_MACHINE
   hostname
   ```
   👉 Explication : écrit `/etc/hostname` et applique le nom immédiatement.

2. Associer le nom court au FQDN dans `/etc/hosts` (remplacer `ADRESSE_IP`, `NOM_MACHINE`, `DOMAINE`) :
   ```sh
   doas sh -c 'cat >> /etc/hosts <<EOF
   ADRESSE_IP NOM_MACHINE.DOMAINE NOM_MACHINE
   EOF'
   hostname -f
   ```
   👉 Explication : l'adresse de la machine est résolue localement, même sans DNS.

3. Redémarrer le service pour que le nom soit relu :
   ```sh
   doas rc-service hostname restart
   ```
   👉 Explication : applique le contenu de `/etc/hostname` sans redémarrer la machine.

## 2. Production — Contrôles

Appliquer la convention de nommage de l'entreprise.

## 3. Production — Sécurité

Ne pas laisser un nom par défaut (`localhost`) : il complique la supervision et les certificats.

## Validation et retour arrière

- **Validation** : `hostname` et `hostname -f` retournent les valeurs attendues.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)