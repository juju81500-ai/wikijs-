# Réparation : accès SSH impossible après un changement de configuration

- **Périmètre** : Serveur Linux OpenSSH
- **Tags** : `reparation`, `linux`, `ssh`, `acces-distant`, `pare-feu`

## Règle de sécurité

Garder une session SSH existante ouverte et disposer d'un accès console avant toute correction. Ne pas désactiver le pare-feu ni réactiver globalement les mots de passe comme premier réflexe.

## 1. Identifier où la connexion échoue

Depuis le client :

```bash
ssh -vvv -o ConnectTimeout=5 admin@serveur.example.net
```

Sur le serveur via la console ou une session encore ouverte :

```bash
sudo systemctl --no-pager status ssh
sudo ss -lntp | grep sshd
sudo journalctl -u ssh --since '-15 minutes' --no-pager
```

Un délai dépassé suggère un problème de route ou de filtrage ; un refus immédiat suggère un port sans écoute ; `Permission denied` indique plutôt un problème d'identité ou de méthode d'authentification.

## 2. Vérifier la configuration effective

```bash
sudo sshd -t
sudo sshd -T -C user=admin,host=serveur.example.net,addr=192.0.2.20 | grep -E '^(port|pubkeyauthentication|passwordauthentication|permitrootlogin|allowgroups) '
```

Remplacer les exemples par le vrai utilisateur, nom et adresse client. Corriger la directive fautive dans son fichier d'origine après sauvegarde. Vérifier les fichiers inclus dans `/etc/ssh/sshd_config.d/` : l'ordre d'inclusion peut rendre une valeur antérieure prioritaire.

## 3. Restaurer le service sans perdre l'accès

Après validation syntaxique, vérifier le port et la règle de pare-feu correspondants, puis recharger le service :

```bash
sudo systemctl reload ssh
sudo systemctl --no-pager status ssh
```

Ouvrir une nouvelle connexion dans un second terminal avant de fermer la session de secours. Si le rechargement échoue, restaurer la copie de configuration sauvegardée depuis la console, relancer `sshd -t`, puis corriger le filtrage sur le seul port attendu.