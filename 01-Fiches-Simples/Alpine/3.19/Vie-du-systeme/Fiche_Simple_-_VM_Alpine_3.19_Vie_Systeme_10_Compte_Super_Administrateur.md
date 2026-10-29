# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Sécuriser le compte `root`.

## 1. Hors-Production (Lab / Test / POC)

1. Définir un mot de passe long et unique pour `root` :
   ```sh
   passwd root
   ```
   👉 Explication : stocke le mot de passe haché dans `/etc/shadow` (l'ISO live n'en a pas).

2. Contrôler l'état des comptes à mot de passe :
   ```sh
   doas awk -F: '$2 ~ /^[!*]/ {print $1": verrouillé"} $2 !~ /^[!*]/ {print $1": mot de passe défini"}' /etc/shadow | head
   ```
   👉 Explication : identifie les comptes utilisables; seuls les comptes réellement nécessaires doivent avoir un mot de passe.

3. Interdire la connexion SSH de `root` (Alpine autorise `root` par clé seulement par défaut) :
   ```sh
   doas grep -E '^#?PermitRootLogin' /etc/ssh/sshd_config
   ```
   👉 Explication : affiche la valeur courante; la valeur cible `no` est posée à l'étape 27.

## 2. Production — Contrôles

Stocker le mot de passe `root` dans le coffre de l'entreprise; l'utiliser uniquement en dépannage.

## 3. Production — Sécurité

Aucun mot de passe en clair dans un ticket ni dans le runbook.

## Validation et retour arrière

- **Validation** : Connexion `root` testée sur la console et refusée à distance.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
