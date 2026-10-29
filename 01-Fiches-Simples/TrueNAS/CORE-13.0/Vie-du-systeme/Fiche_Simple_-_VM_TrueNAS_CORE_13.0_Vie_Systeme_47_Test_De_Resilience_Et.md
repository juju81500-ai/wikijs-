# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Valider qu'une panne déclenche une alerte.

## 1. Hors-Production (Lab / Test / POC)

1. En lab, mettre un disque hors ligne : GUI Stockage > Pools > Statut > disque > Offline.
   ```sh
   zpool offline POOL da2
   zpool status POOL
   ```
   👉 Explication : pool DEGRADED, alerte attendue ; lab uniquement.

2. Remettre en ligne :
   ```sh
   zpool online POOL da2
   zpool status POOL
   ```
   👉 Explication : resilver puis ONLINE.

3. Tester l'envoi d'alerte : Système > E-mail > Envoyer un e-mail test.
   ```sh
   midclt call mail.send '{"subject":"Test","text":"Test d'alerte","to":["ADRESSE_MAIL"]}'
   ```
   👉 Explication : ADRESSE_MAIL est la boîte de l'équipe.

## 2. Production — Contrôles

Documenter le délai alerte.

## 3. Production — Sécurité

Jamais sur un pool de production sans redondance.

## Validation et retour arrière

- **Validation** : Alerte reçue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
