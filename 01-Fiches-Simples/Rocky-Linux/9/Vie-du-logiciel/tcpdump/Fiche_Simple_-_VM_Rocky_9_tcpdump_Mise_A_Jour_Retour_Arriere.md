# Fiche_Simple_-_VM_Rocky_9_tcpdump_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 dédiée à tcpdump
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / mise à jour et retour arrière
- **Tags** : `tcpdump`, `rocky9`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour tcpdump et libpcap, et revenir à la version précédente en cas de régression.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner la version actuelle :
   ```bash
   tcpdump --version 2>&1 | head -n 2
   ```
   👉 Explication : Point de comparaison avant changement.

2. Mettre à jour le paquet :
   ```bash
   sudo dnf check-update tcpdump libpcap
   sudo dnf upgrade tcpdump
   ```
   👉 Explication : Applique la version publiée par le dépôt du système; lire les notes de sécurité avant production.

3. Contrôler après mise à jour :
   ```bash
   tcpdump --version
   sudo tcpdump -D
   ```
   👉 Explication : Confirme que l’outil fonctionne et voit les interfaces.

4. Revenir en arrière si nécessaire :
   ```bash
   dnf history list tcpdump
   sudo dnf history undo ID_TRANSACTION
   ```
   👉 Explication : ID_TRANSACTION (à remplacer) est l’identifiant de la transaction dnf à annuler; si l’annulation échoue, utiliser `sudo dnf downgrade tcpdump` après vérification de la version disponible.

## 2. Production — Contrôles

Tester en lab, planifier la fenêtre, conserver la version précédente disponible.

## 3. Production — Sécurité

- Mettre à jour régulièrement : tcpdump analyse des données non fiables.
- Utiliser les dépôts approuvés uniquement.

## Validation et retour arrière

- **Validation** : La nouvelle version est installée et la capture de recette réussit.
- **Retour arrière** : Appliquer l’étape de retour arrière ci-dessus, puis relancer la recette.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_tcpdump.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_tcpdump_Sauvegarder_Restaurer.md)
