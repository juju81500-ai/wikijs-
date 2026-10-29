# Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Securite_Retour_Arriere.md

- **Environnement** : Deux nœuds Linux sur le même segment L2, serveurs applicatifs redondés
- **OS / Version** : Linux (Debian/Ubuntu); HAProxy et Keepalived des dépôts de la distribution
- **Catégorie** : haute disponibilité / réseau

---

## Problème précis à résoudre

Sécuriser la HA et revenir en arrière en cas de flapping.

## 1. Hors-Production (Lab / Test / POC)

1. Filtrer VRRP entre les seuls pairs (protocole 112) avec le pare-feu hôte (remplacer 192.0.2.2 par l'IP du pair) :
   ```bash
   sudo iptables -A INPUT -p 112 -s 192.0.2.2 -j ACCEPT
   ```
   👉 Explication : n'autorise VRRP (protocole IP 112) que depuis le pair; exemple iptables non persistant, à adapter à votre pare-feu (nftables, ufw, etc.).

2. Limiter les ports HAProxy aux clients attendus.
   👉 Explication : réduit la surface d'attaque.

3. Surveiller l'état des deux nœuds et signaler un split-brain (IP présente sur les deux).
   ```bash
   ip addr show
   ```
   👉 Explication : vérifie qui porte l'IP virtuelle.

4. Conserver les fichiers antérieurs et la console d'administration accessible.
   👉 Explication : permet de revenir en arrière.

5. Si l'IP flappe, désactiver le changement récent sur un seul nœud à la fois et rétablir le service sur le nœud sain.
   👉 Explication : stabilise sans coupure totale.

## 2. Production — Contrôles

Mettre en place une supervision d'état Keepalived et HAProxy sur les deux nœuds.

## 3. Production — Sécurité

- VRRP limité aux pairs.
- Statistiques et administration HAProxy filtrées.

## Validation et retour arrière

- **Validation** : une seule IP active, pas de flapping, règles de filtrage en place.
- **Retour arrière** : restaurer les fichiers de configuration précédents et redémarrer `keepalived` puis `haproxy` sur un nœud à la fois.

## Si le problème n'est pas résolu

- [Keepalived — documentation](https://keepalived.readthedocs.io/en/latest/)
- [Keepalived — documentation](https://keepalived.readthedocs.io/en/latest/)
- [Guide complet](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy#5-securite-et-retour-arriere)