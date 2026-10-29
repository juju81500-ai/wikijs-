# Les stratégies de groupe local

## 🧩 La base de registre Windows

### 🔹 Rôle

- Base de données hiérarchique centrale
- Stocke toute la configuration système, utilisateur, applications, matériels
- Interrogée en permanence par Windows

### 🔹 Accès

```bash
regedit   # Ouvre l'éditeur du registre
```

⚠️ Manipuler avec précaution (modification immédiate du comportement système)

### 🔹 Les 5 ruches principales

|Clé|Description|
|---|---|
|`HKEY_CLASSES_ROOT`|Infos sur les applis, objets COM/OLE, associations fichiers|
|`HKEY_CURRENT_USER`|Config utilisateur en session (équiv. `HKEY_USERS\<SID>`)|
|`HKEY_LOCAL_MACHINE`|Configuration système globale, matérielle, pilotes|
|`HKEY_USERS`|Profils chargés sur la machine|
|`HKEY_CURRENT_CONFIG`|Profil matériel actif (imprimantes, cartes, etc.)|

---

## 🛠️ Les LGPO (Local Group Policy Objects)

### 🔹 Buts

- Appliquer des paramètres via une interface graphique (MMC)
- Modifier de façon conviviale des clés de registre sensibles
- Réduire la gestion manuelle des postes

### 🔹 Outils MMC

|Console|Commande|Rôle principal|
|---|---|---|
|Éditeur de stratégie|`gpedit.msc`|Stratégies utilisateur et ordinateur|
|Sécurité locale|`secpol.msc`|Mots de passe, audit, stratégies restreintes|

### 🔹 Exemples d'actions

- Changer la **stratégie de mot de passe**
- Désactiver l’accès à la **CMD**, au **Panneau de configuration**, etc.
- Restreindre les **applications** ou les **options de session**
- Lancer des **scripts à la connexion / déconnexion**
- Uniformiser l’interface utilisateur (fond d’écran, barre des tâches)

### 🔹 Fonctionnement

Chaque paramètre :

- Peut être : **Activé**, **Désactivé** ou **Non configuré**
- Peut contenir des **commentaires**, **conditions** ou **options** supplémentaires
- Dispose souvent d’une **aide intégrée précieuse**

---

## ✅ À retenir pour les révisions

- Les LGPO permettent de modifier des comportements utilisateurs/système **sans passer par le registre**
- Les paramètres sont visibles et modifiables dans `gpedit.msc` ou `secpol.msc`
- Attention : les LGPO sont locales et **ne s’appliquent qu’à la machine** (non centralisées)
- Utilisation idéale dans les environnements **hors domaine**, **mono-poste** ou **tests de stratégie**

---

## 📌 Bonnes pratiques professionnelles

|Bonne pratique|Pourquoi ?|
|---|---|
|Toujours documenter les paramètres modifiés|Suivi clair et réversible en cas de problème|
|Tester sur un poste hors production|Éviter des blocages système ou utilisateur involontaires|
|Sauvegarder le registre avant modification|Permet de revenir à un état stable si besoin|
|Utiliser les commentaires intégrés aux stratégies|Facilite la compréhension pour les autres administrateurs|
|Préférer les LGPO avant toute modification directe|Moins risqué que la manipulation brute du registre|