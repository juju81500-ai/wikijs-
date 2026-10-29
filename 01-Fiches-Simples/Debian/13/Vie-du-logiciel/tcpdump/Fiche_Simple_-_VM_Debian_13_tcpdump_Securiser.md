# Fiche_Simple_-_VM_Debian_13_tcpdump_Securiser

- **Environnement** : VM Debian 13 dédiée à tcpdump
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : tcpdump / sécuriser
- **Tags** : `tcpdump`, `debian13`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Réduire l’exposition des captures et éviter un accès privilégié persistant.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler propriétaire et permissions du répertoire et du pcap :
   ```bash
   sudo stat -c "%a %U:%G %n" /var/tmp/tcpdump-lab /var/tmp/tcpdump-lab/capture.pcap
   ```
   👉 Explication : Le répertoire doit rester inaccessible aux utilisateurs non autorisés.

2. Vérifier si le binaire dispose de capacités Linux :
   ```bash
   command -v tcpdump
   getcap "$(command -v tcpdump)"
   ```
   👉 Explication : Ne pas ajouter cap_net_raw ou cap_net_admin sans approbation et contrôle du moindre privilège.

3. Calculer une empreinte avant transfert ou analyse :
   ```bash
   sudo sha256sum /var/tmp/tcpdump-lab/capture.pcap
   ```
   👉 Explication : Conserver l’empreinte dans le dossier d’incident protégé, séparément du fichier.

## 2. Production — Contrôles

Chiffrer stockage/transfert, limiter lecteurs, documenter rétention et effacement, auditer les sessions de capture.

## 3. Production — Sécurité

- Les pcap sont sensibles; ne pas les joindre à un ticket public ou les laisser dans un répertoire partagé.

## Validation et retour arrière

- **Validation** : Modes d’accès validés, empreinte consignée et données limitées à la période nécessaire.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_tcpdump_Valider.md)
