# Fiche_Simple_-_Cloud_Google_Workspace_Configurer_SPF_DKIM_DMARC

- **Environnement** : Tenant Google Workspace (SaaS), administré via la console d'administration admin.google.com
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif

---

## Problème précis à résoudre

Publier SPF, activer DKIM et publier DMARC pour DOMAINE afin de limiter l'usurpation d'identité.

## 1. Hors-Production (Lab / Test / POC)

1. Publier un TXT SPF sur DOMAINE (à remplacer) : `v=spf1 include:_spf.google.com ~all` (ajouter les autres expéditeurs légitimes; un seul SPF par domaine).
   👉 Explication : valeur recommandée par Google; durcir en `-all` quand l'inventaire est complet.

2. Interface : console d'administration > Applications > Google Workspace > Gmail > Authentifier les e-mails : sélectionner DOMAINE, générer la clé DKIM (2048 bits recommandé), publier le TXT indiqué (nom et valeur propres au domaine) chez l'hébergeur DNS, puis cliquer sur « Démarrer l'authentification ».
   👉 Explication : DKIM ne signe qu'après publication DNS et propagation.

3. Publier un TXT `_dmarc.DOMAINE` : `v=DMARC1; p=none; rua=mailto:ADRESSE_RAPPORTS`.
   👉 Explication : ADRESSE_RAPPORTS est à remplacer; démarrer en `p=none`, puis `quarantine`, puis `reject`.

## 2. Production — Contrôles

Analyser les rapports DMARC plusieurs semaines avant de durcir.

## 3. Production — Sécurité

- Protéger la zone DNS.
- Inventorier tous les expéditeurs tiers.

## Validation et retour arrière

- **Validation** : Un message de test affiche spf=pass, dkim=pass et dmarc=pass; la console indique « Authentification des e-mails ».
- **Retour arrière** : Passer DMARC en `p=none` ou retirer l'enregistrement; arrêter l'authentification DKIM dans la console.

## Si le problème n'est pas résolu

- [Définir SPF](https://support.google.com/a/answer/33786)
- [Activer DKIM](https://support.google.com/a/answer/180504)
- [Définir DMARC](https://support.google.com/a/answer/2466563)
- [Centre d'aide Google Workspace Admin](https://support.google.com/a/)
- [Fiche d'entrée Google Workspace](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-google-workspace)