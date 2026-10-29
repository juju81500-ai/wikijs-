# Fiche_Simple_-_VM_Windows_11_MobaXterm_Sessions_SSH

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; MobaXterm Home/Professional, version VERSION_MOBAXTERM (à remplacer)
- **Catégorie** : client SSH/RDP multi-sessions

---

## Problème précis à résoudre

Créer une session SSH MobaXterm propre vers un serveur de test.

## 1. Hors-Production (Lab / Test / POC)

1. Cliquer **Session > SSH**.
   👉 Explication : ouvre l'assistant de session.

2. Renseigner **Remote host** = HOTE_CIBLE, cocher **Specify username** = UTILISATEUR_SSH, **Port** = 22 (valeurs à remplacer).
   👉 Explication : évite l'utilisation d'un compte partagé.

3. Onglet **Advanced SSH settings** : décocher **X11-Forwarding** si inutile ; **Use private key** : pointer vers `%USERPROFILE%\.ssh\CLE_PRIVEE` (nom à remplacer).
   👉 Explication : réduit la surface d'exposition ; l'authentification par clé évite le mot de passe enregistré.

4. Onglet **Bookmark settings** : nommer la session `NOM_SESSION` et choisir un dossier.
   👉 Explication : classement exploitable.

5. Valider avec **OK** ; accepter la clé d'hôte après comparaison avec l'empreinte fournie par l'administrateur : `ssh-keygen -lf` côté serveur.
   👉 Explication : évite une attaque de type interception.

## 2. Production — Contrôles

Standardiser le nommage des sessions et interdire le stockage du mot de passe dans la session.

## 3. Production — Sécurité

- Ne jamais cocher la mémorisation du mot de passe en clair ; préférer clé privée protégée par passphrase.
- Désactiver l'agent forwarding sauf besoin approuvé.

## Validation et retour arrière

- **Validation** : La session s'ouvre et la commande `whoami` renvoie UTILISATEUR_SSH.
- **Retour arrière** : Clic droit sur la session > **Delete session**.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [MobaXterm — documentation officielle](https://mobaxterm.mobatek.net/documentation.html)
- [MobaXterm — téléchargement](https://mobaxterm.mobatek.net/download.html)
- [MobaXterm — FAQ](https://mobaxterm.mobatek.net/faq.html)