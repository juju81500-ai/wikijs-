# 📄 cURL

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : cURL 7.88.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Scripting, développement et administration

## 🎯 Problème précis à résoudre
Installer cURL sur Debian 12, vérifier qu'un service web interne répond et que son certificat est valide, tester une API avec un jeton lu depuis un fichier protégé, puis appliquer des options TLS et de sécurité strictes pour les scripts de production. Les tests ne ciblent que vos propres services.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation et contrôle de la version :
```bash
sudo apt update
sudo apt install -y curl
curl --version
```
👉 Explication : Installe cURL depuis les dépôts Debian 12. `curl --version` affiche la version et les protocoles compilés (HTTPS, HTTP/2, etc.).

2. Test de réponse d'un service web du lab :
```bash
curl -sS -o /dev/null -w "%{http_code}\n" https://wiki.lab.local/
```
👉 Explication : Affiche uniquement le code HTTP reçu (`200` attendu). `-sS` masque la barre de progression mais affiche les erreurs. Une erreur `SSL certificate problem` indique un certificat non reconnu par la machine.

3. Affichage détaillé de la négociation TLS et de l'en-tête :
```bash
curl -v -I https://wiki.lab.local/ 2>&1 | head -n 30
```
👉 Explication : `-I` ne demande que les en-têtes. L'option `-v` montre la version TLS négociée et le certificat présenté (émetteur, nom, dates de validité).

4. Test d'une API avec un jeton lu depuis un fichier :
```bash
curl -sS -H "Accept: application/json" -H @/home/julien/.config/curl/entete_api.txt https://wiki.lab.local/api/health
```
👉 Explication : `-H @fichier` lit les en-têtes depuis un fichier, ce qui évite de laisser un jeton dans l'historique de la commande. Le fichier contient une ligne `Authorization: Bearer <jeton_de_lab>`. Ce jeton ne doit être utilisé qu'en lab.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un fichier de configuration cURL pour les options communes :
```bash
nano ~/.curlrc
```
Contenu à saisir :
```
proto = "=https"
tlsv1.2
fail
silent
show-error
```
👉 Explication : cURL lit automatiquement `~/.curlrc` à chaque appel. Ces options imposent HTTPS uniquement (`proto = "=https"`), TLS 1.2 minimum, un code d'erreur HTTP en cas d'échec (`fail`) et des messages d'erreur lisibles.

2. Vérification que le certificat du service est signé par l'autorité interne :
```bash
curl --cacert /etc/ssl/certs/ca-certificates.crt -sS -o /dev/null -w "%{http_code}\n" https://wiki.lab.local/
```
👉 Explication : Indique explicitement le magasin de certificats à utiliser. Si l'autorité interne n'est pas dans ce fichier, la commande échoue au lieu de passer outre.

3. Test de l'échéance du certificat :
```bash
echo | openssl s_client -connect wiki.lab.local:443 -servername wiki.lab.local 2>/dev/null | openssl x509 -noout -enddate
```
👉 Explication : Affiche la date de fin de validité du certificat présenté (`notAfter=`). Utile pour anticiper un renouvellement.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Identifiants dans un fichier netrc protégé, jamais en ligne de commande :
```bash
sudo install -o root -g root -m 600 /dev/null /root/.curl-netrc
sudo nano /root/.curl-netrc
sudo ls -l /root/.curl-netrc
```
Contenu à saisir :
```
machine api.entreprise.lab
login svc_supervision
password <mot_de_passe_du_compte_de_service>
```
👉 Explication : Le fichier n'est lisible que par root (`-rw-------`). Il est utilisé avec `--netrc-file`, ce qui évite que le mot de passe apparaisse dans `ps` ou dans l'historique du shell. Le mot de passe réel vient du coffre-fort de l'entreprise.

2. Appel sécurisé d'une API avec ce fichier :
```bash
sudo curl --netrc-file /root/.curl-netrc --proto '=https' --tlsv1.2 --cacert /etc/ssl/certs/ca-certificates.crt -sS --fail https://api.entreprise.lab/status
```
👉 Explication : Authentification lue dans le fichier, HTTPS obligatoire, TLS 1.2 minimum, vérification du certificat avec l'autorité interne et échec sur code HTTP d'erreur. Le code de retour de cURL reste exploitable par un script.

3. Contrôle des droits des fichiers de configuration :
```bash
ls -l ~/.curlrc
find ~ -maxdepth 1 -name ".curlrc" -perm /077 -print
```
👉 Explication : La seconde commande ne doit rien afficher : aucun fichier de configuration cURL ne doit être lisible par d'autres comptes. Corriger avec `chmod 600` si besoin.

4. Journalisation de l'appel sans fuite de secrets :
```bash
sudo curl --netrc-file /root/.curl-netrc --proto '=https' --tlsv1.2 -sS --fail -o /dev/null -w "%{http_code} %{time_total}s\n" https://api.entreprise.lab/status | sudo tee -a /var/log/curl_supervision.log
```
👉 Explication : Enregistre seulement le code HTTP et la durée de réponse. L'option `-v` n'est pas utilisée en production car elle peut afficher des en-têtes d'authentification.

---

**Point à vérifier** : le chemin du magasin de certificats `/etc/ssl/certs/ca-certificates.crt` est celui de Debian 12 ; le nom de domaine `api.entreprise.lab` et le point d'API `/status` sont à remplacer par ceux du service réel, et doivent être confirmés avant usage.