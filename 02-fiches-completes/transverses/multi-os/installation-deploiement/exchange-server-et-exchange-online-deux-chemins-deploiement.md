# Exchange : choisir et déployer entre Exchange Server (sur site) et Exchange Online (Microsoft 365)

- **OS / Version** : Windows Server (Exchange Server) / tenant Microsoft 365 (Exchange Online)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Deux chemins distincts : A Exchange Server autohébergé, B Exchange Online ; point de décision et hybride
- **Catégorie** : Messagerie
- **Tags** : `exchange-server`,`exchange-online`,`microsoft-365`,`messagerie`,`hybride`

## 1. Portée, hypothèses et licences

- Les deux produits sont **différents** : Exchange Server est un logiciel installé et exploité par vous ; Exchange Online est un service SaaS inclus dans des abonnements Microsoft 365/Office 365. Ne pas mélanger leurs procédures.
- **Licences** : Exchange Server requiert des licences serveur et des CAL ; Exchange Online requiert un abonnement par utilisateur. La version « Subscription Edition » d'Exchange Server et le calendrier de fin de support des versions antérieures sont publiés par Microsoft : consulter la politique de cycle de vie avant de choisir une version.
- Hypothèses : domaine [[Glossary:DNS]] maîtrisé, Active Directory en place pour le chemin A ou hybride, mandat de migration signé.
- Ce document ne remplace pas les guides de l'éditeur ; les prérequis de version (Windows Server, .NET, Active Directory) varient par build et doivent être lus dans la matrice de support Exchange.

## 2. Arbre de décision

| Critère | Chemin A : Exchange Server | Chemin B : Exchange Online |
|---|---|---|
| Hébergement | Vos serveurs | Microsoft |
| Maintenance | Correctifs, sauvegarde, DAG par vos soins | Gérée par Microsoft |
| Identité | Active Directory obligatoire | Microsoft Entra ID (synchronisation facultative) |
| Cas d'usage | Contraintes de localisation, applications héritées | Cas général |
| Hybride | Possible avec les deux (Hybrid Configuration Wizard) | Idem |

## 3. Chemin A — Exchange Server (sur site)

1. Lire la matrice de support et les prérequis de la version retenue ; dimensionner avec l'outil de dimensionnement Microsoft (Exchange Server Role Requirements Calculator selon la version).
2. Préparer Active Directory (extension de schéma, préparation du domaine) uniquement après sauvegarde de l'état système des contrôleurs de domaine et accord du responsable [[Glossary:AD]]. La syntaxe des options de `Setup.exe` (`/PrepareSchema`, `/PrepareAD`, acceptation de licence) est propre à la version : la copier depuis la documentation de la version retenue.
3. Installer les prérequis Windows et le runtime documentés, puis lancer l'installation depuis le média officiel en mode assistant ou ligne de commande.
4. Configuration post-installation : certificats publics, URLs de services (autodiscover, EWS, OWA), connecteurs d'envoi/réception, retrait des accès anonymes ou ouverts, configuration de la sauvegarde.
5. Vérifications :

```powershell
Get-ExchangeServer | Format-List Name,AdminDisplayVersion,ServerRole
Test-ServiceHealth
Get-MailboxDatabase -Status | Format-List Name,Mounted
Test-MailFlow
```

6. Exposer uniquement les services nécessaires par un reverse proxy/pare-feu ; appliquer les correctifs de sécurité cumulatifs dès leur validation.

## 4. Chemin B — Exchange Online

1. Valider le domaine dans le centre d'administration Microsoft 365 et attribuer les licences.
2. Se connecter en PowerShell (module `ExchangeOnlineManagement`) :

```powershell
Install-Module ExchangeOnlineManagement -Scope CurrentUser
Connect-ExchangeOnline -UserPrincipalName admin@contoso.example
Get-AcceptedDomain
Get-Mailbox -ResultSize 10
```

3. Configurer les enregistrements DNS demandés par la console (MX, [[Glossary:SPF]], Autodiscover) ; publier SPF, [[Glossary:DKIM]] et [[Glossary:DMARC]]. Contrôler : `Get-DkimSigningConfig -Identity contoso.example`.
4. Imposer l'authentification moderne et l'accès conditionnel côté Entra ID ; désactiver l'authentification de base selon la politique de Microsoft en vigueur.
5. Migrer les boîtes par la méthode adaptée (basculement, par étapes, hybride, [[Glossary:IMAP]]) via le centre d'administration, par lots pilotes.

## 5. Chemin hybride (optionnel)

Utiliser l'assistant de configuration hybride (Hybrid Configuration Wizard) publié par Microsoft : il exige un serveur Exchange à jour, une synchronisation d'annuaire et des certificats valides. Planifier le routage du courrier et la décommission documentée des serveurs.

## 6. Validation

- Chemin A : bases montées, `Test-MailFlow` réussi, envoi/réception externe testé depuis une boîte pilote, certificat valide, sauvegarde restaurée sur un environnement isolé.
- Chemin B : `Get-AcceptedDomain` correct, flux entrant/sortant testé, SPF/DKIM/DMARC en réussite sur un message de test, accès conditionnel appliqué.
- Dans les deux cas : journaux consultés, comptes de service documentés, contacts d'urgence validés.

## 7. Retour arrière

- Chemin A : conserver MX inchangé jusqu'à validation ; restaurer le snapshot/la sauvegarde de l'installation, ne pas désinstaller Exchange d'un domaine sans la procédure officielle (les attributs AD restent).
- Chemin B : repasser les MX vers l'ancien système, suspendre les lots de migration, retirer les licences après vérification des données ; la suppression d'une boîte entre dans une période de conservation définie par Microsoft.
- Les modifications de schéma Active Directory sont en pratique irréversibles : exiger une restauration de forêt documentée avant de les appliquer.

## Sources officielles

- [Exchange Server — documentation](https://learn.microsoft.com/exchange/exchange-server)
- [Exchange Server — configuration requise et support](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Exchange Online — documentation](https://learn.microsoft.com/exchange/exchange-online)
- [Se connecter à Exchange Online PowerShell](https://learn.microsoft.com/powershell/exchange/connect-to-exchange-online-powershell)
- [Exchange hybride](https://learn.microsoft.com/exchange/exchange-hybrid)

Aucun serveur Exchange ni tenant Microsoft 365 n'a été utilisé pendant la rédaction ; les syntaxes et versions doivent être validées sur la documentation en vigueur.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |
