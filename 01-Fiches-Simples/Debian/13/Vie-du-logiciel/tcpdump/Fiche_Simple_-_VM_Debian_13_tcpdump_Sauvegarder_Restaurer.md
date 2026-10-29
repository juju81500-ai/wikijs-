# Fiche_Simple_-_VM_Debian_13_tcpdump_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 dédiée à tcpdump
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : tcpdump / sauvegarder / restaurer
- **Tags** : `tcpdump`, `debian13`, `vie-du-logiciel`, `sauvegarder_restaurer`

---

## Problème précis à résoudre

Préserver seulement les pcap nécessaires et restaurer leur intégrité dans un stockage protégé.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive d’une capture déjà autorisée :
   ```bash
   sudo tar -czf /root/tcpdump-capture-$(date +%F).tar.gz /var/tmp/tcpdump-lab/capture.pcap
   sudo chmod 600 /root/tcpdump-capture-$(date +%F).tar.gz
   sudo sha256sum /root/tcpdump-capture-$(date +%F).tar.gz
   ```
   👉 Explication : L’archive est sensible; chiffrer avant transfert et appliquer la conservation autorisée.

2. Vérifier l’archive puis préparer un répertoire temporaire privé :
   ```bash
   sudo tar -tzf /root/tcpdump-capture-$(date +%F).tar.gz
   sudo install -d -m 0700 /var/tmp/tcpdump-restore-test
   sudo tar -xzf /root/tcpdump-capture-$(date +%F).tar.gz -C /var/tmp/tcpdump-restore-test
   ```
   👉 Explication : Ne pas écraser la capture originale ni restaurer dans un répertoire exposé.

3. Relire le pcap restauré depuis son chemin extrait et comparer son empreinte à l’original.
   👉 Explication : Supprimer la copie de test selon la politique de conservation après validation.

## 2. Production — Contrôles

Définir si les captures doivent réellement être sauvegardées; stocker chiffrées, accès nominatif et rétention minimale.

## 3. Production — Sécurité

- Sauvegarder une capture prolonge sa durée de sensibilité; supprimer les copies temporaires après test.

## Validation et retour arrière

- **Validation** : Archive intègre, pcap relisible et accès conforme après restauration.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_tcpdump_Mise_A_Jour_Retour_Arriere.md)
