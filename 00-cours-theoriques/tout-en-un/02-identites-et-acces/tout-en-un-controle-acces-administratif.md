# Fiche_Simple_-_Tout-en-un_Controle_Acces_Administratif

- **Environnement** : serveur Linux ou Windows administré
- **OS / Version** : multi-OS ; lecture seule
- **Catégorie** : Tout-en-un / Identités et accès
- **Tags** : `transverse`, `tout-en-un`, `identites`, `acces`, `audit`

---

## Problème précis à résoudre

Vérifier quels comptes locaux et membres des groupes administrateurs existent, sans créer, supprimer ni modifier de compte.

## 1. Hors-Production (Lab / Test / POC)

1. Afficher l'identité et les groupes du compte courant sous Linux :
   ```bash
   id
   getent group sudo
   ```
   👉 Explication : affiche les groupes effectifs et les membres configurés du groupe `sudo`. Sur certaines distributions, le groupe privilégié porte un autre nom.

2. Afficher les comptes humains et leurs shells sous Linux :
   ```bash
   getent passwd
   ```
   👉 Explication : lit la base NSS, qui peut inclure un annuaire distant ; ne pas supposer que chaque entrée est un utilisateur humain.

3. Lister les comptes locaux et les membres du groupe Administrateurs sous Windows :
   ```powershell
   Get-LocalUser | Select-Object Name,Enabled,LastLogon
   $Administrateurs = Get-LocalGroup -SID 'S-1-5-32-544'
   Get-LocalGroupMember -Group $Administrateurs.Name
   ```
   👉 Explication : affiche l'état des comptes locaux et les membres du groupe Administrateurs local, identifié par son [[Glossary:SID]] afin d'éviter les différences de langue.

4. Contrôler la politique effective [[Glossary:SSH]] si le service est installé :
   ```bash
   sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|pubkeyauthentication) '
   ```
   👉 Explication : affiche les options effectives du serveur SSH. L'absence de `sshd` signifie que ce contrôle ne s'applique pas.

## 2. Production — Contrôles

Comparer les résultats avec la [[Glossary:CMDB]], les groupes approuvés et la politique d'accès de l'organisation. Faire examiner les appartenances privilégiées par une seconde personne.

## 3. Production — Sécurité

Ne jamais publier la sortie contenant des noms de comptes ou des groupes internes. N'effectuer aucune suppression à partir de cette seule collecte.

## Validation et retour arrière

- **Validation** : l'inventaire est comparé à la source d'autorité et les écarts sont attribués à un propriétaire.
- **Retour arrière** : aucune modification n'est effectuée. Une correction doit utiliser la fiche dédiée à l'OS ou à l'annuaire, après snapshot et avec compte de secours testé.

## Si le problème n'est pas résolu

- [Fiches comptes Debian 12](../../../01-fiches-simples/debian/12/vie-du-systeme/fiches-par-theme/administration-systeme)
- [Fiches comptes Windows Server 2022](../../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiches-par-theme/administration-systeme)
- [Documentation Microsoft — Get-LocalUser](https://learn.microsoft.com/powershell/module/microsoft.powershell.localaccounts/get-localuser)
