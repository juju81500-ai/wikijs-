# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Disposer d'un réseau pendant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans anaconda, ouvrir « Réseau et nom d'hôte » et activer l'interface.
   👉 Explication : le DHCP donne une adresse temporaire pour télécharger les paquets.

2. Après le premier démarrage, contrôler l'état :
   ```bash
   nmcli device status
   ip -br a
   ip r
   ```
   👉 Explication : montre l'interface connectée, l'adresse et la passerelle.

3. Tester la sortie réseau :
   ```bash
   ping -c 2 8.8.8.8
   curl -sI https://download.rockylinux.org | head -n1
   ```
   👉 Explication : valide routage, DNS et accès aux miroirs.

## 2. Production — Contrôles

Prévoir VLAN, passerelle et DNS corrects dès l'installation.

## 3. Production — Sécurité

Ne pas laisser la machine sur un réseau non maîtrisé avant les mises à jour.

## Validation et retour arrière

- **Validation** : Adresse, route et sortie vers les miroirs fonctionnent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)