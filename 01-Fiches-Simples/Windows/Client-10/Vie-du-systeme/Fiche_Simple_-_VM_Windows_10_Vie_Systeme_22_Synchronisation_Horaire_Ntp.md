# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Synchroniser l'horloge avec le domaine ou une source NTP fiable.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler : **Paramètres > Heure et langue > Date et heure > Synchroniser maintenant**.
   ```powershell
   w32tm /query /status
   w32tm /query /source
   ```
   👉 Explication : indique la source et le décalage; un poste de domaine suit le contrôleur de domaine.

2. Pour un poste hors domaine, fixer une source NTP (`SOURCE_NTP`, par exemple le serveur de l'entreprise).
   ```powershell
   w32tm /config /manualpeerlist:"SOURCE_NTP" /syncfromflags:manual /reliable:no /update
   Restart-Service w32time
   w32tm /resync
   ```
   👉 Explication : configure le client NTP, redémarre le service et force la synchronisation.

3. Mesurer le décalage avec la source.
   ```powershell
   w32tm /stripchart /computer:SOURCE_NTP /samples:3 /dataonly
   ```
   👉 Explication : affiche le décalage en secondes.

4. S'assurer que le service est automatique.
   ```powershell
   Set-Service w32time -StartupType Automatic
   Get-Service w32time
   ```
   👉 Explication : garantit la synchronisation après redémarrage.

## 2. Production — Contrôles

Source = contrôleur de domaine pour les postes joints; NTP interne sinon.

## 3. Production — Sécurité

Une dérive supérieure à 5 minutes casse Kerberos et fausse les journaux.

## Validation et retour arrière

- **Validation** : Décalage inférieur à une seconde et `Source` attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
