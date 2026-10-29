# Réparer un disque Linux presque plein

### ❓ Question
Comment retrouver la cause d'une saturation et libérer de l'espace sans supprimer de données utiles ?

---

### 📋 Procédure Pas-à-Pas (1 Commande = 1 Explication Technique)

1. **Vérifier blocs et inodes** :
   ```bash
   df -hT
   df -i
   ```
   👉 *Explication : Distingue saturation en capacité et saturation du nombre de fichiers, et repère le point de montage concerné.*

2. **Localiser la consommation sur le système de fichiers concerné** :
   ```bash
   sudo du -xhd1 /var 2>/dev/null | sort -h
   sudo lsof +L1
   ```
   👉 *Explication : La première commande compare les sous-répertoires sans franchir de montage ; `lsof` repère les fichiers supprimés encore ouverts.*

3. **Nettoyer uniquement le cache APT identifié** :
   ```bash
   sudo apt clean
   sudo apt autoremove --dry-run
   ```
   👉 *Explication : `apt clean` retire les archives téléchargées. Examiner la simulation avant toute suppression de paquets ; ne pas lancer `autoremove --purge -y` en urgence.*

4. **Contrôler et réduire les journaux si nécessaire** :
   ```bash
   journalctl --disk-usage
   sudo journalctl --vacuum-time=14d
   journalctl --disk-usage
   ```
   👉 *Explication : Vérifier les exigences de rétention avant la purge ; préférer une durée explicitement approuvée à une taille arbitraire.*

5. Si un fichier supprimé est encore ouvert, identifier son service dans `lsof +L1` et recharger/redémarrer ce service dans une fenêtre adaptée. Ne pas supprimer de fichiers inconnus dans `/var/lib`, `/var/log` ou les répertoires de bases de données.

---

### ⚙️ Matrice des 3 Modes d'Exécution

| Mode | Gestion Disque | Maintenance Préventive |
| :--- | :--- | :--- |
| **🧪 Hors-Prod** | Diagnostic manuel et nettoyage ciblé. | Vérifier le résultat après chaque action. |
| **⚡ Production** | Seuils d'alerte adaptés aux partitions et à la croissance. | Rétention journaux définie par la politique. |
| **🔒 Production renforcée** | Capacité supervisée, sauvegarde vérifiée et runbook d'incident testé. | Éviter les purges automatiques non auditées. |