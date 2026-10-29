# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer le NAS de façon cohérente avec le DNS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Configuration globale > Nom d'hôte et Domaine.
   ```sh
   midclt call network.configuration.update '{"hostname": "NOM_NAS", "domain": "EXEMPLE.LOCAL"}'
   ```
   👉 Explication : NOM_NAS suit la convention ; EXEMPLE.LOCAL est le domaine interne.

2. Vérifier :
   ```sh
   hostname
   ```
   👉 Explication : nom enregistré.

## 2. Production — Contrôles

Créer les enregistrements DNS A et PTR.

## 3. Production — Sécurité

Pas de nom révélant le contenu.

## Validation et retour arrière

- **Validation** : `hostname` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
