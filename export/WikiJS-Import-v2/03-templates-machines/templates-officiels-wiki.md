---
title: "📝 Templates Officiels Markdown - Wiki.js Lab & TSSR"
description: "1. Commande d'exécution :"
published: true
date: 2026-10-27T14:41:20Z
tags: ["[tag1]", "[tag2]", "[tag3]"]
editor: markdown
dateCreated: 2026-10-27T14:41:20Z
dateModified: 2026-10-27T14:41:20Z
---

# 📝 Templates Officiels Markdown - Wiki.js Lab & TSSR

## 1. Template : Fiche Simple

```markdown
# 📄 [NOM_DU_FICHIER]

- **Environnement** : [LXC | VM | Hôte Docker | Conteneur | Windows]
- **OS / Version** : [ex: Alpine 3.19 | Debian 12/13 | Ubuntu 24.04 | Rocky 9 | Windows Server 2022]
- **Machine ciblée (optionnel)** : [ex: srv-dns | N/A]
- **Catégorie** : [Réseau | Sécurité | Système | Stockage | Service]
- **Tags** : `[tag1]`, `[tag2]`, `[tag3]`

---

## 🎯 Problème précis à résoudre
> *Rédiger ici le problème unique ou la tâche concrète à traiter (un seul problème par fiche simple).*

---

## 🧪 1. Hors-Production (Lab / Test / POC)
> **Objectif** : Application immédiate et rapide pour maquettage.

1. **Commande d'exécution** :
   ```bash
   [Saisir la commande exacte]
   ```
   👉 *Explication : Tu fais ça, ça applique [expliquer simplement l'effet de la commande].*

2. **Vérification rapide** :
   ```bash
   [Commande de contrôle]
   ```
   👉 *Explication : Tu contrôles que [résultat attendu].*

---

## ⚡ 2. Production — Façon Simplifiée
> **Objectif** : Configuration propre, lisible, permanente au reboot et stable.

1. **Ouverture du fichier de configuration** :
   ```bash
   [Commande d'ouverture du fichier]
   ```
   👉 *Explication : Tu ouvres le fichier [nom du fichier] pour éditer la configuration de base.*

2. **Saisie du bloc de configuration** :
   ```text
   [Bloc de configuration à copier-coller]
   ```
   👉 *Explication : Tu insères ces paramètres pour [expliquer le rôle du bloc].*

3. **Application & Démarrage du service** :
   ```bash
   [Commande de redémarrage de service ou réseau]
   ```
   👉 *Explication : Tu recharges le service pour appliquer les modifications sans couper la machine.*

---

## 🔒 3. Production — Façon Sécurisée (si pertinent)
> **Objectif** : Réduire les risques sans introduire de réglage non nécessaire. Adapter cette section au rôle et à l'OS.

1. **Application de la configuration durcie** :
   ```bash
   [Commande de hardening]
   ```
   👉 *Explication : Tu appliques cette règle pour bloquer [risque spécifique].*

2. **Permissions minimales (si nécessaire)** :
   ```bash
   [Commande de permission avec propriétaire et mode explicitement justifiés]
   ```
   👉 *Explication : Ne pas appliquer `chmod 777`, `chattr +i` ou des permissions récursives sans vérifier le propriétaire et l'effet sur le service.*

3. **Filtrage réseau (uniquement si le sujet le nécessite)** :
   ```bash
   [Règle dans le gestionnaire de pare-feu propriétaire et persistant]
   ```
   👉 *Explication : Préciser source, destination, protocole, port et persistance. Ne pas ajouter une règle runtime sans identifier le pare-feu actif.*

## ✅ Validation et retour arrière
- **Précontrôles** : sauvegarde, accès de secours et état initial.
- **Validation** : commande de syntaxe et test fonctionnel attendu.
- **Retour arrière** : restauration de la configuration précédente si la validation échoue.

---

## 🔗 Si le problème n'est pas résolu
- **Fiche de résolution complémentaire** : [[Env_OS_Version_Type_Sujet-Incident]]
```

---

## 2. Template : Fiche Complexe (Fiche Complète)

Chaque fiche complète doit indiquer son **OS / Version** et un seul **Type de fiche** principal :

- **Installation / Déploiement** : installer et mettre en service un OS, un rôle ou un logiciel.
- **Diagnostic** : analyser une panne, appliquer une correction contrôlée et valider le retour du service.
- **Autres** : architecture, sécurité, stockage, sauvegarde, migration ou haute disponibilité.

Classer les guides dans la matrice par OS puis par type. Pour un guide multi-OS, inscrire toutes les versions prises en charge au lieu de dupliquer la fiche.

```markdown
# 📄 [NOM_DU_FICHIER]

- **OS / Version** : [OS et version(s) réellement ciblés]
- **Type de fiche** : [Installation/Déploiement | Diagnostic | Autres]
- **Environnement** : [LXC | VM | Hôte Docker | Conteneur | Windows]
- **Machine ciblée** : [ex: srv-dns | N/A]
- **Catégorie** : [Services / Installation / Infrastructure]
- **Tags** : `[tag1]`, `[tag2]`, `[tag3]`

---

## 📋 1. Présentation & Paramètres Machine
- **Rôle** : [Présentation du service et fonction dans l'infrastructure]
- **IP / Masque** : [ex: 192.168.1.53/24]
- **Passerelle** : [ex: 192.168.1.1]
- **Ports / Flux requis** : [ex: TCP/22, UDP/53]

---

## ⚙️ 2. Protocole complet d'installation logicielle
1. **Mise à jour des dépôts & installation des packages** :
   ```bash
   [Commandes d'installation]
   ```
2. **Activation du service au démarrage (Boot)** :
   ```bash
   [rc-update / systemctl enable]
   ```

---

## 🛠️ 3. Méthodologies de Configuration (3 Approches)

### 🧪 A. Configuration Hors-Production (Test / POC)
- Configuration basique sans chiffrement ni régulation des flux.

### ⚡ B. Configuration Production Simplifiée
- Configuration persistante, propre et documentée.

### 🔒 C. Configuration Production Sécurisée (selon le service)
- Décrire les contrôles réellement nécessaires, leurs prérequis, leur validation et leur retour arrière.

---

## 🔍 4. Vérification, Dépannage & Maintenance
- **Commandes de vérification du statut** : `systemctl status` / `rc-service status`
- **Vérification des logs** : `journalctl` / `/var/log/...`
- **Sauvegarde et retour arrière** : [méthode de sauvegarde cohérente et procédure de restauration testable]

---

## 🔗 Si le problème n'est pas résolu
- **Fiche de résolution complémentaire** : [[Env_OS_Version_Type_Sujet-Incident]]
```

---

## 3. Template : Fiche Machine (Documentation Machine)

```markdown
# 📄 [MachinePhysique_Env_Type_NomMachine_OS_Statut]

- **Nomenclature officielle** : `[MachinePhysique]_[Env]_[Type]_[NomMachine]_[OS]_[Statut]`
- **Tags** : `fiche-machine`, `[type]`, `[os]`, `[statut]`

---

### 📌 1. Identification & Métadonnées
* **Machine Physique / Hôte** : [ex: pve1002]
* **Environnement** : [ex: Lab / Prod / DMZ]
* **Type d'équipement** : [LXC | VM | Physique]
* **Nom de la Machine** : [ex: srv-dns]
* **Système d'Exploitation (OS)** : [ex: Alpine 3.19]
* **Statut Opérationnel** : [Actif | Inactif | Maintenance]

---

### 📋 2. Rôle, Utilisation & Besoins (Ressources)
* **Rôle et Utilisation** : [Description précise de la fonction]
* **Besoins (Allocation ressources)** :
  * **vCPU** : [ex: 1 Coeur]
  * **RAM** : [ex: 512 Mo]
  * **Stockage** : [ex: 8 Go ZFS]
  * **Adresse IP** : [ex: 192.168.1.53/24]

---

### 📦 3. Logiciels & Ports
* **Logiciels installés** : [Liste des applications et packages principaux]
* **Ports ouverts** : [Liste des ports TCP/UDP ouverts]

---

### 🛡️ 4. Sécurité & Pare-feu
* **Firewall Machine (local)** : [Règles IPtables/Nftables/Windows Firewall]
* **Firewall Externe (Hôte / Routeur)** : [Règles appliquées en amont]

---

### ⚙️ 5. Mode d'Exécution Appliqué
| Mode | État de la Machine | Configuration Réseau & SSH |
| :--- | :--- | :--- |
| **🧪 Hors-Production** | Mode Test / POC | Accès temporaire contrôlé, données non sensibles. |
| **⚡ Prod Simplifiée** | Mode Actif de base | Configuration persistante et sauvegardée. |
| **🔒 Prod Sécurisée** | Mode conforme au risque | Contrôles justifiés, testés et réversibles. |

---

### 📅 6. Suivi des Dates & Historique (Automatisé)
- **Date de création** : [AAAA-MM-JJ]
- **Dernière modification** : [AAAA-MM-JJ]
- **Historique des modifications datées** :
  - `AAAA-MM-JJ` : [Description du changement]
```