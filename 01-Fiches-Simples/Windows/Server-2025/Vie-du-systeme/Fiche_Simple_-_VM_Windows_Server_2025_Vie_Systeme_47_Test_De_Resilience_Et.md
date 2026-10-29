# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Valider que la supervision détecte un incident.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter volontairement un service non critique en fenêtre de test (**services.msc > Arrêter**) :
   ```powershell
   Stop-Service NOM_SERVICE
   ```
   👉 Explication : simule une panne de service.

2. Contrôler que l'alerte est reçue puis rétablir :
   ```powershell
   Start-Service NOM_SERVICE
   Get-Service NOM_SERVICE
   ```
   👉 Explication : l'alerte doit arriver à l'équipe puis se clôturer.

3. Simuler un disque presque plein sur un volume de test :
   ```powershell
   fsutil file createnew D:\Test\remplissage.bin 1073741824
   Remove-Item D:\Test\remplissage.bin
   ```
   👉 Explication : crée un fichier de 1 Go puis le supprime; à adapter pour franchir le seuil d'alerte.

## 2. Production — Contrôles

Documenter le temps de détection et l'équipe notifiée.

## 3. Production — Sécurité

Réaliser les tests en fenêtre autorisée, jamais sur un service critique en production.

## Validation et retour arrière

- **Validation** : Alerte reçue dans le délai prévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
