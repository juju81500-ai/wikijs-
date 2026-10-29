# Fiche_Simple_-_Appliance_OPNsense_CARP_pfsync_Creer_VIP_CARP.md

- **Environnement** : Deux appliances OPNsense en haute disponibilité (CARP et pfsync)
- **OS / Version** : OPNsense (toutes versions compatibles entre les deux nœuds)
- **Catégorie** : pare-feu / haute disponibilité

---

## Problème précis à résoudre

Créer les adresses virtuelles CARP identiques sur les deux pare-feu.

## 1. Hors-Production (Lab / Test / POC)

1. Sur chaque pare-feu : **Interfaces > Virtual IPs > Settings > +**, mode **CARP**.
   👉 Explication : crée l'adresse virtuelle partagée.

2. Utiliser le même VHID, le même réseau et le même mot de passe CARP sur les deux nœuds, mais des adresses individuelles distinctes.
   👉 Explication : le VHID doit être unique par segment.

3. Nœud principal en MASTER (skew faible) et secondaire en BACKUP (skew plus élevé).
   👉 Explication : définit la priorité d'élection.

4. Choisir le comportement de préemption : **System > High Availability > Settings** (option de préemption).
   👉 Explication : détermine si le primaire reprend la main au retour.

5. Avant activation, vérifier adresse, masque, interface et absence de conflit.
   👉 Explication : ne jamais copier une VIP d'exemple dans le réseau réel.

## 2. Production — Contrôles

Documenter VHID, VIP, priorités et nœud maître.

## 3. Production — Sécurité

- Mot de passe CARP unique, absent des documents.

## Validation et retour arrière

- **Validation** : la VIP est active sur le MASTER et le BACKUP est prêt.
- **Retour arrière** : supprimer la VIP fautive sur chaque nœud, un nœud à la fois, depuis la console si besoin.

## Si le problème n'est pas résolu

- [OPNsense — CARP](https://docs.opnsense.org/manual/how-tos/carp.html)
- [OPNsense — haute disponibilité](https://docs.opnsense.org/manual/hacarp.html)
- [Guide complet](/02-fiches-completes/opnsense/toutes-versions/autres/10-pare-feu-appliance-opnsense-carp-pfsync-ha#3-creer-les-vip-carp)