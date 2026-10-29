# Fiche_Simple_-_VM_Windows_11_PuTTY_Valider_SSH_HostKey.md

- **Environnement** : PuTTY 0.85 Stable x64 sur Windows 11, serveur SSH de test autorisé
- **OS / Version** : Windows 11 x64
- **Catégorie** : administration distante / SSH

---

## Problème précis à résoudre

Valider une session PuTTY vers un serveur SSH autorisé en vérifiant le logiciel, l'empreinte hôte et l'authentification sans exposer de clé privée.

## 1. Hors-Production (Lab / Test / POC)

1. **Interface graphique** : télécharger le MSI 0.85 depuis le site officiel; vérifier la signature Authenticode et la signature GPG avec la clé Release 2026 et son empreinte officielle.
2. Installer sous Windows 11 et confirmer la version avec **Help > About PuTTY**.
3. Obtenir le nom d'hôte, le compte, le port et l'empreinte SSH du serveur par un canal indépendant.
4. Ouvrir la session et comparer exactement l'empreinte de la première connexion. Annuler si elle diffère ou si une clé connue change sans explication confirmée.
5. Si une clé utilisateur est requise, en générer une protégée par phrase secrète, ne remettre que la clé publique à l'administrateur et vérifier la connexion depuis une nouvelle session.

**Équivalent ligne de commande (PowerShell) :**

```powershell
Get-AuthenticodeSignature .\putty-0.85-installer.msi | Select-Object Status, SignerCertificate
Get-FileHash .\putty-0.85-installer.msi -Algorithm SHA256
ssh-keyscan -t ed25519 SERVEUR | ssh-keygen -lf -
ssh-keygen -t ed25519 -f $HOME\.ssh\id_ed25519_lab
```
👉 Explication : vérifie la signature et le hash du MSI, affiche l'empreinte SSH du serveur à comparer à celle reçue par canal indépendant, puis génère une clé protégée par phrase secrète (saisie à l'invite, jamais en argument). Remplacer `SERVEUR` et le nom de fichier.

## 2. Production — Contrôles

N'utiliser que des hôtes, comptes et méthodes d'authentification approuvés. Garder l'agent forwarding désactivé par défaut; protéger toute journalisation et les sessions enregistrées.

## 3. Production — Sécurité

- Ne jamais désactiver ou ignorer le contrôle de clé d'hôte; vérifier tout changement via l'administrateur hors bande.
- Ne jamais transmettre ou enregistrer la clé privée `.ppk` sur le serveur, dans un ticket ou dans un dossier partagé.
- Ne pas lancer PuTTY en administrateur; garder Pageant limité aux clés nécessaires et fermer l'agent après usage.
- Éviter Telnet/Rlogin et les options de transfert non approuvées.

## Validation et retour arrière

- **Validation** : MSI signé, version attendue, host key conforme, nouvelle session SSH réussie avec le compte autorisé.
- **Retour arrière** : fermer la session, retirer la clé de Pageant et désactiver/supprimer le profil enregistré si le poste est partagé; signaler une empreinte qui change au lieu de la remplacer à l'aveugle.

## Si le problème n'est pas résolu

- [PuTTY — FAQ officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/faq.html)
- [PuTTY — clés et signatures](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet PuTTY 0.85 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/84-deploiement-putty-0-85-windows-11)