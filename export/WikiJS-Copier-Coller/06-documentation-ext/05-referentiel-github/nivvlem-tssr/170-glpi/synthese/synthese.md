# Synthèse – GLPI
## 🧩 Présentation de GLPI

- **GLPI = Gestion Libre de Parc Informatique**
- Logiciel libre **ITSM** compatible **ITIL**
- Fonctionne en mode **web** → stack LAMP
- Modules principaux :
    - **Inventaire** matériel & logiciel
    - **HelpDesk** (tickets)
    - **Contrats / Licences / Fournisseurs**
    - **Suivi des consommables**
    - **Gestion multi-entités / multi-sites**
    - **Supervision étendue** via plugins

---

## 🔑 Structure générale de GLPI

|Élément|Rôle|
|---|---|
|Entités|Cloisonnement (clients, services, sites)|
|Profils|Définissent les **droits** et les **interfaces**|
|Habilitations|Associent un **profil** à une **entité**|
|Règles d’affectation|Attribution automatique via LDAP (groupes AD)|
|Interfaces|Anonyme, simplifiée, standard|

---

## 🔒 Authentification & LDAP

- Authentification **LDAP** fortement recommandée
- **Habilitations dynamiques** via groupes AD (`GG_GLPI_*`)
- Filtrage des utilisateurs (désactivés / obsolètes)
- Règles d’import **fiables et documentées**

---

## 🖥️ Gestion de parc

### Objets inventoriables

- Ordinateurs, serveurs
- Matériel réseau (switch, firewall…)
- Imprimantes & consommables
- Écrans, téléphones, périphériques divers
- Licences logicielles
- Baies / Datacenter
- Réservations de ressources

### Fonctionnalités avancées

- **Ports réseau & connexions** (cartographie physique)
- **Gabarits** (modèles de saisie accélérés)
- **Plan de nommage** : essentiel en prod

### Commandes utiles

```bash
# Sauvegarde BDD GLPI
mysqldump -u root -p glpidata > /var/backups/glpidata-$(date +%F).sql
```

---

## 🎟️ Gestion des tickets (Assistance)

### Flux d’entrée

|Flux|Moyen|
|---|---|
|Interface anonyme|URL publique|
|Interface simplifiée|Compte utilisateur|
|Interface standard|Compte technicien|
|Collecteur mail|IMAP/POP3|
|API|Intégration externe|

### Cycle de vie typique

```text
Nouveau → En cours → Résolu → Clos
```

### Structuration recommandée

1️⃣ Catégories cohérentes  
2️⃣ Gabarits de tickets (incident / demande)  
3️⃣ Calendriers de service  
4️⃣ SLA (délais de prise en charge et résolution)  
5️⃣ Règles métier → automatisation des tickets

### Commandes SQL utiles

```sql
-- Utilisateurs
SELECT name, firstname FROM glpi_users ORDER BY name;

-- Tickets ouverts
SELECT id, name, status FROM glpi_tickets WHERE status < 6;
```

---

## 🔄 Plug-ins

### FusionInventory

- Inventaire **automatique** : matériel / logiciels / réseau / SNMP
- Communication agent → GLPI en HTTP
- **Règles d’import** cruciales pour maîtriser le volume
- Cohérence avec l’inventaire manuel

### Data Injection

- Import **ponctuel** de données via CSV
- Idéal pour migration initiale ou imports spécifiques
- Pas destiné à remplacer FusionInventory !

### Marketplace

- Simplifie l’installation et la gestion des plugins
- Vérification des compatibilités à chaque **mise à jour GLPI**

---

## 📌 Bonnes pratiques professionnelles

### Installation & maintenance

- Installer **les plugins compatibles** avec ta version GLPI
- Vérifier les droits sur `/var/www/glpi/plugins` → `www-data`
- Documenter les versions / changelogs des plugins
- **Sauvegarder la base** avant toute mise à jour majeure

### Gestion de parc

- Plan de nommage **standardisé**
- Gabarits pour limiter les erreurs
- **Connexions réseau à jour** → indispensable pour audit
- Cohérence avec les données **réseau & AD**

### Assistance

- Structurer les **catégories de tickets** avant les gabarits
- Automatiser **via règles métier** (éviter surcharge manuelle)
- Construire des SLA **atteignables** selon capacité réelle de l’équipe
- Vérifier les escalades avant prod

### Supervision / surveillance

- **Surveiller la santé de FusionInventory** (logs + cohérence des remontées)
- Auditer régulièrement :
    - Agents actifs / inactifs
    - Coût réseau (scan SNMP)
    - Cohérence utilisateurs ↔ matériel

### Sauvegardes

- Planifier une **sauvegarde quotidienne** de `glpidata`
- Sauvegarder aussi `/var/lib/glpi` (fichiers liés)

---

## ⚠️ Pièges à éviter

- Modifier les gabarits pour **ajouter une logique métier** (mauvais usage → utiliser les règles métier)
- Lancer un **scan SNMP non maîtrisé** → surcharge réseau
- Activer **trop de tâches FusionInventory** sur les postes (maîtriser le volume)
- Utiliser un agent FusionInventory **non compatible**
- Ne pas gérer les versions des plugins lors d’une mise à jour GLPI
- Oublier de **supprimer les comptes par défaut** (ex: `tech`, `normal`)
- Oublier d’auditer les **règles d’affectation LDAP**

---

## ✅ À retenir pour les révisions

- GLPI est un outil complet **ITSM** extensible par plugins
- Une bonne **structuration initiale** = clé d’une utilisation pro réussie
- L’**automatisation** (LDAP, règles métier, FusionInventory) est indispensable en production
- Une documentation **à jour** des processus et des règles est nécessaire pour la maintenabilité
- Le cycle d’un ticket est structuré, piloté par les **SLA**
- **Surveiller et superviser** l’ensemble de la solution (agents, volumes, cohérence)