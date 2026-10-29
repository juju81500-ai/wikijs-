# Fiche_Simple_-_VM_Debian_13_Suricata_IDS_Regles.md

- **Environnement** : VM Debian 13 avec Suricata configuré
- **OS / Version** : Debian 13 Trixie; Suricata 8.0.7 et suricata-update (Debian Backports)
- **Catégorie** : detection reseau / regles

---

## Problème précis à résoudre

Télécharger les règles et tester la configuration avant démarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les sources activées :
   ```bash
   sudo suricata-update list-sources --enabled
   ```
   👉 Explication : par défaut Emerging Threats Open, sans clé payante.

2. Télécharger et fusionner les règles :
   ```bash
   sudo suricata-update
   ```
   👉 Explication : le résultat est généralement `/var/lib/suricata/rules/suricata.rules`; vérifier que `default-rule-path` et `rule-files` pointent dessus.

3. Tester configuration et règles :
   ```bash
   sudo suricata -T -c /etc/suricata/suricata.yaml
   ```
   👉 Explication : aucune erreur YAML, SID invalide, fichier de règles absent ou interface inconnue ne doit apparaître avant de continuer.

## 2. Production — Contrôles

Relire les changements de règles et lancer `suricata -T` avant chaque redémarrage après mise à jour.

## 3. Production — Sécurité

- Ne pas activer de sources tierces inconnues ni de règles non relues.

## Validation et retour arrière

- **Validation** : `suricata -T` se termine sans erreur.
- **Retour arrière** : Désactiver la source ajoutée ou restaurer `suricata.yaml.pre-lab`, puis relancer `sudo suricata-update` et `suricata -T`.

## Si le problème n'est pas résolu

- [Suricata — suricata-update](https://docs.suricata.io/en/latest/rule-management/suricata-update.html)
- [Suricata — options CLI](https://docs.suricata.io/en/latest/command-line-options.html)
- [Guide complet Suricata Debian 13](/02-fiches-completes/debian/13/installation-deploiement/71-deploiement-suricata-8-debian-13-backports#5-mettre-a-jour-et-valider-les-regles)