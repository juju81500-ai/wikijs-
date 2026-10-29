# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-26`

---

## Problème précis à résoudre

Remplacer les mots de passe par des clés.

## 1. Hors-Production (Lab / Test / POC)

1. Générer une clé Ed25519 sur le poste d'administration :
   ```sh
   ssh-keygen -t ed25519 -C 'ADMIN@POSTE'
   ```
   👉 Explication : crée la paire de clés (`~/.ssh/id_ed25519`); protéger par une phrase secrète.

2. Copier la clé publique sur le serveur (remplacer `ADMIN` et `ADRESSE_IP`) :
   ```sh
   ssh-copy-id -i ~/.ssh/id_ed25519.pub ADMIN@ADRESSE_IP
   ```
   👉 Explication : ajoute la clé dans `~/.ssh/authorized_keys` du compte.

3. Tester la connexion sans mot de passe :
   ```sh
   ssh ADMIN@ADRESSE_IP 'id'
   ```
   👉 Explication : doit répondre sans demander le mot de passe du compte.

## 2. Production — Contrôles

Une clé par administrateur, retirée au départ de la personne.

## 3. Production — Sécurité

Ne jamais copier de clé privée sur un serveur.

## Validation et retour arrière

- **Validation** : Connexion par clé fonctionnelle.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](<../Vie-du-logiciel/OpenSSH/Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
