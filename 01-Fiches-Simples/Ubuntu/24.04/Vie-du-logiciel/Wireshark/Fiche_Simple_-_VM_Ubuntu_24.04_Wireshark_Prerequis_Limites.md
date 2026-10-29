# Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Prerequis_Limites

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Wireshark
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / prérequis et limites
- **Tags** : `wireshark`, `ubuntu24.04`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer l’usage autorisé de Wireshark/TShark sur VM Ubuntu Server 24.04 LTS : analyse de fichiers et captures bornées, sans capture non autorisée.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l’autorisation de capture ou d’analyse (ticket TICKET, propriétaire des données, durée, interface INTERFACE_AUTORISEE).
   👉 Explication : Une capture contient souvent des données personnelles ou des identifiants; TICKET et INTERFACE_AUTORISEE sont des placeholders à remplacer.

2. Contrôler les ressources et l’affichage :
   ```bash
   cat /etc/os-release
   free -h
   df -h /var/tmp
   echo "${XDG_SESSION_TYPE:-aucune session graphique}"
   ```
   👉 Explication : L’interface graphique demande une session X11/Wayland; sur un serveur sans bureau, utiliser TShark en ligne de commande. Le disque doit accueillir les captures.

3. Noter les limites.
   👉 Explication : Wireshark ne déchiffre pas TLS sans clés fournies légalement; une VM ne voit que le trafic de son vSwitch; les dissecteurs traitent des données non fiables, d’où la nécessité de rester à jour. 

## 2. Production — Contrôles

Valider par écrit le périmètre, le lieu de stockage des .pcap et la durée de conservation.

## 3. Production — Sécurité

- Ne capturer que des réseaux autorisés.
- Ne pas ouvrir de capture d’origine inconnue sur un poste sensible.

## Validation et retour arrière

- **Validation** : Autorisation, ressources et limites consignées.
- **Retour arrière** : Aucune modification système; archiver les notes de cadrage.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Installer.md)
