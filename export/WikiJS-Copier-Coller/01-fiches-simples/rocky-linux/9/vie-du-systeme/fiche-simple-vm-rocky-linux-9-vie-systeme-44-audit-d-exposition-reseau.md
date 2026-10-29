# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier ce que voit l'extérieur.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis une machine externe autorisée, scanner (adapter `192.0.2.10`) :
   ```bash
   nmap -sS -p- 192.0.2.10
   ```
   👉 Explication : liste les ports ouverts vus de l'extérieur; scanner uniquement avec autorisation.

2. Comparer avec la configuration locale :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : les ports vus doivent correspondre.

3. Contrôler le service SSH exposé :
   ```bash
   nmap -sV -p 22 192.0.2.10
   ```
   👉 Explication : vérifie la version annoncée.

## 2. Production — Contrôles

Planifier l'audit après chaque changement de flux.

## 3. Production — Sécurité

Obtenir l'accord écrit avant tout scan.

## Validation et retour arrière

- **Validation** : Aucun port inattendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)