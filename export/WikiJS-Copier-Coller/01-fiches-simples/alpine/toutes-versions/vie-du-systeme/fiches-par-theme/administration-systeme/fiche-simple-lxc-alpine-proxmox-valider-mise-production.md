# Fiche_Simple_-_LXC_Alpine_Proxmox_Valider_Mise_Production.md

- **Environnement** : CT Alpine finalisé sur Proxmox VE et client de test autorisé
- **OS / Version** : branche Alpine maintenue choisie pour le service
- **Catégorie** : virtualisation / validation de production

---

## Problème précis à résoudre

Confirmer que le CT, son réseau, ses services et sa procédure de sauvegarde/restauration sont prêts avant la mise en service.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis le CT, vérifier version, paquets, services, réseau :
   ```sh
   cat /etc/alpine-release
   apk info | wc -l
   rc-status
   ip -br addr
   ip route
   nslookup example.net
   ss -lntup
   ```
   👉 Explication : tout doit correspondre au plan; les ports ouverts sont ceux attendus.

2. Depuis un client autorisé, tester le parcours applicatif; depuis une source non autorisée, vérifier le refus :
   ```bash
   nc -zv IP_DU_CT PORT
   ```
   👉 Explication : remplacer IP et port; le client autorisé réussit, l'autre est refusé.

3. Créer la tâche de sauvegarde : **Datacenter > Backup > Add** (Storage = PBS, Selection mode = Include selected VMs, choisir le CT, planification, rétention).
   👉 Explication : cible indépendante du nœud.

4. Restaurer vers un ID temporaire et un réseau isolé pour prouver la sauvegarde (voir fiche de restauration isolée).
   👉 Explication : sans restauration prouvée, la mise en production n'est pas validée.

## 2. Production — Contrôles

Approuver responsable, fenêtre de bascule, IP/DNS, supervision, sauvegarde, restauration, critères d'acceptation et procédure de retour arrière.

## 3. Production — Sécurité

- Ne pas ouvrir le service avant la validation des tests positifs et négatifs.
- Ne pas considérer une sauvegarde comme restaurable sans exercice réel.
- Ne pas connecter le CT de restauration au réseau de production avec une IP dupliquée.
- Protéger les journaux et données récupérées selon leur classification.

## Validation et retour arrière

- **Validation** : configuration conforme, sauvegarde restaurée en isolation, exposition réseau limitée et critères signés.
- **Retour arrière** : basculer vers l'ancien service ou restaurer la sauvegarde sans conflit d'adresse.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet LXC Alpine sur Proxmox](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox#6-verification-et-mise-en-production)