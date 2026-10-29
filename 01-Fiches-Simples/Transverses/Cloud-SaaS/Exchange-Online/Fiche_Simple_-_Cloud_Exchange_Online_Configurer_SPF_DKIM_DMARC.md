# Fiche_Simple_-_Cloud_Exchange_Online_Configurer_SPF_DKIM_DMARC

- **Environnement** : Tenant Microsoft 365 / Exchange Online (SaaS), administré depuis un poste d'administration
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif
- **Tags** : `exchange-online`, `microsoft-365`, `cloud-saas`, `administration-defensive`, `messagerie`, `tssr`

---

## Problème précis à résoudre

Publier SPF, activer DKIM et publier DMARC pour DOMAINE afin de limiter l'usurpation d'identité.

## 1. Hors-Production (Lab / Test / POC)

1. Publier un enregistrement TXT SPF sur DOMAINE (à remplacer), valeur recommandée par Microsoft pour Exchange Online : `v=spf1 include:spf.protection.outlook.com -all` (ajouter les autres expéditeurs légitimes avant `-all`; un seul enregistrement SPF par domaine).
   👉 Explication : SPF déclare les serveurs autorisés à émettre.

2. Lire la configuration DKIM :
   ```powershell
   Get-DkimSigningConfig -Identity DOMAINE | Format-List Domain,Enabled,Selector1CNAME,Selector2CNAME
   ```
   👉 Explication : fournit les deux CNAME de sélecteurs à publier dans le DNS.

3. Après propagation des deux CNAME, activer la signature :
   ```powershell
   Set-DkimSigningConfig -Identity DOMAINE -Enabled $true
   ```
   👉 Explication : si la configuration n'existe pas, la créer avec `New-DkimSigningConfig -DomainName DOMAINE -Enabled $true` (vérifier la syntaxe dans la documentation). Équivalent GUI : portail Microsoft Defender > E-mail et collaboration > Stratégies et règles > Stratégies de menaces > Authentification des e-mails.

4. Publier un TXT `_dmarc.DOMAINE` : `v=DMARC1; p=none; rua=mailto:ADRESSE_RAPPORTS`.
   👉 Explication : ADRESSE_RAPPORTS est à remplacer; démarrer en `p=none` pour observer, puis durcir vers `quarantine` puis `reject`.

## 2. Production — Contrôles

Analyser les rapports DMARC pendant plusieurs semaines avant d'appliquer `quarantine` ou `reject`.

## 3. Production — Sécurité

- Utiliser `-all` seulement quand tous les expéditeurs sont inventoriés.
- Protéger la zone DNS.

## Validation et retour arrière

- **Validation** : Un message de test affiche spf=pass, dkim=pass et dmarc=pass dans les en-têtes.
- **Retour arrière** : Retirer ou assouplir l'enregistrement DMARC (`p=none`) ; désactiver DKIM avec `Set-DkimSigningConfig -Identity DOMAINE -Enabled $false`.

## Si le problème n'est pas résolu

- [SPF dans Microsoft 365](https://learn.microsoft.com/defender-office-365/email-authentication-spf-configure)
- [DKIM dans Microsoft 365](https://learn.microsoft.com/defender-office-365/email-authentication-dkim-configure)
- [DMARC dans Microsoft 365](https://learn.microsoft.com/defender-office-365/email-authentication-dmarc-configure)
- [Exchange Online — documentation officielle](https://learn.microsoft.com/exchange/exchange-online)
- [Fiche d'entrée Exchange Online](../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Online.md)
