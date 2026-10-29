# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Installer.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / installation
- **Tags** : `rocky9`, `freeipa`, `idm`, `kerberos`

---

## Problème précis à résoudre

Installer les paquets FreeIPA, ouvrir le pare-feu et lancer l'assistant d'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo dnf install ipa-server
   ```
   👉 Explication : Installe le serveur IdM sans DNS intégré. Avec DNS intégré, installer aussi `ipa-server-dns`.

2. Ouvrir le pare-feu :
   ```bash
   sudo firewall-cmd --permanent --add-service=freeipa-4
   sudo firewall-cmd --reload
   ```
   👉 Explication : Ouvre les ports FreeIPA et recharge le pare-feu. Ajouter `--add-service=dns` seulement si le DNS intégré est retenu.

3. Lancer l'installation interactive :
   ```bash
   sudo ipa-server-install
   ```
   👉 Explication : Lance l'assistant interactif : il demande realm, mot de passe Directory Manager et mot de passe `admin`, saisis au clavier et non en argument.

4. Consulter le journal :
   ```bash
   sudo tail -n 30 /var/log/ipaserver-install.log
   ```
   👉 Explication : Le journal d'installation permet de diagnostiquer un échec (DNS, nom d'hôte, heure).

## 2. Production — Contrôles

Utiliser le mode interactif; avec un DNS externe, publier dans la zone existante les enregistrements générés dans `/tmp/ipa.system.records.*.db`.

## 3. Production — Sécurité

- Ne pas utiliser le mode non interactif en production : les mots de passe seraient visibles dans l'historique et la liste des processus.
- `--no-dnssec-validation` seulement si DNSSEC n'est pas requis.

## Validation et retour arrière

- **Validation** : l'assistant se termine sans erreur et `sudo ipactl status` montre les services démarrés.
- **Retour arrière** : `sudo ipa-server-install --uninstall` sur un serveur non mis en production (supprime la configuration IdM locale), ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [Red Hat — Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 3](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/88_Deploiement_FreeIPA_Rocky_Linux_9.md#3-installer)
