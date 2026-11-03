# Réparation : un poste Windows ne peut pas joindre le domaine Active Directory

- **Périmètre** : Windows 10/11 et Windows Server membre d'un domaine AD DS
- **Tags** : `reparation`, `windows`, `active-directory`, `dns`, `domaine`

## 1. Vérifier le réseau et le DNS

Ouvrir PowerShell en administrateur :

```powershell
ipconfig /all
Resolve-DnsName -Type SRV _ldap._tcp.dc._msdcs.ad.example.net
nltest /dsgetdc:ad.example.net
Test-NetConnection dc01.ad.example.net -Port 389
```

Remplacer le domaine et le contrôleur par les valeurs réelles. Le poste doit utiliser les DNS des contrôleurs de domaine, pas un DNS public configuré directement sur sa carte réseau.

## 2. Distinguer les causes

- **SRV introuvable** : vérifier les DNS configurés, la zone AD et l'enregistrement du contrôleur.
- **Contrôleur trouvé mais port inaccessible** : vérifier route, pare-feu et services AD DS sur le contrôleur.
- **Erreur d'identifiants ou de compte** : vérifier l'heure, l'état du compte et les droits de délégation ; ne pas réinitialiser le compte machine sans diagnostic.

```powershell
w32tm /query /status
Test-ComputerSecureChannel -Verbose
```

## 3. Réparer le canal sécurisé si le poste est déjà membre

Conserver un compte administrateur local fonctionnel et saisir un compte autorisé lorsqu'il est demandé :

```powershell
$cred = Get-Credential
Test-ComputerSecureChannel -Repair -Credential $cred -Verbose
```

Redémarrer uniquement si PowerShell le demande, puis valider l'ouverture de session et les stratégies. Ne pas quitter puis rejoindre le domaine de manière répétée : cela peut créer des comptes machine en conflit.

## 4. Retour arrière

Si la réparation échoue, conserver l'accès local, exporter les résultats des commandes et demander une vérification côté contrôleur de domaine (DNS, réplication, compte ordinateur et journaux). Ne pas désactiver le pare-feu Windows ni remplacer les DNS du poste par un résolveur public.