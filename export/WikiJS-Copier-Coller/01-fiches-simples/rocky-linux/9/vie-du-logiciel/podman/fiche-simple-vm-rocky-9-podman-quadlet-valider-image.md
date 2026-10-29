# Fiche_Simple_-_VM_Rocky_9_Podman_Quadlet_Valider_Image.md

- **Environnement** : VM Rocky Linux 9 avec Podman rootless, systemd et Quadlet (pilote local)
- **OS / Version** : Rocky Linux 9; Podman des dépôts maintenus
- **Catégorie** : conteneurs / image

---

## Problème précis à résoudre

Tester une image officielle à version épinglée avant déploiement (valeurs d'exemple à remplacer par le registre, l'organisation, l'image et la version réels).

## 1. Hors-Production (Lab / Test / POC)

1. Récupérer l'image avec son registre complet et une version :
   ```bash
   sudo -iu svcpodman podman pull registre.example.net/organisation/image:1.0
   ```
   👉 Explication : évite `latest` et l'ambiguïté du registre.

2. Inspecter l'image :
   ```bash
   sudo -iu svcpodman podman image inspect registre.example.net/organisation/image:1.0
   ```
   👉 Explication : vérifie provenance, ports exposés et utilisateur.

## 2. Production — Contrôles

Vérifier provenance/signature selon la politique interne, lire le Containerfile, tester configuration, ports et stockage avant déploiement.

## 3. Production — Sécurité

- Éviter `latest` en production.
- Ne jamais monter le socket Podman ou le système racine de l'hôte dans le conteneur.
- Lier les ports de test seulement à l'adresse nécessaire.

## Validation et retour arrière

- **Validation** : image inspectée et validée.
- **Retour arrière** : `sudo -iu svcpodman podman rmi registre.example.net/organisation/image:1.0`.

## Si le problème n'est pas résolu

- [Podman — Quadlet et unités systemd](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Podman — référence CLI](https://docs.podman.io/en/latest/markdown/podman.1.html)
- [Guide complet Podman Quadlet Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/57-deploiement-podman-quadlet-rocky-linux-9#2-valider-une-image-en-laboratoire)