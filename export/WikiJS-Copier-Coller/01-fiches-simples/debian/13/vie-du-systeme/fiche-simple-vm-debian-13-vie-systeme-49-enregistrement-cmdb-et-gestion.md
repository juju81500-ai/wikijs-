# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Inscrire la machine dans l'inventaire.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les informations à saisir :
   ```bash
   hostnamectl
   ip -br address
   cat /etc/os-release | head -3
   dmidecode -s system-serial-number 2>/dev/null
   ```
   👉 Explication : nom, IP, version et numéro de série pour GLPI ou NetBox.

2. Enregistrer les secrets dans le coffre (Vaultwarden, KeePass ou Vault) et réserver l'IP dans l'IPAM.
   👉 Explication : aucun mot de passe ne reste dans un fichier ou un ticket.

## 2. Production — Contrôles

Renseigner propriétaire, criticité et date de fin de vie.

## 3. Production — Sécurité

Accès au coffre nominatif et journalisé.

## Validation et retour arrière

- **Validation** : La machine est visible dans la CMDB.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)