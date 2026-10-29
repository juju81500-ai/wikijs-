# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Systeme_Timezone_Locale

- **Environnement** : VM ou serveur Ubuntu (installation Subiquity ou image cloud-init)
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Système / Fuseau horaire et langue

---

## 🎯 Problème précis à résoudre

Régler le fuseau horaire (Europe/Paris), la synchronisation NTP et la locale française UTF-8 d'un serveur Ubuntu 26.04, pour que les journaux, les tâches planifiées et les messages des services soient horodatés et lisibles de façon cohérente.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Relever l'état horaire actuel :
```bash
timedatectl status
```
👉 Explication : Affiche l'heure locale, l'heure UTC, le fuseau, l'état de la synchronisation NTP et le mode de l'horloge matérielle (RTC).

2. Définir le fuseau horaire :
```bash
sudo timedatectl set-timezone Europe/Paris
```
👉 Explication : Crée le lien `/etc/localtime` vers la base `tzdata`. L'horloge matérielle reste en UTC, ce qui est le comportement attendu sous Linux.

3. Installer les locales et générer la locale française :
```bash
sudo apt update
sudo apt install -y locales
sudo locale-gen fr_FR.UTF-8
```
👉 Explication : Le paquet `locales` fournit `locale-gen`. Sans lui, la locale demandée n'existe pas sur le système.

4. Appliquer la locale par défaut :
```bash
sudo localectl set-locale LANG=fr_FR.UTF-8
localectl status
```
👉 Explication : `localectl` écrit la variable `LANG` dans `/etc/default/locale`. La nouvelle valeur est effective pour les prochaines sessions (ouvrir une nouvelle connexion SSH).

## ⚡ 2. Production — Façon Simplifiée

1. Activer la synchronisation NTP en vérifiant d'abord le client utilisé :
```bash
systemctl status chrony --no-pager
chronyc tracking
```
👉 Explication : Sur Ubuntu 26.04, Chrony est le client NTP par défaut. Si Chrony est actif, ne pas lancer `timedatectl set-ntp true` en parallèle : deux clients NTP sur la même machine se disputent l'horloge.

2. Contrôler la dérive réelle de l'horloge :
```bash
chronyc sources -v
```
👉 Explication : Chaque source doit apparaître. Une source marquée `^*` est celle utilisée ; `^?` signale une source non joignable.

## 🔒 3. Production — Façon Sécurisée

1. Vérifier que l'horloge matérielle reste en UTC :
```bash
timedatectl show --property=LocalRTC
```
👉 Explication : La valeur doit être `LocalRTC=no`. Une RTC en heure locale fausse les horodatages lors des changements d'heure d'été et complique la corrélation des journaux.

2. Vérifier la présence des locales utilisées :
```bash
locale -a | grep -i fr
```
👉 Explication : Confirme que `fr_FR.utf8` est disponible avant de l'imposer aux services qui en dépendent.

## ✅ Validation et retour arrière

- **Précontrôles** : accès console, serveur NTP interne ou externe autorisé par le pare-feu (UDP 123).
- **Validation** : `timedatectl status` affiche `Europe/Paris`, `System clock synchronized: yes`, et `chronyc tracking` indique une référence valide.
- **Retour arrière** : `sudo timedatectl set-timezone <ancien_fuseau>` ; `sudo localectl set-locale LANG=<ancienne_locale>`.