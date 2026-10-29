# Fiche_Simple_-_VM_Rocky_9_Suricata_Configurer

- **Environnement** : VM Rocky Linux 9 dédiée à Suricata
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / configuration IDS passif

---

## Problème précis à résoudre

Configurer Suricata en IDS passif sur l’interface autorisée et mettre à jour les règles.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration livrée :
   ```bash
   sudo cp -a /etc/suricata/suricata.yaml /etc/suricata/suricata.yaml.before-change
   ```
   👉 Explication : Permet un retour arrière.

2. Éditer les paramètres essentiels :
   ```bash
   sudoedit /etc/suricata/suricata.yaml
   ```
   👉 Explication : Régler `vars.address-groups.HOME_NET` sur HOME_NET_AUTORISE (à remplacer) et, dans `af-packet`, `interface: INTERFACE_AUTORISEE`. Laisser `eve-log` activé; ne pas configurer `nfq` ni `ips`. Sur Rocky/EPEL, le service lit `/etc/sysconfig/suricata` (variable OPTIONS, par exemple `-i INTERFACE_AUTORISEE`); la section `af-packet` de `suricata.yaml` doit rester cohérente. Contrôler `systemctl cat suricata`.

3. Mettre à jour les règles :
   ```bash
   sudo suricata-update
   sudo suricata-update list-sources | head -n 20
   ```
   👉 Explication : `suricata-update` télécharge le jeu de règles par défaut (ET Open) vers `/var/lib/suricata/rules`. Les sources et leurs conditions de licence sont à valider; ne jamais écrire de clé d’accès dans la fiche.

4. Tester la configuration :
   ```bash
   sudo suricata -T -c /etc/suricata/suricata.yaml -v
   ```
   👉 Explication : `-T` teste configuration et règles sans capturer; le test doit se terminer sans erreur.

5. Démarrer et observer :
   ```bash
   sudo systemctl enable --now suricata
   systemctl status suricata --no-pager
   sudo tail -n 30 /var/log/suricata/suricata.log
   ```
   👉 Explication : Démarre le service et contrôle que le moteur est en cours d’exécution sur la bonne interface.

## 2. Production — Contrôles

Faire relire HOME_NET, interface et sources de règles; mesurer la perte de paquets (`stats.log`).

## 3. Production — Sécurité

- Désactiver toute action de blocage.
- Journaux accessibles aux seuls comptes habilités.
- SELinux : rester en Enforcing; pour tout refus, `sudo ausearch -m avc -ts recent` puis corriger le contexte plutôt que désactiver SELinux.

## Validation et retour arrière

- **Validation** : `suricata -T` réussit, le service est actif et `suricata.log` n’indique pas d’erreur.
- **Retour arrière** : Restaurer `/etc/suricata/suricata.yaml.before-change`, relancer `sudo suricata -T -c /etc/suricata/suricata.yaml`, puis `sudo systemctl restart suricata`.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-securiser)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-installer)