# Fiche_Simple_-_VM_Rocky_9_Snort_Sauvegarder_Restaurer

- **Environnement** : VM Rocky Linux 9 dédiée à Snort
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / sauvegarde et restauration
- **Tags** : `snort`, `rocky9`, `vie-du-logiciel`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer configuration et règles locales de Snort.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder :
   ```bash
   sudo tar -czf /var/tmp/snort3-DATE.tar.gz /opt/snort3/etc /opt/snort3/rules /etc/systemd/system/snort3-ids.service
   sudo chmod 0600 /var/tmp/snort3-DATE.tar.gz
   ```
   👉 Explication : Archive configuration, règles et unité; DATE est à remplacer. Retirer le fichier d’unité de la commande s’il n’existe pas. Les logs suivent la politique de rétention.

2. Copier vers le stockage approuvé (non détaillé).
   👉 Explication : L’archive est chiffrée hors de la VM.

3. Restaurer :
   ```bash
   sudo tar -xzf /var/tmp/snort3-DATE.tar.gz -C /
   sudo systemctl daemon-reload
   sudo /opt/snort3/bin/snort -c /opt/snort3/etc/snort/snort.lua -T
   ```
   👉 Explication : Remet les fichiers puis teste la configuration.

## 2. Production — Contrôles

Tester la restauration en lab.

## 3. Production — Sécurité

- Archive en 0600.

## Validation et retour arrière

- **Validation** : `snort -T` réussit après restauration.
- **Retour arrière** : Restaurer l’archive précédente connue bonne.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Snort.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Snort_Mise_A_Jour_Retour_Arriere.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Snort_Valider.md)
