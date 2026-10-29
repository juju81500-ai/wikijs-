# Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à tcpdump
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / sauvegarde et restauration

---

## Problème précis à résoudre

Conserver et restaurer ce qui est utile : captures de preuve et liste de commandes validées (tcpdump n’a pas de configuration serveur).

## 1. Hors-Production (Lab / Test / POC)

1. Calculer l’empreinte d’une capture à conserver :
   ```bash
   sha256sum /var/tmp/captures/TICKET.pcap | tee /var/tmp/captures/TICKET.pcap.sha256
   ```
   👉 Explication : Prouve l’intégrité du fichier; TICKET est à remplacer.

2. Archiver captures et empreintes dans un stockage protégé :
   ```bash
   sudo tar -czf /var/tmp/captures-TICKET.tar.gz -C /var/tmp/captures .
   sudo chmod 0600 /var/tmp/captures-TICKET.tar.gz
   ```
   👉 Explication : Crée une archive lisible uniquement par root; la copier ensuite vers le stockage approuvé (non détaillé ici).

3. Restaurer et contrôler :
   ```bash
   mkdir -p /var/tmp/restore && sudo tar -xzf /var/tmp/captures-TICKET.tar.gz -C /var/tmp/restore
   (cd /var/tmp/restore && sha256sum -c TICKET.pcap.sha256)
   ```
   👉 Explication : Vérifie que l’empreinte correspond après restauration.

## 2. Production — Contrôles

Tester la restauration sur un échantillon et respecter la durée de conservation.

## 3. Production — Sécurité

- Chiffrer l’archive avant sortie de la VM.
- Ne pas mettre de mot de passe d’archive dans un script.

## Validation et retour arrière

- **Validation** : `sha256sum -c` retourne OK après restauration.
- **Retour arrière** : Supprimer le répertoire de restauration `/var/tmp/restore` après contrôle.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-tcpdump)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-mise-a-jour-retour-arriere)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-valider)