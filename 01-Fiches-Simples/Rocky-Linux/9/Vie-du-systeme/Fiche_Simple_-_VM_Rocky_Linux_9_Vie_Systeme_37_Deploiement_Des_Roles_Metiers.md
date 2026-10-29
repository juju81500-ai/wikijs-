# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Installer le rôle attendu.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le paquet du rôle (exemple web) :
   ```bash
   sudo dnf install -y nginx
   sudo systemctl enable --now nginx
   ```
   👉 Explication : installe et démarre le service.

2. Ouvrir le flux dans firewalld :
   ```bash
   sudo firewall-cmd --permanent --add-service=https
   sudo firewall-cmd --reload
   ```
   👉 Explication : autorise uniquement HTTPS.

3. Autoriser le rôle dans SELinux si nécessaire :
   ```bash
   sudo setsebool -P httpd_can_network_connect on
   ```
   👉 Explication : booléen permanent pour un proxy inverse.

## 2. Production — Contrôles

Déployer avec un outil de configuration (Ansible) pour la reproductibilité.

## 3. Production — Sécurité

Un rôle par machine quand c'est possible.

## Validation et retour arrière

- **Validation** : Le service répond sur le port prévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Pile Web Configurer Nginx PHP FPM](<../Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Configurer_Nginx_PHP_FPM.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
