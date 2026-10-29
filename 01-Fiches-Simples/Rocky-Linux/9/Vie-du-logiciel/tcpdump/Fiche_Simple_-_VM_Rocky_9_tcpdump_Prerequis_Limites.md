# Fiche_Simple_-_VM_Rocky_9_tcpdump_Prerequis_Limites

- **Environnement** : VM Rocky Linux 9 dédiée à tcpdump
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / prérequis et limites
- **Tags** : `tcpdump`, `rocky9`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer l’usage autorisé de tcpdump sur VM Rocky Linux 9 avant toute capture : périmètre, durée, données concernées et limites techniques.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir et consigner l’autorisation de capture (ticket, propriétaire du réseau, durée, interface, hôtes et ports concernés).
   👉 Explication : Une capture peut contenir des données personnelles ou des secrets en clair; elle ne se fait qu’avec un cadre écrit. Les valeurs TICKET, INTERFACE_AUTORISEE et DUREE_MAX sont des placeholders à remplacer par vos valeurs.

2. Relever l’OS, le noyau et l’accès réseau de la VM :
   ```bash
   cat /etc/os-release
   uname -r
   ip -br link
   ip -br addr
   ```
   👉 Explication : Identifier les interfaces réellement présentes; une VM ne voit que le trafic de son vSwitch (mode promiscuité du réseau virtuel à vérifier côté hyperviseur).

3. Contrôler l’espace disponible pour les captures :
   ```bash
   df -h /var/tmp
   ```
   👉 Explication : Une capture non bornée peut remplir le disque; prévoir un volume dédié et une limite de taille.

4. Noter les limites connues.
   👉 Explication : tcpdump ne déchiffre pas TLS, ne voit pas le trafic entre deux VM d’un autre vSwitch, et tronque les paquets selon la taille de capture (`-s`). Il capture en lecture seule : il ne bloque rien. SELinux : écrire dans `/var/tmp` ou dans un répertoire dédié au bon contexte; en cas de refus, consulter `sudo ausearch -m avc -ts recent` sans désactiver SELinux.

## 2. Production — Contrôles

Valider par écrit le périmètre, l’emplacement des fichiers .pcap, leur durée de conservation et les personnes habilitées à les lire.

## 3. Production — Sécurité

- Capturer uniquement un réseau dont vous avez l’autorisation; jamais de capture « pour voir » en production.
- Limiter durée, volume et filtres; ne pas capturer sur l’interface de gestion sans besoin.

## Validation et retour arrière

- **Validation** : Autorisation tracée, interface et volume identifiés, limites comprises.
- **Retour arrière** : Aucune modification système à annuler; archiver les notes de cadrage obsolètes.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_tcpdump.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_tcpdump_Installer.md)
