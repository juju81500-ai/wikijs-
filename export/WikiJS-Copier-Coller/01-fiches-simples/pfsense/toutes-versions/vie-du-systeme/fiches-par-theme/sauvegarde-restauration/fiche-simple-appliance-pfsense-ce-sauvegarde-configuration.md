# 📄 Fiche_Simple_-_Appliance_pfSense_CE_Sauvegarde_Configuration.md

- **Environnement** : pfSense CE sur VM Proxmox VE ou appliance dédiée, dépôt de sauvegarde hors pare-feu
- **OS / Version** : pfSense CE 2.x (base FreeBSD) - Toutes-versions
- **Catégorie** : Sauvegarde / Configuration

---

## 🎯 Problème précis à résoudre
Exporter la configuration complète de pfSense CE sous forme chiffrée, conserver la copie hors de l'appliance, et disposer d'une procédure de restauration qui ne compromet pas la production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ouvrir l'export de configuration :
   `Diagnostics > Backup & Restore` (onglet Backup/Restore) : Backup area = `All configuration`
   👉 Explication : Exporte l'ensemble du fichier `/cf/conf/config.xml` : interfaces, règles, alias, utilisateurs, VPN.
2. Chiffrer l'export avant téléchargement :
   cocher `Encrypt this configuration file`, saisir une phrase de passe d'au moins 16 caractères, puis cliquer `Download configuration as XML`
   👉 Explication : Le fichier contient des secrets (clés VPN, certificats privés). Sans chiffrement, il est lisible en clair.
3. Calculer l'empreinte du fichier téléchargé sur le poste d'administration :
   `sha256sum <fichier_config_telecharge>.xml`
   👉 Explication : L'empreinte est notée dans le dossier d'exploitation pour vérifier l'intégrité lors d'une restauration.
4. Contrôler la configuration active depuis la console (option 8 Shell) :
   `ls -l /cf/conf/config.xml && sha256 -q /cf/conf/config.xml`
   👉 Explication : Confirme la taille, la date et l'empreinte de la configuration en cours.
5. Consulter l'historique local des révisions :
   `ls -l /cf/conf/backup/`
   👉 Explication : pfSense conserve des copies horodatées de la configuration à chaque modification. Elles complètent l'export manuel.

---

## ⚡ 2. Production — Façon Simplifiée
1. Exporter la configuration chiffrée avant chaque changement majeur (règles, mise à jour, ajout d'interface) :
   `Diagnostics > Backup & Restore` : Encrypt this configuration file, puis `Download configuration as XML`
   👉 Explication : Garantit un point de retour arrière daté juste avant la modification.
2. Copier l'export chiffré hors de l'appliance depuis le shell :
   `openssl enc -aes-256-cbc -pbkdf2 -salt -in /cf/conf/config.xml -out /root/config-$(date +%F).xml.enc`
   `scp /root/config-$(date +%F).xml.enc <utilisateur_backup>@<serveur_sauvegarde>:/srv/backup/pfsense/`
   👉 Explication : Chiffre une copie de la configuration puis la transfère vers un serveur de sauvegarde. Supprimer ensuite le fichier local : `rm /root/config-*.xml.enc`.
3. Planifier une revue mensuelle des sauvegardes :
   `Diagnostics > Backup & Restore` et contrôle du dossier `<serveur_sauvegarde>:/srv/backup/pfsense/`
   👉 Explication : pfSense CE ne propose pas de sauvegarde automatique distante (fonction réservée à pfSense Plus). La planification relève donc de l'exploitation.

---

## 🔒 3. Production — Façon Sécurisée
1. Stocker la phrase de passe de chiffrement dans le coffre-fort, séparément des sauvegardes :
   `<coffre_secrets>` (Vaultwarden, KeePass ou HashiCorp Vault)
   👉 Explication : Une sauvegarde chiffrée dont la phrase de passe est sur la même machine ne protège de rien.
2. Conserver plusieurs générations de sauvegardes hors de l'appliance :
   `ls -lt /srv/backup/pfsense/` sur `<serveur_sauvegarde>`
   👉 Explication : Permet de revenir à une configuration antérieure si une erreur n'est détectée qu'après plusieurs jours.
3. Restaurer uniquement sur une appliance de même version majeure et après test :
   `Diagnostics > Backup & Restore > Restore Configuration` : Choose File = `<fichier_chiffre>`, Encrypted configuration password = `<phrase_de_passe>`, Restore area = `All configuration`
   👉 Explication : La restauration remplace la configuration et redémarre l'appliance. Garder une console (hors bande ou console Proxmox) ouverte pendant l'opération, car une interface peut changer de nom ou d'adresse.