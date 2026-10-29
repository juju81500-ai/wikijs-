# Fiche_Simple_-_VM_Debian_13_tcpdump_Valider

- **Environnement** : VM Debian 13 dédiée à tcpdump
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : tcpdump / valider

---

## Problème précis à résoudre

Valider une capture locale et son intégrité sans réémettre le trafic capturé.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier présence et empreinte :
   ```bash
   sudo ls -lh /var/tmp/tcpdump-lab/capture.pcap
   sudo sha256sum /var/tmp/tcpdump-lab/capture.pcap
   ```
   👉 Explication : Comparer l’empreinte au dossier de suivi après transfert.

2. Lire un échantillon de paquets hors ligne :
   ```bash
   sudo tcpdump -nn -r /var/tmp/tcpdump-lab/capture.pcap -c 20
   ```
   👉 Explication : Vérifier que filtre et horaires correspondent au ticket autorisé.

3. Contrôler le nombre et la durée avec les métadonnées du changement.
   👉 Explication : Ne pas lancer une capture plus large pour compenser une capture manquante sans nouvelle approbation.

## 2. Production — Contrôles

Faire approuver résultat, vérifier absence de données hors périmètre et confirmer l’effacement selon rétention.

## 3. Production — Sécurité

- Limiter l’accès à l’échantillon; le contenu ne doit pas être publié dans des journaux généraux.

## Validation et retour arrière

- **Validation** : Lecture pcap réussie, filtre conforme, empreinte vérifiée et rétention définie.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-sauvegarder-restaurer)