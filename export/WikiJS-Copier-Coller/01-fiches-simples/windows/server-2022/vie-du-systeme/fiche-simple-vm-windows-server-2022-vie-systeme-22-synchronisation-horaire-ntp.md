# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Garder une heure exacte avec le service Temps Windows.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Paramètres > Heure et langue > Date et heure > Synchroniser maintenant**.
   ```powershell
   w32tm /query /status
   w32tm /query /source
   ```
   👉 Explication : affiche la source de temps et l'écart; hors domaine, la source est `time.windows.com`.

2. Hors domaine, définir des sources NTP (remplacer `SOURCE_NTP`, ex. `fr.pool.ntp.org`) :
   ```powershell
   w32tm /config /manualpeerlist:"SOURCE_NTP" /syncfromflags:manual /reliable:yes /update
   Restart-Service w32time
   w32tm /resync
   ```
   👉 Explication : fixe la source et force la synchronisation; dans un domaine, le contrôleur de domaine PDC est la source.

3. Mesurer l'écart par rapport à une source :
   ```powershell
   w32tm /stripchart /computer:SOURCE_NTP /samples:3 /dataonly
   ```
   👉 Explication : l'écart doit rester sous la seconde.

## 2. Production — Contrôles

Dans un domaine, ne configurer manuellement que l'émulateur PDC.

## 3. Production — Sécurité

Limiter le trafic UDP 123 sortant aux sources de confiance.

## Validation et retour arrière

- **Validation** : `w32tm /query /status` indique une synchronisation récente.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)