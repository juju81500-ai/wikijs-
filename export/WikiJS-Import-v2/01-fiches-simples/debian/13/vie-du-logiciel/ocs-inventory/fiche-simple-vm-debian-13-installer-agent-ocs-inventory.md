---
title: "Fiche Simple - VM Debian 13 Installer Agent OCS Inventory"
description: "Installer l'agent OCS 3 depuis le dépôt officiel et le configurer pour remonter un inventaire vers une API autorisée."
published: true
date: 2026-10-29T19:24:32Z
tags: ["debian13", "ocs-inventory", "agent", "inventaire", "https"]
editor: markdown
dateCreated: 2026-10-29T19:24:32Z
dateModified: 2026-10-29T19:24:32Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Installer_Agent_OCS_Inventory.md

- **Environnement** : VM Debian 13 membre d'un parc inventorié
- **OS / Version** : Debian 13 Trixie, agent OCS Inventory 3
- **Catégorie** : Système / inventaire
- **Tags** : `debian13`, `ocs-inventory`, `agent`, `inventaire`, `https`

---

## 🎯 Problème précis à résoudre

Installer l'agent OCS 3 depuis le dépôt officiel et le configurer pour remonter un inventaire vers une API autorisée.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier que l'API est joignable en HTTPS :
   ```bash
   curl -fsSI https://ocs.example.net/ocsapi/v1/ | head -1
   ```
   👉 Explication : remplacer le nom; certificat valide exigé, VM de test.

2. Créer côté serveur le compte agent avec droits minimaux : dans l'interface OCS, **Configuration > Users (ou Administration) > Add** avec profil restreint à l'inventaire.
   👉 Explication : le secret est conservé dans le coffre.


## ⚡ 2. Production — Façon Simplifiée

1. Ajouter le dépôt officiel (la clé est vérifiée par APT) :
   ```bash
   curl -fsSL https://deb-v3.ocsinventory-ng.org/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/ocs-archive-keyring.gpg
   echo "deb https://deb-v3.ocsinventory-ng.org/ trixie main" | sudo tee /etc/apt/sources.list.d/ocsinventory.list
   sudo apt update
   sudo apt install ocsinventory-agent
   ```
   👉 Explication : installe l'agent depuis le dépôt de l'éditeur.

2. Lancer l'assistant :
   ```bash
   sudo /usr/share/ocsinventory-agent/install.sh
   ```
   👉 Explication : choisir le mode distant `1`, saisir l'URL API HTTPS puis le compte et son secret à l'invite; ne pas désactiver la validation TLS.

3. Vérifier la configuration et lancer un inventaire :
   ```bash
   sudo stat -c '%a %U:%G %n' /etc/ocsinventory-agent/config.json
   sudo ocsinventory-cli
   sudo systemctl enable --now ocsinventory-agent.service
   sudo systemctl --no-pager status ocsinventory-agent.service
   ```
   👉 Explication : la configuration contenant des identifiants doit être `600 root:root`.


## 🔒 3. Production — Façon Sécurisée

- Utiliser le certificat TLS approuvé par le système; si une CA privée est utilisée, installer sa racine dans le magasin de confiance et conserver `bypass_certificate: false`.
- Ne pas utiliser un compte administrateur humain pour l'agent; accorder seulement les permissions de consultation et d'envoi d'inventaire requises.
- Restreindre les connexions sortantes à l'URL/API OCS nécessaire et protéger le secret agent.
- Ne pas activer les fonctions de déploiement de paquets/actions à distance sans gouvernance distincte, validation de changements et approbation explicite.

## ✅ Validation et retour arrière

- **Précontrôles** : version Debian, DNS, certificat et compte agent autorisé.
- **Validation** : exécution `ocsinventory-cli`, état `ocsinventory-agent.service`, puis présence de la VM dans la console.
- **Retour arrière** : arrêter le service et désinstaller avec `sudo apt remove ocsinventory-agent`; préserver `config.json` uniquement si sa protection et sa nécessité sont vérifiées.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[Debian13_OCS_Agent_Echec_Connexion]]
- [Documentation officielle OCS — Agent Linux](https://documentation.ocsinventory-ng.org/administrator-docs/agent-setup/installation-methods/using-official-repositories-linux.md)
- [Documentation officielle OCS — Configuration de l'agent](https://documentation.ocsinventory-ng.org/administrator-docs/agent-setup/configuration.md)