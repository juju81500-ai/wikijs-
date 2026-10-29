# Fiche_Simple_-_VM_Rocky_9_Securite_Hardening_Flux_Firewalld.md

- **Environnement** : VM ou serveur dédié Rocky Linux 9 avant ouverture en production
- **OS / Version** : Rocky Linux 9 / famille RHEL 9
- **Catégorie** : sécurité / pare-feu

---

## Problème précis à résoudre

N'ouvrir que les services requis dans la bonne zone.

## 1. Hors-Production (Lab / Test / POC)

1. Repérer interface et zone :
   ```bash
   sudo firewall-cmd --get-active-zones
   ```
   👉 Explication : évite de modifier la mauvaise zone.

2. Lister la zone active (remplacer `public` par la zone relevée) :
   ```bash
   sudo firewall-cmd --zone=public --list-all
   ```
   👉 Explication : montre services et ports ouverts.

3. Lister les ports en écoute :
   ```bash
   sudo ss -lntup
   ```
   👉 Explication : compare l'écoute réelle et les règles.

4. Ouvrir uniquement un service requis (exemple `https`, à adapter), vérifier et recharger :
   ```bash
   sudo firewall-cmd --permanent --zone=public --add-service=https
   sudo firewall-cmd --reload
   ```
   👉 Explication : la règle permanente est contrôlée avant rechargement.

## 2. Production — Contrôles

Garder une source d'administration explicitement autorisée et tester depuis le client prévu.

## 3. Production — Sécurité

- Ne jamais désactiver globalement le pare-feu.

## Validation et retour arrière

- **Validation** : seuls les flux attendus sont ouverts; refus depuis une source non autorisée.
- **Retour arrière** : `sudo firewall-cmd --permanent --zone=public --remove-service=https` puis `sudo firewall-cmd --reload`.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Red Hat — SELinux sur RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
- [Guide complet hardening Rocky Linux 9](/02-fiches-completes/rocky-linux/9/autres/24-hardening-production-rocky-linux-9#5-limiter-les-flux-firewalld)