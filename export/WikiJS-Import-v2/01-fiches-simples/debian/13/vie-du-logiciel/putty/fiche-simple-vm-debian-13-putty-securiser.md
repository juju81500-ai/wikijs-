---
title: "Fiche Simple - VM Debian 13 PuTTY Securiser"
description: "Utiliser PuTTY en ligne de commande sans affaiblir la sécurité SSH."
published: true
date: 2026-10-29T21:24:09Z
tags: ["putty", "putty-tools", "plink", "puttygen", "ssh", "securite", "hostkey"]
editor: markdown
dateCreated: 2026-10-29T21:24:09Z
dateModified: 2026-10-29T21:24:09Z
---

# Fiche_Simple_-_VM_Debian_13_PuTTY_Securiser

- **Environnement** : VM Debian 13 (Trixie), poste d'administration en ligne de commande
- **OS / Version** : Debian 13 (Trixie) — paquet putty-tools
- **Catégorie** : outils d'administration / SSH
- **Tags** : `putty`, `putty-tools`, `plink`, `puttygen`, `ssh`, `securite`, `hostkey`

---

## Problème précis à résoudre

Utiliser PuTTY en ligne de commande sans affaiblir la sécurité SSH.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'empreinte de clé d'hôte hors bande avant d'accepter, puis la figer dans un script :
   ```bash
   plink -batch -hostkey EMPREINTE_A_REMPLACER -i ~/.ssh/CLE_A_REMPLACER.ppk UTILISATEUR@SERVEUR_SSH uptime
   ```
   👉 Explication : `EMPREINTE_A_REMPLACER` est l'empreinte vérifiée ; `-batch` évite toute invite et échoue si l'hôte est inconnu.
2. Ne jamais passer un mot de passe sur la ligne de commande (option `-pw`) : préférer clé et phrase de passe.
   👉 Explication : la ligne de commande est visible dans la liste des processus.
3. Convertir une clé vers OpenSSH si nécessaire :
   ```bash
   puttygen ~/.ssh/CLE_A_REMPLACER.ppk -O private-openssh -o ~/.ssh/CLE_A_REMPLACER_openssh
   ```
   👉 Explication : protéger le fichier converti en `600`.

## 2. Production — Contrôles

- Auditer régulièrement les clés autorisées côté serveur.

## 3. Production — Sécurité

- Clés privées protégées par phrase de passe ; ne pas utiliser Telnet ni rlogin proposés par `plink`.

## Validation et retour arrière

- **Validation** : connexion `-batch` réussie et refusée si l'empreinte diffère. **Retour arrière** : révoquer la clé publique côté serveur.

## Si le problème n'est pas résolu

- [Fiche d'entrée PuTTY](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-putty)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)