# Fiche_Simple_-_Tout-en-un_Revue_Configuration_Securite

- **Environnement** : poste ou serveur administré avec autorisation
- **OS / Version** : Linux ou Windows ; appliquer uniquement les contrôles compatibles avec l'OS
- **Catégorie** : Tout-en-un / Sécurité et durcissement
- **Tags** : `transverse`, `tout-en-un`, `securite`, `durcissement`, `audit-defensif`

---

## Problème précis à résoudre

Collecter un état de sécurité de base en lecture seule et comparer les écarts à une référence approuvée, sans scanner d'autres hôtes ni modifier le système.

## 1. Hors-Production (Lab / Test / POC)

1. Établir l'identité et l'heure système Linux :
   ```bash
   hostnamectl
   date -Is
   ```
   👉 Explication : consigne le contexte de la collecte ; expurger les identifiants avant partage externe.

2. Relever les mises à jour disponibles sans les appliquer sous Debian/Ubuntu :
   ```bash
   apt list --upgradable
   ```
   👉 Explication : liste les mises à jour connues des index APT existants ; ne met pas à jour les index ni les paquets.

3. Relever les services en échec et les sockets à l'écoute sous Linux :
   ```bash
   systemctl --failed --no-pager
   ss -lntup
   ```
   👉 Explication : repère les services défaillants et ports locaux ; interpréter avec le rôle déclaré et ne pas assimiler chaque port à une vulnérabilité.

4. Inspecter le profil pare-feu local si l'outil est présent :
   ```bash
   sudo nft list ruleset
   ```
   👉 Explication : lecture seule des règles nftables ; une sortie vide ne prouve pas l'absence d'autres couches de filtrage.

5. Contrôler sous Windows l'état de Defender et les mises à jour disponibles :
   ```powershell
   Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
   ```
   👉 Explication : collecte deux états locaux sans modifier les protections ; vérifier la politique effective de l'organisation.

## 2. Production — Contrôles

Définir un périmètre, un propriétaire, une référence de configuration et un canal de transfert protégé. Attribuer chaque écart à un responsable et une échéance avant tout changement.

## 3. Production — Sécurité

La fiche est une revue locale défensive : aucun test d'intrusion, balayage, désactivation de protection ou collecte de données hors périmètre. Ne pas transmettre de sorties brutes contenant des noms d'hôtes, IP internes, comptes ou logiciels non publics.

## Validation et retour arrière

- **Validation** : contrôles reproductibles, périmètre autorisé, écarts documentés par rapport à une politique approuvée.
- **Retour arrière** : aucune modification n'a été faite ; les éléments collectés sont conservés selon la politique de rétention.

## Si le problème n'est pas résolu

- [CIS Benchmarks — repères de configuration](https://www.cisecurity.org/cis-benchmarks)
- [Microsoft Learn — Defender Antivirus](https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-windows)

## Historique de vérification

| Vérifié le | OS / version | Logiciel / version | Testeur | Verdict | Sources |
|---|---|---|---|---|---|
| 2026-10-31 | Linux / Windows | Outils intégrés | — | Non testé sur plateforme cible | Références ci-dessus |
