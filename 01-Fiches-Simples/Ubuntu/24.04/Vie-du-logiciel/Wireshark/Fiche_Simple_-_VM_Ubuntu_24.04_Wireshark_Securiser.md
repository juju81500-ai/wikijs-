# Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Securiser

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Wireshark
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / sécurisation
- **Tags** : `wireshark`, `ubuntu24.04`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Réduire les risques liés aux privilèges, aux dissecteurs et aux captures Wireshark.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les droits de dumpcap :
   ```bash
   ls -l "$(command -v dumpcap)"
   getcap "$(command -v dumpcap)"
   getent group wireshark
   ```
   👉 Explication : Seuls root et le groupe `wireshark` doivent exécuter dumpcap; vérifier les membres.

2. Restreindre les captures :
   ```bash
   install -d -m 0700 ~/captures
   chmod 0600 ~/captures/*.pcapng
   ```
   👉 Explication : Les captures peuvent contenir des mots de passe en clair; accès limité au propriétaire.

3. Ne pas conserver de clés TLS :
   ```bash
   ls -l ~/.config/wireshark 2>/dev/null
   ```
   👉 Explication : Un fichier de clés de session TLS (keylog) permet de déchiffrer les captures; ne le stocker que le temps de l’analyse autorisée, avec droits 0600.

4. Éviter les captures distantes non maîtrisées.
   👉 Explication : N’utiliser extcap/SSH que sur des équipements autorisés et avec clés individuelles; ne pas saisir de mot de passe dans un script.

## 2. Production — Contrôles

Revue périodique des membres du groupe et des fichiers de capture.

## 3. Production — Sécurité

- Mettre à jour Wireshark régulièrement (dissecteurs exposés à des données hostiles).
- Chiffrer les captures transférées.
- AppArmor : un profil peut limiter dumpcap; chercher `DENIED` dans `sudo journalctl -k`.

## Validation et retour arrière

- **Validation** : Droits conformes, aucune clé TLS résiduelle, captures en 0600.
- **Retour arrière** : Restaurer l’appartenance de groupe antérieure et les permissions consignées.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Valider.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Configurer.md)
