# Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Installer_Prometheus.md

- **Environnement** : Debian 13 amd64, archive officielle Prometheus 3.15.1
- **OS / Version** : Debian 13; Prometheus 3.15.1
- **Catégorie** : supervision / installation
- **Tags** : `debian13`, `prometheus`, `installation`, `checksum`, `systemd`

---

## Problème précis à résoudre

Installer les binaires Prometheus et promtool depuis une release identifiée et vérifier l'intégrité de l'archive.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'architecture et la version attendue :
   ```bash
   dpkg --print-architecture
   uname -m
   ```
   👉 Explication : `amd64` et `x86_64` confirment que l'archive `linux-amd64` convient.

2. Télécharger l'archive officielle et vérifier son SHA-256 :
   ```bash
   cd /tmp
   curl -fLO https://github.com/prometheus/prometheus/releases/download/v3.15.1/prometheus-3.15.1.linux-amd64.tar.gz
   echo '6a726885328ad9efebbf36e876ce2fb6225468a71fd1e7ce3ba666d5f4d97a84  prometheus-3.15.1.linux-amd64.tar.gz' | sha256sum -c -
   ```
   👉 Explication : `sha256sum -c` doit afficher `OK`; en cas d'échec, supprimer l'archive et ne pas poursuivre.

3. Créer l'utilisateur de service et les répertoires :
   ```bash
   sudo useradd --system --no-create-home --shell /usr/sbin/nologin prometheus
   sudo install -d -o prometheus -g prometheus -m 0750 /etc/prometheus /var/lib/prometheus
   ```
   👉 Explication : le compte système sans shell exécutera le service; les données lui appartiennent.

4. Extraire et installer uniquement les binaires nécessaires :
   ```bash
   tar -xzf prometheus-3.15.1.linux-amd64.tar.gz
   sudo install -o root -g root -m 0755 prometheus-3.15.1.linux-amd64/prometheus /usr/local/bin/prometheus
   sudo install -o root -g root -m 0755 prometheus-3.15.1.linux-amd64/promtool /usr/local/bin/promtool
   sudo cp -a prometheus-3.15.1.linux-amd64/consoles prometheus-3.15.1.linux-amd64/console_libraries /etc/prometheus/
   ```
   👉 Explication : les binaires appartiennent à `root`, l'utilisateur de service ne peut donc pas les modifier.

5. Régler et vérifier les permissions :
   ```bash
   sudo chown -R root:prometheus /etc/prometheus
   sudo chown prometheus:prometheus /var/lib/prometheus
   ls -ld /etc/prometheus /var/lib/prometheus
   prometheus --version
   ```
   👉 Explication : la configuration est lisible par le groupe `prometheus` sans écriture; `--version` doit afficher `3.15.1`.

## 2. Production — Contrôles

Consigner version, URL de release, checksum, date d'installation, procédure de patching et compatibilité des règles/dashboards.

## 3. Production — Sécurité

- Si le checksum ne correspond pas, arrêter; ne pas exécuter ni installer l'archive.
- Ne pas utiliser un miroir non approuvé ou télécharger une version flottante.
- Exécuter Prometheus sous un compte système non privilégié.
- Protéger les répertoires de données et de configuration contre l'écriture non autorisée.

## Validation et retour arrière

- **Validation** : archive vérifiée, versions des binaires consignées, propriétaires et permissions minimaux.
- **Retour arrière** : conserver l'ancienne version approuvée et ses données avant remplacement.

## Si le problème n'est pas résolu

- [Prometheus — installation](https://prometheus.io/docs/prometheus/latest/installation/)
- [Prometheus 3.15.1 — release](https://github.com/prometheus/prometheus/releases/tag/v3.15.1)
- [Guide complet Prometheus/Grafana Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/45_Deploiement_Prometheus_Grafana_Debian_13.md#2-installer-prometheus-3-15-1)
