# Déployer PuTTY 0.85 sur Windows 11

- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : installateur MSI officiel, session SSH vers un hôte approuvé, authentification par clé et contrôle de clé d'hôte
- **Catégorie** : client d'administration distante
- **Tags** : `putty`, `windows11`, `ssh`, `puttygen`, `pageant`, `host-key`

## 1. Version et périmètre

Fiche simple : [vérifier la version et le périmètre](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Version_Perimetre.md).

Au 27 octobre 2026, PuTTY 0.85, publié le 16 août 2026, est la dernière version Stable indiquée par l'équipe. PuTTY est un client pour Windows, pas un serveur SSH. Cette procédure ne couvre qu'une connexion SSH à un système autorisé; Telnet, Rlogin, transfert de ports, PSCP/PSFTP en production et administration des serveurs sont exclus.

Télécharger depuis le site officiel `chiark.greenend.org.uk/~sgtatham/putty/` ou le domaine officiel `putty.software`. Éviter les sites d'agrégation et les domaines ressemblants; l'équipe PuTTY avertit spécifiquement que `putty.org` n'est pas son site.

## 2. Télécharger et vérifier l'installateur

Fiche simple : [télécharger et vérifier l'installateur](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Telecharger_Verifier.md).

Télécharger le MSI x64, sa signature détachée et la clé de publication depuis les URL officielles :

```powershell
$download = Join-Path $HOME 'Downloads\putty-0.85'
New-Item -ItemType Directory -Force -Path $download | Out-Null
Set-Location $download
Invoke-WebRequest -Uri 'https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.85-installer.msi' -OutFile '.\putty-64bit-0.85-installer.msi'
Invoke-WebRequest -Uri 'https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.85-installer.msi.gpg' -OutFile '.\putty-64bit-0.85-installer.msi.gpg'
Invoke-WebRequest -Uri 'https://www.chiark.greenend.org.uk/~sgtatham/putty/keys/release-2026.asc' -OutFile '.\release-2026.asc'
```

Avant la vérification GPG, importer la clé et confirmer son empreinte complète avec la page officielle PuTTY :

```powershell
gpg --import .\release-2026.asc
gpg --fingerprint 5C67D0F88BC3E5B5
gpg --verify .\putty-64bit-0.85-installer.msi.gpg .\putty-64bit-0.85-installer.msi
```

L'empreinte publiée pour la clé Release 2026 est `1A07 DAC0 F220 CF12 248E A719 5C67 D0F8 8BC3 E5B5`. Refuser l'artefact si l'empreinte ne correspond pas exactement ou si GPG ne confirme pas une bonne signature. Gpg4win fournit GPG sur Windows s'il n'est pas déjà installé.

Windows peut aussi vérifier la signature Authenticode intégrée au MSI :

```powershell
$signature = Get-AuthenticodeSignature .\putty-64bit-0.85-installer.msi
$signature.Status
$signature.SignerCertificate.Subject
Get-FileHash .\putty-64bit-0.85-installer.msi -Algorithm SHA256
```

Le statut doit être `Valid`; comparer l'identité du signataire et le SHA-256 aux informations publiées par l'équipe PuTTY. Ne pas installer en cas de signature invalide, d'empreinte différente ou de provenance incertaine.

## 3. Installer l'application

Fiche simple : [installer l'application](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Installer.md).

Après validation du MSI, lancer l'installation interactive :

```powershell
Start-Process msiexec.exe -Wait -ArgumentList '/i', (Join-Path $download 'putty-64bit-0.85-installer.msi')
```

Laisser l'installateur inscrire ses fichiers et composants par défaut. Ne pas exécuter PuTTY en tant qu'administrateur pour une session SSH ordinaire. Vérifier la version dans **Help > About PuTTY** ou depuis PowerShell :

```powershell
& "$env:ProgramFiles\PuTTY\putty.exe" -V
```

## 4. Préparer l'authentification

Fiche simple : [préparer l'authentification](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Authentification.md).

Utiliser d'abord la méthode d'authentification et le nom de compte fournis par l'administrateur du serveur. Pour une authentification par clé, générer une clé dans PuTTYgen au format PuTTY `.ppk`, avec une phrase secrète robuste; copier la clé publique affichée pour `authorized_keys` et la remettre à l'administrateur du serveur par le canal approuvé. Ne jamais transmettre le fichier privé `.ppk`.

Dans la session PuTTY, configurer **Connection > SSH > Auth > Credentials** pour sélectionner le fichier `.ppk`. Laisser l'agent forwarding désactivé sauf besoin explicite et approbation : lorsqu'il est activé, un serveur distant peut demander à l'agent local d'utiliser les clés chargées pendant la session. Si Pageant est nécessaire, charger uniquement les clés requises et les retirer après le travail.

## 5. Créer une session SSH sûre

Fiche simple : [créer une session SSH sûre](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Session_SSH_Sure.md).

1. Obtenir l'adresse, le port, le compte et l'empreinte de la clé d'hôte SSH auprès de l'administrateur par un canal indépendant de la première connexion.
2. Dans PuTTY, choisir le type **SSH**, saisir le nom d'hôte et le port approuvés, puis enregistrer la session sous un nom descriptif non sensible.
3. Sélectionner **Open**. Lors de la première connexion, comparer l'empreinte affichée avec celle fournie hors bande. N'accepter la clé que si l'algorithme et l'empreinte correspondent.
4. Si l'empreinte ne correspond pas, ou si PuTTY signale un changement de clé déjà connue, annuler et contacter l'administrateur via un canal séparé. Ne pas effacer l'ancienne clé et réessayer sans avoir compris le changement.
5. Se connecter avec le compte nominatif autorisé et appliquer les restrictions d'accès propres au serveur.

Ne pas configurer l'acceptation automatique des clés d'hôte et ne pas désactiver les vérifications SSH. Les sessions enregistrées et les clés d'hôte se trouvent dans le profil Windows de l'utilisateur, sous le registre PuTTY; protéger ce profil et inclure ces paramètres dans les procédures de sauvegarde/suppression appropriées.

## 6. Journalisation, transferts et données sensibles

Fiche simple : [gérer journalisation, transferts et données sensibles](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Journalisation_Transferts.md).

La journalisation de terminal est désactivée par défaut; si une politique exige un journal, sélectionner un dossier approuvé à ACL restreintes et définir la rotation/rétention. Les sorties de session peuvent contenir des identifiants, noms d'hôtes, commandes et données métier : inspecter les journaux avant de les partager.

Ne pas utiliser les protocoles Telnet ou Rlogin pour une administration réelle; leurs sessions ne protègent pas les identifiants et les données de la même façon que SSH. Les transferts PSCP/PSFTP exigent une destination autorisée et une vérification indépendante des fichiers transférés. Éviter l'option SCP non sûre et ne jamais transférer de clé privée vers l'hôte distant.

## 7. Mise à jour et réception

Fiche simple : [mettre à jour et recetter](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PuTTY/Fiche_Simple_-_VM_Windows_11_PuTTY_Mise_A_Jour_Reception.md).

Vérifier régulièrement la page Stable officielle et ses notes de version, en particulier les correctifs de sécurité. Télécharger le nouveau MSI et sa signature, vérifier la clé Release en cours selon la page des clés (elle peut changer après une rotation), puis tester la mise à jour sur un poste pilote.

- L'installateur est PuTTY 0.85 x64 officiel; la signature GPG et Authenticode sont validées.
- La connexion utilise SSH vers un hôte et un compte explicitement autorisés.
- La clé d'hôte est comparée à une empreinte obtenue hors bande; un changement inattendu bloque la connexion.
- La clé privée est chiffrée par phrase secrète et reste locale; Pageant/agent forwarding sont désactivés sauf besoin approuvé.
- Toute journalisation ou copie de fichier est protégée et revue pour données sensibles.

## Sources

- [PuTTY — téléchargement Stable 0.85 et fichiers signés](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- [PuTTY — clés de téléchargement et empreinte Release 2026](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [PuTTY — FAQ officielle, vérification des clés d'hôte et sécurité](https://www.chiark.greenend.org.uk/~sgtatham/putty/faq.html)
- [PuTTY — documentation et manuel](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)
- [PuTTY — licence](https://www.chiark.greenend.org.uk/~sgtatham/putty/licence.html)

L'installation Windows, la vérification du MSI et la connexion vers un serveur pilote n'ont pas été exécutées dans cette fiche. Tester sur une machine et un serveur autorisés avant généralisation.