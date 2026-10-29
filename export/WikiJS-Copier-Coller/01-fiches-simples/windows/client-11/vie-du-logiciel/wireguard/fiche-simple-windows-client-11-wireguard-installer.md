# Fiche_Simple_-_Windows_Client_11_WireGuard_Installer

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / installer

---

## Problème précis à résoudre

Installer le client WireGuard depuis la source officielle.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : télécharger l'installateur Windows depuis la page officielle wireguard.com/install puis l'exécuter en administrateur.
   👉 Explication : N'utiliser que wireguard.com; consigner la version.

2. Alternative en PowerShell élevé avec winget (vérifier l'identifiant publié) :
   ```powershell
   winget search wireguard
   winget install --id WireGuard.WireGuard -e
   ```
   👉 Explication : Contrôler dans le résultat de winget search que l'identifiant WireGuard.WireGuard correspond bien au paquet officiel avant d'installer.

3. Contrôler l'installation :
   ```powershell
   Get-Package -Name '*WireGuard*' -ErrorAction SilentlyContinue
   ```
   👉 Explication : Le client WireGuard doit être listé; l'application apparaît dans le menu Démarrer.

## 2. Production — Contrôles

Consigner la version installée.

## 3. Production — Sécurité

- Ne pas utiliser de build tiers.

## Validation et retour arrière

- **Validation** : Application WireGuard présente.
- **Retour arrière** : Paramètres > Applications > WireGuard > Désinstaller.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-configurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)