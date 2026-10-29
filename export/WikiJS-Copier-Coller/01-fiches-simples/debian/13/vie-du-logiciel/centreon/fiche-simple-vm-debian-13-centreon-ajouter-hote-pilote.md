# 📄 Fiche_Simple_-_VM_Debian_13_Centreon_Ajouter_Hote_Pilote.md

- **Environnement** : Console Centreon 26.10 avec droits opérateur
- **OS / Version** : Debian 13 Trixie pour le poller; équipements de test autorisés
- **Catégorie** : Supervision / configuration

---

## 🎯 Problème précis à résoudre

Ajouter un hôte autorisé dans Centreon et vérifier une collecte minimale avant généralisation.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Créer l'hôte de test : **Configuration > Hosts > Hosts > Add** (nom, alias, adresse IP, **Monitoring server** = poller de test, modèle approuvé).
   👉 Explication : un seul hôte pilote autorisé au départ.

2. Définir la credential SNMPv3 : dans les macros de l'hôte, `SNMPEXTRAOPTIONS` ou les options du modèle (`--snmp-version=3 --snmp-username=UTILISATEUR_RO --authpassphrase=... --privpassphrase=...`) ou via une credential protégée.
   👉 Explication : authPriv, lecture seule; stocker les secrets dans le coffre; marquer la macro comme **Password**.

3. Attacher les templates nécessaires : onglet **Templates** de l'hôte (ex. ICMP et interfaces SNMP), puis **Save** et **Deploy services**.
   👉 Explication : contrôler les services générés.

4. Exporter et appliquer la configuration : **Configuration > Pollers > Export configuration**, cocher **Generate Configuration Files**, **Run monitoring engine debug (-v)**, **Move Export Files**, **Restart Monitoring Engine** (méthode **Reload**), puis **Export**. Contrôle côté serveur :
   ```bash
   sudo systemctl status centengine --no-pager
   ```
   👉 Explication : vérifier ensuite **Monitoring > Resources Status** (premières collectes).

## ⚡ 2. Production — Façon Simplifiée

1. Ajouter un seul sous-ensemble d'hôtes approuvés à la fois : **Configuration > Hosts > Hosts > Add** ou **Duplicate** depuis l'hôte pilote.
   👉 Explication : renseigner propriétaire, criticité, groupe d'hôtes, poller et intervalle.

2. Configurer contacts et seuils avant activation : **Configuration > Users > Contacts / Users** et **Configuration > Services > Templates** (seuils Warning/Critical).
   👉 Explication : alertes et fenêtres de maintenance validées avant notification.

## 🔒 3. Production — Façon Sécurisée

- Utiliser SNMPv3 authPriv lecture seule; limiter UDP/161 depuis le poller autorisé et ne pas activer l'écriture SNMP.
- Éviter les comptes `admin` de l'équipement pour la collecte; conserver les secrets dans le coffre et dans la credential Centreon protégée.
- Ne pas lancer la découverte réseau sur un bloc CIDR sans validation écrite du propriétaire réseau et fenêtre approuvée.
- Valider alertes et fenêtres de maintenance avant notification des équipes.

## ✅ Validation et retour arrière

- **Précontrôles** : IP, propriétaire, poller, credential, modèle et ports approuvés.
- **Validation** : export de configuration réussi, hôte et services attendus `OK`, seuil d'alerte testé.
- **Retour arrière** : désactiver l'hôte ou retirer les services ajoutés, puis réexporter la configuration du poller.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : consulter la documentation officielle Centreon ci-dessous.
- [Centreon — Démarrer la supervision](https://docs.centreon.com/docs/getting-started/welcome/)