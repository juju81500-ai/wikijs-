# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un message légal à l'ouverture de session et appliquer la charte graphique.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le texte légal : **Stratégie de sécurité locale (secpol.msc) > Stratégies locales > Options de sécurité > Ouverture de session interactive : titre / texte du message**.
   ```powershell
   $k='HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
   Set-ItemProperty $k legalnoticecaption 'Accès réservé'
   Set-ItemProperty $k legalnoticetext 'Système réservé aux utilisateurs autorisés. Toute activité est journalisée.'
   ```
   👉 Explication : crée la bannière affichée avant l'ouverture de session.

2. Définir le fond d'écran et l'écran de verrouillage par GPO : **Configuration utilisateur > Modèles d'administration > Bureau > Papier peint du Bureau**, ou Intune **Personnalisation**.
   👉 Explication : uniformise l'identité visuelle du parc.

3. Régler le verrouillage automatique : **Paramètres > Comptes > Options de connexion > Exiger la connexion**, ou par stratégie (`InactivityTimeoutSecs`).
   ```powershell
   Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System InactivityTimeoutSecs 900 -Type DWord
   ```
   👉 Explication : verrouille la session après 900 secondes d'inactivité.

4. Vérifier au prochain verrouillage.
   ```powershell
   Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System | Select-Object legalnotice*,InactivityTimeoutSecs
   ```
   👉 Explication : contrôle les valeurs en place.

## 2. Production — Contrôles

Bannière validée par le juridique et déployée par GPO ou Intune.

## 3. Production — Sécurité

Ne mentionner ni version, ni information technique ou nom de domaine dans la bannière.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion suivante.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
