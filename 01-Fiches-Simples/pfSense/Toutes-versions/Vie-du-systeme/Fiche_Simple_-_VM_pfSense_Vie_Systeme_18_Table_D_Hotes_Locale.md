# Fiche_Simple_-_VM_pfSense_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-18`

---

## Problème précis à résoudre

Déclarer les noms locaux sans serveur DNS dédié.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter un enregistrement dans Services > DNS Resolver > General Settings > Host Overrides > Add : Host `srv01`, Domain `exemple.lan`, IP `IP_SERVEUR`.
   👉 Explication : `IP_SERVEUR` est l'adresse de la machine nommée.

2. Contrôler la résolution :
   ```sh
   drill srv01.exemple.lan @127.0.0.1
   ```
   👉 Explication : doit renvoyer l'adresse déclarée.

## 2. Production — Contrôles

Centraliser ces entrées et les documenter plutôt que de les multiplier.

## 3. Production — Sécurité

Les noms internes ne doivent pas fuiter vers le DNS public.

## Validation et retour arrière

- **Validation** : Le nom local se résout vers la bonne adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
