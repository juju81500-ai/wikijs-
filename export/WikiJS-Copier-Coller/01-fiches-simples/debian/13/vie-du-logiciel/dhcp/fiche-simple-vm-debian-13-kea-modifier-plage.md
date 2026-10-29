# Fiche_Simple_-_VM_Debian_13_Kea_Modifier_Plage.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP

---

## Problème précis à résoudre

Modifier une plage ou une option en sécurité et savoir revenir à l'état précédent.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration et l'état des baux (le nom du fichier de baux dépend du paquet : vérifier son chemin) :
   ```bash
   sudo cp -a /etc/kea/kea-dhcp4.conf /etc/kea/kea-dhcp4.conf.avant-changement
   ```
   👉 Explication : documente l'état avant modification.

2. Éditer le fichier, contrôler pools, options et chevauchements, puis valider :
   ```bash
   sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
   ```
   👉 Explication : aucune application tant que la validation échoue.

3. Appliquer par un redémarrage contrôlé :
   ```bash
   sudo systemctl restart isc-kea-dhcp4-server.service
   sudo systemctl --no-pager status isc-kea-dhcp4-server.service
   sudo journalctl -u isc-kea-dhcp4-server.service -n 50 --no-pager
   ```
   👉 Explication : charge le nouveau fichier et vérifie le démarrage.

4. En cas d'erreur, restaurer le fichier précédent, revalider et redémarrer :
   ```bash
   sudo cp -a /etc/kea/kea-dhcp4.conf.avant-changement /etc/kea/kea-dhcp4.conf
   sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
   sudo systemctl restart isc-kea-dhcp4-server.service
   ```
   👉 Explication : retour arrière documenté.

## 2. Production — Contrôles

Changement approuvé et annoncé; valeurs actuelles du VLAN consignées.

## 3. Production — Sécurité

- Ne pas supprimer le fichier des baux pour « réparer » une panne.
- Tester toute restauration de baux hors production.

## Validation et retour arrière

- **Validation** : Nouveau service actif et clients obtiennent des baux conformes.
- **Retour arrière** : Restaurer `kea-dhcp4.conf.avant-changement` et redémarrer le service.

## Si le problème n'est pas résolu

- [ISC Kea — Serveur DHCPv4](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html)
- [Guide complet Kea DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13#6-changer-une-plage-ou-revenir-en-arriere)