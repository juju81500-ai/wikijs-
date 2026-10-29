# Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Sauvegarder_Restaurer

- **Environnement** : Ubuntu Server 24.04 LTS x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Ubuntu 24.04 — plateforme de déploiement listée dans les exigences NAKIVO; valider le build produit
- **Catégorie** : sauvegarde / restauration

---

## Problème précis à résoudre

Protéger la configuration NAKIVO (self-backup du Director) et prouver qu'une restauration fonctionne, pour un nœud Transporter hébergé sur Ubuntu 24.04.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'interface web du Director, ouvrir : **Settings** > onglet **General** > **Self-Backup**.
   👉 Explication : le self-backup protège la configuration du produit (inventaire, jobs, nœuds, dépôts), pas les données des machines protégées; il se configure sur le Director, pas sur le Transporter.

2. Choisir la destination (**Back up system configuration to all repositories** ou **to selected repositories only**), exclure tout dépôt de type DD Boost ou SaaS, puis définir l'horaire et le nombre de points de récupération à conserver (**Options**).
   👉 Explication : un dépôt DD Boost serait démonté par le self-backup et un dépôt SaaS n'est pas pris en charge comme cible.

3. Cocher **Encrypt self-backup**, sélectionner ou créer un mot de passe dans le gestionnaire de mots de passe NAKIVO (saisi dans l'interface, jamais écrit dans une fiche), puis cliquer sur **Apply**.
   👉 Explication : la configuration peut contenir des paramètres sensibles; conserver le mot de passe dans un coffre approuvé, sans lui la récupération est impossible.

4. Cliquer sur **Run Self-backup Now** pour obtenir un premier point de récupération.
   👉 Explication : ne pas attendre l'horaire pour vérifier que la sauvegarde s'écrit.

5. Sauvegarder les données de la machine Transporter selon la politique de l'organisation (snapshot VM ou image du système), en plus du self-backup.
   👉 Explication : le self-backup ne remplace pas la sauvegarde de l'hôte Linux; les données de sauvegarde restent dans les dépôts.

6. Restaurer en lab : **Settings** > **Repositories**, sélectionner un dépôt contenant un self-backup, choisir le self-backup dans la liste **Backups**, cliquer sur **Recover** puis **Restore**, et attendre le message de succès.
   👉 Explication : cette procédure officielle remplace la configuration courante; ne la tester que sur une instance de lab.

7. Tester aussi la restauration d'un objet ou d'une machine de test depuis l'assistant de récupération du Director vers une destination isolée.
   👉 Explication : valider le parcours de restauration des données, distinct de celui de la configuration.

## 2. Production — Contrôles

- Planifier le self-backup, surveiller son résultat et conserver plusieurs points de récupération.
- Noter le build NAKIVO courant : restaurer une configuration sur un build compatible (vérifier la documentation publiée).
- Le self-backup n'est pas pris en charge pour une configuration multi-tenant et ne peut pas cibler un dépôt fédéré.
- Répéter un test de restauration à fréquence définie et consigner le résultat.

## 3. Production — Sécurité

- Chiffrer le self-backup et stocker le mot de passe dans un coffre approuvé; ne jamais l'écrire dans une fiche ou un ticket.
- Restreindre l'accès aux dépôts qui contiennent les self-backups.
- Ne pas exposer SSH ou l'interface NAKIVO sur Internet sans architecture de sécurité approuvée.

## Validation et retour arrière

- **Validation** : un self-backup récent existe dans le dépôt, et une restauration de test (configuration en lab, objet de test) réussit.
- **Retour arrière** : en cas d'échec de récupération, conserver la configuration actuelle et le dépôt intacts, puis ouvrir un dossier avec l'éditeur avant toute suppression.

## Si le problème n'est pas résolu

- [NAKIVO — Self-Backup](https://helpcenter.nakivo.com/User-Guide/Content/Settings/General/Self-Backup.htm)
- [NAKIVO — Self-Backup Feature](https://helpcenter.nakivo.com/User-Guide/Content/Overview/Self-Backup-Feature.htm)
- [Fiche sécurité du Transporter](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-securiser)
- [Fiche validation et maintenance du Transporter](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-valider-mettre-a-jour)
- [Fiche d'entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)