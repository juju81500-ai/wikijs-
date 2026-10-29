# Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Partage.md

- **Environnement** : NAS autonome pilote (matériel x86-64 ou VM de laboratoire)
- **OS / Version** : TrueNAS SCALE 25.10 Community Edition
- **Catégorie** : stockage NAS / partage

---

## Problème précis à résoudre

Publier un partage SMB ou NFS contrôlé et le tester avec un client pilote.

## 1. Hors-Production (Lab / Test / POC)

1. **Network > Interfaces** : configurer l'interface et l'adresse de gestion.
   👉 Explication : sépare si possible administration et flux SMB/NFS.

2. **Shares > Windows (SMB) Shares > Add** : choisir le dataset dédié et les comptes nominatifs.
   👉 Explication : permissions minimales.

3. Vérifier l'ACL du dataset, puis tester depuis un seul client pilote autorisé.
   👉 Explication : valide lecture/écriture, héritage ACL, verrouillage et reprise après interruption.

4. Surveiller pool, alertes SMART, scrubs, températures et espace.
   👉 Explication : anticipe les pannes.

## 2. Production — Contrôles

Définir une fenêtre de maintenance avant extension ou remplacement de disque.

## 3. Production — Sécurité

- Comptes nominatifs et permissions minimales.

## Validation et retour arrière

- **Validation** : Le client pilote lit et écrit; un client non autorisé est refusé.
- **Retour arrière** : Désactiver le partage depuis **Shares** sans toucher au dataset.

## Si le problème n'est pas résolu

- [TrueNAS SCALE 25.10 — installation](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/)
- [TrueNAS SCALE 25.10 — guide matériel](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/)
- [Guide complet — 4. Mettre en service le partage](/02-fiches-completes/truenas/scale-25-10/installation-deploiement/60-deploiement-truenas-scale-25-10#4-mettre-en-service-le-partage)