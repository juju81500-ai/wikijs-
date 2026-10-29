# Fiche_Simple_-_VM_Debian_13_Zeek_Cadrer.md

- **Environnement** : VM Debian 13 capteur passif Zeek standalone sur interface miroir approuvée
- **OS / Version** : Debian 13 Trixie; Zeek 8.0 LTS (dépôt OBS officiel)
- **Catégorie** : supervision / analyse passive du trafic

---

## Problème précis à résoudre

Définir la source de trafic (SPAN/TAP), les VLAN visibles et la gouvernance des journaux avant d'installer Zeek.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les interfaces de la VM et repérer l'interface de capture, séparée de l'interface de gestion :
   ```bash
   ip -br address
   ip -d link show
   ```
   👉 Explication : l'interface miroir ne doit servir ni à l'administration ni au trafic utilisateur.

2. Faire confirmer à l'équipe réseau le port miroir/SPAN ou TAP, les VLAN visibles, le sens du miroir et les sous-réseaux internes.
   👉 Explication : une interface sur un commutateur ordinaire ne voit que le trafic de la VM.

3. Définir qui accède aux journaux et leur durée de conservation.
   👉 Explication : les captures contiennent des données sensibles.

## 2. Production — Contrôles

Périmètre autorisé par écrit; politique de rétention, accès et transfert des journaux validée.

## 3. Production — Sécurité

- Ne pas capturer un réseau tiers sans autorisation.
- Ne pas modifier pont, VLAN ou interface de capture sans changement réseau autorisé.

## Validation et retour arrière

- **Validation** : Interface de capture, VLAN, sous-réseaux et règles d'accès documentés.
- **Retour arrière** : Aucune modification n'est faite à cette étape.

## Si le problème n'est pas résolu

- [Zeek — supervision passive](https://docs.zeek.org/en/stable/monitoring.html)
- [Guide complet Zeek 8 LTS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/72-deploiement-zeek-8-lts-debian-13#1-definir-le-perimetre-et-la-source-reseau)