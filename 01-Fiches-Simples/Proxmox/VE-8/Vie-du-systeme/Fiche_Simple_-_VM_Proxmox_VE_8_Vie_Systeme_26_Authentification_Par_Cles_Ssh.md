# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-26`

---

## Problème précis à résoudre

Remplacer le mot de passe SSH par des clés.

## 1. Hors-Production (Lab / Test / POC)

1. Sur le poste d'administration, générer une clé et la copier (remplacer `ADMIN1` et `IP_HOTE`) :
   ```bash
   ssh-keygen -t ed25519 -C "admin1@poste"
   ssh-copy-id ADMIN1@IP_HOTE
   ```
   👉 Explication : crée la clé; `ssh-copy-id` la dépose dans `~/.ssh/authorized_keys`.

2. Pour root, la clé est dans `/etc/pve/priv/authorized_keys` (partagée dans le cluster) :
   ```bash
   ls -l /root/.ssh/authorized_keys
   ```
   👉 Explication : ce fichier est un lien vers `/etc/pve/priv/authorized_keys`; ne pas le casser.

3. Tester la connexion par clé dans une 2e session avant de désactiver le mot de passe.
   ```bash
   ssh ADMIN1@IP_HOTE
   ```
   👉 Explication : évite de se verrouiller hors de l'hôte.

## 2. Production — Contrôles

Clés protégées par phrase secrète; une clé par administrateur.

## 3. Production — Sécurité

Interdire la connexion par mot de passe à l'étape suivante.

## Validation et retour arrière

- **Validation** : Connexion par clé réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
