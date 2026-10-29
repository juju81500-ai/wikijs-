# Déployer FreeIPA (Identity Management) sur Rocky Linux 9

- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution (version non figée, à relever sur l'hôte)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : premier serveur FreeIPA/IdM avec CA intégrée et DNS intégré optionnel, sauvegarde `ipa-backup`
- **Catégorie** : annuaire / identité / Kerberos

## 1. Périmètre et statut de support

Fiche simple : [cadrer le périmètre FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-cadrer-perimetre).

FreeIPA fournit LDAP (389 Directory Server), Kerberos, une CA et, en option, DNS. Le projet FreeIPA indique supporter Fedora et Red Hat Enterprise Linux; la procédure détaillée la plus précise est la documentation RHEL 9 « Installing Identity Management ». Rocky Linux 9 est compatible RHEL, mais cette compatibilité est une hypothèse à valider en laboratoire : aucune procédure Rocky dédiée n'a été trouvée dans une source officielle. Ce guide n'a pas été testé sur Rocky Linux 9.

Ne pas installer FreeIPA sur un serveur qui héberge déjà un autre service d'annuaire, DNS, serveur web ou CA. Réplicas, relation de confiance AD (`ipa-server-trust-ad`), CA externe et migration depuis OpenLDAP/NIS ne sont pas couverts; pour un simple annuaire LDAP, voir le [guide OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13).

## 2. Prérequis à valider avant l'installation

Fiche simple : [valider les prérequis FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-prerequis).

- VM dédiée, snapshot avant installation. Pour un petit déploiement, la documentation RHEL 9 dimensionne la RAM selon la volumétrie (10 000 utilisateurs : au moins 4 Go de RAM et 4 Go de swap); le démarrage rapide FreeIPA donne un minimum absolu de 1,2 Go avec CA et 2 Go pour un test. Réserver la RAM (pas de ballooning).
- Nom d'hôte FQDN statique, jamais `localhost`; il doit se résoudre en l'IP du serveur et la résolution inverse doit correspondre. Dans `/etc/hosts`, le FQDN vient en premier. Utiliser un domaine que l'organisation possède, pas `example.com`.
- Heure synchronisée (chrony) : Kerberos échoue en cas de dérive.
- Pare-feu : ports 80/tcp, 443/tcp, 389/tcp, 636/tcp, 88/tcp+udp, 464/tcp+udp et, avec DNS intégré, 53/tcp+udp.
- Considérer le domaine, le realm Kerberos et le FQDN du serveur comme définitifs : les arrêter par écrit avant de continuer.

## 3. Installer

Fiche simple : [installer FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-installer).

```bash
hostnamectl status
sudo dnf install ipa-server            # sans DNS intégré
# sudo dnf install ipa-server ipa-server-dns   # avec DNS intégré
sudo firewall-cmd --permanent --add-service=freeipa-4
sudo firewall-cmd --reload
```

Ajouter `--add-service=dns` seulement si le DNS intégré est retenu. Lancer ensuite l'assistant interactif (il demande realm, mot de passe Directory Manager et mot de passe `admin`) :

```bash
sudo ipa-server-install
```

Le journal est `/var/log/ipaserver-install.log`. Le mode non interactif place les mots de passe dans la ligne de commande (visible dans l'historique et la liste des processus) : ne pas l'utiliser en production. Si le DNS intégré est activé, l'option `--no-dnssec-validation` n'est à ajouter que si DNSSEC n'est pas requis, comme l'indique la documentation Red Hat. Avec un DNS externe, l'installeur génère `/tmp/ipa.system.records.*.db` : publier ces enregistrements dans la zone existante.

## 4. Premières actions

Fiche simple : [premières actions FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-premieres-actions).

```bash
kinit admin
ipa user-add --first=Test --last=Lab testlab
ipa user-find testlab
sudo dnf install ipa-healthcheck && sudo ipa-healthcheck
```

Remplacer ces essais par la politique de comptes, groupes, règles HBAC et sudo de l'organisation. Utiliser le compte `admin` seulement pour l'administration, le compte Directory Manager pour des opérations bas niveau rares.

## 5. Sauvegarder

Fiche simple : [sauvegarder FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-sauvegarder).

`ipa-backup` s'exécute en root. Par défaut il fonctionne hors ligne et arrête les services IdM; la sauvegarde est écrite sous `/var/lib/ipa/backup/`. La sauvegarde d'un serveur doit contenir tous les rôles du cluster (CA, DNS, KRA). Planifier une fenêtre de maintenance :

```bash
sudo ipa-backup
sudo ls -l /var/lib/ipa/backup/
```

Copier ensuite le répertoire de sauvegarde, chiffré, hors de l'hôte. Il contient des clés et condensats : le protéger comme un secret. `--disable-role-check` produit une sauvegarde insuffisante pour une restauration complète : ne pas l'utiliser pour le PRA.

## 6. Restaurer

Fiche simple : [restaurer FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-restaurer).

`ipa-restore` remplace les données et la configuration de l'hôte; ce n'est pas un test sans risque. Répéter la restauration sur une VM isolée de même nom d'hôte et même version de paquets, sans accès au DNS ni aux clients de production, en suivant « Preparing for disaster recovery with Identity Management » de la documentation RHEL 9. Ne jamais restaurer sur le serveur de production tant que le test n'a pas réussi.

## 7. Validation

Fiche simple : [valider FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-valider).

- `kinit admin` obtient un ticket; `klist` le montre.
- `ipa user-find`, `ipa host-find` répondent; l'interface web `https://FQDN/ipa/ui/` est accessible depuis un poste autorisé.
- `systemctl status ipa` (ou `ipactl status`) montre tous les services démarrés.
- Un client de test rejoint le domaine avec `ipa-client-install` après l'installation du paquet `ipa-client`, sans toucher aux postes de production.
- Une sauvegarde `ipa-backup` existe et sa restauration a été jouée sur une VM isolée.

## 8. Retour arrière

Fiche simple : [retour arrière FreeIPA](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/freeipa/fiche-simple-vm-rocky-9-freeipa-retour-arriere).

Avant l'installation : snapshot de la VM. Après un échec d'installation : `sudo ipa-server-install --uninstall`, corriger la cause (DNS, nom d'hôte, heure), puis recommencer; cette commande supprime la configuration IdM locale et ne doit être utilisée que sur un serveur non mis en production ou après sauvegarde. Après mise en production : restaurer le snapshot ou la sauvegarde sur une VM isolée, puis basculer les clients; ne pas désinstaller le seul serveur IdM d'un domaine utilisé.

## Sources

- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Red Hat — RHEL 9, Preparing for disaster recovery with Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/preparing_for_disaster_recovery_with_identity_management/index)
- [Rocky Linux — documentation](https://docs.rockylinux.org/)

L'installation sur Rocky Linux 9, les options de DNS intégré, la sauvegarde et la restauration n'ont pas été testées. Conserver les statuts **À revoir** et **À tester** jusqu'à validation sur une VM pilote.