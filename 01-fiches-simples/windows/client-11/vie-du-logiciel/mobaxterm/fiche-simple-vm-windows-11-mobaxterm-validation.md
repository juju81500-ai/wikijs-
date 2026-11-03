# Fiche_Simple_-_VM_Windows_11_MobaXterm_Validation

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; MobaXterm Home/Professional, version VERSION_MOBAXTERM (à remplacer)
- **Catégorie** : client SSH/RDP multi-sessions
- **Tags** : `mobaxterm`, `windows11`, `validation`

---

## Problème précis à résoudre

Prouver que MobaXterm fonctionne et respecte la configuration attendue.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir la session NOM_SESSION (à remplacer).
   👉 Explication : test de bout en bout.

2. Exécuter dans le terminal MobaXterm : `hostname; whoami; ssh -V`.
   👉 Explication : vérifie la machine, le compte et le client SSH intégré.

3. Côté Windows : `Get-Process MobaXterm | Select-Object Name,Id,Path`.
   👉 Explication : confirme le binaire réellement exécuté.

4. Vérifier le journal d'authentification du serveur : `journalctl -u ssh --since "10 minutes ago"` (sur le serveur Linux).
   👉 Explication : preuve côté serveur.

5. Fermer la session puis la rouvrir.
   👉 Explication : vérifie la persistance de la configuration.

## 2. Production — Contrôles

Conserver la preuve (capture sans secret) dans le ticket de changement.

## 3. Production — Sécurité

- Masquer noms d'utilisateurs et adresses internes dans les captures.

## Validation et retour arrière

- **Validation** : Connexion réussie, version correcte, journal serveur cohérent.
- **Retour arrière** : Revenir à la configuration sauvegardée (voir fiche Sauvegarde_Restauration).

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [MobaXterm — documentation officielle](https://mobaxterm.mobatek.net/documentation.html)
- [MobaXterm — téléchargement](https://mobaxterm.mobatek.net/download.html)
- [MobaXterm — FAQ](https://mobaxterm.mobatek.net/faq.html)
