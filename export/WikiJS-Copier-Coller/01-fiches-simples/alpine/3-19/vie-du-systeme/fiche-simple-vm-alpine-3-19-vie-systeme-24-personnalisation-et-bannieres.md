# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Afficher l'avertissement légal et les informations de la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Modifier le message du jour :
   ```sh
   doas sh -c 'cat > /etc/motd <<EOF
   Accès réservé aux personnes autorisées. Toute activité est journalisée.
   Machine : NOM_MACHINE - Rôle : ROLE_SERVICE
   EOF'
   ```
   👉 Explication : affiché après connexion; remplacer `NOM_MACHINE` et `ROLE_SERVICE`.

2. Ajouter une bannière avant l'authentification SSH :
   ```sh
   doas sh -c 'cat > /etc/issue.net <<EOF
   Accès réservé aux personnes autorisées.
   EOF'
   doas sed -i 's|^#\?Banner.*|Banner /etc/issue.net|' /etc/ssh/sshd_config
   doas rc-service sshd restart
   ```
   👉 Explication : la bannière est montrée avant la saisie du mot de passe.

3. Vérifier depuis un autre poste :
   ```sh
   ssh ADMIN@ADRESSE_IP
   ```
   👉 Explication : la bannière apparaît avant l'authentification.

## 2. Production — Contrôles

Utiliser le texte validé par le service juridique.

## 3. Production — Sécurité

Ne pas révéler la version ni la topologie dans la bannière.

## Validation et retour arrière

- **Validation** : Bannière visible à la connexion.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](</01-fiches-simples/alpine/3-19/vie-du-logiciel/openssh/fiche-simple-lxc-alpine-3-19-securite-openssh-cle-et-openrc>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)