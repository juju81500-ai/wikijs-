# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Supprimer ce qui est inutile.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services actifs et les ports ouverts :
   ```bash
   systemctl list-unit-files --state=enabled --no-pager
   ss -tulpn
   ```
   👉 Explication : relève ce qui tourne et écoute.

2. Désactiver un service inutile (adapter `SERVICE`) :
   ```bash
   sudo systemctl disable --now SERVICE
   ```
   👉 Explication : arrête et empêche le démarrage; `SERVICE` est l'unité à retirer, par exemple `cups`.

3. Retirer un paquet inutile :
   ```bash
   sudo dnf remove -y PAQUET
   ```
   👉 Explication : `PAQUET` est le nom du paquet à supprimer; vérifier les dépendances proposées.

## 2. Production — Contrôles

Comparer à la baseline et justifier chaque service.

## 3. Production — Sécurité

Tout port ouvert doit avoir un propriétaire.

## Validation et retour arrière

- **Validation** : `ss -tulpn` ne montre que les ports attendus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
