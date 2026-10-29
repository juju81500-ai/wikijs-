# Fiche_Simple_-_VM_Debian_12_FreePBX_Sauvegarder_Maintenir.md

- **Environnement** : PBX FreePBX/Asterisk opérationnel; cible de sauvegarde hors serveur
- **OS / Version** : versions FreePBX/Asterisk maintenues et compatibles
- **Catégorie** : téléphonie IP / sauvegarde et maintenance
- **Tags** : `debian12`, `freepbx`, `asterisk`, `backup`, `restore`, `upgrade`

---

## Problème précis à résoudre

Protéger la configuration téléphonique et les données associées, puis tester une restauration avant la mise en production.

## 1. Hors-Production (Lab / Test / POC)

1. Planifier la sauvegarde : **Admin > Backup & Restore > Add Backup** (inclure Settings, CDR, enregistrements si nécessaire, planification).
   👉 Explication : les enregistrements, CDR et secrets sont sensibles; protéger la sauvegarde.

2. Lancer une sauvegarde manuelle et la copier hors serveur :
   ```bash
   sudo fwconsole backup --list
   ls -lh /var/spool/asterisk/backup/
   ```
   👉 Explication : copier l'archive hors du serveur (`rsync`, `scp`) vers un stockage chiffré.

3. Restaurer sur un environnement isolé : **Admin > Backup & Restore > Restore**, choisir l'archive.
   👉 Explication : jamais d'essai directement sur la production.

4. Maintenance : mises à jour des modules après sauvegarde :
   ```bash
   sudo fwconsole ma upgradeall
   sudo fwconsole reload
   ```
   👉 Explication : relire les notes de version; contrôler ensuite les appels de test.

## 2. Production — Contrôles

Faire approuver fréquence, rétention, chiffrement, accès, restauration, fenêtre de mise à niveau et critères de recette téléphonique.

## 3. Production — Sécurité

- Les enregistrements, CDR et secrets peuvent contenir des données sensibles; limiter leur accès.
- Ne pas conserver l'unique copie sur le serveur PBX.
- Ne pas appliquer une mise à jour hors du mécanisme supporté.
- Ne pas basculer une restauration isolée sur le réseau téléphonique sans validation.

## Validation et retour arrière

- **Validation** : sauvegarde indépendante restaurée en isolation, comptes et appels de test vérifiés.
- **Retour arrière** : restaurer l'état cohérent antérieur et confirmer routage, trunks et tests avant réouverture.

## Si le problème n'est pas résolu

- [FreePBX — documentation](https://www.freepbx.org/documentation/)
- [Asterisk — documentation](https://docs.asterisk.org/)
- [Guide complet FreePBX/Asterisk Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/13_Telephonie_IP_FreePBX_Asterisk_20_Debian_12.md)
