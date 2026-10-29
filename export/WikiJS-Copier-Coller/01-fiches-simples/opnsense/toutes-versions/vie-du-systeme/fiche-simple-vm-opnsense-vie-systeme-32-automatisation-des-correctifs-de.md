# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Être alerté des mises à jour et vulnérabilités.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier régulièrement Système > Micrologiciel > Mises à jour (une notification apparaît dans le Tableau de bord).
   👉 Explication : OPNsense ne s'applique pas seul; la mise à jour reste une action contrôlée.

2. Rechercher les paquets vulnérables en shell :
   ```sh
   pkg audit -F
   configctl firmware audit
   ```
   👉 Explication : télécharge la base de vulnérabilités et signale les paquets concernés.

3. Programmer la vérification (Système > Paramètres > Cron) si une tâche de contrôle est utile.
   👉 Explication : automatise l'alerte sans appliquer automatiquement.

## 2. Production — Contrôles

Appliquer les correctifs de sécurité dans une fenêtre de maintenance avec point de restauration.

## 3. Production — Sécurité

Appliquer sans délai les correctifs critiques exposant le WAN.

## Validation et retour arrière

- **Validation** : `pkg audit` ne signale aucune vulnérabilité ouverte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)