# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Donner à chacun uniquement les commandes nécessaires.

## 1. Hors-Production (Lab / Test / POC)

1. Écrire une règle limitée à une commande (remplacer `AUDITEUR`) :
   ```sh
   doas sh -c 'cat > /etc/doas.d/20-audit.conf <<EOF
   permit nopass AUDITEUR cmd rc-status
   permit persist :wheel
   EOF'
   doas chmod 0400 /etc/doas.d/20-audit.conf
   ```
   👉 Explication : AUDITEUR peut lancer seulement `rc-status` sans mot de passe; la règle du groupe reste en place.

2. Contrôler la syntaxe :
   ```sh
   doas -C /etc/doas.d/20-audit.conf && echo OK
   ```
   👉 Explication : `-C` vérifie le fichier sans l'exécuter.

3. Tester avec le compte concerné :
   ```sh
   su - AUDITEUR -c 'doas rc-status; doas ls /root'
   ```
   👉 Explication : la première commande passe, la seconde est refusée.

## 2. Production — Contrôles

Revoir les règles à chaque départ ou changement de poste.

## 3. Production — Sécurité

`nopass` est limité à des commandes précises, jamais à `ALL`.

## Validation et retour arrière

- **Validation** : Les commandes non autorisées sont refusées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
