# Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu 24.04 dédiée à un serveur WireGuard natif
- **OS / Version** : Ubuntu 24.04 LTS Noble; noyau avec module WireGuard et paquet wireguard, versions à vérifier
- **Catégorie** : WireGuard natif / sauvegarder / restaurer

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration WireGuard sans exposer les clés.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive protégée :
   ```bash
   sudo install -d -m 0700 /var/backups/wireguard
   sudo tar czf /var/backups/wireguard/wireguard-$(date +%F).tar.gz -C / etc/wireguard
   sudo chmod 600 /var/backups/wireguard/*.tar.gz
   ```
   👉 Explication : L'archive contient la clé privée : la chiffrer et la stocker hors de la VM.

2. Restaurer sur un hôte de test :
   ```bash
   sudo tar xzf /var/backups/wireguard/wireguard-DATE.tar.gz -C /
   sudo systemctl restart wg-quick@wg0
   ```
   👉 Explication : DATE est la date de l'archive (à remplacer).

## 2. Production — Contrôles

Tester la restauration périodiquement.

## 3. Production — Sécurité

- Ne jamais transmettre l'archive en clair.

## Validation et retour arrière

- **Validation** : Le serveur restauré accepte le pair pilote.
- **Retour arrière** : Restaurer le snapshot de la VM.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-mise-a-jour-retour-arriere)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)