# Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Importer_Images_Autorisees

- **Environnement** : VM EVE-NG (appliance basée sur Ubuntu Server 24.04 LTS) hébergée sur un poste ou serveur de virtualisation
- **OS / Version** : EVE-NG 7.x (7.2.0-18 au contrôle du 29/10/2026), Ubuntu 24.04 LTS embarqué; Community 6.2.0-4 (Ubuntu 22.04) en fin de support juin 2026
- **Catégorie** : simulation réseau / images

---

## Problème précis à résoudre

Ajouter à EVE-NG des images d'équipements que vous avez le droit d'utiliser, sans télécharger d'image propriétaire depuis ce guide.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer le droit d'usage de l'image (contrat, licence éditeur, compte autorisé) et noter son origine; ne jamais utiliser d'image provenant d'une source non officielle.
   👉 Explication : EVE-NG ne fournit pas d'images éditeur; l'obtention reste de votre responsabilité.

2. Identifier le dossier attendu dans la table officielle **QEMU image naming** et la fiche **How-To** de l'éditeur concerné (remplacer `PREFIXE_TABLE-VERSION` par le nom de dossier exact, par exemple le préfixe indiqué par la table suivi de la version).
   👉 Explication : les noms de dossier QEMU sont sensibles : le préfixe doit correspondre à la table, ce qui suit le `-` est libre.

3. Dans WinSCP (Windows) ou FileZilla (Linux/macOS), ouvrir une session **SFTP**, hôte `IP_EVE`, port `22`, utilisateur `root`, mot de passe `MOT_DE_PASSE_ROOT_EVE`.
   👉 Explication : la doc officielle recommande WinSCP ou FileZilla en SSH/SFTP (port 22); les valeurs en majuscules sont à remplacer.

4. Créer le dossier cible côté EVE-NG et y envoyer l'image : `/opt/unetlab/addons/qemu/PREFIXE_TABLE-VERSION/` avec un disque nommé selon le format attendu, par exemple `hda.qcow2` ou `virtioa.qcow2`. Pour les images IOL ou Dynamips, utiliser `/opt/unetlab/addons/iol/bin/` ou `/opt/unetlab/addons/dynamips/`.
   👉 Explication : emplacements cités par le cookbook; le nom exact du disque dépend du template (voir la fiche How-To de l'image).

5. Corriger les permissions depuis la CLI d'EVE-NG :
   ```bash
   /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
   ```
   👉 Explication : commande de réparation des droits mentionnée par la documentation EVE-NG (page de sauvegarde et fiches How-To); ⚠️ vérifier dans la fiche How-To de l'image si une conversion ou une autre étape est requise avant.

6. Dans l'interface web : ouvrir un lab, **Add an object > Node**, filtrer le modèle voulu et vérifier que le nom de l'image est affiché en bleu.
   👉 Explication : un nom en gris signifie qu'aucune image n'est détectée dans le bon dossier.

## 2. Production — Contrôles

- Conserver la preuve de licence ou le contrat associé à chaque image.
- Vérifier l'espace disque (`df -h`) avant un transfert volumineux.
- Tester une seule image à la fois pour isoler une éventuelle erreur de nommage.

## 3. Production — Sécurité

- Ne pas déposer d'images éditeur sur un partage public ni dans un dépôt Git.
- Utiliser SFTP (port 22), pas FTP en clair, pour le transfert.
- Limiter l'accès SSH de l'hôte EVE-NG au poste d'administration; ne pas enregistrer le mot de passe root dans WinSCP ou FileZilla sur un poste partagé.

## Validation et retour arrière

- **Validation** : le modèle apparaît en bleu dans **Add an object > Node** et le nœud démarre dans un lab de test.
- **Retour arrière** : supprimer uniquement le dossier de l'image ajoutée `/opt/unetlab/addons/qemu/PREFIXE_TABLE-VERSION/` (vérifier le chemin avant), puis relancer la commande `fixpermissions`.

## Si le problème n'est pas résolu

- [EVE-NG — noms de dossiers d'images QEMU](https://www.eve-ng.net/index.php/documentation/qemu-image-namings/)
- [EVE-NG — How-To par éditeur](https://www.eve-ng.net/index.php/documentation/howtos/)
- [EVE-NG — images supportées](https://www.eve-ng.net/index.php/documentation/supported-images/)
- [EVE-NG — Professional Cookbook (PDF, chapitre 18)](https://www.eve-ng.net/wp-content/uploads/2026/09/EVE-PE-BOOK-7.9-2026.pdf)
[EVE-NG — documentation officielle](https://www.eve-ng.net/index.php/documentation/)
- [Fiche logiciel EVE-NG](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-eve-ng)
- [Créer et valider un lab](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-creer-valider-lab)