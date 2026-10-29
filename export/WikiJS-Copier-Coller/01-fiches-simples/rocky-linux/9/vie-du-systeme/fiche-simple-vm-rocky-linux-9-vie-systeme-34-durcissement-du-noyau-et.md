# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Ajuster les paramètres noyau.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier sysctl :
   ```bash
   sudo tee /etc/sysctl.d/90-durcissement.conf >/dev/null <<'EOT'
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.tcp_syncookies = 1
   kernel.kptr_restrict = 2
   kernel.dmesg_restrict = 1
   EOT
   ```
   👉 Explication : filtre l'usurpation, ignore les redirections et masque les adresses noyau.

2. Appliquer sans redémarrer :
   ```bash
   sudo sysctl --system
   ```
   👉 Explication : recharge tous les fichiers.

3. Contrôler une valeur :
   ```bash
   sysctl net.ipv4.tcp_syncookies
   ```
   👉 Explication : doit renvoyer `1`.

## 2. Production — Contrôles

Documenter chaque paramètre modifié.

## 3. Production — Sécurité

Ne pas activer `ip_forward` sans besoin de routage.

## Validation et retour arrière

- **Validation** : Les valeurs actives correspondent au fichier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)