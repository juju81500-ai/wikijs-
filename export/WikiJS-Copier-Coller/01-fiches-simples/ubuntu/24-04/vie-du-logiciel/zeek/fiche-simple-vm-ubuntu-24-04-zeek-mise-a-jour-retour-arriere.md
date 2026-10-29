# Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Zeek
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / mise à jour et retour arrière

---

## Problème précis à résoudre

Mettre à jour Zeek dans la ligne LTS et revenir en arrière en cas de régression.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration (fiche Sauvegarder_Restaurer).
   👉 Explication : Condition préalable à tout changement.

2. Mettre à jour dans la ligne LTS :
   ```bash
   sudo apt update
   apt-cache policy zeek-8.0
   sudo apt install --only-upgrade zeek-8.0
   /opt/zeek/bin/zeek --version
   ```
   👉 Explication : Reste dans la ligne 8.0; un changement de ligne (ex. 9.0) est un projet distinct à tester en lab.

3. Redéployer et contrôler :
   ```bash
   sudo /opt/zeek/bin/zeekctl check
   sudo /opt/zeek/bin/zeekctl deploy
   sudo /opt/zeek/bin/zeekctl status
   ```
   👉 Explication : Applique la nouvelle version avec la configuration contrôlée.

4. Retour arrière :
   ```bash
   apt-cache madison zeek-8.0
   sudo apt install zeek-8.0=VERSION_ANTERIEURE
   ```
   👉 Explication : VERSION_ANTERIEURE est à remplacer par une version encore disponible; sinon restaurer depuis le miroir interne.

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
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-sauvegarder-restaurer)