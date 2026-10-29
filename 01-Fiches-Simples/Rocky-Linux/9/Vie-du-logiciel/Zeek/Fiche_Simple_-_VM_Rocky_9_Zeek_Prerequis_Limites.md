# Fiche_Simple_-_VM_Rocky_9_Zeek_Prerequis_Limites

- **Environnement** : VM Rocky Linux 9 dédiée à Zeek
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / prérequis et limites
- **Tags** : `zeek`, `rocky9`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer un capteur Zeek passif (journaux de métadonnées réseau) sur VM Rocky Linux 9 dans un périmètre autorisé.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l’autorisation d’analyse (propriétaire, interface INTERFACE_AUTORISEE, réseaux LOCAL_NET_AUTORISE, rétention des logs).
   👉 Explication : Zeek enregistre des métadonnées de connexions, DNS, HTTP, TLS; elles sont sensibles. Les valeurs en majuscules sont des placeholders à remplacer.

2. Contrôler les ressources :
   ```bash
   cat /etc/os-release
   nproc
   free -h
   ip -br link
   df -h /opt /var
   ```
   👉 Explication : Zeek est gourmand en CPU/RAM et disque selon le débit; prévoir une interface de capture dédiée.

3. Choisir le mode d’installation.
   👉 Explication : Rocky 9 : le dépôt OBS de Zeek ne propose pas de répertoire RHEL/Rocky dans sa liste actuelle (vérifier avant de commencer). Cette série utilise l’image conteneur officielle `zeek/zeek` avec Podman; la compilation depuis les sources reste l’alternative (documentation officielle).

4. Noter les limites.
   👉 Explication : Mode traité : capteur standalone passif. Les clusters, la haute disponibilité et tout blocage ne sont pas couverts. Zeek ne déchiffre pas TLS. SELinux : rester en Enforcing; en cas de refus, `sudo ausearch -m avc -ts recent`.

## 2. Production — Contrôles

Faire valider architecture (SPAN/TAP), volumétrie et propriétaire des journaux.

## 3. Production — Sécurité

- Capture passive uniquement.
- Interface de capture sans IP de service si possible.

## Validation et retour arrière

- **Validation** : Autorisation tracée, mode d’installation choisi, limites comprises.
- **Retour arrière** : Aucun changement système à annuler.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Zeek.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Zeek_Installer.md)
