# Fiche_Simple_-_VM_Debian_13_WireGuard_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 dédiée à WireGuard natif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : WireGuard natif / sauvegarder / restaurer

---

## Problème précis à résoudre

Préserver configuration et clés WireGuard avec permissions et stockage adaptés.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive protégée :
   ```bash
   sudo tar --acls --xattrs -czf /root/wireguard-$(date +%F).tar.gz /etc/wireguard
   sudo chmod 600 /root/wireguard-$(date +%F).tar.gz
   sudo sha256sum /root/wireguard-$(date +%F).tar.gz
   ```
   👉 Explication : L’archive contient la clé privée serveur; chiffrer avant transfert.

2. Consigner l’inventaire des pairs, clés publiques, AllowedIPs et procédure de rotation; ne pas recopier les clés privées clients.
   👉 Explication : L’inventaire doit permettre d’identifier et révoquer un pair sans partager ses secrets.

3. Tester la restauration dans une VM isolée, en contrôlant propriétaire, modes et démarrage hors réseau de production.
   👉 Explication : Une copie ne remplace pas un test périodique de restauration.

## 2. Production — Contrôles

Définir RPO/RTO, rétention, accès nominatif, chiffrement et test de restauration.

## 3. Production — Sécurité

- Ne pas déposer l’archive en clair ni stocker les clés dans un ticket ou dépôt partagé.

## Validation et retour arrière

- **Validation** : Empreinte vérifiée et restauration testée en environnement isolé.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [WireGuard natif — documentation officielle](https://www.wireguard.com/quickstart/)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-mise-a-jour-retour-arriere)