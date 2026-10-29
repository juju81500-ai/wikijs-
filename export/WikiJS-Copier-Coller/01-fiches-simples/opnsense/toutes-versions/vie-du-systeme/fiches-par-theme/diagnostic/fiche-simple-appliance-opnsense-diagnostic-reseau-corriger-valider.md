# Fiche_Simple_-_Appliance_OPNsense_Diagnostic_Reseau_Corriger_Valider.md

- **Environnement** : Appliance OPNsense seule ou paire CARP; accès console recommandé
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / correction

---

## Problème précis à résoudre

Appliquer un correctif minimal et le valider.

## 1. Hors-Production (Lab / Test / POC)

1. **System > Configuration > Backups > Download configuration**.
   👉 Explication : sauvegarde avant changement.

2. Corriger une seule chose : route, règle précise ou configuration DNS; garder un accès console.
   👉 Explication : limite le risque de coupure.

3. Tester succès et refus attendus depuis des postes représentatifs.
   👉 Explication : confirme que la règle est correcte et pas trop large.

4. Relire **Firewall > Log Files > Live View** pour confirmer un niveau de journalisation normal.
   👉 Explication : le bruit doit revenir à la normale.

## 2. Production — Contrôles

Documenter le changement et la méthode de retour arrière.

## 3. Production — Sécurité

- Pas de règle `any/any` temporaire laissée en place.

## Validation et retour arrière

- **Validation** : Les flux attendus passent et les flux interdits restent bloqués.
- **Retour arrière** : Restaurer la configuration exportée : **System > Configuration > Backups > Restore**.

## Si le problème n'est pas résolu

- [OPNsense — outils de diagnostic](https://docs.opnsense.org/manual/diagnostics_interfaces.html)
- [OPNsense — dépannage](https://docs.opnsense.org/troubleshooting.html)
- [Guide complet — 5. Corriger et valider](/02-fiches-completes/opnsense/toutes-versions/diagnostic/35-diagnostic-reseau-opnsense-flux-dns-vpn#5-corriger-et-valider)