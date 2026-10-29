# Haute disponibilité d'un service avec HAProxy et Keepalived

- **Environnement** : Deux nœuds Linux sur le même segment L2, plus des serveurs applicatifs redondés
- **Composants** : HAProxy pour le proxy, Keepalived/VRRP pour l'adresse IP virtuelle

## 1. Préparer l'architecture

Fiche simple : [préparer l'architecture](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-preparer-architecture).

Définir une IP virtuelle libre, les IP fixes des pairs, l'interface L2, les backends et les sondes de santé. Vérifier que le commutateur, l'hyperviseur et le réseau autorisent VRRP/multicast ou le mode unicast choisi. Configurer une seule IP virtuelle ; elle ne remplace ni la redondance des backends ni celle du stockage/base.

## 2. Installer et valider HAProxy

Fiche simple : [installer et valider HAProxy](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy).

Installer HAProxy depuis le dépôt maintenu de la distribution. Configurer un frontend sur l'adresse prévue, des backends explicites et une sonde correspondant à un endpoint de santé réel. Valider avant activation :

```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
sudo systemctl enable --now haproxy
sudo systemctl --no-pager status haproxy
```

Restreindre le frontend, les ports d'administration et les métriques aux réseaux nécessaires. Ne pas exposer les interfaces de statistiques sans authentification et filtrage.

## 3. Configurer VRRP de façon symétrique

Fiche simple : [configurer VRRP de façon symétrique](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-configurer-vrrp-symetrique).

Installer Keepalived sur les deux nœuds. Créer une instance VRRP avec le même `virtual_router_id`, la même interface et le même groupe d'adresses ; utiliser des priorités distinctes. La sonde doit retirer l'éligibilité si HAProxy est indisponible. Utiliser une méthode d'authentification compatible avec la version, sans considérer une clé VRRP comme un chiffrement.

Avant activation, vérifier que les deux configurations ne peuvent pas revendiquer des adresses différentes et que le filtrage laisse passer VRRP entre les pairs uniquement.

```bash
sudo keepalived --config-test -f /etc/keepalived/keepalived.conf
sudo systemctl enable --now keepalived
ip addr show
```

Si `--config-test` n'existe pas dans le paquet installé, valider selon la page de manuel locale puis activer en fenêtre de maintenance.

## 4. Tester le basculement

Fiche simple : [tester le basculement](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-tester-basculement).

Vérifier le service via l'IP virtuelle, puis simuler séparément l'arrêt de HAProxy et la perte d'un nœud dans une fenêtre contrôlée. Confirmer le déplacement de l'IP, les journaux, les connexions existantes et le retour au primaire selon le comportement voulu.

## 5. Sécurité et retour arrière

Fiche simple : [sécurité et retour arrière](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-securite-retour-arriere).

- Filtrer VRRP entre les seuls pairs et limiter les ports HAProxy aux clients attendus.
- Surveiller l'état des deux nœuds et signaler une situation split-brain.
- Conserver les fichiers antérieurs et la console d'administration accessible.
- Si l'IP virtuelle flappe, désactiver le changement le plus récent sur un nœud à la fois et rétablir le service sur le nœud sain.