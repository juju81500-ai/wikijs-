# Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Prerequis_Limites

- **Environnement** : VM Debian 13 cliente d'un domaine FreeIPA existant
- **OS / Version** : Debian 13 Trixie; paquet freeipa-client des dépôts, version à vérifier
- **Catégorie** : FreeIPA client / prérequis et limites
- **Tags** : `freeipa`, `debian13`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Valider les prérequis avant d'inscrire un client Debian dans un domaine FreeIPA existant (serveur Rocky 9 du pack).

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'identité réseau du client :
   ```bash
   hostnamectl
   ip -br address
   cat /etc/os-release
   ```
   👉 Explication : Le client doit avoir un FQDN stable dans le domaine DNS de FreeIPA (CLIENT_FQDN à consigner).

2. Vérifier la résolution du serveur FreeIPA et des enregistrements de service :
   ```bash
   getent hosts IPA_SERVER_FQDN
   dig +short -t SRV _ldap._tcp.IPA_DOMAIN
   ```
   👉 Explication : IPA_SERVER_FQDN et IPA_DOMAIN sont à remplacer par le serveur et le domaine du déploiement; si dig est absent, installer le paquet dnsutils. Si le SRV est vide, pointer le DNS du client vers le DNS FreeIPA ou prévoir --server à l'installation.

3. Contrôler l'heure :
   ```bash
   timedatectl
   ```
   👉 Explication : L'écart d'heure avec le serveur doit rester faible (Kerberos).

## 2. Production — Contrôles

Prérequis côté serveur : voir [la fiche serveur Rocky 9 Prérequis](../../../../Rocky-Linux/9/Vie-du-logiciel/FreeIPA/Fiche_Simple_-_VM_Rocky_9_FreeIPA_Prerequis.md). Limites : intégration cliente via le paquet de la distribution; la compatibilité exacte des versions client/serveur est à vérifier dans la documentation FreeIPA. Pas de HA ni de réplication traitées ici.

## 3. Production — Sécurité

- Disposer d'un compte autorisé à inscrire des hôtes (ou d'un mot de passe à usage unique) fourni par l'administrateur; jamais en clair dans un ticket.

## Validation et retour arrière

- **Validation** : FQDN, DNS, SRV et heure vérifiés.
- **Retour arrière** : Aucun changement : rien à restaurer.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Installer.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_FreeIPA.md)
- [FreeIPA — page Client](https://www.freeipa.org/page/Client)
- [FreeIPA — page Documentation](https://www.freeipa.org/page/Documentation)
