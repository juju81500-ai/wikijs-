# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Prouver que la supervision détecte une panne.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter volontairement un service non critique (par exemple chrony) :
   ```sh
   doas rc-service chronyd stop
   rc-service chronyd status
   ```
   👉 Explication : le service passe à `stopped`; la supervision doit lever une alerte.

2. Simuler un arrêt brutal :
   ```sh
   doas pkill -9 -x chronyd
   rc-status --crashed
   ```
   👉 Explication : affiche `crashed`; la reprise manuelle relance le service.

3. Restaurer le service :
   ```sh
   doas rc-service chronyd zap
   doas rc-service chronyd start
   ```
   👉 Explication : `zap` efface l'état erroné puis le service redémarre.

## 2. Production — Contrôles

Tester en dehors des heures de production, avec l'équipe prévenue.

## 3. Production — Sécurité

Ne pas tester sur le service SSH sans accès de secours.

## Validation et retour arrière

- **Validation** : L'alerte est reçue puis résolue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](</01-fiches-simples/alpine/3-19/vie-du-logiciel/openssh/fiche-simple-lxc-alpine-3-19-securite-openssh-cle-et-openrc>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)