# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Limiter ce qui peut s'exécuter sur certains volumes.

## 1. Hors-Production (Lab / Test / POC)

1. Relire `/etc/fstab` et les options montées :
   ```sh
   cat /etc/fstab
   mount | grep -E ' /tmp | /var '
   ```
   👉 Explication : repère les volumes sans restrictions.

2. Monter `/tmp` en mémoire avec `nodev,nosuid,noexec` :
   ```sh
   doas sh -c 'cat >> /etc/fstab <<EOF
   tmpfs /tmp tmpfs nodev,nosuid,noexec,size=256m 0 0
   EOF'
   doas mount -a
   mount | grep ' /tmp '
   ```
   👉 Explication : empêche l'exécution de binaires déposés dans `/tmp`.

3. Contrôler les fichiers setuid :
   ```sh
   find / -xdev -perm -4000 -type f 2>/dev/null
   ```
   👉 Explication : liste les binaires qui s'exécutent avec les droits de leur propriétaire.

## 2. Production — Contrôles

Tester les services avant et après (un service qui exécute depuis `/tmp` échouera).

## 3. Production — Sécurité

Sauvegarder `/etc/fstab` avant modification.

## Validation et retour arrière

- **Validation** : `/tmp` apparaît avec `noexec,nosuid,nodev`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
