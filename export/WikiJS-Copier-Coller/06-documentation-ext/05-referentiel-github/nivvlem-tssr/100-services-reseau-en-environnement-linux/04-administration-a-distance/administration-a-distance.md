# Administration à distance (Linux / Debian)

## 🔑 Le protocole SSH (Secure Shell)

### 🔹 Avantages

- Connexion distante **sécurisée** (chiffrement, authentification)
- Accès **ligne de commande** au système distant
- Possibilité de **copier** des fichiers (via `scp`, `rsync`, `sftp`)

### 🔹 Installation (Debian)

```bash
sudo apt update && sudo apt install openssh-server
```

### 🔹 Vérification du service

```bash
systemctl status ssh
```

### 🔹 Connexion depuis une autre machine

```bash
ssh nom_utilisateur@adresse_ip
```

### 🔹 Sécurisation de SSH (bonnes pratiques)

- Fichier : `/etc/ssh/sshd_config`
- Exemples :
    - Désactiver l’accès root : `PermitRootLogin no`
    - Restreindre à certains utilisateurs : `AllowUsers user1 user2`
    - Forcer l’usage de clés : `PasswordAuthentication no`

Redémarrage du service après modification :

```bash
systemctl restart ssh
```

---

## 🎨 Accès distant graphique – VNC

### 🔹 Utilisation

- Permet un **accès à l’environnement graphique** d’un poste à distance (ex : CLI-DB-12)
- Utilisable en parallèle d’un accès SSH

### 🔹 Installation

```bash
sudo apt install tigervnc-standalone-server tigervnc-viewer
```

### 🔹 Configuration VNC

1. Définir un mot de passe VNC :

```bash
vncpasswd
```

2. Lancer un serveur VNC pour l’utilisateur :

```bash
vncserver
```

- Premier lancement crée `~/.vnc/xstartup`

3. Éditer le fichier `xstartup` pour charger l’environnement graphique :

```bash
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startlxsession   # pour LXDE (ou autre selon DE)
```

Rendre exécutable :

```bash
chmod +x ~/.vnc/xstartup
```

4. Redémarrer VNC :

```bash
vncserver -kill :1
vncserver :1
```

### 🔹 Connexion au bureau à distance

- Utiliser un **client VNC** (TigerVNC Viewer, Remmina, etc.)
- Adresse IP : `IP_du_poste:5901` ou `IP_du_poste:1`

---

## ✅ À retenir pour les révisions

- SSH est le **standard pour l’administration distante sécurisée** en mode texte
- Le fichier `/etc/ssh/sshd_config` permet de **restreindre et sécuriser l’accès**
- VNC permet une **prise en main graphique**, mais moins sécurisée (préférer avec tunnel SSH)
- Toujours tester SSH **avant** d’installer/configurer VNC
- Utiliser des **comptes non-root**, avec sudo pour les opérations d’administration

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Ne jamais autoriser le login root SSH|Limite l’exposition directe d’un compte critique|
|Utiliser des clés SSH|Authentification plus robuste que le mot de passe|
|Ouvrir le port SSH seulement si nécessaire|Réduire la surface d’attaque|
|Tunneler VNC dans SSH si en production|Garantir le chiffrement des flux|
|Activer et tester l’accès SSH avant modification critique|Pour éviter toute perte d’accès à distance|