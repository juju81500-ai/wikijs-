# Fiche_Simple_-_VM_Debian_12_FreePBX_Installer_Methode_Supportee.md

- **Environnement** : VM de test dédiée, accès console, image ou procédure éditeur validée
- **OS / Version** : plateforme explicitement supportée par la version FreePBX retenue
- **Catégorie** : téléphonie IP / installation
- **Tags** : `debian12`, `freepbx`, `asterisk`, `installation`, `integrity`

---

## Problème précis à résoudre

Installer FreePBX selon la méthode officielle compatible sans exécuter de script tiers ou de paquets incompatibles.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'image ou la procédure officielle de la version retenue (site Sangoma/FreePBX) puis vérifier l'intégrité :
   ```bash
   sha256sum FreePBX-IMAGE.iso
   ```
   👉 Explication : comparer à la somme publiée par l'éditeur; installer d'abord sur une VM de test.

2. Après installation, fixer le nom d'hôte et contrôler :
   ```bash
   sudo hostnamectl set-hostname pbx.example.net
   hostnamectl; cat /etc/os-release | head -3
   ```
   👉 Explication : remplacer le nom; noter la version réellement installée.

3. Vérifier les services :
   ```bash
   sudo fwconsole --version
   sudo asterisk -rx 'core show version'
   ```
   👉 Explication : FreePBX et Asterisk doivent répondre.

4. Ne jamais lancer un script trouvé sur un forum par `curl | bash`, ni mélanger des paquets Asterisk de dépôts incompatibles.
   👉 Explication : cela casse la compatibilité avec FreePBX.

## 2. Production — Contrôles

Faire approuver source, empreinte, versions, méthode, paramètres réseau, fenêtre et procédure de mise à jour.

## 3. Production — Sécurité

- Ne pas exécuter un script téléchargé depuis un forum avec `curl | bash`.
- Ne pas mélanger des paquets Asterisk provenant de dépôts incompatibles avec FreePBX.
- Ne pas forcer Debian si la version FreePBX choisie ne le supporte pas.
- Ne pas exposer l'interface avant configuration et durcissement des comptes.

## Validation et retour arrière

- **Validation** : installation réalisée sur plateforme supportée, version et sources documentées, mise à jour compatible appliquée.
- **Retour arrière** : conserver snapshot de test ou sauvegarde validée avant modification; réinstaller selon la procédure éditeur si nécessaire.

## Si le problème n'est pas résolu

- [FreePBX — documentation](https://www.freepbx.org/documentation/)
- [Asterisk — documentation](https://docs.asterisk.org/)
- [Guide complet FreePBX/Asterisk Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/13_Telephonie_IP_FreePBX_Asterisk_20_Debian_12.md)
