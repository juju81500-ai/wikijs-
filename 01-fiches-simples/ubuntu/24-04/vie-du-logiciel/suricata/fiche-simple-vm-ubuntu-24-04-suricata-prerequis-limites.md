# Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Prerequis_Limites

- **Environnement** : [[Glossary:VM]] Ubuntu Server 24-04 [[Glossary:LTS]] dédiée à Suricata
- **OS / Version** : Ubuntu Server 24-04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / prérequis et limites
- **Tags** : `suricata`, `ubuntu24.04`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer un capteur Suricata [[Glossary:IDS]] passif (détection et journalisation uniquement) sur VM Ubuntu Server 24-04 LTS, dans un périmètre autorisé.

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
   👉 Explication : Suricata consomme [[Glossary:CPU]]/RAM selon le débit et les règles; prévoir deux interfaces (gestion et capture) et un volume de logs.

3. Noter les limites.
   👉 Explication : Mode traité : IDS passif (AF_PACKET sur interface miroir/TAP). Le mode IPS/inline (NFQUEUE, blocage) n’est pas couvert. Le trafic chiffré n’est pas inspecté dans son contenu. Aucune détection ne remplace une revue des alertes. AppArmor : un profil `suricata` peut exister; en cas de refus, `sudo journalctl -k | grep DENIED`.

## 2. Production — Contrôles

Faire valider architecture ([[Glossary:SPAN]]/TAP), HOME_NET, volumétrie des logs et propriétaire des alertes.

## 3. Production — Sécurité

- Détection uniquement, sans action de blocage.
- Interface de capture sans adresse [[Glossary:IP]] si possible.

## Validation et retour arrière

- **Validation** : Autorisation tracée, ressources suffisantes, limites comprises.
- **Retour arrière** : Aucun changement système à annuler.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](../../../../logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata.md)
- [Étape suivante du guide](./fiche-simple-vm-ubuntu-24-04-suricata-installer.md)
