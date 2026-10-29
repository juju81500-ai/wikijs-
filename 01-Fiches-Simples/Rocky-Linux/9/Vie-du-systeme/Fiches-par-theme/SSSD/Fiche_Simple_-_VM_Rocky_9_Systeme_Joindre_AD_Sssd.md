# 📄 Fiche_Simple_-_VM_Rocky_9_Systeme_Joindre_AD_Sssd.md

- **Environnement** : VM ou serveur Rocky Linux membre d'un domaine Active Directory
- **OS / Version** : Rocky Linux 9 / RHEL 9 (realmd, sssd, authselect)
- **Catégorie** : Système & Services / Authentification centralisée
- **Tags** : `[rocky9]`, `[rhel9]`, `[realmd]`, `[sssd]`, `[active-directory]`, `[kerberos]`

## 🎯 Problème précis à résoudre
Joindre un serveur Rocky Linux 9 à un domaine Active Directory avec `realmd` et `sssd`, puis vérifier que les comptes du domaine se connectent et que leur répertoire personnel est créé automatiquement.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer les composants de jonction et d'authentification :
   ```bash
   sudo dnf install -y realmd sssd oddjob oddjob-mkhomedir adcli samba-common-tools krb5-workstation
   ```
   👉 Explication : `realmd` découvre et joint le domaine, `sssd` gère l'authentification, `adcli` crée le compte machine dans l'annuaire, `oddjob-mkhomedir` crée le répertoire personnel au premier login.

2. Vérifier que le domaine est découvrable depuis le serveur :
   ```bash
   sudo realm discover <domaine.local>
   ```
   👉 Explication : Interroge les enregistrements DNS SRV du contrôleur de domaine. Si rien n'est retourné, corriger d'abord le DNS (voir la fiche Reseau_DNS_Et_Hosts).

3. Joindre le domaine avec un compte autorisé à créer des objets machine :
   ```bash
   sudo realm join --user=<admin_ad> <domaine.local>
   ```
   👉 Explication : Le mot de passe est demandé de façon interactive. Le compte machine est créé dans l'OU par défaut `Computers`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Joindre le domaine dans une OU dédiée aux serveurs :
   ```bash
   sudo realm join --user=<admin_ad> --computer-ou="OU=Serveurs Linux,DC=<domaine>,DC=<extension>" <domaine.local>
   ```
   👉 Explication : Sépare les serveurs Linux des postes utilisateurs, ce qui permet d'appliquer des stratégies de groupe dédiées. Le nom de l'OU doit exister au préalable.

2. Activer la création automatique du répertoire personnel et le service `oddjobd` :
   ```bash
   sudo authselect select sssd with-mkhomedir --force
   sudo systemctl enable --now oddjobd
   ```
   👉 Explication : `authselect` configure PAM pour `sssd`. Sans `with-mkhomedir`, l'utilisateur AD se connecte mais n'a pas de répertoire personnel.

3. Vérifier la jonction et la résolution d'un compte du domaine :
   ```bash
   sudo realm list
   id <utilisateur_ad>
   ```
   👉 Explication : `realm list` affiche le domaine, le type de bail et les services configurés. `id` doit retourner les groupes AD de l'utilisateur.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restreindre les connexions à un groupe AD dédié (ici le groupe des administrateurs Linux) :
   ```bash
   sudo realm deny --all
   sudo realm permit --groups "<groupe_ssh_linux>"
   ```
   👉 Explication : Par défaut, tous les comptes du domaine peuvent ouvrir une session. La liste blanche limite l'accès au groupe désigné. La syntaxe exacte de `--groups` dépend de la version de realmd; vérifier avec `realm permit --help`.

2. Vérifier l'état réel de sssd et de la connexion aux contrôleurs de domaine :
   ```bash
   sudo sssctl domain-status <domaine.local>
   sudo journalctl -u sssd -p warning --no-pager -n 50
   ```
   👉 Explication : `domain-status` indique si le serveur est en ligne et quel contrôleur est utilisé. Le journal `sssd` révèle les erreurs Kerberos ou LDAP.

3. Imposer le chiffrement des échanges LDAP en gardant `ldap_id_use_start_tls` et la validation des certificats dans `/etc/sssd/sssd.conf` (voir la documentation sssd de la version installée) :
   ```bash
   sudo grep -E '^(ad_domain|use_fully_qualified_names|ldap_id_mapping|ldap_tls)' /etc/sssd/sssd.conf
   ```
   👉 Explication : Les identifiants et le trafic Kerberos ne doivent jamais transiter en clair. Vérifier que les options TLS ne sont pas désactivées.

---

## ✅ Contrôle
```bash
sudo realm list
```
👉 Explication : Le domaine doit apparaître avec `configured: kerberos-member`. Se connecter ensuite avec un compte autorisé par `realm permit`.
