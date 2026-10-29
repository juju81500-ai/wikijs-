# Fiche_Simple_-_VM_Rocky_9_Wireshark_Valider

- **Environnement** : VM Rocky Linux 9 dédiée à Wireshark
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / validation
- **Tags** : `wireshark`, `rocky9`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter une capture locale bornée et sa relecture.

## 1. Hors-Production (Lab / Test / POC)

1. Capturer cinq paquets ICMP autorisés :
   ```bash
   dumpcap -i INTERFACE_AUTORISEE -c 5 -f icmp -w /var/tmp/recette.pcapng &
   ping -c 3 HOTE_AUTORISE
   wait
   ```
   👉 Explication : Le ping produit des paquets à capturer; `-c 5` termine automatiquement.

2. Relire :
   ```bash
   tshark -r /var/tmp/recette.pcapng -c 5
   ```
   👉 Explication : Affiche les paquets capturés sans toucher au réseau.

3. Nettoyer :
   ```bash
   rm -f /var/tmp/recette.pcapng
   pgrep -a dumpcap || echo "aucune capture active"
   ```
   👉 Explication : Supprime le fichier de test et vérifie qu’aucun processus ne reste.

## 2. Production — Contrôles

Archiver date, version et résultat de la recette.

## 3. Production — Sécurité

- Tester uniquement vers des hôtes autorisés.

## Validation et retour arrière

- **Validation** : Les paquets ICMP sont lus par tshark et aucune capture ne reste active.
- **Retour arrière** : Arrêter un éventuel dumpcap restant avec `kill PID_DUMPCAP` (PID à remplacer).

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Wireshark_Sauvegarder_Restaurer.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Wireshark_Securiser.md)
