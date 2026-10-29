# Fiche_Simple_-_VM_Rocky_9_Zeek_Configurer

- **Environnement** : VM Rocky Linux 9 dédiée à Zeek
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / capteur passif standalone

---

## Problème précis à résoudre

Configurer et exploiter Zeek en capteur passif standalone sur l’interface autorisée.

## 1. Hors-Production (Lab / Test / POC)

1. Créer les répertoires de travail :
   ```bash
   sudo install -d -m 0750 /var/lib/zeek-lab/logs /var/lib/zeek-lab/pcap
   ```
   👉 Explication : Les logs et pcap restent hors du conteneur, avec droits restreints.

2. Analyser d’abord un pcap autorisé (mode recommandé pour la recette) :
   ```bash
   sudo podman run --rm -v /var/lib/zeek-lab/pcap:/pcap:ro,Z -v /var/lib/zeek-lab/logs:/logs:Z -w /logs docker.io/zeek/zeek:lts zeek -C -r /pcap/TICKET.pcap
   ```
   👉 Explication : `-r` lit le fichier, `-C` ignore les erreurs de checksum fréquentes en capture; les logs sont écrits dans `/var/lib/zeek-lab/logs`. `:Z` ajuste le contexte SELinux. TICKET est à remplacer.

3. Capture live passive bornée (lab, interface autorisée) :
   ```bash
   sudo timeout DUREE_SECONDES podman run --rm --network host --cap-add NET_RAW --cap-add NET_ADMIN -v /var/lib/zeek-lab/logs:/logs:Z -w /logs docker.io/zeek/zeek:lts zeek -C -i INTERFACE_AUTORISEE
   ```
   👉 Explication : `--network host` et les capacités NET_RAW/NET_ADMIN permettent d’écouter l’interface; `timeout` borne la durée (DUREE_SECONDES est à remplacer). Pour la production, faire valider un service systemd/Quadlet dédié (non détaillé).

4. Observer les journaux :
   ```bash
   sudo ls -l /var/lib/zeek-lab/logs
   sudo head -n 20 /var/lib/zeek-lab/logs/conn.log
   ```
   👉 Explication : Contrôle que `conn.log` et les autres journaux sont produits.

## 2. Production — Contrôles

Faire relire interface et réseaux locaux; surveiller l’espace disque et les pertes de paquets.

## 3. Production — Sécurité

- Aucune action de blocage.
- Journaux accessibles aux seuls comptes habilités.
- SELinux : rester en Enforcing; en cas de refus, `sudo ausearch -m avc -ts recent`.

## Validation et retour arrière

- **Validation** : Les journaux conn.log (et dns.log si du DNS est observé) sont produits sans erreur.
- **Retour arrière** : arrêter le conteneur (`sudo podman ps` puis `sudo podman stop NOM_CONTENEUR`, nom à remplacer) et supprimer les logs de test selon la politique.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-securiser)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-installer)