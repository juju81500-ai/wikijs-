# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-44`

---

## Problème précis à résoudre

Vérifier ce qui est visible depuis l'extérieur.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis une machine du réseau de test, scanner l'hôte (remplacer `IP_HOTE`) :
   ```sh
   nmap -sS -p- IP_HOTE
   nmap -sV -p 22,443,902 IP_HOTE
   ```
   👉 Explication : doit montrer uniquement les ports autorisés (443 Host Client, 902 vCenter, 22 SSH seulement si activé).

2. Contrôler que le Host Client n'est pas accessible depuis un réseau non autorisé.
   👉 Explication : valide les règles de l'étape 29.

3. Tester les protocoles TLS :
   ```sh
   nmap --script ssl-enum-ciphers -p 443 IP_HOTE
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

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
