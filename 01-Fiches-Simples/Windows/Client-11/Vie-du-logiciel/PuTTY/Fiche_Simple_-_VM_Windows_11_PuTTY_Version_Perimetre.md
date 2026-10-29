# Fiche_Simple_-_VM_Windows_11_PuTTY_Version_Perimetre.md

- **Environnement** : Poste Windows 11 x64 d'administration
- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Catégorie** : client SSH / cadrage
- **Tags** : `putty`, `windows11`, `ssh`, `puttygen`, `host-key`

---

## Problème précis à résoudre

Confirmer la version Stable et la source officielle avant de télécharger.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter la page officielle : **https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html** (ou `putty.software`).
   👉 Explication : le guide indique PuTTY 0.85 comme dernière version Stable; à reconfirmer avant usage.

2. Éviter les sites d'agrégation et les domaines ressemblants : `putty.org` n'est pas le site de l'équipe PuTTY.
   👉 Explication : limite le risque de faux installateur.

3. Limiter l'usage à SSH vers un hôte autorisé : pas de Telnet, Rlogin ni transfert de ports.
   👉 Explication : périmètre de la procédure.

## 2. Production — Contrôles

Faire valider la version et la source par l'équipe de sécurité du poste de travail.

## 3. Production — Sécurité

- Télécharger uniquement depuis les domaines officiels.

## Validation et retour arrière

- **Validation** : Version et URL officielles notées.
- **Retour arrière** : Aucune installation n'est faite à ce stade.

## Si le problème n'est pas résolu

- [PuTTY — page officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [PuTTY — clés de signature](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet — 1. Version et périmètre](../../../../../02-Fiches-Completes/Windows/Client-11/Installation-Deploiement/84_Deploiement_PuTTY_0.85_Windows_11.md#1-version-et-perimetre)
