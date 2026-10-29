# 📄 Fiche_Simple_-_VMware_ESXi_8_Securite_SSH_Comptes_Lockdown.md

- **Environnement** : Hôte physique VMware ESXi 8 (DCUI, ESXi Shell, SSH, vSphere Client)
- **OS / Version** : VMware ESXi 8.0 - Accès d'administration
- **Catégorie** : Sécurité / Accès distant, comptes et lockdown
- **Tags** : `[vmware-esxi-8]`, `[ssh]`, `[esxi-shell]`, `[lockdown]`, `[comptes]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Activer SSH et l'ESXi Shell uniquement le temps d'une intervention, créer des comptes d'administration nominatifs avec droits limités, restreindre le service SSH aux postes d'administration et activer le mode lockdown.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister l'état des services d'accès à l'hôte :
```bash
esxcli system service list
```
👉 Explication : affiche chaque service (dont `TSM-SSH` pour SSH et `TSM` pour l'ESXi Shell) avec son état d'exécution et de démarrage automatique.

2. Activer SSH pour une intervention ponctuelle :
```bash
vim-cmd hostsvc/enable_ssh
vim-cmd hostsvc/start_ssh
```
👉 Explication : configure le démarrage de SSH et lance le service ; la connexion se fait ensuite depuis le poste d'administration avec `ssh root@<nom_de_l_hote>`.

3. Vérifier l'accès depuis le poste d'administration :
```bash
ssh root@<nom_de_l_hote> 'vmware -vl'
```
👉 Explication : ouvre une session SSH et exécute `vmware -vl` à distance ; le résultat confirme que l'accès fonctionne avant de désactiver le service.

**Équivalent interface graphique :**

- **Host Client > Manage > Services > TSM-SSH > Start** (ou **Stop**), et **Actions > Policy** pour le démarrage automatique.
  👉 Explication : équivalent de `vim-cmd hostsvc/start_ssh` et du contrôle de `TSM-SSH`.
- Console de l'hôte (DCUI, **F2**) : **Troubleshooting Options > Enable SSH**.
  👉 Explication : utile sans accès réseau; le mode Lockdown se règle côté vCenter (**Host > Configure > Security Profile > Lockdown Mode**).

## ⚡ 2. Production — Façon Simplifiée
1. Arrêter et désactiver SSH et l'ESXi Shell après usage :
```bash
vim-cmd hostsvc/stop_ssh
vim-cmd hostsvc/disable_ssh
vim-cmd hostsvc/stop_esx_shell
vim-cmd hostsvc/disable_esx_shell
```
👉 Explication : arrête les services puis supprime leur démarrage automatique ; l'hôte ne reste plus joignable en SSH sauf intervention explicitement planifiée.

2. Définir un délai d'inactivité pour les shells :
```bash
esxcli system settings advanced set --option=/UserVars/ESXiShellTimeOut --int-value=900
esxcli system settings advanced set --option=/UserVars/ESXiShellInteractiveTimeOut --int-value=900
```
👉 Explication : ferme automatiquement les sessions inactives après 900 secondes (15 minutes), pour limiter le risque de session oubliée ouverte.

3. Activer le mode lockdown depuis vSphere :
```bash
esxcli system account list
```
👉 Explication : dans vSphere Client, ouvrir Hôte > Configure > Security Profile > Lockdown Mode et choisir « Normal » ou « Strict » selon le design. La commande liste les comptes locaux qui resteront accessibles ; le compte d'administration nominatif doit y figurer avant d'activer le mode.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Créer un compte d'administration nominatif :
```bash
esxcli system account add --id=<utilisateur_admin> --password=<mot_de_passe_fort> --password-confirmation=<mot_de_passe_fort> --description="Administrateur nominatif"
```
👉 Explication : crée un compte individuel pour chaque administrateur au lieu d'un partage du compte root ; éviter de laisser le mot de passe dans l'historique du shell (`history -c` après la commande, ou saisie via vSphere Client).

2. Attribuer un rôle limité au compte :
```bash
esxcli system permission set --id=<utilisateur_admin> --role=Admin
esxcli system permission list
```
👉 Explication : accorde le rôle `Admin` au compte nominatif et affiche toutes les permissions de l'hôte pour vérifier qu'aucun compte inconnu n'est présent.

3. Limiter le service SSH aux postes d'administration :
```bash
esxcli network firewall ruleset set --ruleset-id=sshServer --allowed-all=false
esxcli network firewall ruleset allowedip add --ruleset-id=sshServer --ip-address=<ip_poste_admin>
```
👉 Explication : le pare-feu ESXi n'accepte plus les connexions SSH que depuis `<ip_poste_admin>` ; répéter `allowedip add` pour chaque poste autorisé.

4. Contrôler les clés SSH autorisées pour root :
```bash
cat /etc/ssh/keys-root/authorized_keys
```
👉 Explication : liste les clés publiques autorisées à se connecter en root ; chaque clé doit être identifiée, et toute clé inconnue doit être supprimée du fichier.

5. Vérifier la configuration du pare-feu SSH :
```bash
esxcli network firewall ruleset list --ruleset-id=sshServer
esxcli network firewall ruleset allowedip list --ruleset-id=sshServer
```
👉 Explication : confirme que la règle `sshServer` n'autorise que les adresses définies à l'étape précédente.
