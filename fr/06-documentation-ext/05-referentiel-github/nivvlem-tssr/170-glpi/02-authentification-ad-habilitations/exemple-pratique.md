---
title: "TP – Liaison LDAP et ajout d’utilisateurs"
description: "- Serveur AD srv-CD1 (domaine olympus.gr)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Liaison LDAP et ajout d’utilisateurs
## 🧾 Prérequis

- **AD et GLPI opérationnels**
- Serveur AD `srv-CD1` (domaine `olympus.gr`)
- Serveur GLPI `srv-glpi`

---

## 🏗️ Étapes détaillées

### 1️⃣ Structure AD et utilisateurs

#### a) Création des OUs

Suivre l’**annexe 2** : créer la structure sous `OU=Olympus` :

```text
_Olympus
 ├── Les_utilisateurs
 │   ├── Direction
 │   ├── Service_compta
 │   │   ├── Comptables
 │   │   ├── Stagiaires
 │   ├── Service_commercial
 │   │   ├── Commerciaux
 │   │   ├── Secrétaires
 │   ├── Service_info
 │   │   ├── Administrateurs
 │   │   ├── Administrateurs_AD
 │   │   ├── Techniciens
 │   │   ├── Stagiaires
 ├── Les_groupes
 │   ├── Groupes_GLPI
 │   ├── Groupes_GG
 │   ├── Groupes_DL
```

#### b) Création des groupes

Créer les **groupes globaux** suivants (AD) :

```text
Groupes_GLPI
├── GG_GLPI_Observer
├── GG_GLPI_Super-Admin
├── GG_GLPI_Technician
├── GG_GLPI_Hotliner
```

Créer les **groupes métier** (Groupes_GG) selon l’annexe 1 :

```text
GG_dir
GG_secretaires_dir
GG_secretaires
GG_experts-compta
GG_compta
GG_stag_compta
GG_dir_comm
GG_comm
GG_admin
GG_admin_ad
GG_techniciens
GG_stagiaires_info
```

#### c) Création des utilisateurs

Créer les utilisateurs **avec convention de nommage claire** :

```text
Login = prenom.nom (ex: zeus, hephaistos...)
```

Affecter les **utilisateurs dans les groupes AD** (Groupes_GLPI + Groupes_GG) conformément à l’annexe 1.

### 2️⃣ Configuration de GLPI

#### a) Création d’un compte admin local

- Créer un **compte personnel** (ex: votre nom)
- Affecter le **profil Super-Admin**
- Se connecter ensuite avec ce compte pour le TP

#### b) Création des lieux

- **Configuration > Lieux**
- Créer les lieux de l’**annexe 3** :

```text
Temple de Zeus
Temple d’Héra
Hôtellerie
Salle des trésors
```

### 3️⃣ Liaison LDAP (Active Directory)

#### a) Ajout de l’annuaire LDAP

**Configuration > Authentification > Annuaires LDAP** → Ajouter :

- Préconfig : **Active Directory**
- Nom : `AD Olympus`
- Adresse IP du contrôleur : `192.168.1.10 (IP de `srv-CD1`)
- Base DN :

```text
DC=olympus,DC=gr
```

- DN du compte de lecture :

```text
CN=Administrateur,CN=Users,DC=olympus,DC=gr
```

- Mot de passe : mot de passe de l’Administrateur AD

**Tester la connexion !**

#### b) Synchronisation des attributs

Vérifier que les **attributs standards** sont bien mappés :

|Champ GLPI|Attribut LDAP|
|---|---|
|Nom|sn|
|Prénom|givenName|
|Adresse mail|mail|

### 4️⃣ Règles d’habilitation dynamiques

**Configuration > Gestion des utilisateurs > Règles d’importation des utilisateurs**

Créer une **règle par groupe GLPI** :

#### a) Exemple : GG_GLPI_Observer

|Critère|Valeur|
|---|---|
|(LDAP) MemberOf|GG_GLPI_Observer|

Actions :

- Profil : Observer
- Entité : Racine (ou spécifique selon le besoin)
- Récursivité : selon l’entité

#### b) Répéter pour :

- GG_GLPI_Super-Admin → Super-Admin
- GG_GLPI_Technician → Technician
- GG_GLPI_Hotliner → Hotliner

### 5️⃣ Import des utilisateurs

**Onglet Utilisateurs > LDAP directory synchronization**

Importer les utilisateurs :

- Affecter le bon **lieu** à chaque utilisateur (cf. annexe 1)

### 6️⃣ Import des groupes

**Onglet Groupes > LDAP synchronization**

Importer les groupes **GLPI** + **Groupes métier**

### 7️⃣ Désactivation des comptes par défaut

Désactiver les comptes suivants :

- normal
- post-only
- tech

**Onglet Utilisateurs > Modifier > État = Désactivé**

---

## ✅ À retenir pour les révisions

- La **liaison LDAP** permet une authentification centralisée
- Les **habilitations dynamiques** sont basées sur l’appartenance à des groupes AD
- Une convention claire pour :
    - Groupes GLPI : `GG_GLPI_*`
    - Groupes métier : `GG_*`
- Les règles d’import doivent être **testées et validées**
- Il faut **désactiver les comptes GLPI par défaut** en production

---

## 📌 Bonnes pratiques professionnelles

- **Documenter** la structure AD (OUs, groupes, utilisateurs)
- Toujours tester la **connexion LDAP** après configuration
- Préférer **les habilitations dynamiques** (maintenance simplifiée)
- Conserver un **audit des comptes synchronisés**
- Planifier une **revue régulière des règles d’habilitation**
- Limiter le nombre de comptes ayant un **profil Super-Admin**