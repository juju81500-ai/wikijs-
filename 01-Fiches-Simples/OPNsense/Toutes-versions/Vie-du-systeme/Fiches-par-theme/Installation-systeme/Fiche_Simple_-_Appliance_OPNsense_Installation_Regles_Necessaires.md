# Fiche_Simple_-_Appliance_OPNsense_Installation_Regles_Necessaires.md

- **Environnement** : Appliance physique ou VM dédiée avec interfaces réseau identifiées
- **OS / Version** : OPNsense Community ou Business Edition, release maintenue compatible avec la plateforme
- **Catégorie** : pare-feu / règles
- **Tags** : `opnsense`, `installation`, `pare-feu`, `wan`, `lan`

---

## Problème précis à résoudre

Créer uniquement les règles de filtrage strictement nécessaires.

## 1. Hors-Production (Lab / Test / POC)

1. **Firewall > Rules > LAN** puis **Add** : ajouter une règle par flux nécessaire, dans le bon ordre.
   👉 Explication : par défaut les flux sont refusés sauf autorisation explicite.

2. Limiter les sources d'administration au sous-réseau dédié (**Source** de la règle).
   👉 Explication : réduit l'exposition de l'interface d'administration.

3. Ne créer aucune règle autorisant la gestion Web/SSH depuis **Firewall > Rules > WAN**.
   👉 Explication : pas de gestion depuis le WAN sans architecture sécurisée et justification.

4. Configurer DHCP, DNS, VLAN, NAT, VPN ou haute disponibilité seulement si le rôle le nécessite, étape par étape.
   👉 Explication : tester chaque flux avant d'ajouter le suivant.

5. Contrôler les règles actives :
   ```sh
   pfctl -sr | head -n 40
   ```
   👉 Explication : Dans le shell de la console, affiche les premières règles effectivement chargées.

## 2. Production — Contrôles

Documenter chaque règle (but, responsable) et garder la console accessible.

## 3. Production — Sécurité

- Aucune gestion Web/SSH depuis le WAN.
- Règles minimales et sources limitées.

## Validation et retour arrière

- **Validation** : les flux autorisés passent et les refus attendus sont effectifs.
- **Retour arrière** : désactiver ou supprimer la dernière règle ajoutée, ou restaurer la configuration exportée.

## Si le problème n'est pas résolu

- [OPNsense — Installation](https://docs.opnsense.org/manual/install.html)
- [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html)
- [Guide complet — étape 4](../../../../../../02-Fiches-Completes/OPNsense/Toutes-versions/Installation-Deploiement/33_Installation_Appliance_OPNsense_Production.md#4-creer-les-regles-necessaires)
