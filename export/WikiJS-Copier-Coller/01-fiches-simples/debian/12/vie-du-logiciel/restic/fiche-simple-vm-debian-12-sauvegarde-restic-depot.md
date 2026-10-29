# 📄 VM_Debian_12_Sauvegarde_Restic-Depot.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sauvegarde & Données / Dépôt Restic chiffré

## 🎯 Problème précis à résoudre
Créer un dépôt de sauvegarde chiffré avec `restic` sur Debian 12, y enregistrer les répertoires de configuration et de données, contrôler son intégrité et appliquer une politique de rétention.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de restic :
   `sudo apt-get update && sudo apt-get install -y restic`
   👉 Explication : Installe `restic`, outil de sauvegarde chiffrée et dédupliquée disponible dans les dépôts Debian 12.
2. Vérification de la version :
   `restic version`
   👉 Explication : Confirme la version installée, à noter dans la fiche serveur.
3. Création du répertoire du dépôt de test :
   `sudo install -d -m 700 <chemin_depot>`
   👉 Explication : Crée le dossier de destination (disque secondaire, NFS ou point de montage dédié) avec des droits réservés à root.

---

## ⚡ 2. Production — Façon Simplifiée
1. Génération du mot de passe du dépôt, accessible à root uniquement :
   `sudo sh -c 'umask 077; openssl rand -base64 32 > /root/.restic-pass'`
   👉 Explication : Crée un mot de passe aléatoire de 256 bits dans `/root/.restic-pass`. Ce mot de passe doit aussi être stocké dans le coffre-fort de l'entreprise, sinon le dépôt est irrécupérable.
2. Initialisation du dépôt chiffré :
   `sudo restic -r <chemin_depot> --password-file /root/.restic-pass init`
   👉 Explication : Crée la structure du dépôt et sa clé de chiffrement AES-256 protégée par le mot de passe.
3. Première sauvegarde :
   `sudo restic -r <chemin_depot> --password-file /root/.restic-pass backup /etc /home --tag quotidien`
   👉 Explication : Enregistre un instantané des dossiers `/etc` et `/home`, étiqueté pour la rétention.

---

## 🔒 3. Production — Façon Sécurisée (Intégrité & Rétention)
1. Consultation des instantanés :
   `sudo restic -r <chemin_depot> --password-file /root/.restic-pass snapshots`
   👉 Explication : Liste les sauvegardes disponibles avec identifiant, date, nom d'hôte et chemins.
2. Vérification de l'intégrité du dépôt :
   `sudo restic -r <chemin_depot> --password-file /root/.restic-pass check`
   👉 Explication : Contrôle la cohérence des index et des paquets ; à lancer régulièrement, et après tout incident disque.
3. Application de la rétention et purge :
   `sudo restic -r <chemin_depot> --password-file /root/.restic-pass forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune`
   👉 Explication : Conserve 7 quotidiens, 4 hebdomadaires et 6 mensuels, puis supprime physiquement les données devenues inutiles.