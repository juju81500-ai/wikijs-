# Fiche_Simple_-_Windows_Client_11_OpenVPN_Valider

- **Environnement** : Poste Windows 11 (client OpenVPN Community)
- **OS / Version** : Windows 11; version du client à vérifier sur la page de téléchargement officielle
- **Catégorie** : OpenVPN Community client / valider

---

## Problème précis à résoudre

Vérifier la connexion VPN et les routes.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : clic droit sur l'icône OpenVPN GUI > Connecter, puis saisir la phrase de passe si demandée.
   👉 Explication : L'icône devient verte une fois la connexion établie.

2. Vérifier l'interface et les routes :
   ```powershell
   Get-NetAdapter | Where-Object { $_.InterfaceDescription -match 'TAP|Wintun|OpenVPN' }
   route print
   Test-NetConnection HOTE_INTERNE -Port PORT_INTERNE
   ```
   👉 Explication : HOTE_INTERNE et PORT_INTERNE désignent une ressource autorisée de test (à remplacer). Seules les routes approuvées doivent apparaître.

3. Consulter le journal :
   ```powershell
   Get-Content "$env:USERPROFILE\OpenVPN\log\NOM_PROFIL.log" -Tail 30
   ```
   👉 Explication : NOM_PROFIL est le profil utilisé (à remplacer); le dossier de journaux peut différer selon l'installation (vérifier). Rechercher une authentification réussie.

## 2. Production — Contrôles

Consigner le résultat et l'heure du test.

## 3. Production — Sécurité

- Se déconnecter après le test si le poste est partagé.

## Validation et retour arrière

- **Validation** : Connexion établie, ressource interne joignable, pas de route inattendue.
- **Retour arrière** : Déconnecter via l'icône et supprimer le profil si la recette échoue.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-sauvegarder-restaurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — téléchargements officiels](https://openvpn.net/community-downloads/)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)