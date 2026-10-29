# Fiche_Simple_-_VM_Debian_13_OpenVPN_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 dédiée à OpenVPN Community Edition
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : OpenVPN Community Edition / sauvegarder / restaurer
- **Tags** : `openvpn`, `debian13`, `vie-du-logiciel`, `sauvegarder_restaurer`

---

## Problème précis à résoudre

Sauvegarder la configuration et les artefacts nécessaires au rétablissement sans exposer les clés privées.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive protégée de la configuration :
   ```bash
   sudo tar --acls --xattrs -czf /root/openvpn-server-$(date +%F).tar.gz /etc/openvpn/server
   sudo chmod 600 /root/openvpn-server-$(date +%F).tar.gz
   sudo sha256sum /root/openvpn-server-$(date +%F).tar.gz
   ```
   👉 Explication : L’archive contient des clés privées; transférer chiffrée vers un dépôt approuvé et consigner son empreinte séparément.

2. Vérifier que CA hors ligne, inventaire de certificats et procédure de révocation sont sauvegardés séparément.
   👉 Explication : Ne pas regrouper les clés privées clients avec la configuration serveur.

3. Tester une restauration dans une VM isolée, sans connexion au réseau de production.
   👉 Explication : Contrôler démarrage, permissions et révocation avant de déclarer la sauvegarde exploitable.

## 2. Production — Contrôles

Définir RPO/RTO, chiffrement, accès nominatif au dépôt, rétention, vérification d’intégrité et responsable de test.

## 3. Production — Sécurité

- Ne pas déposer l’archive dans un partage non chiffré ou un ticket; préserver propriétaires et modes de fichiers.

## Validation et retour arrière

- **Validation** : Empreinte vérifiée et restauration répétée en environnement isolé.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [OpenVPN Community Edition — documentation officielle](https://openvpn.net/community-resources/)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_OpenVPN_Mise_A_Jour_Retour_Arriere.md)
