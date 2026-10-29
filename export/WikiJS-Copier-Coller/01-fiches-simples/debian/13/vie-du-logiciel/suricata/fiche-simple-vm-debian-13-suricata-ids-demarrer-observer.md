# Fiche_Simple_-_VM_Debian_13_Suricata_IDS_Demarrer_Observer.md

- **Environnement** : VM Debian 13 avec Suricata configuré
- **OS / Version** : Debian 13 Trixie; Suricata 8.0.7 et suricata-update (Debian Backports)
- **Catégorie** : detection reseau / service

---

## Problème précis à résoudre

Démarrer le service et vérifier que les événements sont produits.

## 1. Hors-Production (Lab / Test / POC)

1. Activer et démarrer :
   ```bash
   sudo systemctl enable --now suricata.service
   sudo systemctl --no-pager --full status suricata.service
   sudo journalctl -u suricata.service -b --no-pager
   ```
   👉 Explication : le service doit être `active (running)` sans erreur au journal.

2. Après du trafic légitime de laboratoire, lire les journaux :
   ```bash
   sudo tail -n 50 /var/log/suricata/suricata.log
   sudo jq -c 'select(.event_type == "stats")' /var/log/suricata/eve.json | tail -n 5
   ```
   👉 Explication : les compteurs doivent évoluer et `eve.json` rester lisible.

3. Préparer un dossier protégé pour un test pcap autorisé :
   ```bash
   sudo install -d -o suricata -g suricata -m 0750 /var/tmp/suricata-lab
   sudo -u suricata suricata -T -c /etc/suricata/suricata.yaml
   ```
   👉 Explication : dossier accessible au seul compte `suricata`; le test de configuration confirme les règles mais pas la carte miroir.

4. Rejouer un pcap approuvé (remplacer `capture-lab.pcap` par votre fichier de test autorisé) :
   ```bash
   sudo suricata -r capture-lab.pcap -c /etc/suricata/suricata.yaml -l /var/tmp/suricata-lab
   ```
   👉 Explication : on valide la chaîne de règles hors réseau; lire seulement alertes et stats produites.

## 2. Production — Contrôles

Définir supervision, rotation des journaux, rétention et transfert chiffré de `eve.json`.

## 3. Production — Sécurité

- Protéger pcap et sorties comme données sensibles.
- Transférer EVE JSON uniquement par canal chiffré avec compte minimal.

## Validation et retour arrière

- **Validation** : Service actif, compteurs qui évoluent, événements lisibles.
- **Retour arrière** : `sudo systemctl disable --now suricata.service`; supprimer `/var/tmp/suricata-lab` si inutile.

## Si le problème n'est pas résolu

- [Suricata — démarrage rapide](https://docs.suricata.io/en/latest/quickstart.html)
- [Suricata — options CLI](https://docs.suricata.io/en/latest/command-line-options.html)
- [Guide complet Suricata Debian 13](/02-fiches-completes/debian/13/installation-deploiement/71-deploiement-suricata-8-debian-13-backports#6-demarrer-le-service-et-controler-lobservation)