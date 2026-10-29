# Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Valider

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Zeek
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / validation
- **Tags** : `zeek`, `ubuntu24.04`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter le capteur Zeek : processus, journaux et pertes de paquets.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le statut :
   ```bash
   sudo /opt/zeek/bin/zeekctl status
   sudo /opt/zeek/bin/zeekctl netstats
   ```
   👉 Explication : `netstats` montre les paquets reçus et perdus.

2. Générer du trafic de test autorisé :
   ```bash
   ping -c 3 HOTE_AUTORISE
   sudo /opt/zeek/bin/zeekctl cron
   ```
   👉 Explication : Produit des connexions observables; `zeekctl cron` force la rotation/maintenance (qui ne doit pas être répétée en boucle).

3. Lire les journaux :
   ```bash
   sudo /opt/zeek/bin/zeek-cut ts id.orig_h id.resp_h proto < /opt/zeek/logs/current/conn.log | tail -n 10
   ```
   👉 Explication : Affiche quelques colonnes de `conn.log` (le trafic ICMP y figure avec proto icmp).

## 2. Production — Contrôles

Archiver version, date et extrait des journaux de recette.

## 3. Production — Sécurité

- Tests sur trafic autorisé uniquement.

## Validation et retour arrière

- **Validation** : Les journaux de connexion sont produits et cohérents avec le trafic de test.
- **Retour arrière** : Arrêter le capteur ou le conteneur de test et nettoyer les fichiers de test.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Zeek.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Sauvegarder_Restaurer.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Securiser.md)
