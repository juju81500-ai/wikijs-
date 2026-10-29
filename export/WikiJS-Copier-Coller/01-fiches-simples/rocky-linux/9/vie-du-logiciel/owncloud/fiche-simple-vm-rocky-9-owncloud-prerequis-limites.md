# Fiche_Simple_-_VM_Rocky_9_ownCloud_Prerequis_Limites

- **Environnement** : VM Rocky Linux 9; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / ownCloud — Prérequis et limites

---

## Problème précis à résoudre

Distinguer oCIS (binaire Infinite Scale) de ownCloud Classic 10 et confirmer l’architecture.

## 1. Hors-Production (Lab / Test / POC)

1. Prérequis et limites :
   ```bash
   cat /etc/os-release | head -5
uname -m
free -h
df -h /var
curl -fsSL https://download.owncloud.com/ocis/ocis/stable/
   ```
   👉 Explication : La liste officielle permet de choisir une version stable; cette série ne concerne pas ownCloud Classic.

## 2. Production — Contrôles

Documenter version, FQDN, reverse proxy, stockage et RPO/RTO.

## 3. Production — Sécurité

Ne pas exposer le backend 9200 à Internet; utiliser HTTPS via reverse proxy.

## Validation et retour arrière

- **Validation** : Variante, version et stockage consignés.
- **Retour arrière** : Aucun changement si compatibilité incertaine.

## Si le problème n'est pas résolu

- [Installer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-installer)
- [Configurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-configurer)
- [Sécuriser](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-securiser)
- [Valider (recette)](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-mise-a-jour-retour-arriere)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)