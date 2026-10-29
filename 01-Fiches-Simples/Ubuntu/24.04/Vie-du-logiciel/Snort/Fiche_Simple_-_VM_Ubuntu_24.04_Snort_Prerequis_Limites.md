# Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Prerequis_Limites

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Snort
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / prérequis et limites
- **Tags** : `snort`, `ubuntu24.04`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer un capteur Snort IDS passif sur VM Ubuntu Server 24.04 LTS : détection et journalisation uniquement, dans un périmètre autorisé.

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
   👉 Explication : Ubuntu 24.04 : le paquet `snort` des dépôts peut correspondre à l’ancienne branche 2.9 (fin de vie) ou à une version packagée spécifique; contrôler `apt-cache policy snort` avant de décider. Cette série privilégie Snort 3 compilé depuis les sources officielles (préfixe `/opt/snort3`).

4. Noter les limites.
   👉 Explication : Mode traité : IDS passif (lecture de pcap ou capture sur interface miroir). Le mode inline/IPS et le blocage ne sont pas couverts. Les règles « subscriber » demandent une clé d’accès personnelle à ne jamais écrire dans une fiche. AppArmor : en cas de refus, `sudo journalctl -k | grep DENIED`.

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
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Snort.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Installer.md)
