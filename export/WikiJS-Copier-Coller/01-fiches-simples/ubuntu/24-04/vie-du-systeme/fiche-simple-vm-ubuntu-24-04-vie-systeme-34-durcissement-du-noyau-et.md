# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler sysctl.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier de réglages :
   ```bash
   sudo tee /etc/sysctl.d/90-durcissement.conf >/dev/null <<'EOT'
   net.ipv4.tcp_syncookies = 1
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.ip_forward = 0
   EOT
   ```
   👉 Explication : durcit la pile IP (mettre `ip_forward = 1` seulement pour un routeur).

2. Appliquer :
   ```bash
   sudo sysctl --system
   sysctl net.ipv4.tcp_syncookies
   ```
   👉 Explication : recharge et affiche la valeur.

## 2. Production — Contrôles

Tester chaque réglage : `ip_forward` casse Docker et les routeurs.

## 3. Production — Sécurité

Documenter tout écart au référentiel.

## Validation et retour arrière

- **Validation** : `sysctl` renvoie les valeurs attendues.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)