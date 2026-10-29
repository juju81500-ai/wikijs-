# Fiche_Simple_-_VM_Debian_13_K3s_Installer_Noeud_Lab.md

- **Environnement** : VM de laboratoire Debian 13 isolée
- **OS / Version** : Debian 13; version K3s explicitement épinglée
- **Catégorie** : Kubernetes / K3s / installation
- **Tags** : `debian13`, `k3s`, `kubernetes`, `installation`, `lab`

---

## Problème précis à résoudre

Installer un premier nœud K3s de laboratoire avec une version vérifiée, une configuration minimale et un accès limité.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les prérequis du nœud :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   free -h; df -h /var/lib
   sudo ss -tlnp | grep -E ':(6443|10250)\b' || echo "ports libres"
   ```
   👉 Explication : on contrôle l'OS, les ressources et la disponibilité des ports.

2. Télécharger le script officiel puis l'examiner avant exécution :
   ```bash
   curl -fsSL https://get.k3s.io -o /tmp/k3s-install.sh
   less /tmp/k3s-install.sh
   ```
   👉 Explication : on lit le script au lieu de l'exécuter directement depuis le réseau.

3. Installer une version épinglée (remplacer par la version retenue au cadrage) :
   ```bash
   sudo INSTALL_K3S_VERSION="v1.XX.Y+k3s1" sh /tmp/k3s-install.sh
   ```
   👉 Explication : la variable `INSTALL_K3S_VERSION` évite l'installation automatique de la dernière version; `v1.XX.Y+k3s1` est un exemple à remplacer.

4. Vérifier le service et le nœud :
   ```bash
   sudo systemctl --no-pager status k3s
   sudo k3s kubectl get nodes -o wide
   sudo k3s kubectl get pods -A
   ```
   👉 Explication : le nœud doit être `Ready` et les pods système `Running`.

5. Contrôler les droits du kubeconfig :
   ```bash
   sudo ls -l /etc/rancher/k3s/k3s.yaml
   ```
   👉 Explication : ce fichier donne l'accès administrateur; ne pas le copier vers un poste non autorisé.

## 2. Production — Contrôles

- Répéter d'abord l'installation sur un environnement représentatif et documenter les paquets, versions et options.
- Confirmer les ports et dépendances système nécessaires avec la matrice de compatibilité.
- Prévoir un créneau, une sauvegarde et une procédure de retour arrière avant de créer le service.
- Vérifier que le kubeconfig administrateur est lisible uniquement par le compte autorisé.

## 3. Production — Sécurité

- Ne jamais publier le kubeconfig, le token ou des secrets dans des journaux, tickets ou dépôts.
- N'exposer ni l'API ni les composants K3s sur toutes les interfaces sans filtrage et contrôle d'accès explicites.
- Ne pas exécuter un script distant sans vérifier son contenu et sa provenance.
- Limiter les droits du compte d'administration et protéger les fichiers de configuration.

## Validation et retour arrière

- **Validation** : `systemctl` confirme le service actif et `kubectl get nodes` retourne le nœud attendu.
- **Retour arrière** : conserver journaux, configuration et instantané; utiliser la procédure officielle de désinstallation après avoir sauvegardé les données à préserver.

## Si le problème n'est pas résolu

- [K3s — démarrage rapide](https://docs.k3s.io/quick-start)
- [K3s — options d'installation](https://docs.k3s.io/installation/configuration)
- [Guide complet K3s Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/14_Orchestration_Cluster_K3s_Kubernetes_Debian_13.md#2-installer-un-noeud-de-laboratoire)
