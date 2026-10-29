# Fiche_Simple_-_VM_Rocky_9_Suricata_Sauvegarder_Restaurer

- **Environnement** : VM Rocky Linux 9 dédiée à Suricata
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / sauvegarde et restauration
- **Tags** : `suricata`, `rocky9`, `vie-du-logiciel`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer configuration et règles locales de Suricata.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder les éléments utiles :
   ```bash
   sudo systemctl stop suricata
   sudo tar -czf /var/tmp/suricata-DATE.tar.gz /etc/suricata /var/lib/suricata/rules
   sudo chmod 0600 /var/tmp/suricata-DATE.tar.gz
   sudo systemctl start suricata
   ```
   👉 Explication : Archive configuration, règles et fichiers de suricata-update (enable/disable/modify.conf). DATE est à remplacer. Les logs ne sont pas sauvegardés ici : ils suivent la politique de rétention.

2. Copier l’archive vers le stockage approuvé (non détaillé).
   👉 Explication : L’archive ne doit pas rester sur la VM seule et ne contient aucun secret si les sources n’utilisent pas de clé.

3. Restaurer :
   ```bash
   sudo systemctl stop suricata
   sudo tar -xzf /var/tmp/suricata-DATE.tar.gz -C /
   sudo suricata -T -c /etc/suricata/suricata.yaml
   sudo systemctl start suricata
   ```
   👉 Explication : Remet configuration et règles; le test avant redémarrage évite un capteur cassé.

## 2. Production — Contrôles

Tester la restauration en lab chaque semestre.

## 3. Production — Sécurité

- Archive en 0600 et chiffrée hors VM.

## Validation et retour arrière

- **Validation** : Test de configuration OK et service actif après restauration.
- **Retour arrière** : Restaurer l’archive précédente connue bonne.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Suricata.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Suricata_Mise_A_Jour_Retour_Arriere.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Suricata_Valider.md)
