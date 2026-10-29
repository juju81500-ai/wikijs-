# Haute disponibilité de pare-feu OPNsense avec CARP et pfsync

- **Environnement** : Deux appliances OPNsense, idéalement matériel et chemins réseau redondés

## 1. Préparer le basculement

Fiche simple : [préparer le basculement](/01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/carp-pfsync-ha/fiche-simple-appliance-opnsense-carp-pfsync-preparer-basculement).

Attribuer à chaque appliance une IP propre sur chaque interface, puis une VIP CARP distincte. Prévoir un réseau dédié pour pfsync et un réseau de synchronisation de configuration. Vérifier que les commutateurs autorisent les adresses MAC virtuelles CARP et que les deux appliances utilisent une version compatible.

Exporter et chiffrer les configurations actuelles. Conserver un accès console local aux deux appliances : une erreur de VIP ou de règle peut couper l'administration.

## 2. Configurer les interfaces et la synchronisation

Fiche simple : [configurer les interfaces et la synchronisation](/01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/carp-pfsync-ha/fiche-simple-appliance-opnsense-carp-pfsync-configurer-interfaces-synchronisation).

Dans l'interface Web OPNsense, configurer les IP fixes et les rôles d'interface sur les deux équipements. Sur le nœud principal, activer la synchronisation de configuration vers l'adresse de l'interface dédiée du secondaire et sélectionner uniquement les composants à synchroniser. Définir un compte de synchronisation dédié, protégé par secret.

Configurer pfsync sur l'interface privée dédiée. Ne pas utiliser le réseau WAN/public pour transporter la synchronisation d'état.

## 3. Créer les VIP CARP

Fiche simple : [créer les VIP CARP](/01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/carp-pfsync-ha/fiche-simple-appliance-opnsense-carp-pfsync-creer-vip-carp).

Créer les VIP sur les deux pare-feu avec le même VHID, le même réseau et le même mot de passe CARP, mais des adresses individuelles distinctes. Configurer le nœud principal en MASTER et le secondaire en BACKUP avec des priorités cohérentes. Définir le comportement de préemption selon le scénario de retour au primaire.

Ne pas copier une VIP d'exemple dans le réseau réel : vérifier l'adresse, le masque, l'interface et l'absence de conflit avant activation.

## 4. Tester

Fiche simple : [tester le basculement](/01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/carp-pfsync-ha/fiche-simple-appliance-opnsense-carp-pfsync-tester-basculement).

- Vérifier l'état CARP des deux nœuds dans **Status > CARP**.
- Confirmer que les états de sessions sont synchronisés.
- Depuis un client de test, couper proprement le nœud actif et mesurer le basculement.
- Restaurer le nœud et observer le comportement de préemption.
- Vérifier que DHCP, DNS, VPN, NAT et règles nécessaires restent fonctionnels.

## 5. Exploitation et retour arrière

Fiche simple : [exploitation et retour arrière](/01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/carp-pfsync-ha/fiche-simple-appliance-opnsense-carp-pfsync-exploitation-retour-arriere).

Documenter quel nœud est maître, les adresses, les règles synchronisées et la procédure de changement manuel. Si CARP oscille ou si des conflits d'IP apparaissent, isoler le nœud secondaire et rétablir la dernière configuration sauvegardée depuis la console. Les commandes de gestion de paquets Linux (`apt`, `systemctl`) ne s'appliquent pas à OPNsense ; utiliser les fonctions de mise à jour et de diagnostic de l'appliance.