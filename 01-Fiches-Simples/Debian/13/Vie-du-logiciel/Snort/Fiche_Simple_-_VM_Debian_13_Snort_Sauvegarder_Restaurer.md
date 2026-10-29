# Fiche_Simple_-_VM_Debian_13_Snort_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 dédiée à Snort IDS passif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : Snort IDS passif / sauvegarder / restaurer
- **Tags** : `snort`, `debian13`, `vie-du-logiciel`, `sauvegarder_restaurer`

---

## Problème précis à résoudre

Sauvegarder configuration et règles locales, puis tester une restauration isolée.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive de configuration avec permissions restreintes :
   ```bash
   sudo tar --acls --xattrs -czf /root/snort-config-$(date +%F).tar.gz /etc/snort
   sudo chmod 600 /root/snort-config-$(date +%F).tar.gz
   sudo sha256sum /root/snort-config-$(date +%F).tar.gz
   ```
   👉 Explication : Adapter le chemin à celui fourni par le paquet; transférer vers un dépôt chiffré et approuvé.

2. Consigner l’inventaire des versions, règles et sources de règles.
   👉 Explication : Éviter de mélanger règles personnalisées et captures; protéger séparément ces données.

3. Restaurer sur une VM isolée, puis relancer le test snort -T avant activation.
   👉 Explication : Vérifier que règles et binaire appartiennent à la même branche.

## 2. Production — Contrôles

Définir RPO/RTO, rétention, intégrité, accès au dépôt et test périodique de restauration.

## 3. Production — Sécurité

- Ne pas publier les règles internes ou détails réseau dans un dépôt public.

## Validation et retour arrière

- **Validation** : Archive intègre, empreinte vérifiée et configuration restaurée/testée hors production.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [Snort IDS passif — documentation officielle](https://www.snort.org/documents)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_Snort_Mise_A_Jour_Retour_Arriere.md)
