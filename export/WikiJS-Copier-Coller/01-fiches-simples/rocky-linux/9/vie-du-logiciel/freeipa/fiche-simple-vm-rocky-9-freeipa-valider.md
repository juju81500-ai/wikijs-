# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Valider.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / validation

---

## Problème précis à résoudre

Contrôler que FreeIPA fonctionne de bout en bout après installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier Kerberos :
   ```bash
   kinit admin
   klist
   ```
   👉 Explication : Obtient puis affiche le ticket Kerberos.

2. Interroger l'annuaire :
   ```bash
   ipa user-find
   ipa host-find
   ```
   👉 Explication : Les requêtes LDAP/IPA doivent répondre.

3. Vérifier les services :
   ```bash
   sudo ipactl status
   ```
   👉 Explication : Tous les services IdM doivent être démarrés (`systemctl status ipa` est équivalent).

4. Ouvrir **https://FQDN/ipa/ui/** depuis un poste autorisé (remplacer FQDN par le nom du serveur).
   👉 Explication : vérifie l'interface web.

5. Sur un client de test, installer `ipa-client` puis lancer `ipa-client-install`.
   👉 Explication : confirme la jonction au domaine sans toucher aux postes de production.

## 2. Production — Contrôles

Valider aussi qu'une sauvegarde `ipa-backup` existe et que sa restauration a été jouée.

## 3. Production — Sécurité

- Accès à l'interface web limité aux postes d'administration.
- Ne pas tester sur des postes de production.

## Validation et retour arrière

- **Validation** : ticket Kerberos, requêtes IPA, services et interface web OK.
- **Retour arrière** : corriger la cause puis recommencer; sinon suivre l'étape de retour arrière.

## Si le problème n'est pas résolu

- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 7](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9#7-validation)