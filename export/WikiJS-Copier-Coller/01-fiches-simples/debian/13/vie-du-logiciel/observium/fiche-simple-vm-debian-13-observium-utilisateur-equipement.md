# Fiche_Simple_-_VM_Debian_13_Observium_Utilisateur_Equipement.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / SNMPv3

---

## Problème précis à résoudre

Créer l'administrateur nominatif et ajouter un équipement pilote en SNMPv3 authPriv.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le compte administrateur (niveau 10) en saisissant un mot de passe temporaire masqué :
   ```bash
   cd /opt/observium
   read -rsp 'Mot de passe temporaire : ' OBS_PW; echo
   sudo ./adduser.php observium-admin "$OBS_PW" 10
   unset OBS_PW
   ```
   👉 Explication : l'outil prend le mot de passe en argument : le visible dans `ps` n'est possible que brièvement; faire l'opération depuis une session d'administration contrôlée et changer le mot de passe à la première connexion. `observium-admin` est un nom d'exemple.

2. Vérifier depuis le serveur que l'équipement résout et que SNMPv3 répond (valeurs d'exemple à remplacer) :
   ```bash
   getent hosts sw1.example.invalid
   read -rsp 'Phrase d auth SNMPv3 : ' SNMPAUTH; echo
   read -rsp 'Phrase de chiffrement SNMPv3 : ' SNMPPRIV; echo
   snmpget -v3 -l authPriv -u supervision -a SHA -A "$SNMPAUTH" -x AES -X "$SNMPPRIV" sw1.example.invalid 1.3.6.1.2.1.1.5.0
   unset SNMPAUTH SNMPPRIV
   ```
   👉 Explication : `snmpget` lit le nom système; les phrases de passe sont demandées en saisie masquée. Préférer SHA-2/AES si l'équipement les gère.

3. Dans l'interface HTTPS : **Devices > Add Device**, saisir le nom, la version SNMP v3 et les identifiants SNMPv3.
   👉 Explication : l'ajout par l'interface évite d'exposer les secrets en arguments de commande.

4. Contrôler le nom canonique, le modèle, le sysObjectID, les interfaces et la date de dernière interrogation dans la fiche de l'équipement.
   👉 Explication : l'appareil est correctement identifié; ne pas activer de découverte automatique de voisins hors des sous-réseaux autorisés.

## 2. Production — Contrôles

Compte administrateur nominatif unique, utilisateur SNMPv3 en lecture seule limité à l'IP de supervision.

## 3. Production — Sécurité

- Jamais de communauté `public` ni SNMPv1/v2c pour le pilote.
- Ne pas noter les phrases SNMPv3 dans un ticket.

## Validation et retour arrière

- **Validation** : l'équipement pilote apparaît avec ses interfaces et une date de dernière interrogation.
- **Retour arrière** : supprimer l'équipement dans l'interface (**Device > Delete device**) et le compte via l'administration des utilisateurs.

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 6](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13#6-creer-lutilisateur-et-ajouter-un-equipement-pilote)