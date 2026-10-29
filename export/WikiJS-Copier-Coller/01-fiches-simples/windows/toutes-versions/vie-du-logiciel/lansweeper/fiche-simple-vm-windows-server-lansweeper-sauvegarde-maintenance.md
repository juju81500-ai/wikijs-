# Fiche_Simple_-_VM_Windows_Server_Lansweeper_Sauvegarde_Maintenance.md

- **Environnement** : Serveur Windows x64 avec Lansweeper Classic (SQL LocalDB ou SQL Server selon l'échelle)
- **OS / Version** : Windows Server 2022 recommandé; Lansweeper Classic selon la matrice officielle
- **Catégorie** : inventaire de parc / découverte réseau

---

## Problème précis à résoudre

Sauvegarder et mettre à jour sans perdre la clé de chiffrement des identifiants.

## 1. Hors-Production (Lab / Test / POC)

1. Avant toute mise à jour, sauvegarder la base SQL, les rapports, la configuration, `Encryption.txt`, l'identité des serveurs de scan et le certificat.
   👉 Explication : sans la clé, les identifiants chiffrés sont inutilisables.

2. Tester la restauration sur un lab.
   👉 Explication : prouve que la sauvegarde fonctionne.

3. Mettre à jour chaque composant selon les instructions de la version.
   👉 Explication : respecter l'ordre officiel.

4. Confirmer après mise à jour que la clé de chiffrement des identifiants reste cohérente.
   👉 Explication : évite des échecs de scan.

## 2. Production — Contrôles

Planifier sauvegardes régulières et fenêtres de mise à jour.

## 3. Production — Sécurité

- Chiffrer et isoler la sauvegarde de `Encryption.txt`.

## Validation et retour arrière

- **Validation** : restauration en lab réussie et scan fonctionnel après mise à jour.
- **Retour arrière** : restaurer la base et la clé sauvegardées avant la mise à jour.

## Si le problème n'est pas résolu

- [Lansweeper Classic — documentation](https://docs.lansweeper.com/classic/)
- [Lansweeper Classic — prérequis](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md)
- [Guide complet](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server#6-sauvegarde-et-maintenance)