# Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Acces_Minimaux.md

- **Environnement** : Poste Debian 13 avec GNS3 installé
- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Catégorie** : simulation reseau / droits

---

## Problème précis à résoudre

Donner à un compte nominatif seulement les groupes nécessaires.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'existence des groupes :
   ```bash
   getent group ubridge libvirt kvm
   ```
   👉 Explication : les trois groupes doivent exister.

2. Ajouter le compte courant :
   ```bash
   sudo usermod -aG ubridge,libvirt,kvm "$USER"
   ```
   👉 Explication : ces groupes permettent interfaces virtuelles, libvirt et KVM.

3. Fermer puis rouvrir la session, puis vérifier :
   ```bash
   id
   ```
   👉 Explication : les groupes ajoutés doivent apparaître.

## 2. Production — Contrôles

Utiliser un compte nominatif de laboratoire et revoir régulièrement les membres des groupes.

## 3. Production — Sécurité

- Ne pas ajouter au groupe `docker` (équivalent à un contrôle privilégié de l'hôte).
- N'ajouter `wireshark` que pour une capture autorisée.

## Validation et retour arrière

- **Validation** : `id` montre ubridge, libvirt et kvm.
- **Retour arrière** : `sudo gpasswd -d "$USER" libvirt` (idem pour `kvm` et `ubridge`), puis rouvrir la session.

## Si le problème n'est pas résolu

- [GNS3 — installation Linux](https://docs.gns3.com/docs/getting-started/installation/linux)
- [Debian — groupes libvirt](https://wiki.debian.org/KVM)
- [Guide complet GNS3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13#4-accorder-les-acces-minimaux-necessaires)