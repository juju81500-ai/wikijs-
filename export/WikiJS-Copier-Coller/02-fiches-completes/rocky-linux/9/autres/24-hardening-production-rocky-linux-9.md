# Hardening d'un serveur Rocky Linux 9 avant production

- **Type de fiche** : Autres — sécurité / exploitation
- **Environnement** : VM ou serveur dédié Rocky Linux
- **OS / Version** : Rocky Linux 9 / famille RHEL 9
- **Rôle** : Appliquer une base de sécurité et vérifier l'état avant ouverture du service

## 1. Périmètre et accès de secours

Fiche simple : [périmètre et accès de secours](/01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/securite/fiche-simple-vm-rocky-9-securite-hardening-perimetre-acces-secours).

Cette fiche prépare un serveur installé; elle ne remplace pas l'installation ni le hardening spécifique d'un rôle applicatif.

- Confirmer le rôle, l'adresse/zone réseau, les ports entrants nécessaires, les utilisateurs et le responsable.
- Garder la console hyperviseur et un compte de secours testé.
- Sauvegarder la configuration et planifier une fenêtre avant toute modification SSH ou firewall.

## 2. Mettre à jour et inventorier

Fiche simple : [mettre à jour et inventorier](/01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/securite/fiche-simple-vm-rocky-9-securite-hardening-mises-a-jour-inventaire).

```bash
cat /etc/rocky-release
sudo dnf check-update
sudo dnf update --security
sudo dnf history list
systemctl --failed
```

Examiner les changements proposés avant confirmation. Après une mise à jour noyau/libc, planifier puis effectuer un redémarrage contrôlé.

## 3. Limiter les comptes et l'accès SSH

Fiche simple : [limiter les comptes et l'accès SSH](/01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/securite/fiche-simple-vm-rocky-9-securite-hardening-comptes-ssh).

Créer un compte nominatif, l'ajouter à `wheel` selon la politique, installer une clé publique approuvée puis tester une seconde connexion avant de réduire l'accès mot de passe.

```bash
id <compte_admin>
sudo -l -U <compte_admin>
sudo sshd -t
sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication|pubkeyauthentication'
```

Gérer les réglages dans un fichier SSH documenté, ne pas ajouter de directives en double, puis recharger `sshd` seulement après `sshd -t`. Ne pas exposer SSH à tout Internet.

## 4. Conserver SELinux en application

Fiche simple : [conserver SELinux en application](/01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/securite/fiche-simple-vm-rocky-9-securite-hardening-selinux-enforcing).

```bash
getenforce
sestatus
sudo ausearch -m AVC -ts recent
```

Maintenir `Enforcing`. Pour un refus, examiner l'événement AVC et corriger le contexte ou la politique minimale; ne pas basculer le système en permissif ni générer automatiquement une règle large.

## 5. Limiter les flux firewalld

Fiche simple : [limiter les flux firewalld](/01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/securite/fiche-simple-vm-rocky-9-securite-hardening-flux-firewalld).

Repérer l'interface et sa zone avant de changer une règle :

```bash
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --zone=<ZONE_ACTIVE> --list-all
sudo ss -lntup
```

Ouvrir uniquement les services requis dans la zone réelle, vérifier la syntaxe, recharger puis tester depuis le client prévu. Garder une source d'administration explicitement autorisée et une console en secours.

## 6. Exploitation et journaux

Fiche simple : [exploitation et journaux](/01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/securite/fiche-simple-vm-rocky-9-securite-hardening-exploitation-journaux).

- Activer une synchronisation horaire Chrony approuvée et surveiller les écarts.
- Vérifier journaux systemd, espace disque, sauvegardes, supervision et services activés au démarrage.
- Supprimer les paquets et comptes de test seulement après inventaire de leurs dépendances.
- Documenter les exceptions et leur date de revue.

## 7. Recette et retour arrière

Fiche simple : [recette et retour arrière](/01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/securite/fiche-simple-vm-rocky-9-securite-hardening-recette-retour).

Tester administration, application, ports attendus, refus depuis une source non autorisée, SELinux, redémarrage et restauration d'une sauvegarde en VM isolée.

En cas de perte d'accès, corriger la dernière règle ou configuration depuis la console et restaurer le fichier sauvegardé. Ne jamais désactiver globalement le pare-feu ou SELinux pour rétablir un service.

## Sources

- [Rocky Linux — Documentation](https://docs.rockylinux.org/)
- [Red Hat — Utilisation et configuration de SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
- [Red Hat — Sécurisation des réseaux avec firewalld](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_firewalls_and_packet_filters/)