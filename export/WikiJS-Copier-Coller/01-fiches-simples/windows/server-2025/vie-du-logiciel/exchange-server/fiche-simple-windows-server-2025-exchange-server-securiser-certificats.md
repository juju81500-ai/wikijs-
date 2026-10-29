# Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Securiser_Certificats

- **Environnement** : Windows Server 2025 Standard ou Datacenter; Exchange Server Subscription Edition
- **OS / Version** : Windows Server 2025; Exchange SE — valider le build et les prérequis publiés avant intervention
- **Catégorie** : messagerie / sécurité TLS

---

## Problème précis à résoudre

Installer et affecter un certificat TLS public ou interne valide aux services Exchange nécessaires.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier les noms DNS réellement utilisés par les clients et les services Exchange avant de demander le certificat.
   👉 Explication : seuls les noms nécessaires au service doivent être inclus; la liste est à valider avec les responsables DNS.

2. Dans l’EAC, ouvrir **Serveurs > Certificats**, sélectionner le serveur Exchange SE et suivre l’action de création de demande ou d’import décrite par Microsoft.
   👉 Explication : adapter les intitulés à la version et ne pas transmettre la clé privée par un canal non approuvé.

3. Affecter le certificat validé uniquement aux services requis (par exemple IIS et SMTP selon le scénario documenté).
   👉 Explication : une affectation erronée peut interrompre les connexions clientes ou le transport de courrier.

4. Contrôler les certificats présents dans Exchange Management Shell :
   ```powershell
   Get-ExchangeCertificate | Format-Table Thumbprint,Services,NotAfter,Status
   ```
   👉 Explication : confirmer l’expiration, l’état et les services affectés; ne pas publier de clé privée.

## 2. Production — Contrôles

Planifier une fenêtre de changement, sauvegarder les configurations concernées, vérifier l’état AD/DNS et Exchange, puis appliquer les étapes d’abord en environnement pilote.

## 3. Production — Sécurité

- Utiliser des comptes nominatifs et les rôles minimaux requis; retirer les privilèges temporaires après l’opération.
- Restreindre EAC et Exchange Management Shell au réseau d’administration.
- Ne pas consigner de mot de passe, clé privée, jeton ou donnée de boîte aux lettres dans cette fiche.

## Validation et retour arrière

**Validation** : vérifier les certificats présentés par les services Exchange depuis les réseaux clients et examiner les événements TLS.
- **Retour arrière** : réaffecter un certificat précédent encore valide, selon le changement approuvé.

## Si le problème n’est pas résolu

- [Microsoft — Certificats Exchange](https://learn.microsoft.com/en-us/exchange/architecture/client-access/certificates)
- [Microsoft — Supportability Matrix](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d’entrée Exchange Server](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-server)