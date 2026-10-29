# Fiche_Simple_-_VM_Rocky_9_Suricata_Securiser

- **Environnement** : VM Rocky Linux 9 dédiée à Suricata
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / sécurisation

---

## Problème précis à résoudre

Durcir le capteur Suricata : compte, droits, journaux et exposition réseau.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l’identité d’exécution :
   ```bash
   ps -o user,pid,cmd -C suricata
   id suricata 2>/dev/null
   ```
   👉 Explication : Suricata ouvre la capture avec des privilèges puis doit pouvoir être exécuté sous un compte dédié si le paquet le prévoit; confirmer l’utilisateur réellement utilisé et ne pas le modifier sans test.

2. Restreindre les journaux :
   ```bash
   sudo ls -l /var/log/suricata
   sudo chmod -R o-rwx /var/log/suricata
   ```
   👉 Explication : Les logs eve.json contiennent adresses et métadonnées; interdire la lecture aux autres comptes.

3. Contrôler les ports en écoute :
   ```bash
   ss -tulpn | grep -i suricata || echo "aucun port réseau ouvert par suricata"
   ```
   👉 Explication : Un capteur passif n’a pas à écouter; la socket de commande Unix, si présente, reste locale.

4. Restreindre l’accès de gestion :
   ```bash
   sudo ss -tlnp | grep ":22"
   ```
   👉 Explication : Limiter SSH aux administrateurs et au réseau de gestion; la politique de pare-feu relève de la fiche de durcissement de l’OS.

5. Définir rotation et rétention :
   ```bash
   sudo cat /etc/logrotate.d/suricata
   ```
   👉 Explication : Vérifier que la rotation existe et que la durée respecte la politique de conservation.

## 2. Production — Contrôles

Revue trimestrielle des règles activées, des comptes et de l’espace disque.

## 3. Production — Sécurité

- Envoyer les alertes vers un collecteur approuvé via un canal chiffré (non détaillé).
- Pas de secret en clair dans `suricata.yaml` ni dans les sources de règles.
- SELinux : rester en Enforcing; pour tout refus, `sudo ausearch -m avc -ts recent` puis corriger le contexte plutôt que désactiver SELinux.

## Validation et retour arrière

- **Validation** : Aucun port inutile, journaux non lisibles par tous, rotation active.
- **Retour arrière** : Rétablir les permissions précédentes et la configuration sauvegardée.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-valider)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-configurer)