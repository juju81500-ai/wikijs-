# Réparation : un serveur Linux ne résout plus les noms DNS

- **Périmètre** : Debian, Ubuntu et distributions avec `systemd-resolved`

## Symptômes

Les connexions par adresse IP fonctionnent, mais les noms de domaine échouent, ou bien les applications signalent des erreurs de résolution.

## 1. Diagnostiquer sans modifier

```bash
ip route
resolvectl status
getent ahosts deb.debian.org
resolvectl query deb.debian.org
```

- Si la passerelle n'est pas joignable, corriger d'abord l'adresse ou la route réseau.
- Si `resolvectl status` n'affiche aucun DNS pour le lien actif, vérifier le gestionnaire qui possède la configuration (Netplan, NetworkManager, DHCP ou systemd-networkd).
- Comparer avec un autre poste du même réseau et vérifier que le serveur DNS choisi est autorisé par la politique locale.

## 2. Vérifier la configuration propriétaire

```bash
ls -l /etc/resolv.conf
networkctl status
```

Ne pas remplacer `/etc/resolv.conf` à l'aveugle : il peut s'agir d'un lien géré par `systemd-resolved` ou par un autre service. Modifier la configuration persistante dans son outil propriétaire, en utilisant le DNS interne prévu par l'organisation.

Après correction, renouveler la configuration du lien ou redémarrer uniquement le service réseau concerné, depuis une console si l'accès est distant.

## 3. Vérifier et revenir en arrière

```bash
resolvectl flush-caches
resolvectl query deb.debian.org
getent ahosts deb.debian.org
```

Si le problème commence après la modification, restaurer la sauvegarde du fichier Netplan ou de la configuration réseau, puis réappliquer depuis la console. Ne pas publier de DNS public comme contournement sans validation de la politique réseau.