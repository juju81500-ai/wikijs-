# Fiche_Simple_-_VM_Rocky_9_Securite_Hardening_Perimetre_Acces_Secours.md

- **Environnement** : VM ou serveur dédié Rocky Linux 9 avant ouverture en production
- **OS / Version** : Rocky Linux 9 / famille RHEL 9
- **Catégorie** : sécurité / cadrage

---

## Problème précis à résoudre

Se garantir un accès de secours avant de durcir le serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'identité du serveur et les comptes ouverts :
   ```bash
   hostnamectl
   who
   ```
   👉 Explication : confirme le périmètre (hôte, utilisateurs connectés).

2. Sauvegarder la configuration SSH avant toute modification :
   ```bash
   sudo cp -a /etc/ssh /etc/ssh.avant-hardening
   ```
   👉 Explication : permet de restaurer depuis la console en cas de perte d'accès.

3. Console hyperviseur : **Console de la VM > Ouvrir une session locale** et tester un compte de secours.
   👉 Explication : l'accès console prouve que l'on peut corriger une règle SSH ou pare-feu fautive.

## 2. Production — Contrôles

Confirmer rôle, zone réseau, ports entrants, utilisateurs, responsable et fenêtre de changement.

## 3. Production — Sécurité

- Ne pas modifier SSH ou le pare-feu sans console de secours testée.

## Validation et retour arrière

- **Validation** : console et compte de secours testés, copie SSH faite.
- **Retour arrière** : `sudo rm -r /etc/ssh && sudo cp -a /etc/ssh.avant-hardening /etc/ssh` (depuis la console).

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Red Hat — SELinux sur RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
- [Guide complet hardening Rocky Linux 9](/02-fiches-completes/rocky-linux/9/autres/24-hardening-production-rocky-linux-9#1-perimetre-et-acces-de-secours)