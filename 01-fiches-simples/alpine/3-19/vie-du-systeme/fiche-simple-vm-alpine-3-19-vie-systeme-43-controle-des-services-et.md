# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : VM Alpine Linux 3-19 (serveur)
- **OS / Version** : Alpine Linux 3-19; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier que seuls les services prévus tournent.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services OpenRC :
   ```sh
   rc-status -a
   ```
   👉 Explication : montre les niveaux de démarrage et l'état de chaque service.

2. Contrôler les services en échec :
   ```sh
   rc-status --crashed
   ```
   👉 Explication : affiche les services qui se sont arrêtés anormalement.

3. Lister les ports en écoute :
   ```sh
   ss -tulpn
   ```
   👉 Explication : chaque port doit correspondre à un service autorisé.

## 2. Production — Contrôles

Comparer avec la baseline de l'étape 25.

## 3. Production — Sécurité

Tout port inattendu est traité comme un incident.

## Validation et retour arrière

- **Validation** : Services et ports conformes à la liste attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3-19 Securite OpenSSH Cle Et OpenRC](../vie-du-logiciel/openssh/fiche-simple-lxc-alpine-3-19-securite-openssh-cle-et-openrc.md)
- [Vie du système : les 50 étapes, tous OS](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md)
- [Sommaire Alpine Linux 3-19](./sommaire-vie-du-systeme-alpine-3-19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
