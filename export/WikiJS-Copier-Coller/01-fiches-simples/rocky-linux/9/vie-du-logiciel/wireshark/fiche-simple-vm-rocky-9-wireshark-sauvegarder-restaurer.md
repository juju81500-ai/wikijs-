# Fiche_Simple_-_VM_Rocky_9_Wireshark_Sauvegarder_Restaurer

- **Environnement** : VM Rocky Linux 9 dédiée à Wireshark
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / sauvegarde et restauration

---

## Problème précis à résoudre

Sauvegarder les profils/préférences Wireshark et les captures de preuve.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder le profil utilisateur :
   ```bash
   tar -czf ~/wireshark-profil-DATE.tar.gz -C ~/.config wireshark
   ```
   👉 Explication : Archive préférences, profils et filtres; DATE est à remplacer. Ne pas y inclure de keylog TLS : le retirer au besoin.

2. Empreinte d’une capture de preuve :
   ```bash
   sha256sum /var/tmp/TICKET.pcapng | tee /var/tmp/TICKET.pcapng.sha256
   ```
   👉 Explication : Garantit l’intégrité du fichier conservé.

3. Restaurer :
   ```bash
   tar -xzf ~/wireshark-profil-DATE.tar.gz -C ~/.config
   sha256sum -c /var/tmp/TICKET.pcapng.sha256
   ```
   👉 Explication : Rétablit le profil et contrôle l’empreinte.

## 2. Production — Contrôles

Tester la restauration; appliquer la rétention.

## 3. Production — Sécurité

- Chiffrer les archives avant de les sortir de la VM.

## Validation et retour arrière

- **Validation** : Profil restauré; `sha256sum -c` renvoie OK.
- **Retour arrière** : Supprimer le profil restauré et réinstaller l’ancien depuis l’archive validée.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireshark)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-mise-a-jour-retour-arriere)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-valider)