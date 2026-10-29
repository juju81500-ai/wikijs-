# Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Valider

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à tcpdump
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / validation

---

## Problème précis à résoudre

Recetter l’installation et le comportement borné de tcpdump.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version :
   ```bash
   tcpdump --version
   ```
   👉 Explication : Compare à la version consignée à l’installation.

2. Générer un trafic de test autorisé et le capturer :
   ```bash
   sudo tcpdump -i INTERFACE_AUTORISEE -nn -c 5 icmp &
   ping -c 3 HOTE_AUTORISE
   wait
   ```
   👉 Explication : Le ping vers un hôte autorisé produit des paquets ICMP visibles; `-c 5` termine la capture automatiquement.

3. Vérifier l’absence de capture résiduelle :
   ```bash
   pgrep -a tcpdump || echo "aucune capture active"
   ```
   👉 Explication : Garantit qu’aucun processus n’est laissé en arrière-plan.

## 2. Production — Contrôles

Archiver la sortie de recette avec date, version et opérateur.

## 3. Production — Sécurité

- Ne tester que sur des hôtes autorisés.

## Validation et retour arrière

- **Validation** : Les paquets ICMP de test sont visibles et aucune capture ne reste active.
- **Retour arrière** : Arrêter tout processus restant avec `kill PID_TCPDUMP` (PID à remplacer) et supprimer les fichiers de test.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-tcpdump)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-sauvegarder-restaurer)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-securiser)