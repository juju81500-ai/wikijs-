---
title: "TP - Mise en œuvre RDS et session à distance"
description: "Domaine : nivvlem.tssr.eni"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP - Mise en œuvre RDS et session à distance  

Domaine : `nivvlem.tssr.eni`  
Réseau : `192.168.13.X`  

---

## 🏗️ Pré-requis

✅ **TP1 terminé**  
✅ Domaine **nivvlem.tssr.eni** fonctionnel  
✅ `RDS` intégré au domaine  
✅ Utilisateurs et groupes créés :  
- `Direction` → Estelle, Baptiste  
- `Pédagogique` → Frédéric, Mathieu  
- `Informatique` → Benoît, VotrePrénom (Admin)

---

## ⚙️ Étapes de mise en œuvre
### 1️⃣ Préparation du serveur

#### Installation de LibreOffice :

- Télécharger **LibreOffice** depuis le partage `distrib`
- Copier sur `RDS`  
- Installation **par défaut** → mode local

Validation :

```
Menu démarrer → LibreOffice → Tester le lancement
```

---

### 2️⃣ Installation et configuration du service RDS

#### Installer le rôle RDS

Depuis **Gestionnaire de serveur** → Ajouter des rôles :

```powershell
Install-WindowsFeature RDS-RD-Server -IncludeManagementTools
```

#### Type de déploiement

- **Standard**  
- **Bureaux basés sur session**

#### Services de rôle → sur **RDS** :

| Service RDS            | Hébergement |
|------------------------|-------------|
| RD Session Host        | RDS         |
| RD Licensing           | RDS         |
| RD Connection Broker   | RDS         |
| RD Web Access          | RDS         |

#### Création de la collection

- **Nouvelle collection** :  
  - Nom : `RDS-Session-Collection`  
  - **Bureaux complets**  
  - **Pas de disques de profil**  

---

### 3️⃣ Test du service Bureau à distance

#### Test basique depuis `Cli10`

- Ouvrir **mstsc.exe**  
- Cibler : `RDS.nivvlem.tssr.eni` ou `192.168.13.2`  
- Se connecter avec un utilisateur du domaine :

```
Utilisateur : nivvlem.tssr.eni\estelle  (ou autre)
```

---

#### Contrôle des groupes autorisés

##### Modifier les droits d’accès :

- Aller dans **Propriétés de la collection**  
- Autoriser uniquement :

```
Groupes autorisés :
- Direction
- Pédagogique
```

##### Tester :

| Utilisateur    | Résultat attendu |
|----------------|------------------|
| Frédéric       | OK               |
| Benoît         | Refusé           |

---

#### Désactiver la redirection des lecteurs locaux

Dans **Paramètres de la collection** → **Redirection de périphériques** :

```
Décocher → Redirection des lecteurs locaux
```

Tester avec :

| Utilisateur    | Résultat attendu |
|----------------|------------------|
| Estelle        | OK sans lecteurs |
| Mathieu        | OK sans lecteurs |

---

#### Test des fonctionnalités de gestion des connexions

Depuis **Gestionnaire de serveur** :

| Action                | Test |
|-----------------------|------|
| Envoyer un message    | OK   |
| Déconnexion forcée    | OK   |
| Fermer la session     | OK   |
| Cliché instantané     | Vérification OK |

---

### 4️⃣ Snapshot de l’infrastructure

Machines concernées :

| VM          | Action |
|-------------|--------|
| INFRA       | Snapshot "Atelier 2 OK" |
| RDS         | Snapshot "Atelier 2 OK" |

---

## 📌 Bonnes pratiques

✅ Toujours valider l’installation du rôle **avant** de créer la collection  
✅ Limiter l’accès RDS par **groupes** → jamais "Tout le monde"  
✅ Désactiver les redirections non nécessaires → **principe de moindre privilège**  
✅ Surveiller la consommation **CAL RDS**  
✅ Documenter les collections créées  
✅ Vérifier le **licensing RDS** (30 jours de grâce si non activé)

---

## ⚠️ Pièges à éviter

- Ne pas mettre tous les rôles sur des serveurs différents (ici tout sur `RDS` car maquette)  
- Oublier d’**activer** les groupes autorisés  
- Mauvais nom DNS → échec de la connexion RDP  
- Ne pas tester la **redirection des lecteurs**  
- Ne pas documenter les sessions ouvertes avant snapshot