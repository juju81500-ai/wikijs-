# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier ce qui est visible depuis l'extérieur.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis une machine du réseau de test, scanner l'hôte (remplacer `IP_HOTE`) :
   ```bash
   nmap -sS -p- IP_HOTE
   nmap -sV -p 22,8006,3128 IP_HOTE
   ```
   👉 Explication : doit montrer uniquement les ports autorisés depuis ce réseau.

2. Contrôler que 8006 n'est pas joignable depuis un réseau non autorisé (le pare-feu doit bloquer).
   👉 Explication : valide les règles de l'étape 29.

3. Tester le certificat et les protocoles TLS :
   ```bash
   nmap --script ssl-enum-ciphers -p 8006 IP_HOTE
   ```
   👉 Explication : refuser TLS 1.0 et 1.1.

## 2. Production — Contrôles

Planifier l'audit après chaque changement réseau.

## 3. Production — Sécurité

Obtenir l'autorisation avant tout scan.

## Validation et retour arrière

- **Validation** : Aucun port inattendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)