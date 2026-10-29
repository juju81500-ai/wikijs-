# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier ce qu'un tiers voit de la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis un autre poste, scanner tous les ports (remplacer `ADRESSE_IP`) :
   ```sh
   nmap -sV -p- ADRESSE_IP
   ```
   👉 Explication : liste les ports ouverts et les services; à exécuter avec autorisation.

2. Tester un port précis :
   ```sh
   nc -zv ADRESSE_IP 22
   ```
   👉 Explication : confirme que SSH est joignable depuis le réseau d'administration.

3. Comparer avec les règles du pare-feu :
   ```sh
   doas nft list ruleset
   ```
   👉 Explication : tout port ouvert doit correspondre à une règle.

## 2. Production — Contrôles

Répéter l'audit après chaque changement de pare-feu.

## 3. Production — Sécurité

Scanner uniquement avec autorisation écrite.

## Validation et retour arrière

- **Validation** : Seuls les ports autorisés répondent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)