# Fiche_Simple_-_VM_Windows_11_PuTTY_Authentification.md

- **Environnement** : Poste Windows 11 x64 d'administration
- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Catégorie** : client SSH / clés
- **Tags** : `putty`, `windows11`, `ssh`, `puttygen`, `host-key`

---

## Problème précis à résoudre

Préparer une clé SSH protégée par phrase secrète.

## 1. Hors-Production (Lab / Test / POC)

1. Utiliser d'abord la méthode d'authentification et le compte fournis par l'administrateur du serveur.
   👉 Explication : on respecte la politique du serveur.

2. Lancer **PuTTYgen > Generate**, enregistrer la clé privée au format `.ppk` avec une phrase secrète robuste.
   👉 Explication : la phrase secrète protège la clé si le fichier est volé.

3. Copier la clé publique affichée et la remettre à l'administrateur par un canal approuvé.
   👉 Explication : il l'ajoute à `authorized_keys`.

4. Dans PuTTY : **Connection > SSH > Auth > Credentials**, sélectionner le fichier `.ppk`.
   👉 Explication : associe la clé à la session.

5. Laisser l'agent forwarding désactivé; si Pageant est nécessaire, charger seulement les clés requises et les retirer ensuite.
   👉 Explication : un serveur distant pourrait utiliser l'agent local.

## 2. Production — Contrôles

Définir qui génère, stocke et révoque les clés.

## 3. Production — Sécurité

- Ne jamais transmettre le fichier privé `.ppk`.
- Agent forwarding désactivé sauf besoin approuvé.

## Validation et retour arrière

- **Validation** : La clé s'authentifie sur le serveur pilote.
- **Retour arrière** : Faire retirer la clé publique du serveur et supprimer le `.ppk`.

## Si le problème n'est pas résolu

- [PuTTY — page officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [PuTTY — clés de signature](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet — 4. Préparer l'authentification](../../../../../02-Fiches-Completes/Windows/Client-11/Installation-Deploiement/84_Deploiement_PuTTY_0.85_Windows_11.md#4-preparer-lauthentification)
