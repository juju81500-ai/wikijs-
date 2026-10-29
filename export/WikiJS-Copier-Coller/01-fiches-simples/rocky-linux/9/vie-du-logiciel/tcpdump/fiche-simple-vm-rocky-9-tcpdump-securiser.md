# Fiche_Simple_-_VM_Rocky_9_tcpdump_Securiser

- **Environnement** : VM Rocky Linux 9 dédiée à tcpdump
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / sécurisation

---

## Problème précis à résoudre

Réduire les risques liés aux privilèges et aux fichiers de capture tcpdump.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier qui peut exécuter tcpdump :
   ```bash
   command -v tcpdump
   getcap "$(command -v tcpdump)"
   id
   ```
   👉 Explication : Une capacité réseau sur le binaire permettrait la capture à tout utilisateur qui peut l’exécuter; aucune sortie `getcap` attendue par défaut.

2. Limiter la capture au sudo nominatif :
   ```bash
   sudo -l
   ```
   👉 Explication : Contrôler que seuls les administrateurs réseau autorisés disposent de sudo; ne pas écrire de règle sudo générique pour tcpdump (risque d’échappement via options).

3. Restreindre les droits des fichiers produits :
   ```bash
   sudo chmod 0600 /var/tmp/captures/*.pcap
   ls -l /var/tmp/captures
   ```
   👉 Explication : Les captures peuvent contenir des identifiants en clair; accès limité au propriétaire.

4. Définir la rétention :
   ```bash
   sudo find /var/tmp/captures -name "*.pcap" -mtime +RETENTION_JOURS -print
   ```
   👉 Explication : Liste les fichiers plus anciens que RETENTION_JOURS (à remplacer par la durée de la politique); remplacer `-print` par `-delete` seulement après relecture.

## 2. Production — Contrôles

Revoir trimestriellement les comptes autorisés et la présence de fichiers .pcap oubliés.

## 3. Production — Sécurité

- Chiffrer ou transférer les captures vers un stockage protégé avant partage.
- Ne pas capturer d’identifiants ni de contenu applicatif sauf nécessité documentée.
- SELinux : écrire dans `/var/tmp` ou dans un répertoire dédié au bon contexte; en cas de refus, consulter `sudo ausearch -m avc -ts recent` sans désactiver SELinux.

## Validation et retour arrière

- **Validation** : Aucune capacité sur le binaire, fichiers en 0600, rétention définie.
- **Retour arrière** : Rétablir les permissions précédentes consignées; retirer toute règle sudo ajoutée.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-tcpdump)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-valider)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/tcpdump/fiche-simple-vm-rocky-9-tcpdump-configurer)