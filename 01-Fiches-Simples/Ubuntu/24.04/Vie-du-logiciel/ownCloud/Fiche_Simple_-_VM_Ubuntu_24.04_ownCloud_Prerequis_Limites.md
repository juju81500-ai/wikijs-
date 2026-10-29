# Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Prerequis_Limites

- **Environnement** : VM Ubuntu Server 24.04; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / ownCloud — Prérequis et limites
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `prerequis_limites`

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

- [Installer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)
