# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Fixer l'IP du serveur avec Netplan.

## 1. Hors-Production (Lab / Test / POC)

1. Lister la configuration Netplan existante puis empêcher cloud-init de la réécrire :
   ```bash
   ls -l /etc/netplan/
   sudo netplan get
   echo 'network: {config: disabled}' | sudo tee /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
   ```
   👉 Explication : sur une image installée avec cloud-init, `50-cloud-init.yaml` peut être régénéré; la directive l'évite.

2. Écrire la configuration statique (remplacer `ens18`, l'adresse, la passerelle et les DNS) :
   ```bash
   sudo tee /etc/netplan/01-reseau.yaml >/dev/null <<'EOT'
   network:
     version: 2
     ethernets:
       ens18:
         dhcp4: false
         addresses: [192.0.2.10/24]
         routes:
           - to: default
             via: 192.0.2.1
         nameservers:
           addresses: [192.0.2.53]
           search: [exemple.lan]
   EOT
   sudo chmod 600 /etc/netplan/*.yaml
   ```
   👉 Explication : fichier YAML (indentation par espaces); les fichiers doivent être en `600` sinon Netplan avertit. Retirer l'ancien `50-cloud-init.yaml` s'il définit la même interface.

3. Appliquer avec retour automatique, en gardant la console ouverte, puis tester :
   ```bash
   sudo netplan try
   ip -br address
   ip route
   ping -c 2 192.0.2.1
   ```
   👉 Explication : `netplan try` annule la configuration si elle n'est pas confirmée avec Entrée sous 120 s; utiliser `sudo netplan apply` seulement après ce test.

## 2. Production — Contrôles

Réserver l'adresse dans l'IPAM (étape 49).

## 3. Production — Sécurité

Valider depuis la console : une erreur coupe l'accès SSH.

## Validation et retour arrière

- **Validation** : Le serveur répond sur la nouvelle IP.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)