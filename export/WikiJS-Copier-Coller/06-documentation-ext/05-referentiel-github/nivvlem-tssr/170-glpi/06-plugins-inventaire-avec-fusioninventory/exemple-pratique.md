# TP – Plugins : FusionInventory & Data Injection
## 🏗️ Prérequis

- Serveur GLPI fonctionnel (`srv-glpi`)
- Contrôleur de domaine AD (`srv-CD1`)
- Réseau VMnet 18 → `192.168.1.0/24`
- DHCP configuré sur pfSense

---

## 🛠️ Étapes détaillées

### 1️⃣ Installation du plugin FusionInventory sur GLPI

#### a) Récupération de l’archive

- Fichier : `fusioninventory-9.5.0+1.0.tar.bz2`
- Transfert vers le serveur GLPI (Debian) via **WinSCP** :

```text
/var/www/glpi/plugins/
```

#### b) Décompression de l’archive

```bash
cd /var/www/glpi/plugins

# Copier l’archive si besoin
cp /home/debyann/fusioninventory-9.5.0+1.0.tar.bz2 .

# Décompression
tar xvjf fusioninventory-9.5.0+1.0.tar.bz2
```

#### c) Attribution des droits

```bash
chown -R www-data:www-data /var/www/glpi/plugins
```

#### d) Activation dans GLPI

- Interface GLPI → **Configuration > Plugins**
- Sur la ligne `FusionInventory` → **Installer**, puis **Activer**

---

### 2️⃣ Installation de l’agent FusionInventory sur le contrôleur de domaine (srv-CD1)

#### a) Téléchargement de l’agent

- Version compatible avec la version du plugin (site officiel : [https://fusioninventory.org](https://fusioninventory.org/))

#### b) Installation de l’agent sur `srv-CD1`

- Lancer l’installateur `.exe`
- Configuration de l’URL serveur GLPI :

```text
http://srv-glpi/glpi/plugins/fusioninventory/```
```

- **Planification automatique** des scans → activée
- Vérification : service FusionInventory-Agent démarré

#### c) Vérification de l’inventaire

- Laisser tourner l’agent → vérifier sous :

```text
GLPI > Parc > Ordinateurs
```

L’agent devrait apparaître après le premier scan automatique (~10 min max).

---

### 3️⃣ Activation du Marketplace + installation du plugin Data Injection (Bonus)

#### a) Activation du Marketplace

- Créer un compte sur :

```text
https://services.glpi-network.com/register
```

- Récupérer la clé d’enregistrement → copier dans :

```text
GLPI > Configuration > Générale > Clé d’enregistrement
```

- Sauvegarder → l’onglet **Marketplace** devient actif

#### b) Installation du plugin Data Injection

- Marketplace → rechercher `Data Injection`
- Installer la dernière version compatible
- Activer dans :

```text
Configuration > Plugins > Data Injection > Activer
```

---

### 4️⃣ Préparation des fichiers pour Data Injection

#### a) Fichiers fournis

- `modèle excel data injection gabarit vide.xlsx`
- `modèle excel data injection gabarit.xlsx` (rempli)

#### b) Format attendu

- Format **CSV UTF-8** recommandé pour compatibilité Linux
- L’ordre des colonnes doit respecter le modèle GLPI

#### c) Injection (exemple)

- Créer un **modèle d’import**
- Lier les colonnes CSV ↔ champs GLPI
- Lancer l’import → vérifier les données injectées

---

## ✅ À retenir pour les révisions

- Le plugin **FusionInventory** permet l’inventaire automatique des postes
- L’installation nécessite **droits www-data** et une activation dans l’interface GLPI
- L’agent **client** communique en HTTP vers GLPI
- Le plugin **Data Injection** permet d’importer des données ponctuelles (CSV)
- Le Marketplace simplifie la gestion des plugins mais nécessite une **clé d’enregistrement**

---

## 📌 Bonnes pratiques professionnelles

- Vérifier la **compatibilité** plugin ↔ version GLPI
- Toujours utiliser **les versions stables** de FusionInventory (éviter les nightly builds)
- Vérifier que l’**agent client** est bien configuré (URL correcte)
- Lancer un **inventaire forcé** lors des tests (agent Windows en mode --force)
- Préparer les fichiers CSV **conformes** et tester l’import avec une petite série avant en masse
- Documenter les **versions** des plugins installés et les règles associées
- Surveiller la **santé de la tâche FusionInventory** (logs + suivi dans GLPI)
- Planifier une **revue régulière des agents actifs** et de la cohérence des données remontées