# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_45_Analyse_Des_Journaux_D

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 45 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Repérer les anomalies.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les erreurs du démarrage :
   ```bash
   sudo journalctl -b -p err --no-pager
   ```
   👉 Explication : erreurs depuis le dernier boot.

2. Rechercher les refus SELinux :
   ```bash
   sudo ausearch -m avc -ts recent
   sudo sealert -a /var/log/audit/audit.log
   ```
   👉 Explication : `sealert` (paquet `setroubleshoot-server`) propose des corrections.

3. Rechercher les échecs d'authentification :
   ```bash
   sudo journalctl -u sshd --since today | grep -i failed
   ```
   👉 Explication : détecte les attaques.

## 2. Production — Contrôles

Mettre en place des alertes sur les erreurs critiques.

## 3. Production — Sécurité

Protéger l'accès aux journaux (données personnelles).

## Validation et retour arrière

- **Validation** : Chaque erreur est expliquée ou corrigée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)