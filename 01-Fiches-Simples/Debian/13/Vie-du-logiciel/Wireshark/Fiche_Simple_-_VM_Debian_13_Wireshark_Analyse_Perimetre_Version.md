# Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Perimetre_Version.md

- **Environnement** : Poste Debian 13 amd64
- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark des dépôts Debian
- **Catégorie** : analyse reseau / cadrage
- **Tags** : `wireshark`, `debian13`, `cadrage`, `autorisation`

---

## Problème précis à résoudre

Définir le périmètre autorisé et relever la version Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'architecture et la version candidate :
   ```bash
   dpkg --print-architecture
   apt-cache policy wireshark wireshark-qt tshark
   ```
   👉 Explication : la version Debian peut différer de la dernière version amont; on la consigne.

2. Noter par écrit les interfaces et réseaux autorisés à l'analyse.
   👉 Explication : seuls les appareils et réseaux possédés ou explicitement autorisés peuvent être capturés.

## 2. Production — Contrôles

Définir motif de collecte, durée, interfaces et approbations avant toute capture.

## 3. Production — Sécurité

- Pas de scan de réseaux tiers, d'interception ni de déchiffrement de session.

## Validation et retour arrière

- **Validation** : Version et périmètre consignés.
- **Retour arrière** : Aucune modification à cette étape.

## Si le problème n'est pas résolu

- [Wireshark — téléchargements](https://www.wireshark.org/download.html)
- [Wireshark — FAQ](https://www.wireshark.org/faq.html)
- [Guide complet Wireshark Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/83_Installation_Wireshark_Debian_13_Analyse_Capture.md#1-perimetre-et-version)
