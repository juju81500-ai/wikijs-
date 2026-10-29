# Fiche_Simple_-_VM_Debian_13_NetBox_Config_Secrets.md

- **Environnement** : NetBox 4.7.4 installé sur Debian 13; secrets gérés par coffre approuvé
- **OS / Version** : Debian 13; NetBox 4.7.4
- **Catégorie** : IPAM / DCIM / configuration et secrets
- **Tags** : `debian13`, `netbox`, `configuration`, `secrets`, `postgresql`, `redis`

---

## Problème précis à résoudre

Configurer les hôtes autorisés, PostgreSQL, Redis et les secrets NetBox avec permissions minimales.

## 1. Hors-Production (Lab / Test / POC)

1. Créer `configuration.py` à partir de l'exemple :
   ```bash
   sudo cp /opt/netbox/netbox/netbox/configuration_example.py /opt/netbox/netbox/netbox/configuration.py
   ```
   👉 Explication : on part du fichier fourni par la version installée.

2. Générer la clé secrète et le pepper :
   ```bash
   python3 /opt/netbox/netbox/generate_secret_key.py
   python3 -c "import secrets; print(secrets.token_urlsafe(48))"
   ```
   👉 Explication : la clé a ≥ 50 caractères; le pepper doit être aléatoire, d'au moins 50 caractères (utiliser une sortie plus longue si nécessaire). Les stocker dans le coffre.

3. Éditer le fichier :
   ```bash
   sudoedit /opt/netbox/netbox/netbox/configuration.py
   ```
   👉 Explication : renseigner `ALLOWED_HOSTS` (FQDN, jamais `['*']`), `API_TOKEN_PEPPERS`, `DATABASES` (hôte `localhost`, base/rôle `netbox`), `REDIS` (deux entrées `tasks` et `caching`, bases différentes) et `SECRET_KEY`.

4. Protéger le fichier :
   ```bash
   sudo chown root:netbox /opt/netbox/netbox/netbox/configuration.py
   sudo chmod 0640 /opt/netbox/netbox/netbox/configuration.py
   ls -l /opt/netbox/netbox/netbox/configuration.py
   ```
   👉 Explication : le groupe `netbox` lit le fichier; les autres comptes n'y ont pas accès.

## 2. Production — Contrôles

Consigner le stockage des secrets, les rotations, les hôtes, les paramètres DB/Redis, le responsable et les sauvegardes chiffrées.

## 3. Production — Sécurité

- Ne jamais réutiliser de valeurs d'exemple ou copier des secrets d'une autre instance.
- Ne pas placer `configuration.py` dans le dépôt ou le document root.
- Garder mots de passe, `SECRET_KEY` et `API_TOKEN_PEPPERS` dans le coffre et protéger leurs sauvegardes.
- Ne pas rendre Redis ou PostgreSQL accessibles publiquement.

## Validation et retour arrière

- **Validation** : NetBox lit la configuration, les secrets sont présents et protégés, l'accès DB/Redis local est opérationnel.
- **Retour arrière** : conserver une copie chiffrée et approuvée de l'ancienne configuration; ne pas restaurer une clé compromise.

## Si le problème n'est pas résolu

- [NetBox — paramètres requis](https://netbox.readthedocs.io/en/stable/configuration/required-parameters/)
- [NetBox — configuration](https://netbox.readthedocs.io/en/stable/configuration/)
- [Guide complet NetBox Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/73_Deploiement_NetBox_4.7.4_Debian_13.md#4-configurer-les-secrets-et-la-base-de-donnees)
