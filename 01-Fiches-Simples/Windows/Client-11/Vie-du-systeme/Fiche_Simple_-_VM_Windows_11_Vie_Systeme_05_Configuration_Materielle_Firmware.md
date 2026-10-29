# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-05`

---

## Problème précis à résoudre

Régler l'UEFI : démarrage sécurisé, TPM 2.0, virtualisation.

## 1. Hors-Production (Lab / Test / POC)

1. Accéder au firmware : **Paramètres > Système > Récupération > Démarrage avancé > Redémarrer maintenant > Dépannage > Options avancées > Paramètres du micrologiciel UEFI**.
   ```powershell
   shutdown /r /fw /t 0
   ```
   👉 Explication : redémarre directement dans l'interface UEFI (touche constructeur F2, F10, Suppr sinon).

2. Dans l'UEFI : activer **UEFI (désactiver CSM/Legacy)**, **Secure Boot**, **TPM 2.0** (« PTT » chez Intel, « fTPM » chez AMD) et la virtualisation (VT-x/AMD-V) si besoin.
   👉 Explication : prérequis de Windows 11, de BitLocker et des protections basées sur la virtualisation.

3. Définir un mot de passe d'administrateur du firmware (`MOT_DE_PASSE_UEFI`, stocké dans le coffre de l'entreprise, jamais dans la fiche) et placer le disque système en premier dans l'ordre de démarrage.
   👉 Explication : empêche la modification du firmware et le démarrage sur support externe.

4. Après installation, contrôler l'état depuis Windows : **Informations système (msinfo32) > Mode BIOS = UEFI, État du démarrage sécurisé = Activé**.
   ```powershell
   Confirm-SecureBootUEFI
   Get-Tpm | Select-Object TpmPresent,TpmReady,TpmEnabled
   $env:firmware_type
   ```
   👉 Explication : contrôle l'état de Secure Boot et du TPM; `$env:firmware_type` doit valoir `UEFI`.

## 2. Production — Contrôles

Mettre le firmware à jour via l'outil du constructeur (Dell Command Update, HP Image Assistant, Lenovo System Update) avant la mise en production.

## 3. Production — Sécurité

Mot de passe firmware, désactivation du démarrage USB hors maintenance, TPM actif.

## Validation et retour arrière

- **Validation** : `Confirm-SecureBootUEFI` renvoie `True` et le TPM est prêt.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
