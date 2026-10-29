# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Limiter SSH.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Services > SSH > Actions > décocher « Connexion root avec mot de passe » et « Authentification par mot de passe ».
   ```sh
   midclt call ssh.update '{"rootlogin": false, "passwordauth": false}'
   ```
   👉 Explication : interdit root et les mots de passe.

2. Vérifier :
   ```sh
   midclt call ssh.config
   ```
   👉 Explication : valeurs actives.

3. Arrêter SSH si non utilisé :
   ```sh
   midclt call service.stop ssh
   ```
   👉 Explication : réduit l'exposition.

## 2. Production — Contrôles

SSH uniquement depuis le réseau d'administration.

## 3. Production — Sécurité

Tester une seconde session avant de fermer la première.

## Validation et retour arrière

- **Validation** : Mot de passe refusé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
