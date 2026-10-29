# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Prouver que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Comparer l'empreinte SHA-256 :
   ```sh
   sha256sum -c alpine-virt-3.19.PATCH-x86_64.iso.sha256
   ```
   👉 Explication : doit afficher `alpine-virt-3.19.PATCH-x86_64.iso: OK`.

2. Importer la clé publique de signature publiée par le projet :
   ```sh
   curl -LO https://alpinelinux.org/keys/ncopa.asc
   gpg --import ncopa.asc
   gpg --fingerprint | grep -i -B1 -A1 ncopa
   ```
   👉 Explication : charge la clé; comparer l'empreinte affichée avec celle de la page officielle https://alpinelinux.org/downloads/ (autre canal que le téléchargement).

3. Vérifier la signature de l'ISO :
   ```sh
   gpg --verify alpine-virt-3.19.PATCH-x86_64.iso.asc alpine-virt-3.19.PATCH-x86_64.iso
   ```
   👉 Explication : `Good signature` prouve l'authenticité; l'avertissement « clé non certifiée » est normal tant que l'empreinte n'est pas validée manuellement.

## 2. Production — Contrôles

Conserver la preuve de vérification avec l'image archivée.

## 3. Production — Sécurité

Une empreinte qui ne correspond pas impose de supprimer l'ISO et de la retélécharger.

## Validation et retour arrière

- **Validation** : `OK` pour le SHA-256 et `Good signature` pour GPG.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)