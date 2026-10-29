# Fiche_Simple_-_VM_Rocky_9_OpenVPN_Sauvegarder_Restaurer

- **Environnement** : VM Rocky Linux 9 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Rocky Linux 9; paquets openvpn et easy-rsa issus d'EPEL, version à vérifier
- **Catégorie** : OpenVPN Community Edition / sauvegarder / restaurer
- **Tags** : `openvpn`, `rocky9`, `vie-du-logiciel`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration du serveur sans exposer les clés.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive protégée de la configuration :
   ```bash
   sudo install -d -m 0700 /var/backups/openvpn
   sudo tar czf /var/backups/openvpn/openvpn-$(date +%F).tar.gz -C / etc/openvpn
   sudo chmod 600 /var/backups/openvpn/*.tar.gz
   ```
   👉 Explication : L'archive contient la clé serveur et tls-crypt : la stocker chiffrée, hors de la VM, avec accès restreint.

2. Restaurer sur un hôte de test :
   ```bash
   sudo tar xzf /var/backups/openvpn/openvpn-DATE.tar.gz -C /
   sudo systemctl restart openvpn-server@server
   ```
   👉 Explication : DATE est la date de l'archive à restaurer (à remplacer).

3. Sauvegarder séparément la PKI :
   👉 Explication : La PKI (CA hors ligne, base d'émission) est sauvegardée par la procédure de la CA, jamais dans cette archive.

## 2. Production — Contrôles

Tester la restauration périodiquement et consigner l'emplacement de stockage.

## 3. Production — Sécurité

- Chiffrer l'archive avant transfert; ne jamais l'envoyer par messagerie.

## Validation et retour arrière

- **Validation** : Un serveur restauré sur hôte de test accepte le client pilote.
- **Retour arrière** : Revenir à l'état précédent la restauration via le snapshot de la VM.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_OpenVPN_Mise_A_Jour_Retour_Arriere.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_OpenVPN.md)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)
