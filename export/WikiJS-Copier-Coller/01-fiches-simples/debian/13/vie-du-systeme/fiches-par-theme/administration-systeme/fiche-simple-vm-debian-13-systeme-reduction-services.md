# 📄 Fiche_Simple_-_VM_Debian_13_Systeme_Reduction_Services

- **Environnement** : VM ou serveur Debian 13 en production
- **OS / Version** : Debian 13 (Trixie) avec systemd - Famille Debian
- **Catégorie** : Système & Services / Réduction de la surface d'attaque

## 🎯 Problème précis à résoudre
Identifier les services systemd en écoute ou démarrés automatiquement mais inutiles au rôle du serveur, puis les désactiver, les masquer et retirer leurs paquets sur Debian 13, sans couper les services nécessaires (SSH, journald, chrony, pare-feu).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les services activés au démarrage et les ports en écoute :
   ```bash
   systemctl list-unit-files --type=service --state=enabled --no-pager
   sudo ss -tulnp
   ```
   👉 Explication : La première commande liste les services qui démarrent avec la machine ; la seconde associe chaque port TCP/UDP en écoute à son processus. Un service sans rôle défini doit être justifié ou supprimé.

2. Vérifier les dépendances avant de désactiver un service :
   ```bash
   systemctl list-dependencies --reverse <service_inutile>
   systemctl is-enabled <service_inutile>
   ```
   👉 Explication : La commande inverse liste les unités qui dépendent du service ; si une unité métier en dépend, le retrait doit être replanifié.

3. Désactiver et arrêter le service en test, puis vérifier :
   ```bash
   sudo systemctl disable --now <service_inutile>
   systemctl is-active <service_inutile>
   sudo ss -tulnp
   ```
   👉 Explication : `disable --now` retire le démarrage automatique et arrête l'unité. `is-active` doit répondre `inactive`, et le port associé doit disparaître de la liste.

---

## ⚡ 2. Production — Façon Simplifiée
1. Désactiver les services identifiés comme inutiles au rôle, en conservant une liste de référence :
   ```bash
   sudo systemctl disable --now <service_inutile_1> <service_inutile_2>
   ```
   👉 Explication : Limiter la liste à des noms justifiés par l'inventaire du serveur. Ne jamais désactiver `ssh`, `systemd-journald`, `chrony` ou `nftables` sur un serveur qui les utilise.

2. Vérifier l'état global du système après la modification :
   ```bash
   systemctl --failed --no-pager
   sudo ss -tulnp
   ```
   👉 Explication : Aucun service métier ne doit apparaître en échec, et seuls les ports attendus doivent rester ouverts.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Masquer les unités inutiles pour empêcher leur démarrage manuel ou par dépendance :
   ```bash
   sudo systemctl mask <service_inutile>
   systemctl is-enabled <service_inutile>
   ```
   👉 Explication : `mask` lie l'unité à `/dev/null` dans `/etc/systemd/system/`. La commande `is-enabled` doit alors afficher `masked`.

2. Retirer les paquets qui ne servent plus, plutôt que de seulement les désactiver :
   ```bash
   sudo apt-get purge -y <paquet_inutile>
   sudo apt-get autoremove --purge -y
   ```
   👉 Explication : Un paquet installé reste une surface d'attaque, même désactivé. La purge supprime aussi les fichiers de configuration du paquet.

3. Prévoir le retour arrière en cas de besoin réel :
   ```bash
   sudo systemctl unmask <service_inutile>
   sudo systemctl enable --now <service_inutile>
   ```
   👉 Explication : Permet de rétablir le service à l'identique, après la vérification de ses dépendances.