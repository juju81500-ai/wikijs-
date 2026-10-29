# Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Suricata
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / mise à jour et retour arrière
- **Tags** : `suricata`, `ubuntu24.04`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour Suricata et ses règles, avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder avant changement.
   👉 Explication : Suivre la fiche Sauvegarder_Restaurer de cette série.

2. Mettre à jour le moteur :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade suricata
   sudo suricata -T -c /etc/suricata/suricata.yaml
   ```
   👉 Explication : Applique la version publiée et teste la configuration avant redémarrage.

3. Mettre à jour les règles :
   ```bash
   sudo suricata-update
   sudo suricata -T -c /etc/suricata/suricata.yaml
   sudo systemctl reload suricata || sudo systemctl restart suricata
   ```
   👉 Explication : Recharge les règles; `reload` évite l’arrêt de la capture quand il est supporté.

4. Retour arrière du paquet :
   ```bash
   apt-cache madison suricata
   sudo apt install suricata=VERSION_ANTERIEURE
   ```
   👉 Explication : VERSION_ANTERIEURE est à remplacer par une version listée par `apt-cache madison` et encore disponible; restaurer ensuite `/etc/suricata` depuis la sauvegarde.

## 2. Production — Contrôles

Mettre à jour d’abord en lab; surveiller le volume d’alertes (faux positifs) après un nouveau jeu de règles.

## 3. Production — Sécurité

- Règles provenant de sources approuvées uniquement.
- Mettre à jour rapidement les failles du moteur.

## Validation et retour arrière

- **Validation** : Test OK, service actif, alertes cohérentes.
- **Retour arrière** : Appliquer le retour arrière, restaurer la configuration, puis rejouer la recette.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Suricata.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Sauvegarder_Restaurer.md)
