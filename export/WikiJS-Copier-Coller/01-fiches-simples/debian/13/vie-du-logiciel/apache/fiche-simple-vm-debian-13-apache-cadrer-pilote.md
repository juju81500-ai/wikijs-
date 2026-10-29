# Fiche_Simple_-_VM_Debian_13_Apache_Cadrer_Pilote.md

- **Environnement** : VM Debian 13 Trixie dédiée, test Apache statique sans données métier
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : serveur Web / cadrage

---

## Problème précis à résoudre

Vérifier que le serveur, le nom DNS, le certificat, les règles réseau et le plan de retour arrière sont prêts avant d'installer ou publier Apache.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le système et l'état des ports :
   ```bash
   grep PRETTY_NAME /etc/os-release
   sudo ss -ltnp | grep -E ':(80|443)\b' || echo "ports 80/443 libres"
   ```
   👉 Explication : la VM doit être dédiée et les ports libres.

2. Vérifier le DNS du nom choisi :
   ```bash
   getent hosts www.example.net
   ```
   👉 Explication : remplacer par le FQDN validé; il doit pointer vers la VM.

3. Vérifier la présence du certificat et de la clé fournis par l'organisation :
   ```bash
   sudo ls -l /etc/ssl/certs/www.example.net.crt /etc/ssl/private/www.example.net.key
   sudo openssl x509 -in /etc/ssl/certs/www.example.net.crt -noout -subject -enddate
   ```
   👉 Explication : le périmètre est un site statique; ni application, ni base, ni proxy, ni ACME, ni WAF.

## 2. Production — Contrôles

Pour la production, identifier l'application et son propriétaire, la capacité attendue, les engagements de disponibilité, la supervision, le responsable des certificats, les journaux, les sauvegardes et la fenêtre de mise à jour. Cette fiche ne vaut pas approbation de publication.

## 3. Production — Sécurité

- Ne pas utiliser de données métier ou personnelles dans le site pilote.
- Ne pas copier de clé privée dans le wiki, un dépôt, un ticket ou une capture.
- Ne pas publier de port avant validation du DNS, TLS, filtrage réseau et contrôle d'accès.
- Garder une sauvegarde de la VM et un état de référence de la configuration existante.

## Validation et retour arrière

- **Validation** : périmètre, propriétaire, FQDN, certificat, accès réseau et critères d'arrêt sont documentés.
- **Retour arrière** : ne pas installer si les dépendances, l'approbation ou la restauration ne sont pas définies.

## Si le problème n'est pas résolu

- [Apache HTTP Server — documentation officielle](https://httpd.apache.org/docs/2.4/)
- [Guide complet Apache Debian 13](/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13#1-perimetre-et-prerequis)