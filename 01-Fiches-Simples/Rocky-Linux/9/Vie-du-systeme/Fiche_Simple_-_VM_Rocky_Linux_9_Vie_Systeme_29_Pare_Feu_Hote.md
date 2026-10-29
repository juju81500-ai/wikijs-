# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Filtrer les flux entrants avec firewalld.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état :
   ```bash
   sudo systemctl enable --now firewalld
   sudo firewall-cmd --state
   sudo firewall-cmd --list-all
   ```
   👉 Explication : firewalld est le pare-feu par défaut de Rocky; zone `public`.

2. Autoriser SSH depuis le réseau d'administration seulement (adapter `192.0.2.0/24`) :
   ```bash
   sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.0.2.0/24" service name="ssh" accept'
   sudo firewall-cmd --permanent --remove-service=ssh
   sudo firewall-cmd --reload
   ```
   👉 Explication : limite SSH à une plage; l'option `--permanent` persiste après redémarrage.

3. Contrôler le résultat :
   ```bash
   sudo firewall-cmd --list-all
   ```
   👉 Explication : seuls les services voulus sont listés.

## 2. Production — Contrôles

Documenter chaque ouverture de port.

## 3. Production — Sécurité

Politique par défaut restrictive; tester depuis la console pour éviter l'auto-blocage.

## Validation et retour arrière

- **Validation** : Les ports non listés sont refusés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
