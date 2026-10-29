# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Limiter SSH.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Services > SSH > Modifier : décocher « Connexion root avec mot de passe » et « Authentification par mot de passe ».
   ```bash
   sudo midclt call ssh.update '{"rootlogin": false, "passwordauth": false}'
   ```
   👉 Explication : interdit root et les mots de passe en SSH.

2. Vérifier :
   ```bash
   sudo midclt call ssh.config | python3 -m json.tool
   ```
   👉 Explication : contrôle le résultat.

3. Ne démarrer SSH que si nécessaire : GUI Système > Services.
   ```bash
   sudo midclt call service.stop ssh
   ```
   👉 Explication : arrête SSH quand il n'est pas utilisé.

## 2. Production — Contrôles

Autoriser SSH uniquement depuis le réseau d'administration.

## 3. Production — Sécurité

Tester une seconde session avant de fermer la première.

## Validation et retour arrière

- **Validation** : Connexion par mot de passe refusée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
