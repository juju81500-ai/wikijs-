# 📄 VM_Rocky_9_Utilisateurs_Creer-Utilisateur-Standard-Et-Wheel.md

- **Environnement** : VM / Serveur (Rocky Linux 9 / RHEL 9)
- **OS / Version** : Rocky Linux 9 / RHEL 9 - Famille RedHat
- **Catégorie** : Utilisateurs & Droits / Sudo & Wheel
- **Tags** : `[rocky9]`, `[rhel-family]`, `[utilisateurs]`, `[wheel]`, `[sudo]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Créer un utilisateur restreint et un utilisateur administrateur appartenant au groupe wheel sous Rocky Linux 9 / RHEL 9, et restreindre l'usage de Sudo aux seuls membres du groupe wheel.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer le compte et définir son mot de passe :
   ```bash
   sudo useradd -m user_test
   sudo passwd user_test
   ```
   👉 Explication : `-m` crée le répertoire personnel; le mot de passe est saisi à l'invite.

2. Ajouter au groupe `wheel` (droits sudo) :
   ```bash
   sudo usermod -aG wheel user_test
   id user_test
   ```
   👉 Explication : sur Rocky, `wheel` donne accès à `sudo`; `id` confirme l'appartenance.


---

## ⚡ 2. Production — Façon Simplifiée
1. Créer le compte nominatif :
   ```bash
   sudo useradd -m -c "ADM Jean Dupont" adm-jdupont
   sudo passwd adm-jdupont
   ```
   👉 Explication : remplacer nom et identifiant; `-c` renseigne le nom complet.

2. Donner les droits administrateur :
   ```bash
   sudo usermod -aG wheel adm-jdupont
   ```
   👉 Explication : accès via `sudo`.

3. Ouvrir une nouvelle session en tant que `adm-jdupont`, puis :
   ```bash
   sudo -v
   ```
   👉 Explication : valider le sudo avant de fermer la session de secours.


---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & Wheel Enforcement)
1. Vérifier la configuration sudo existante avec `sudo visudo -c`. Si une règle wheel est nécessaire, créer un fichier dédié avec `sudo visudo -f /etc/sudoers.d/10-wheel` et valider à nouveau ; ne pas écraser la configuration existante par `>`.
2. Pour interdire la connexion root SSH, sauvegarder la configuration, examiner `sshd -T`, éditer un fichier géré sans append répété, valider avec `sshd -t`, recharger `sshd` puis tester une seconde connexion avant de fermer la session.