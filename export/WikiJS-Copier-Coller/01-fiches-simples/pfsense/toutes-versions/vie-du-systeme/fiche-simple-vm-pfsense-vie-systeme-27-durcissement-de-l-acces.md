# Fiche_Simple_-_VM_pfSense_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Limiter l'accès SSH et web.

## 1. Hors-Production (Lab / Test / POC)

1. Dans System > Advanced > Admin Access > Secure Shell : activer SSH, SSHd Key Only = `Public Key Only`, choisir le port (ex. 2222).
   👉 Explication : seules les clés sont acceptées.

2. Dans la même page (webConfigurator) : protocole HTTPS, changer le port TCP, cocher « Anti-lockout » seulement sur LAN, et limiter l'accès via les règles Firewall > Rules > LAN.
   👉 Explication : réduit l'exposition de l'interface web.

3. Contrôler :
   ```sh
   sockstat -4 -l | grep -E 'sshd|nginx'
   grep -E '^(PermitRootLogin|PasswordAuthentication)' /etc/ssh/sshd_config
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

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)