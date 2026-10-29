# Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Wireshark
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / sauvegarde et restauration
- **Tags** : `wireshark`, `ubuntu24.04`, `vie-du-logiciel`, `sauvegarder-restaurer`

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
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Mise_A_Jour_Retour_Arriere.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Valider.md)
