# Fiche_Simple_-_VM_Rocky_9_Zeek_Sauvegarder_Restaurer

- **Environnement** : VM Rocky Linux 9 dédiée à Zeek
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / sauvegarde et restauration
- **Tags** : `zeek`, `rocky9`, `vie-du-logiciel`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration de Zeek.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder scripts locaux et empreinte de l’image :
   ```bash
   sudo tar -czf /var/tmp/zeek-lab-DATE.tar.gz /var/lib/zeek-lab --exclude=/var/lib/zeek-lab/logs
   sudo podman image inspect docker.io/zeek/zeek:lts --format "{{.Digest}}" | sudo tee /var/tmp/zeek-image-digest.txt
   sudo chmod 0600 /var/tmp/zeek-lab-DATE.tar.gz
   ```
   👉 Explication : Conserve scripts et pcap de recette, et le digest d’image à redéployer; DATE est à remplacer.

2. Restaurer :
   ```bash
   sudo tar -xzf /var/tmp/zeek-lab-DATE.tar.gz -C /
   sudo podman pull docker.io/zeek/zeek@sha256:DIGEST_RELEVE
   ```
   👉 Explication : Restaure les fichiers puis retélécharge l’image au digest consigné.

## 2. Production — Contrôles

Tester la restauration en lab.

## 3. Production — Sécurité

- Archive en 0600, chiffrée hors VM.

## Validation et retour arrière

- **Validation** : Les fichiers sont restaurés et l’image au digest consigné démarre.
- **Retour arrière** : Restaurer l’archive précédente connue bonne.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Zeek.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Zeek_Mise_A_Jour_Retour_Arriere.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Zeek_Valider.md)
