# Fiche_Simple_-_VM_Rocky_9_Snort_Prerequis_Limites

- **Environnement** : VM Rocky Linux 9 dédiée à Snort
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / prérequis et limites

---

## Problème précis à résoudre

Cadrer un capteur Snort IDS passif sur VM Rocky Linux 9 : détection et journalisation uniquement, dans un périmètre autorisé.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l’autorisation d’inspecter le réseau (propriétaire, interface INTERFACE_AUTORISEE, HOME_NET_AUTORISE, rétention des alertes).
   👉 Explication : Les valeurs en majuscules sont des placeholders à remplacer par les valeurs approuvées.

2. Contrôler ressources et interfaces :
   ```bash
   cat /etc/os-release
   nproc
   free -h
   ip -br link
   df -h /var/log /opt
   ```
   👉 Explication : Snort a besoin de CPU/RAM proportionnels au débit et aux règles; prévoir une interface de capture dédiée (SPAN/TAP).

3. Choisir la branche.
   👉 Explication : Rocky 9 : les RPM officiels listés par l’éditeur ciblent l’ancienne branche 2.9 (fin de vie) pour CentOS/Fedora; cette série privilégie Snort 3 compilé depuis les sources officielles (préfixe `/opt/snort3`). Vérifier l’état actuel sur snort.org.

4. Noter les limites.
   👉 Explication : Mode traité : IDS passif (lecture de pcap ou capture sur interface miroir). Le mode inline/IPS et le blocage ne sont pas couverts. Les règles « subscriber » demandent une clé d’accès personnelle à ne jamais écrire dans une fiche. SELinux : rester en Enforcing; en cas de refus, `sudo ausearch -m avc -ts recent`.

## 2. Production — Contrôles

Faire valider la branche, le périmètre, la source des règles et le propriétaire des alertes.

## 3. Production — Sécurité

- Détection uniquement; aucun blocage.
- Source de règles approuvée et licence respectée.

## Validation et retour arrière

- **Validation** : Branche choisie, autorisation tracée, limites comprises.
- **Retour arrière** : Aucun changement système à annuler.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-snort)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/snort/fiche-simple-vm-rocky-9-snort-installer)