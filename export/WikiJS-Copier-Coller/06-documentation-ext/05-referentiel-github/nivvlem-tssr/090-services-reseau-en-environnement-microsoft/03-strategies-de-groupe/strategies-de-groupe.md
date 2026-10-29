# Stratégies de groupe (GPO)

## 🧠 Principe de fonctionnement des GPO

|Élément|Description|
|---|---|
|GPO|Objet contenant un ensemble de règles (stratégies)|
|GPMC|Console graphique de gestion des GPO|
|GPC|Composant stocké dans l’AD (objet lié à l’OU)|
|GPT|Composant stocké dans le SYSVOL (paramètres de la stratégie)|

### 🔄 Ordre d'application des stratégies (LSDOU)

1. **Local** – stratégie sur l’ordinateur
2. **Site** – via configuration des sites AD
3. **Domaine** – politiques appliquées à l’échelle du domaine
4. **OU** – priorité à la dernière OU ciblée

> ⚠️ Une GPO liée à une **OU enfant écrase** les stratégies de l’OU parente (sauf exception via héritage ou filtrage)

---

## 🛠️ Création et gestion des GPO

### 🔹 Console GPMC

- `GPMC.msc` : console principale
- Permet de : créer, lier, tester, sauvegarder, restaurer, modéliser

### 🔹 Création rapide

```powershell
New-GPO -Name "GPO_Fond_Ecran" | New-GPLink -Target "OU=Compta,DC=monprenom,DC=local"
```

### 🔹 Forçage d’actualisation sur un client

```powershell
gpupdate /force
```

---

## 🖥️ Exemples concrets de GPO utiles

### 🔹 Personnalisation de l’environnement utilisateur

- Définir un fond d’écran commun
- Cacher les paramètres système
- Bloquer les accès au panneau de configuration

### 🔹 Sécurité / réseau

- Interdire l’accès aux lecteurs (D:, E:, etc.)
- Empêcher l’installation de périphériques USB
- Déployer un mot de passe sécurisé et des règles de verrouillage

### 🔹 Déploiement d’imprimantes

- Configuration via GPO utilisateur > Imprimantes
- Déploiement automatique à la connexion

---

## 🧰 Filtres et ciblage avancés

### 🔹 Filtrage de sécurité

- Définir quels **utilisateurs ou groupes** sont ciblés par la GPO

### 🔹 WMI Filters

- Appliquer la GPO selon des **critères matériels/logiques** : OS, RAM, nom du poste, etc.

### 🔹 Bouclage (Loopback)

- Appliquer des stratégies utilisateur **en fonction de l’ordinateur** utilisé
- Activé dans : Configuration ordinateur > Modèles d’administration > Stratégies > Bouclage de traitement

---

## 🧠 À retenir pour les révisions

- Les GPO permettent d’unifier les règles de sécurité, d’apparence et de fonctionnement
- GPMC est l’interface de gestion, les GPO sont appliquées selon l’ordre **LSDOU**
- Les stratégies peuvent être **filtrées, priorisées ou forcées** (GPO en mode "Enforcement")
- Le **bouclage** est utile pour les salles informatiques, bornes, environnements partagés

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Toujours tester les GPO dans un labo|Éviter les blocages ou pertes d’accès|
|Documenter chaque GPO créée|Facilite la maintenance, l’audit et la transmission|
|Ne pas multiplier les GPO par OU|Privilégier la consolidation pour simplifier la hiérarchie|
|Utiliser des noms explicites|Ex : `GPO_Salle_Info_FondEcran`|
|Éviter les GPO vides ou non liées|Nettoyage régulier du domaine|