# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Configurer les serveurs DNS.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les serveurs et le domaine de recherche (`CONN`, `192.0.2.53`, `exemple.lan` à adapter) :
   ```bash
   sudo nmcli connection modify CONN ipv4.dns 192.0.2.53 ipv4.dns-search exemple.lan
   sudo nmcli connection up CONN
   ```
   👉 Explication : NetworkManager génère `/etc/resolv.conf`; ne pas l'éditer à la main.

2. Contrôler :
   ```bash
   cat /etc/resolv.conf
   getent hosts download.rockylinux.org
   ```
   👉 Explication : montre le serveur utilisé et la résolution réelle.

3. Tester un nom interne :
   ```bash
   getent hosts SRV01.EXEMPLE.LAN
   ```
   👉 Explication : valide la zone interne.

## 2. Production — Contrôles

Au moins deux serveurs DNS pour la redondance.

## 3. Production — Sécurité

Utiliser uniquement des résolveurs de confiance.

## Validation et retour arrière

- **Validation** : Les noms interne et externe se résolvent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)