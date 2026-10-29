# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Ne laisser entrer que SSH et le service prévu.

## 1. Hors-Production (Lab / Test / POC)

1. Installer nftables et écrire les règles (remplacer `RESEAU_ADMIN` par le sous-réseau d'administration) :
   ```sh
   doas apk add nftables
   doas sh -c 'cat > /etc/nftables.nft <<EOF
   flush ruleset
   table inet filter {
     chain input {
       type filter hook input priority 0; policy drop;
       ct state established,related accept
       iif lo accept
       ip protocol icmp accept
       ip saddr RESEAU_ADMIN tcp dport 22 accept
     }
   }
   EOF'
   ```
   👉 Explication : politique `drop` par défaut; SSH n'est accepté que depuis le réseau d'administration. Alpine propose aussi `awall` (voir la fiche liée).

2. Charger, enregistrer et activer au démarrage :
   ```sh
   doas nft -f /etc/nftables.nft
   doas rc-service nftables save
   doas rc-update add nftables default
   ```
   👉 Explication : applique les règles, les sauvegarde pour le prochain démarrage et active le service.

3. Contrôler :
   ```sh
   doas nft list ruleset
   ```
   👉 Explication : montre les règles en vigueur.

## 2. Production — Contrôles

Ajouter un port par service et documenter chaque règle.

## 3. Production — Sécurité

Tester depuis la console : une règle erronée coupe SSH.

## Validation et retour arrière

- **Validation** : SSH autorisé depuis l'administration, le reste est refusé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
