# Fiche_Simple_-_VM_Debian_13_Zeek_Deployer.md

- **Environnement** : VM Debian 13 capteur passif Zeek standalone sur interface miroir approuvée
- **OS / Version** : Debian 13 Trixie; Zeek 8.0 LTS (dépôt OBS officiel)
- **Catégorie** : supervision / analyse passive du trafic

---

## Problème précis à résoudre

Valider la configuration puis démarrer le nœud via ZeekControl.

## 1. Hors-Production (Lab / Test / POC)

1. Générer et vérifier la configuration :
   ```bash
   sudo -u zeek /opt/zeek/bin/zeekctl config
   sudo -u zeek /opt/zeek/bin/zeekctl check
   ```
   👉 Explication : `check` doit réussir avant le premier démarrage.

2. Déployer le nœud et lire son statut :
   ```bash
   sudo -u zeek /opt/zeek/bin/zeekctl deploy
   sudo -u zeek /opt/zeek/bin/zeekctl status
   ```
   👉 Explication : si zeekctl n'est pas sous `/opt/zeek/bin`, utiliser le chemin affiché par `command -v zeekctl`.

3. En cas d'échec de capture, lire les journaux système :
   ```bash
   sudo journalctl -n 100 --no-pager
   getcap /opt/zeek/bin/zeek
   ```
   👉 Explication : cherche une erreur de permission ou de capacités.

## 2. Production — Contrôles

Changement approuvé; statut `running` consigné.

## 3. Production — Sécurité

- Ne pas passer en root pour contourner une erreur de permission.

## Validation et retour arrière

- **Validation** : `zeekctl status` indique le nœud `running`.
- **Retour arrière** : `sudo -u zeek /opt/zeek/bin/zeekctl stop` puis restaurer les configurations `.pre-lab`.

## Si le problème n'est pas résolu

- [Zeek — installation](https://docs.zeek.org/en/stable/install.html)
- [Guide complet Zeek 8 LTS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/72-deploiement-zeek-8-lts-debian-13#5-verifier-la-configuration-et-deployer-zeekcontrol)