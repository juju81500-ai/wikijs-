# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Fixer les adresses définitives des interfaces.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Interfaces > [LAN] : Type de configuration IPv4 = `Static IPv4`, Adresse IPv4 `IP_LAN/24` (ex. `10.0.0.1/24`), Enregistrer puis Appliquer les modifications.
   👉 Explication : `IP_LAN` est l'adresse du pare-feu sur le réseau interne.

2. Interfaces > [WAN] : `DHCP` ou `Static IPv4` avec Passerelle amont `IP_PASSERELLE` (adresse fournie par le FAI).
   👉 Explication : définit la sortie vers Internet.

3. Contrôler en shell :
   ```sh
   ifconfig vtnet0
   netstat -rn | grep default
   ping -c 3 IP_PASSERELLE
   ```
   👉 Explication : vérifie l'adresse, la route par défaut et la joignabilité de la passerelle.

## 2. Production — Contrôles

Réserver les adresses dans le plan d'adressage (IPAM).

## 3. Production — Sécurité

Changer l'adresse LAN peut couper la session d'administration : garder la console.

## Validation et retour arrière

- **Validation** : Adresses conformes au plan et passerelle joignable.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
