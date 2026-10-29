# Fiche_Simple_-_LXC_Alpine_Diagnostic_Corriger_Proprietaire.md

- **Environnement** : console Proxmox et console Alpine; correction selon le propriétaire identifié
- **OS / Version** : branche Alpine maintenue; OpenRC pour les services dans le CT
- **Catégorie** : diagnostic / correction

---

## Problème précis à résoudre

Corriger uniquement la couche responsable de la panne, sans appliquer au LXC des changements destinés à une VM.

## 1. Hors-Production (Lab / Test / POC)

1. Adresse/DNS gérés par Proxmox : corriger sur l'hôte :
   ```bash
   pct set CTID -net0 name=eth0,bridge=vmbr0,ip=192.0.2.10/24,gw=192.0.2.1,tag=VLAN
   pct set CTID -nameserver 192.0.2.53
   pct reboot CTID
   ```
   👉 Explication : adapter toutes les valeurs; ne pas éditer un fichier que Proxmox régénère. Interface équivalente : **CT > Network > Edit**.

2. Service arrêté :
   ```sh
   rc-service SERVICE status
   rc-service SERVICE restart
   ```
   👉 Explication : relancer ce service seulement, après avoir corrigé sa configuration.

3. Firewall : identifier la règle effective : **Datacenter / CT > Firewall**, ou côté routeur/hôte.
   👉 Explication : tester une règle minimale et réversible.

4. Ne pas appliquer à un LXC les commandes d'une VM Alpine (gestion de profil réseau).
   👉 Explication : le propriétaire de la configuration réseau d'un LXC est Proxmox.

## 2. Production — Contrôles

Obtenir l'approbation de changement pour le composant concerné; conserver configuration précédente et accès de secours.

## 3. Production — Sécurité

- Ne pas désactiver le filtrage pour contourner le diagnostic.
- Ne pas redémarrer l'hôte Proxmox pour réparer un seul service CT.
- Ne pas effectuer plusieurs changements simultanés qui empêchent d'isoler la cause.
- Limiter les règles de test à la source, destination et durée approuvées.

## Validation et retour arrière

- **Validation** : correction propriétaire appliquée et résultat vérifié sans élargir l'exposition.
- **Retour arrière** : restaurer la configuration précédente via la console, puis réévaluer la couche fautive.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet de diagnostic LXC Alpine](/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services#4-reparer-selon-le-proprietaire-de-la-configuration)