# Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Securiser

- **Environnement** : Serveurs Windows Server 2022 (Connection Server), vCenter, UAG, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version Horizon à vérifier auprès de l'éditeur
- **Catégorie** : VDI / Horizon
- **Tags** : `vmware-horizon`, `horizon`, `windows-server`, `securite`

---

## Problème précis à résoudre

Sécuriser Horizon : certificats TLS, comptes, pare-feu.

## 1. Hors-Production (Lab / Test / POC)

1. Demander un certificat pour CS1_HORIZON à l'AC interne et l'importer dans le magasin Ordinateur ; vérifier. PowerShell :
```powershell
Get-ChildItem Cert:\LocalMachine\My | Format-List Subject,FriendlyName,NotAfter,Thumbprint
```
   👉 Explication : le Connection Server utilise le certificat portant le nom convivial vdm (à confirmer dans la documentation de la version).

2. Redémarrer le service Connection Server puis valider dans GUI **Settings > Servers > Connection Servers** que le certificat est reconnu.
   👉 Explication : sans redémarrage l'ancien certificat reste servi.

3. Remplacer aussi le certificat de l'UAG via GUI **Admin UI > Advanced Settings > TLS Server Certificate Settings**.
   👉 Explication : évite l'avertissement côté client.

4. Pare-feu : n'autoriser que 443 vers le Connection Server depuis l'UAG et les administrateurs :
```powershell
New-NetFirewallRule -DisplayName 'Horizon CS HTTPS' -Direction Inbound -Protocol TCP -LocalPort 443 -RemoteAddress IP_UAG -Action Allow
```
   👉 Explication : IP_UAG est à remplacer ; les autres ports du protocole sont dans la doc officielle.

5. Administration : GUI **Settings > Administrators**, rôles nominatifs et authentification forte.
   👉 Explication : pas de compte partagé.

## 2. Production — Contrôles

- Surveiller l'expiration des certificats.
- Journaux Horizon centralisés.

## 3. Production — Sécurité

- Désactiver les protocoles TLS faibles selon la politique de l'organisation.
- Pas de secret dans les scripts.

## Validation et retour arrière

- **Validation** : Certificat valide sans alerte, accès restreint.
- **Retour arrière** : Réimporter l'ancien certificat et redémarrer le service.

## Si le problème n'est pas résolu

- [Documentation Horizon (Omnissa/VMware)](https://docs.omnissa.com/)
- [Broadcom TechDocs — Horizon](https://techdocs.broadcom.com/)
- [Fiche d'entrée du logiciel](../../../../Logiciels/13-Poste-de-travail-et-VDI/Fiche_Logiciel_-_VMware-Horizon.md)
