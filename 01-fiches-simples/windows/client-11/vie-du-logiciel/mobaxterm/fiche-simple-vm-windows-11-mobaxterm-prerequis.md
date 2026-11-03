# Fiche_Simple_-_VM_Windows_11_MobaXterm_Prerequis

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; MobaXterm Home/Professional, version VERSION_MOBAXTERM (à remplacer)
- **Catégorie** : client SSH/RDP multi-sessions
- **Tags** : `mobaxterm`, `windows11`, `prerequis`

---

## Problème précis à résoudre

Vérifier qu'un poste Windows 11 est prêt à recevoir MobaXterm (édition, droits, réseau, politique de sécurité).

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Paramètres > Système > À propos** et noter l'édition et la version de Windows 11.
   👉 Explication : confirme que le poste est bien un client Windows 11 et non un Windows Server.

2. Dans PowerShell : `Get-ComputerInfo -Property OsName,OsVersion,OsArchitecture`.
   👉 Explication : version et architecture sous forme exploitable.

3. Choisir l'édition : Home (gratuite) ou Professional selon la licence LICENCE_MOBAXTERM (à remplacer) ; choisir installateur ou version portable.
   👉 Explication : la version portable ne s'installe pas dans Program Files ; la gestion des mises à jour et des chemins diffère.

4. Vérifier l'accès réseau aux hôtes cibles : `Test-NetConnection -ComputerName HOTE_CIBLE -Port 22` (HOTE_CIBLE à remplacer).
   👉 Explication : confirme que le flux SSH est ouvert avant toute configuration.

5. Vérifier l'outil de paquets : `winget --version`.
   👉 Explication : winget est nécessaire pour la commande d'installation ; absent, utiliser l'installation GUI.

## 2. Production — Contrôles

Valider la licence, l'édition autorisée, la liste des hôtes cibles et l'autorisation de l'éditeur logiciel (liste blanche, antivirus/EDR).

## 3. Production — Sécurité

- Télécharger uniquement depuis le site officiel mobatek.net.
- Ne pas exécuter MobaXterm en administrateur permanent.

## Validation et retour arrière

- **Validation** : Version de Windows 11, droits, réseau et édition sont documentés.
- **Retour arrière** : Aucun changement effectué ; rien à annuler.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [MobaXterm — documentation officielle](https://mobaxterm.mobatek.net/documentation.html)
- [MobaXterm — téléchargement](https://mobaxterm.mobatek.net/download.html)
- [MobaXterm — FAQ](https://mobaxterm.mobatek.net/faq.html)
