# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Contrôler ce qui est vu de l'extérieur.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis une machine de contrôle autorisée (remplacer l'IP) :
   ```bash
   sudo apt install nmap
   sudo nmap -sV -p- 192.0.2.10
   ```
   👉 Explication : liste les ports et services visibles; ne scanner que des machines autorisées.

## 2. Production — Contrôles

Planifier le scan avec le propriétaire du réseau.

## 3. Production — Sécurité

Comparer avec les règles du pare-feu.

## Validation et retour arrière

- **Validation** : Les ports visibles correspondent au plan.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)