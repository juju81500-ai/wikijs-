# Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Acces.md

- **Environnement** : Serveur Windows dédié ou VM, accès d'administration restreint
- **OS / Version** : Windows Server 2022 ou 2025 en Desktop Experience; PRTG Network Monitor maintenu
- **Catégorie** : supervision / SNMP / WMI
- **Tags** : `prtg`, `windows-server`, `supervision`, `acces`, `rbac`, `snmpv3`

---

## Problème précis à résoudre

Séparer les droits administrateur, opérateur et comptes de scan.

## 1. Hors-Production (Lab / Test / POC)

1. Créer des comptes nominatifs et des groupes séparés : **Setup > User Accounts** et **Setup > User Groups**.
   👉 Explication : administrateurs et opérateurs lecture seule ont des droits distincts.

2. Restreindre l'interface Web aux réseaux d'administration et activer l'authentification centralisée ou le MFA lorsque disponible.
   👉 Explication : on réduit l'exposition de l'interface.

3. Utiliser des comptes en lecture seule pour WMI/Windows et SNMPv3 authPriv en lecture seule pour le réseau.
   👉 Explication : les scans n'ont jamais besoin de droits d'écriture.

4. Ne pas utiliser Domain Admin ni la communauté SNMP `public`.
   👉 Explication : ces identifiants exposent trop de droits.

## 2. Production — Contrôles

Documenter les droits d'accès aux équipements supervisés.

## 3. Production — Sécurité

- Ne pas utiliser Domain Admin pour les scans.
- Ne pas utiliser la communauté SNMP `public`.

## Validation et retour arrière

- **Validation** : Comptes nominatifs créés; aucun scan avec un compte privilégié.
- **Retour arrière** : Supprimer ou désactiver le compte créé par erreur dans **Setup > User Accounts**.

## Si le problème n'est pas résolu

- [Paessler — Exigences système PRTG](https://www.paessler.com/manuals/prtg/system_requirements)
- [Paessler — Installer le Core Server](https://www.paessler.com/manuals/prtg/install_a_prtg_core_server)
- [Guide complet — définir le modèle d'accès](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/47_Deploiement_PRTG_Network_Monitor_Windows_Server.md#3-definir-le-modele-dacces)
