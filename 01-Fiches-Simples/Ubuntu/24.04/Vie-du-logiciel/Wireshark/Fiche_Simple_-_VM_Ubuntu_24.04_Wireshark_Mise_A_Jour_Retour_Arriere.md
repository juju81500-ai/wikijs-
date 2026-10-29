# Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Wireshark
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / mise à jour et retour arrière
- **Tags** : `wireshark`, `ubuntu24.04`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour Wireshark/TShark et revenir en arrière si nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner la version :
   ```bash
   tshark --version | head -n 1
   ```
   👉 Explication : Référence avant changement.

2. Mettre à jour :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade wireshark wireshark-common tshark
   ```
   👉 Explication : Applique la version publiée par la distribution; lire les avis de sécurité.

3. Contrôler :
   ```bash
   tshark --version | head -n 1
   dumpcap -D
   ```
   👉 Explication : Vérifie le fonctionnement et les droits de capture, qui peuvent être réinitialisés par une mise à jour.

4. Retour arrière :
   ```bash
   apt-cache madison wireshark
   sudo apt install wireshark=VERSION_ANTERIEURE wireshark-common=VERSION_ANTERIEURE tshark=VERSION_ANTERIEURE
   ```
   👉 Explication : VERSION_ANTERIEURE (à remplacer) provient de `apt-cache madison`; les paquets liés doivent rester à la même version, sinon passer par le miroir interne.

## 2. Production — Contrôles

Tester sur lab, sauvegarder le profil avant la mise à jour.

## 3. Production — Sécurité

- Mettre à jour rapidement les failles de dissecteurs.
- Contrôler à nouveau les permissions de dumpcap.

## Validation et retour arrière

- **Validation** : Version attendue et recette réussie.
- **Retour arrière** : Appliquer le retour arrière puis rejouer la recette.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Sauvegarder_Restaurer.md)
