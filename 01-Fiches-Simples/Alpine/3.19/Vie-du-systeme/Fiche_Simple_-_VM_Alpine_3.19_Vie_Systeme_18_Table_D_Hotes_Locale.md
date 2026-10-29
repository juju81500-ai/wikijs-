# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-18`

---

## Problème précis à résoudre

Garder les entrées critiques en local.

## 1. Hors-Production (Lab / Test / POC)

1. Relire `/etc/hosts` :
   ```sh
   cat /etc/hosts
   ```
   👉 Explication : doit contenir `127.0.0.1 localhost` et le FQDN de la machine.

2. Ajouter les hôtes critiques (remplacer `ADRESSE_IP_DC` et `NOM_DC.DOMAINE`) :
   ```sh
   doas sh -c 'cat >> /etc/hosts <<EOF
   ADRESSE_IP_DC NOM_DC.DOMAINE NOM_DC
   EOF'
   getent hosts NOM_DC.DOMAINE
   ```
   👉 Explication : assure la résolution des serveurs essentiels même si le DNS est indisponible.

3. Contrôler que l'ordre des sources de noms reste cohérent :
   ```sh
   cat /etc/nsswitch.conf 2>/dev/null || echo 'musl : fichier hosts puis DNS'
   ```
   👉 Explication : musl interroge `/etc/hosts` avant le DNS; il n'y a pas de `nsswitch.conf` par défaut.

## 2. Production — Contrôles

Limiter les entrées statiques et les documenter.

## 3. Production — Sécurité

Des entrées obsolètes peuvent détourner du trafic : relire à chaque changement d'adresse.

## Validation et retour arrière

- **Validation** : `getent hosts` retourne l'adresse attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
