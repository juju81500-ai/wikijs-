# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Limiter l'accès SSH et web.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Système > Paramètres > Administration > Shell sécurisé : activer SSH, décocher « Autoriser la connexion root » et « Autoriser l'authentification par mot de passe », choisir le port et les interfaces (LAN uniquement).
   👉 Explication : seules les clés sont acceptées et seulement depuis le réseau interne.

2. Dans la même page, forcer HTTPS, changer le port du GUI, restreindre l'écoute au LAN et activer la protection contre les attaques par force brute.
   👉 Explication : réduit l'exposition de l'interface web.

3. Contrôler :
   ```sh
   sockstat -4 -l | grep -E 'sshd|lighttpd|nginx'
   grep -E '^(PermitRootLogin|PasswordAuthentication)' /usr/local/etc/ssh/sshd_config.d/* /etc/ssh/sshd_config 2>/dev/null
   ```
   👉 Explication : montre les ports en écoute et la configuration SSH appliquée.

## 2. Production — Contrôles

Conserver un accès console en cas d'erreur.

## 3. Production — Sécurité

Ne jamais ouvrir SSH ou le GUI sur le WAN.

## Validation et retour arrière

- **Validation** : Seule la connexion par clé depuis le LAN fonctionne.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
