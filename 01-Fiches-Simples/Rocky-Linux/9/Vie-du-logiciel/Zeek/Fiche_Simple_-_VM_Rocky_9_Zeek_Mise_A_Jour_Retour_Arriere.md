# Fiche_Simple_-_VM_Rocky_9_Zeek_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 dédiée à Zeek
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / mise à jour et retour arrière
- **Tags** : `zeek`, `rocky9`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour Zeek dans la ligne LTS et revenir en arrière en cas de régression.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner le digest actuel :
   ```bash
   sudo podman image inspect docker.io/zeek/zeek:lts --format "{{.Digest}}"
   ```
   👉 Explication : Permet le retour arrière.

2. Récupérer la nouvelle image :
   ```bash
   sudo podman pull docker.io/zeek/zeek:lts
   sudo podman run --rm docker.io/zeek/zeek:lts zeek --version
   ```
   👉 Explication : Contrôle la nouvelle version avant bascule.

3. Retour arrière :
   ```bash
   sudo podman pull docker.io/zeek/zeek@sha256:DIGEST_PRECEDENT
   ```
   👉 Explication : DIGEST_PRECEDENT est le digest consigné (à remplacer); relancer la capture avec cette référence.

## 2. Production — Contrôles

Tester en lab; surveiller pertes de paquets et volume de logs.

## 3. Production — Sécurité

- Rester sur la ligne LTS maintenue.
- Appliquer rapidement les avis de sécurité.

## Validation et retour arrière

- **Validation** : Version attendue, capteur actif, journaux cohérents.
- **Retour arrière** : Appliquer l’étape de retour arrière puis rejouer la recette.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Zeek.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Zeek_Sauvegarder_Restaurer.md)
