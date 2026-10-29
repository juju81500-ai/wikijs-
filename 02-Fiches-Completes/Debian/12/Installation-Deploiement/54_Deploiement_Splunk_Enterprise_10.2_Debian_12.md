# Déployer Splunk Enterprise 10.2 sur Debian 12

- **OS / Version** : Debian 12 Bookworm x86-64; Splunk Enterprise 10.2
- **Type de fiche** : Installation/Déploiement
- **Architecture** : instance autonome d'évaluation; dimensionnement production à calculer
- **Catégorie** : SIEM / centralisation et recherche de journaux
- **Tags** : `splunk`, `debian12`, `siem`, `logs`, `enterprise`, `systemd`

## 1. Dimensionner et préparer

Fiche simple : [dimensionner et préparer](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Dimensionner_Preparer.md).

Confirmer que le système d'exploitation et l'architecture sont listés dans la matrice officielle Splunk 10.2. Calculer le débit journalier, le volume hot/warm/cold, la rétention, les recherches simultanées et les besoins IOPS avant de choisir CPU, RAM et disques. Pour une plateforme de production distribuée, appliquer les architectures validées Splunk au lieu de promouvoir cette instance autonome.

Préparer DNS/NTP, stockage local compatible, sauvegarde cohérente, accès d'administration restreint et plan réseau. Limiter l'accès aux ports explicitement requis par les composants du déploiement. Par défaut, l'interface Web écoute sur 8000, la gestion/API sur 8089; ne pas les exposer à Internet. Ne pas ouvrir 9997 ou d'autres ports d'ingestion sans configurer les inputs correspondants.

## 2. Télécharger et vérifier le paquet

Fiche simple : [télécharger et vérifier le paquet](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Telecharger_Verifier_Paquet.md).

Télécharger la version Linux x86-64 `.deb` depuis la page officielle Splunk; récupérer le fichier SHA-512 associé et vérifier le hash avant installation. Si le hash ne correspond pas, supprimer le téléchargement et arrêter la procédure.

Le paquet Debian s'installe uniquement dans `/opt/splunk`, qui doit être un répertoire réel et non un lien symbolique. Créer un compte/groupe système dédiés et préparer les permissions afin que Splunk ne tourne pas avec root.

```bash
sudo groupadd --system splunk
sudo useradd --system --gid splunk --home-dir /opt/splunk --shell /usr/sbin/nologin splunk
sudo test ! -L /opt/splunk
sudo test ! -e /opt/splunk || sudo test -d /opt/splunk
```

Adapter la gestion du compte si une politique centrale ou le paquet Splunk a déjà créé `splunk`; ne pas créer un doublon.

## 3. Installer sans démarrer en root

Fiche simple : [installer sans démarrer en root](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Installer_Sans_Root.md).

```bash
sudo dpkg -i ./splunk-10.2.0-*-linux-amd64.deb
sudo chown -R splunk:splunk /opt/splunk
sudo -H -u splunk /opt/splunk/bin/splunk start
```

Accepter la licence lors du premier démarrage et créer interactivement un nom d'utilisateur admin distinct de l'identité système, avec un secret fort conservé au coffre. Ne pas passer le mot de passe dans la ligne de commande. Splunk 10.2 ne permet plus l'exécution en root par défaut; conserver le service sous compte non-root et accorder uniquement les accès aux fichiers surveillés qui ont été approuvés.

## 4. Sécuriser le premier accès

Fiche simple : [sécuriser le premier accès](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Securiser_Premier_Acces.md).

Au début, garder Splunk Web accessible uniquement en local ou via le réseau d'administration. Utiliser un reverse proxy HTTPS ou activer TLS selon la procédure Splunk avant tout accès utilisateur hors localhost. Vérifier certificats, nom DNS, contrôle d'accès et MFA/SSO disponible avant de connecter des sources réelles.

Configurer le démarrage système avec la méthode officielle pour Debian/systemd et l'utilisateur `splunk`. Examiner l'unité générée, ses limites de ressources et son utilisateur; ne pas lancer une seconde instance manuellement si le service systemd gère déjà le processus.

## 5. Configurer l'ingestion pilote

Fiche simple : [configurer l'ingestion pilote](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Ingestion_Pilote.md).

Définir un premier input de test et un index à rétention limitée. Pour les sources distribuées, utiliser un Universal Forwarder ou un transport approuvé, TLS vérifié et des règles d'accès par source. Ne pas écouter sur des interfaces globales par défaut et ne pas indexer des journaux contenant des mots de passe, tokens ou données personnelles non autorisées.

Créer une recherche de validation sur un événement synthétique connu; confirmer source, sourcetype, index, horodatage et timezone. Contrôler ensuite les volumes d'ingestion et l'impact CPU/disque avant extension.

## 6. Vérifier et exploiter

Fiche simple : [vérifier et exploiter](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Splunk/Fiche_Simple_-_VM_Debian_12_Splunk_Verifier_Exploiter.md).

```bash
sudo -H -u splunk /opt/splunk/bin/splunk status
sudo systemctl --no-pager status Splunkd 2>/dev/null || true
```

Le nom exact de l'unité dépend de la procédure boot-start choisie; vérifier aussi le journal Splunk `var/log/splunk/splunkd.log`. Confirmer la connexion Web avec HTTPS, un compte nominatif et un événement pilote visible.

Sauvegarder `$SPLUNK_HOME/etc`, les certificats, configurations d'index, clés de chiffrement et données selon la stratégie Splunk. Tester la restauration, maintenir la licence, suivre l'utilisation disque et planifier les mises à niveau avec sauvegarde et revue des notes de version.

## Sources

- [Splunk 10.2 — Installer sur Linux](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/install-on-linux)
- [Splunk 10.2 — Systèmes supportés et exigences](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/plan-your-splunk-enterprise-installation/system-requirements-for-use-of-splunk-enterprise-on-premises)
- [Splunk 10.2 — Premier démarrage](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/start-using-splunk-enterprise/start-splunk-enterprise-for-the-first-time)
- [Splunk 10.2 — Exécuter avec un compte non-root](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/run-splunk-enterprise-as-a-different-or-non-root-user)
- [Splunk 10.2 — Vérifier l'intégrité de l'installation](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/secure-your-splunk-enterprise-installation/install-splunk-enterprise-securely)
- [Splunk 10.2 — Sécuriser le système avant installation](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/secure-your-splunk-enterprise-installation/secure-your-system-before-you-install-splunk-enterprise)