# Déployer FreePBX et Asterisk pour une téléphonie de laboratoire

- **Environnement** : VM ou serveur dédié, réseau voix segmenté
- **Version** : Asterisk 20 / FreePBX selon leur matrice de compatibilité et le statut de support actuel
- **Tags** : `freepbx`, `asterisk`, `voip`, `debian12`, `sip`, `telephonie`

> Une installation FreePBX n'est pas un simple paquet Debian. Utiliser uniquement une combinaison OS/FreePBX/Asterisk officiellement supportée. Si Debian 12 n'est pas supporté par la version choisie, employer l'appliance ou la méthode d'installation officiellement recommandée plutôt que forcer un script tiers.

## 1. Préparer la téléphonie

Fiche simple : [préparer la téléphonie](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/FreePBX-Asterisk/Fiche_Simple_-_VM_Debian_12_FreePBX_Preparer_Telephonie.md).

Réserver une adresse IP et un DNS, définir les extensions, numéros, trunks, plages RTP, codecs et plan d'appel. Coordonner les paramètres SIP/RTP avec l'opérateur. Isoler les téléphones et le PBX dans un VLAN voix ; ne jamais publier l'interface d'administration ni SIP directement à Internet sans architecture opérateur sécurisée.

Sauvegarder la configuration et établir un accès console local avant toute règle réseau.

## 2. Installer selon la méthode prise en charge

Fiche simple : [installer selon la méthode supportée](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/FreePBX-Asterisk/Fiche_Simple_-_VM_Debian_12_FreePBX_Installer_Methode_Supportee.md).

Télécharger l'image ou la procédure d'installation officielle adaptée à la version FreePBX retenue. Vérifier l'intégrité de l'image, réaliser l'installation sur une VM de test, fixer le nom d'hôte et l'adresse réseau puis appliquer les mises à jour compatibles.

Ne pas exécuter un script d'installation trouvé dans un forum avec `curl | bash` et ne pas mélanger paquets Asterisk provenant de dépôts incompatibles avec FreePBX.

## 3. Configuration de base

Fiche simple : [configurer les comptes et routes](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/FreePBX-Asterisk/Fiche_Simple_-_VM_Debian_12_FreePBX_Configurer_Base.md).

Depuis l'interface locale protégée :

1. Créer un compte administrateur nominatif et désactiver les identifiants initiaux.
2. Créer un trunk avec les paramètres fournis par l'opérateur et secrets uniques.
3. Créer deux extensions de test et un plan d'appel restreint.
4. Configurer les routes entrantes/sortantes avec restrictions de destination et limite de coût.
5. Activer TLS/SRTP si tous les terminaux et l'opérateur les prennent en charge.

## 4. Réseau et tests

Fiche simple : [sécuriser le réseau et tester](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/FreePBX-Asterisk/Fiche_Simple_-_VM_Debian_12_FreePBX_Configurer_Reseau_Tester.md).

Autoriser SIP/TLS et RTP uniquement depuis les réseaux de téléphones et les adresses opérateur documentées. Désactiver les services de découverte non utilisés. Tester appels internes, entrants, sortants, audio bidirectionnel, DTMF, messagerie et appels d'urgence selon les obligations locales.

Vérifier les journaux et l'horloge, puis simuler une perte du trunk. Ne pas utiliser de vrais appels d'urgence pour les essais ; convenir d'un numéro de test avec l'opérateur.

## 5. Sauvegarde et maintien

Fiche simple : [sauvegarder et maintenir](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/FreePBX-Asterisk/Fiche_Simple_-_VM_Debian_12_FreePBX_Sauvegarder_Maintenir.md).

Planifier une sauvegarde FreePBX et une copie hors serveur, puis restaurer sur un environnement isolé avant production. Les enregistrements vocaux, CDR et secrets peuvent contenir des données sensibles : définir accès et rétention. Mettre à jour uniquement par le mécanisme supporté et avec snapshot/sauvegarde vérifiée.
