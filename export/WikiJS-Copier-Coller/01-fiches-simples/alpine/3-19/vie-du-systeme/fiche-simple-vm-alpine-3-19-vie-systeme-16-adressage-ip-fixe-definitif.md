# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Passer à l'adresse fixe définitive.

## 1. Hors-Production (Lab / Test / POC)

1. Décrire l'interface dans `/etc/network/interfaces` (remplacer `ADRESSE_IP/24` par l'adresse et le masque, `PASSERELLE` par la passerelle) :
   ```sh
   cat > /etc/network/interfaces <<'EOF'
   auto lo
   iface lo inet loopback

   auto eth0
   iface eth0 inet static
       address ADRESSE_IP/24
       gateway PASSERELLE
   EOF
   ```
   👉 Explication : remplace le DHCP par l'adresse fixe; Alpine utilise `ifupdown-ng` qui accepte la notation `adresse/préfixe`.

2. Appliquer depuis la console :
   ```sh
   doas rc-service networking restart
   ```
   👉 Explication : recharge la configuration réseau; une erreur coupe la session SSH.

3. Vérifier l'adresse, la route et la sortie :
   ```sh
   ip -br addr
   ip route
   ping -c 3 PASSERELLE
   ```
   👉 Explication : l'interface porte l'adresse attendue et la passerelle répond.

## 2. Production — Contrôles

Réserver l'adresse dans l'IPAM ou le DHCP et l'inscrire à la CMDB.

## 3. Production — Sécurité

Tester en console ou avec un accès hors bande avant de couper la session.

## Validation et retour arrière

- **Validation** : L'adresse survit à un redémarrage (`ip -br addr` après reboot).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)