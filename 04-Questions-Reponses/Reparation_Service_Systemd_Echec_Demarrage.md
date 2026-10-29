# Réparation : un service systemd échoue au démarrage

- **Périmètre** : Debian, Ubuntu et distributions utilisant systemd
- **Tags** : `reparation`, `linux`, `systemd`, `service`, `journalctl`

## 1. Collecter l'état et les journaux

Remplacer `SERVICE` par le nom exact de l'unité, par exemple `nginx.service` :

```bash
systemctl --no-pager --full status SERVICE
systemctl cat SERVICE
journalctl -u SERVICE -b --no-pager -n 100
systemctl --failed
```

Noter le premier message d'erreur, l'heure et les changements récents. Ne pas commencer par supprimer des fichiers PID, vider les journaux ou réinstaller le paquet.

## 2. Vérifier les dépendances courantes

```bash
systemctl list-dependencies SERVICE
df -h
df -i
ss -lntp
```

Vérifier l'espace, les permissions et la disponibilité du port seulement si les journaux les désignent. Pour une erreur de syntaxe, utiliser le validateur propre au logiciel (par exemple `nginx -t`), pas un redémarrage répété.

## 3. Corriger, tester et relancer

Sauvegarder le fichier modifié, corriger uniquement le paramètre fautif, puis exécuter le validateur du service. Redémarrer une seule fois :

```bash
sudo systemctl reset-failed SERVICE
sudo systemctl restart SERVICE
systemctl --no-pager --full status SERVICE
journalctl -u SERVICE --since '-5 minutes' --no-pager
```

`reset-failed` efface l'état d'échec, mais ne corrige pas la cause. Si le service ne revient pas, restaurer le fichier précédent et suivre le message d'erreur plutôt que de multiplier les redémarrages.