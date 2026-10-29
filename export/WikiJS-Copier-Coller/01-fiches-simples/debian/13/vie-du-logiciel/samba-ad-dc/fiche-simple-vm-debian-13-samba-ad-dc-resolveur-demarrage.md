# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Resolveur_Demarrage.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / service

---

## Problème précis à résoudre

Faire résoudre le domaine par le DNS du DC et démarrer le service samba-ad-dc.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer la pile réseau Debian pour utiliser `192.0.2.10` (adresse d'exemple à remplacer) comme DNS primaire du DC et des clients du lab.
   👉 Explication : le DC doit résoudre le domaine via son propre DNS AD.

2. Exécuter :
   ```bash
   systemctl cat samba-ad-dc.service
   sudo systemctl enable --now samba-ad-dc.service
   ```
   👉 Explication : affiche l'unité fournie, puis l'active et la démarre.

3. Exécuter :
   ```bash
   sudo systemctl --no-pager status samba-ad-dc.service
   sudo journalctl -u samba-ad-dc.service -n 80 --no-pager
   ```
   👉 Explication : contrôle l'état et les derniers journaux du service.

4. Au besoin, ajouter `dns forwarder` (adresse du résolveur amont autorisé) dans `[global]` de `smb.conf`, puis lancer `sudo testparm -s` et redémarrer le service en fenêtre de maintenance.
   👉 Explication : relaie les requêtes externes vers un résolveur approuvé.

## 2. Production — Contrôles

Ne pas utiliser un DNS public comme résolveur primaire du DC.

## 3. Production — Sécurité

- Forwarder DNS limité à un résolveur approuvé.
- Redémarrer le service seulement en fenêtre de maintenance.

## Validation et retour arrière

- **Validation** : `samba-ad-dc` est actif et le DNS répond.
- **Retour arrière** : `sudo systemctl disable --now samba-ad-dc.service` puis corriger la configuration; en lab, recréer la VM.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13#4-configurer-le-resolveur-et-demarrer)