# Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Valider

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Snort
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / validation

---

## Problème précis à résoudre

Recetter Snort sur un fichier pcap autorisé, puis en capture bornée.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un pcap de test inoffensif :
   ```bash
   sudo tcpdump -i INTERFACE_AUTORISEE -c 5 -w /var/tmp/snort-test.pcap icmp &
   ping -c 3 HOTE_AUTORISE
   wait
   ```
   👉 Explication : Génère 5 paquets ICMP vers un hôte autorisé; `tcpdump` est requis (voir la série tcpdump).

2. Analyser hors ligne :
   ```bash
   sudo /opt/snort3/bin/snort -c /opt/snort3/etc/snort/snort.lua -r /var/tmp/snort-test.pcap -A alert_fast -l /tmp/snort-test
   ```
   👉 Explication : Lit le fichier sans toucher au réseau; le répertoire `/tmp/snort-test` doit exister (`mkdir -p /tmp/snort-test`).

3. Lire les alertes :
   ```bash
   cat /tmp/snort-test/alert_fast.txt | head -n 10
   ```
   👉 Explication : Doit montrer l’alerte de la règle de test 1000001; sinon vérifier le chargement des règles.

4. Démarrer l’unité (si créée) :
   ```bash
   sudo systemctl start snort3-ids.service
   systemctl status snort3-ids.service --no-pager
   ```
   👉 Explication : Contrôle le service passif; l’arrêter hors période de recette si non planifié.

## 2. Production — Contrôles

Archiver version, commande, extrait d’alerte et date.

## 3. Production — Sécurité

- Tests sur trafic autorisé uniquement.

## Validation et retour arrière

- **Validation** : Au moins une alerte TEST Snort ICMP lab est produite et le service reste stable.
- **Retour arrière** : `sudo systemctl stop snort3-ids.service`, supprimer `/tmp/snort-test` et `/var/tmp/snort-test.pcap`, retirer la règle de test.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-snort)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-sauvegarder-restaurer)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-securiser)