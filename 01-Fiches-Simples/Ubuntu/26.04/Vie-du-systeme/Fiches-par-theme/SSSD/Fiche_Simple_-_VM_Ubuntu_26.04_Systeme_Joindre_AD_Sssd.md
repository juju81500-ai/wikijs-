# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Systeme_Joindre_AD_Sssd

- **Environnement** : VM Ubuntu intégrée à un domaine Active Directory existant
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Système / Annuaire / Jonction de domaine
- **Tags** : `ubuntu2604`, `realmd`, `sssd`, `active-directory`, `kerberos`, `adcli`

---

## 🎯 Problème précis à résoudre

Joindre un serveur Ubuntu 26.04 à un domaine Active Directory avec `realmd` et `sssd`, pour que les comptes du domaine puissent se connecter en SSH et que seuls les groupes autorisés accèdent à la machine.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier la résolution DNS du domaine (le DNS doit pointer vers un contrôleur de domaine) :
```bash
resolvectl query <domaine_ad>
resolvectl query _ldap._tcp.<domaine_ad>
```
👉 Explication : La jonction échoue si le serveur ne trouve pas les enregistrements SRV du contrôleur. Sur Ubuntu 26.04, la résolution passe par systemd-resolved, qu'il faut configurer avec le DNS AD (Netplan ou `resolvectl dns`).

2. Installer les paquets nécessaires :
```bash
sudo apt update
sudo apt install -y realmd sssd sssd-tools adcli krb5-user samba-common-bin oddjob oddjob-mkhomedir packagekit
```
👉 Explication : `realmd` découvre et joint le domaine, `sssd` fournit l'authentification, `adcli` crée le compte machine, `oddjob-mkhomedir` crée les répertoires personnels au premier login. Vérifier au préalable les noms de paquets avec `apt-cache policy realmd sssd` si un paquet manque.

3. Découvrir le domaine :
```bash
sudo realm discover <domaine_ad>
```
👉 Explication : Affiche le type de domaine, le contrôleur détecté et les logiciels requis. Une sortie vide signale un problème DNS ou réseau (ports 88, 389, 445 vers le DC).

4. Joindre le domaine :
```bash
sudo realm join -U <compte_admin_ad> <domaine_ad>
```
👉 Explication : Crée le compte ordinateur dans l'OU par défaut et génère `/etc/sssd/sssd.conf`. Le mot de passe est demandé de façon interactive, sans l'écrire dans la commande.

5. Vérifier la jonction :
```bash
realm list
id <utilisateur_ad>@<domaine_ad>
```
👉 Explication : `realm list` doit afficher `configured: kerberos-member`. `id` confirme que sssd résout les groupes de l'utilisateur AD.

## ⚡ 2. Production — Façon Simplifiée

1. Activer la création automatique du répertoire personnel :
```bash
sudo pam-auth-update --enable mkhomedir
```
👉 Explication : Ajoute le module PAM qui crée le `$HOME` au premier login d'un utilisateur du domaine, sans intervention manuelle.

2. Restreindre les ouvertures de session à un groupe autorisé :
```bash
sudo realm deny --all
sudo realm permit --groups '<groupe_admins_linux>'
```
👉 Explication : Par défaut, tout utilisateur du domaine peut se connecter. Ces deux commandes ferment l'accès puis l'ouvrent uniquement au groupe désigné.

## 🔒 3. Production — Façon Sécurisée

1. Vérifier les droits du fichier de configuration sssd :
```bash
sudo ls -l /etc/sssd/sssd.conf
```
👉 Explication : Le fichier contient des secrets d'accès ; il doit appartenir à `root` avec les droits `600`. sssd refuse de démarrer si les droits sont plus ouverts.

2. Limiter le cache et les noms longs dans `/etc/sssd/sssd.conf` :
```text
[domain/<domaine_ad>]
use_fully_qualified_names = False
ad_gpo_access_control = enforcing
```
👉 Explication : Ces options se placent dans la section `[domain/<domaine_ad>]` générée par `realm join`, et non dans `[sssd]`. `ad_gpo_access_control = enforcing` applique les GPO de connexion d'AD au serveur Linux. Le nom court (sans domaine) simplifie les ACL, mais vérifier les conflits d'homonymes.

3. Redémarrer sssd et contrôler son état :
```bash
sudo systemctl restart sssd
systemctl status sssd --no-pager
```
👉 Explication : Recharge la configuration après édition manuelle ; un statut `active (running)` confirme que les journaux d'authentification sont accessibles.

## ✅ Validation et retour arrière

- **Précontrôles** : DNS AD fonctionnel, horloge synchronisée (Kerberos tolère environ 5 minutes d'écart), compte administrateur AD dédié à la jonction, console de secours avec compte local.
- **Validation** : `realm list` affiche la configuration ; une connexion SSH avec un compte du groupe autorisé réussit, un compte hors groupe est refusé.
- **Retour arrière** : `sudo realm leave <domaine_ad>` retire la machine du domaine et nettoie `sssd.conf` ; restaurer ensuite les sauvegardes de `/etc/krb5.conf` et `/etc/nsswitch.conf` si elles ont été modifiées.
