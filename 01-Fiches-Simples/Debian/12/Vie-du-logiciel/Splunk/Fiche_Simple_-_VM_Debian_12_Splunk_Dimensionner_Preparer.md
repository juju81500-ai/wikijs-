# Fiche_Simple_-_VM_Debian_12_Splunk_Dimensionner_Preparer.md

- **Environnement** : VM Debian 12 dédiée à Splunk Enterprise autonome (laboratoire)
- **OS / Version** : Debian 12 Bookworm; Splunk Enterprise 10.2
- **Catégorie** : journaux / cadrage
- **Tags** : `debian12`, `splunk`, `logs`, `dimensionnement`

---

## Problème précis à résoudre

Vérifier que l'hôte convient avant d'installer Splunk.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et l'architecture :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   dpkg --print-architecture
   ```
   👉 Explication : ils doivent figurer dans la matrice officielle Splunk 10.2.

2. Contrôler CPU, RAM et disque :
   ```bash
   nproc
   free -h
   df -hT /opt
   ```
   👉 Explication : base du dimensionnement (débit, hot/warm/cold, rétention, recherches simultanées).

3. Contrôler que les ports par défaut sont libres :
   ```bash
   sudo ss -tlnp | grep -E ':(8000|8089|9997)\b' || echo 'ports libres'
   ```
   👉 Explication : l'interface Web écoute sur 8000, la gestion/API sur 8089.

## 2. Production — Contrôles

Pour une plateforme distribuée de production, appliquer les architectures validées Splunk; préparer DNS/NTP, stockage local, sauvegarde et plan réseau.

## 3. Production — Sécurité

- Ne pas exposer 8000 ni 8089 à Internet.
- Ne pas ouvrir 9997 sans configurer l'input correspondant.

## Validation et retour arrière

- **Validation** : matrice respectée et ports libres.
- **Retour arrière** : lecture seule: rien à annuler.

## Si le problème n'est pas résolu

- [Splunk 10.2 — installer sur Linux](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/install-on-linux)
- [Splunk 10.2 — exigences système](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/plan-your-splunk-enterprise-installation/system-requirements-for-use-of-splunk-enterprise-on-premises)
- [Guide complet Splunk Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/54_Deploiement_Splunk_Enterprise_10.2_Debian_12.md#1-dimensionner-et-preparer)
