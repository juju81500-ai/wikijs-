# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-18`

---

## Problème précis à résoudre

Gérer le fichier hosts, uniquement pour un besoin temporaire documenté.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir le fichier `C:\Windows\System32\drivers\etc\hosts` dans un Bloc-notes lancé en administrateur : **Démarrer > Bloc-notes > clic droit > Exécuter en tant qu'administrateur > Fichier > Ouvrir**.
   ```powershell
   Get-Content "$env:SystemRoot\System32\drivers\etc\hosts"
   ```
   👉 Explication : lit le contenu actuel (lignes commençant par `#` ignorées).

2. Sauvegarder puis ajouter une entrée (ADRESSE_IP et NOM_HOTE à adapter).
   ```powershell
   Copy-Item "$env:SystemRoot\System32\drivers\etc\hosts" "$env:SystemRoot\System32\drivers\etc\hosts.bak"
   Add-Content "$env:SystemRoot\System32\drivers\etc\hosts" 'ADRESSE_IP NOM_HOTE # ticket INC-0000'
   ```
   👉 Explication : ajoute une résolution locale avec un commentaire de traçabilité.

3. Vérifier la résolution et vider le cache.
   ```powershell
   Clear-DnsClientCache
   Resolve-DnsName NOM_HOTE -LlmnrNetbiosOnly:$false
   ```
   👉 Explication : confirme que le nom est résolu comme prévu.

4. Retirer l'entrée à la fin du besoin.
   ```powershell
   Copy-Item "$env:SystemRoot\System32\drivers\etc\hosts.bak" "$env:SystemRoot\System32\drivers\etc\hosts" -Force
   ```
   👉 Explication : restaure le fichier d'origine.

## 2. Production — Contrôles

Préférer un enregistrement DNS; toute entrée `hosts` doit être temporaire et tracée.

## 3. Production — Sécurité

Le fichier `hosts` est une cible classique de détournement par les logiciels malveillants : surveiller son intégrité.

## Validation et retour arrière

- **Validation** : Le nom se résout vers l'adresse prévue, puis l'entrée est retirée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
