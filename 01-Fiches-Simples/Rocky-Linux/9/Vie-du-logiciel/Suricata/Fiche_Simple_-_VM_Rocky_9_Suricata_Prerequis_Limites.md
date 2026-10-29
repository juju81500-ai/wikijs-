# Fiche_Simple_-_VM_Rocky_9_Suricata_Prerequis_Limites

- **Environnement** : VM Rocky Linux 9 dédiée à Suricata
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / prérequis et limites
- **Tags** : `suricata`, `rocky9`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer un capteur Suricata IDS passif (détection et journalisation uniquement) sur VM Rocky Linux 9, dans un périmètre autorisé.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l’autorisation d’inspecter le réseau (propriétaire, interface INTERFACE_AUTORISEE, périmètre HOME_NET_AUTORISE, durée de conservation des logs).
   👉 Explication : L’inspection réseau traite des données de tiers; les valeurs en majuscules sont des placeholders à remplacer.

2. Contrôler ressources et interfaces :
   ```bash
   cat /etc/os-release
   nproc
   free -h
   ip -br link
   df -h /var/log
   ```
   👉 Explication : Suricata consomme CPU/RAM selon le débit et les règles; prévoir deux interfaces (gestion et capture) et un volume de logs.

3. Noter les limites.
   👉 Explication : Mode traité : IDS passif (AF_PACKET sur interface miroir/TAP). Le mode IPS/inline (NFQUEUE, blocage) n’est pas couvert. Le trafic chiffré n’est pas inspecté dans son contenu. Aucune détection ne remplace une revue des alertes. SELinux : rester en Enforcing; pour tout refus, `sudo ausearch -m avc -ts recent` puis corriger le contexte plutôt que désactiver SELinux.

## 2. Production — Contrôles

Faire valider architecture (SPAN/TAP), HOME_NET, volumétrie des logs et propriétaire des alertes.

## 3. Production — Sécurité

- Détection uniquement, sans action de blocage.
- Interface de capture sans adresse IP si possible.

## Validation et retour arrière

- **Validation** : Autorisation tracée, ressources suffisantes, limites comprises.
- **Retour arrière** : Aucun changement système à annuler.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Suricata.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Suricata_Installer.md)
