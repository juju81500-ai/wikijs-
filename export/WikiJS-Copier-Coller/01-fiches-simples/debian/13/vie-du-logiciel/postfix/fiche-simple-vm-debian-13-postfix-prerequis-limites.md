# Fiche_Simple_-_VM_Debian_13_Postfix_Prerequis_Limites

- **Environnement** : VM Debian 13; Postfix depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Postfix — Prérequis et limites

---

## Problème précis à résoudre

Vérifier qu'une VM Debian 13 peut héberger un serveur SMTP Postfix avant toute installation, et connaître les limites (relais ouvert, port 25 filtré, réputation d'IP).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version de l'OS et le nom d'hôte :
   ```bash
   cat /etc/os-release | head -3
   hostnamectl --static
   ```
   👉 Explication : un nom pleinement qualifié (FQDN, ex. `MAIL.EXAMPLE.NET`, à remplacer) est indispensable : il sert d'identité SMTP (HELO).

2. Vérifier la version de Postfix proposée par les dépôts Debian 13 :
   ```bash
   apt-cache policy postfix
   ```
   👉 Explication : relever la version candidate (famille 3.10 attendue, à vérifier sur la version publiée) pour la noter dans le dossier d'exploitation.

3. Contrôler que les ports 25/587 sont libres :
   ```bash
   sudo ss -tlnp | grep -E ':(25|587)\b' || echo "ports libres"
   ```
   👉 Explication : aucun autre MTA (exim4 est souvent préinstallé) ne doit écouter. S'il existe, le désinstaller ou le désactiver avant l'installation.

4. Contrôler les enregistrements DNS du domaine (remplacer `EXAMPLE.NET`) :
   ```bash
   dig +short MX EXAMPLE.NET
   dig +short A MAIL.EXAMPLE.NET
   dig +short -x ADRESSE_IP_PUBLIQUE
   ```
   👉 Explication : MX et A doivent exister ; le PTR (DNS inverse) doit renvoyer le FQDN, sinon les envois externes sont souvent rejetés. `ADRESSE_IP_PUBLIQUE` est à remplacer.

5. Tester la sortie SMTP vers Internet (lab) :
   ```bash
   timeout 5 bash -c '</dev/tcp/SMTP-TEST.EXAMPLE.NET/25' && echo ouvert || echo filtre
   ```
   👉 Explication : de nombreux FAI/hébergeurs bloquent le port 25 sortant ; dans ce cas utiliser un relais (smarthost) fourni. `SMTP-TEST.EXAMPLE.NET` est un hôte SMTP de test autorisé, à remplacer.

## 2. Production — Contrôles

Documenter FQDN, IP, PTR, MX, SPF/DKIM/DMARC prévus, volumétrie attendue, présence d'un relais sortant, politique de rétention des files et propriétaire du service. Valider que le domaine est bien géré par l'organisation.

## 3. Production — Sécurité

- Ne jamais ouvrir le port 25 avant d'avoir restreint le relais (voir la fiche Configurer).
- Ne tester qu'avec ses propres boîtes et serveurs.
- Prévoir un snapshot de VM avant installation.

## Validation et retour arrière

- **Validation** : FQDN, DNS et ports vérifiés, aucun MTA concurrent actif.
- **Retour arrière** : aucune modification n'a été faite à ce stade : rien à annuler.

## Si le problème n'est pas résolu

- [Postfix — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-installer)
- [Postfix — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-configurer)
- [Postfix — documentation officielle](https://www.postfix.org/documentation.html)
- [Debian — Postfix](https://wiki.debian.org/Postfix)