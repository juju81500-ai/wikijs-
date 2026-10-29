# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Sécuriser le compte root.

## 1. Hors-Production (Lab / Test / POC)

1. Définir un mot de passe fort pour root (ou verrouiller le compte) :
   ```bash
   sudo passwd root
   ```
   👉 Explication : dans anaconda, choisir « Verrouiller le compte root » si un administrateur wheel existe.

2. Contrôler l'état du compte :
   ```bash
   sudo passwd -S root
   ```
   👉 Explication : `PS` signifie mot de passe défini, `LK` verrouillé.

3. Interdire la connexion SSH directe de root :
   ```bash
   echo 'PermitRootLogin no' | sudo tee /etc/ssh/sshd_config.d/10-root.conf
   sudo sshd -t && sudo systemctl reload sshd
   ```
   👉 Explication : limite la surface d'attaque; `sshd -t` teste la syntaxe.

## 2. Production — Contrôles

Stocker le secret de secours dans un coffre-fort, jamais en clair.

## 3. Production — Sécurité

Ne pas utiliser root au quotidien; passer par `sudo`.

## Validation et retour arrière

- **Validation** : Connexion SSH root refusée, root accessible en console seulement.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
