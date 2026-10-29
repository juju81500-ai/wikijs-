# Fiche_Simple_-_Hote_Windows_11_Deploiement_Inscrire_Configurer_Poste.md

- **Environnement** : Parc de postes utilisateur: poste physique ou VM de test
- **OS / Version** : Windows 11 Pro ou Enterprise selon la gestion prévue
- **Catégorie** : déploiement de poste de travail

---

## Problème précis à résoudre

Nommer, inscrire et configurer le poste selon le mécanisme de gestion.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le nom de poste selon la convention de parc (remplacer PC-EXEMPLE-01 par le nom réel) :
   ```powershell
   Rename-Computer -NewName PC-EXEMPLE-01 -Restart
   ```
   👉 Explication : renomme le poste et le redémarre.

2. Inscrire le poste : **Paramètres > Comptes > Accès Professionnel ou scolaire > Se connecter** (Entra ID/Intune), ou joindre le domaine AD DS selon la procédure de l'organisation.
   👉 Explication : l'étape exacte dépend de l'outil de gestion; vérifier ensuite que le poste apparaît dans la console d'administration.

3. Contrôler l'état d'inscription :
   ```powershell
   dsregcmd /status
   ```
   👉 Explication : affiche l'état de jonction (AzureAdJoined, DomainJoined).

4. Laisser appliquer stratégies, certificats, VPN, Wi-Fi et applications attribuées.
   👉 Explication : ces éléments diffèrent selon l'outil de gestion.

5. Utiliser un compte standard et gérer l'administration locale avec Windows LAPS ou un mécanisme approuvé.
   👉 Explication : évite les comptes administrateurs partagés.

## 2. Production — Contrôles

Vérifier la présence du poste dans la console de gestion et l'application des stratégies.

## 3. Production — Sécurité

- Utilisateur sans droits administrateur locaux permanents.

## Validation et retour arrière

- **Validation** : le poste porte le bon nom, apparaît dans la console et reçoit ses stratégies.
- **Retour arrière** : retirer le poste de la console et du domaine/tenant, puis réinstaller depuis l'image approuvée.

## Si le problème n'est pas résolu

- [Microsoft Learn — Autopilot](https://learn.microsoft.com/en-us/autopilot/)
- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Guide complet](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production#3-inscrire-et-configurer-le-poste)