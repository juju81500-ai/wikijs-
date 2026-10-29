# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

S'assurer que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la somme de contrôle :
   ```bash
   cd ~/iso
   sha256sum -c SHA256SUMS --ignore-missing
   ```
   👉 Explication : doit afficher `OK` pour l'ISO téléchargée.

2. Importer les clés de signature des images Ubuntu puis vérifier la signature (comparer les empreintes avec https://ubuntu.com/tutorials/how-to-verify-ubuntu) :
   ```bash
   sudo apt install gnupg
   gpg --keyid-format long --keyserver hkps://keyserver.ubuntu.com --recv-keys 0x46181433FBB75451 0xD94AA3F0EFE21092
   gpg --keyid-format long --verify SHA256SUMS.gpg SHA256SUMS
   ```
   👉 Explication : confirme que `SHA256SUMS` est signé par la clé « Ubuntu CD Image Automatic Signing Key »; contrôler l'identifiant des clés sur la page officielle.

## 2. Production — Contrôles

Consigner la date, l'empreinte de clé et le résultat dans le dossier.

## 3. Production — Sécurité

Si la vérification échoue, supprimer l'image et la retélécharger.

## Validation et retour arrière

- **Validation** : `OK` pour `sha256sum` et `Good signature` pour `gpg`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)