# 📄 Fiche_Simple_-_VM_Rocky_9_Securite_Autoriser_Port_Web_SELinux_Firewalld.md

- **Environnement** : VM Rocky Linux 9 exécutant un service web sur un port personnalisé
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec SELinux et firewalld
- **Catégorie** : Sécurité / Réseau

## 🎯 Problème précis à résoudre
Autoriser un service HTTP sur un port TCP personnalisé en déclarant le port SELinux approprié et une règle firewalld persistante et limitée.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Confirmer le port d'écoute réel, l'état SELinux et la zone firewalld :
   ```bash
   sudo ss -lntp
   getenforce
   sudo firewall-cmd --get-active-zones
   ```
2. Vérifier si SELinux autorise déjà ce port pour le type web :
   ```bash
   sudo semanage port -l | grep http_port_t
   ```
   👉 *Explication : une règle firewalld seule ne suffit pas si SELinux refuse au serveur web l'utilisation de ce port.*

## ⚡ 2. Production — Façon Simplifiée
1. Installer l'outil de gestion SELinux si nécessaire, puis ajouter le port uniquement s'il n'est pas déjà défini :
   ```bash
   sudo dnf install policycoreutils-python-utils
   sudo semanage port -a -t http_port_t -p tcp 8081
   ```
   Si le port existe déjà avec un type différent, examiner l'usage avant toute modification; ne pas remplacer son type à l'aveugle.
2. Ajouter la règle dans la zone réellement utilisée par l'interface, en limitant la source au réseau autorisé :
   ```bash
   sudo firewall-cmd --get-active-zones
   sudo firewall-cmd --permanent --zone=public --add-rich-rule='rule family="ipv4" source address="192.0.2.0/24" port port="8081" protocol="tcp" accept'
   sudo firewall-cmd --check-config
   sudo firewall-cmd --reload
   ```
3. Vérifier la règle et le service :
   ```bash
   sudo firewall-cmd --zone=public --list-all
   sudo semanage port -l | grep http_port_t
   sudo ss -lntp
   ```
   👉 *Explication : remplacer `public`, `8081` et le réseau documentaire `192.0.2.0/24` par les valeurs validées de l'environnement.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas ouvrir le port à `0.0.0.0/0` si seuls des clients internes doivent joindre le service.
2. Conserver SELinux en `Enforcing`; examiner les refus AVC plutôt que désactiver SELinux.
3. Ouvrir uniquement le protocole et le port réellement utilisés et éviter les règles temporaires non documentées.

## ✅ Validation et retour arrière
- Tester le port depuis une machine appartenant au réseau autorisé puis depuis une source non autorisée; confirmer les résultats attendus.
- Retirer la rich rule exacte avec `--remove-rich-rule`, vérifier la syntaxe, puis recharger firewalld.
- Ne supprimer le mapping SELinux qu'après avoir confirmé qu'aucun autre service n'utilise le port.