# Hub de veille CVE et vulnérabilités

Index de sources pour identifier les vulnérabilités, confirmer les versions concernées et suivre les avis des éditeurs et distributeurs. Une entrée CVE ou un score ne suffit pas à décider du risque pour un système donné.

- **Vérification des liens** : 27 octobre 2026

## Identifiants, détails et bases de données

| Source | Rôle | Limites / usage |
|---|---|---|
| [CVE Program](https://www.cve.org/) et [téléchargements CVE](https://www.cve.org/Downloads) | Identifiants publics et enregistrements de vulnérabilités; l'archive officielle courante est au format CVE JSON v5 | Le CVE identifie un problème; son existence seule ne donne ni sévérité locale, ni preuve d'exploitation, ni correctif à installer. Les formats historiques CSV/HTML/XML/CVRF ont pris fin en juin 2024. |
| [NVD (NIST)](https://nvd.nist.gov/vuln) | Enrichissement et recherche des CVE : métriques, produits, références et données de vulnérabilité | Les enrichissements peuvent arriver après la publication initiale d'un CVE; vérifier l'avis de l'éditeur et le suivi du distributeur. |
| [OSV.dev](https://osv.dev/) | Base distribuée de vulnérabilités open source, avec correspondance version/commit et écosystèmes de paquets | Vérifier le nom exact du paquet, l'écosystème, le champ de versions affectées et les références amont; une recherche par nom similaire peut être trompeuse. |
| [GitHub Advisory Database](https://github.com/advisories) | Avis CVE/GHSA pour les écosystèmes de dépendances suivis par GitHub | Distinguer les avis revus par GitHub de ceux qui ne le sont pas; confirmer la version corrigée et la source mainteneur. |
| [CVE List V5 — dépôt officiel](https://github.com/CVEProject/cvelistV5) | Données CVE structurées et téléchargements en lots selon la documentation du programme | Les archives peuvent être volumineuses et les données nécessitent une analyse structurée; préférer l'interface ou l'API appropriée si un simple contrôle suffit. |

## Alertes et suivi des éditeurs / OS

| Source | Périmètre |
|---|---|
| [CERT-FR / ANSSI](https://cert.cyber.gouv.fr/) | [Avis de sécurité](https://cert.cyber.gouv.fr/avis/), [alertes](https://cert.cyber.gouv.fr/alerte/), [menaces et incidents](https://cert.cyber.gouv.fr/cti/) et [recommandations de durcissement](https://cert.cyber.gouv.fr/dur/). |
| [CISA Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Catalogue des vulnérabilités pour lesquelles une exploitation active est connue par CISA; indicateur prioritaire à examiner pour les actifs concernés. |
| [Dépôt de données KEV de CISA](https://github.com/cisagov/kev-data) | Copie lisible par machine des fichiers KEV CSV/JSON publiés par CISA; son README indique que les fichiers reflètent la source CISA. Utiliser CISA comme source de référence. |
| [Debian Security Tracker](https://security-tracker.debian.org/tracker/) et [DSA](https://www.debian.org/security/) | État par paquet/suite Debian et avis de sécurité Debian; tenir compte des correctifs rétroportés et comparer les versions de paquet Debian, pas uniquement la version amont. |
| [Ubuntu Security Notices](https://ubuntu.com/security/notices) et [Ubuntu CVE](https://ubuntu.com/security/cves) | Avis de sécurité par paquet et versions Ubuntu concernées; les notices indiquent les mises à jour disponibles et les suites affectées. |
| [Red Hat Product Security](https://access.redhat.com/security/security-updates/) | Recherche des avis RHSA, CVE et errata par produit, version et architecture; un compte Red Hat peut être requis pour certaines ressources. |
| [Microsoft Security Update Guide](https://msrc.microsoft.com/update-guide) | CVE, avis et mises à jour de sécurité Microsoft, filtrables par produit et date. |
| [Alpine Linux Security](https://secdb.alpinelinux.org/) | Base de sécurité des paquets Alpine; confirmer la branche et les versions APK. |
| [Rocky Linux Errata](https://errata.rockylinux.org/) et [documentation sécurité](https://docs.rockylinux.org/guides/security/cve_hygiene/) | Errata de la distribution et méthode de suivi des CVE; comparer le paquet et la version Rocky concernés. |

## Priorisation : signaux à ne pas confondre

| Signal | Interprétation | Ce qu'il ne signifie pas |
|---|---|---|
| **CVE** | Identifiant stable d'une vulnérabilité publiée | Ni une note de gravité ni une confirmation d'exploitation. |
| **CVSS** ([FIRST CVSS](https://www.first.org/cvss/)) | Mesure normalisée des caractéristiques et de la gravité technique; la version courante est CVSS v4.0 | Pas un score de risque organisationnel complet; compléter avec exposition, criticité de l'actif et contrôles compensatoires. |
| **CISA KEV** | Présence dans un catalogue de vulnérabilités exploitées dans la nature selon CISA | N'indique pas automatiquement que l'actif local est vulnérable; vérifier produit, version, configuration et exposition. |
| **EPSS** ([FIRST EPSS](https://www.first.org/epss/)) | Estimation probabiliste de la probabilité d'observer une exploitation dans les 30 prochains jours, recalculée quotidiennement | Pas la preuve d'exploitation, pas la sévérité, ni un score de risque local. Combiner avec l'inventaire et les signaux directs; la FAQ FIRST précise ses limites. |

## Parcours de triage défensif

1. Identifier précisément le produit, son éditeur, la version/build installé, le paquet, le composant embarqué et l'actif concerné.
2. Confirmer dans l'avis éditeur et le tracker du distributeur si cette version est touchée, corrigée ou couverte par un correctif rétroporté.
3. Vérifier l'exposition réelle : service activé, interface joignable, fonction vulnérable utilisée, privilèges et criticité des données.
4. Consulter en complément CVSS, KEV, EPSS et les alertes CERT; accorder une attention prioritaire aux actifs exposés et aux KEV applicables.
5. Appliquer le correctif éditeur/distributeur selon le processus de changement, tester le service puis vérifier la version et la disponibilité après intervention.
6. Si aucun correctif n'est disponible, appliquer uniquement les mesures temporaires officielles, documenter le risque résiduel, le responsable et la date de réévaluation.

Ne pas télécharger ni exécuter un exploit depuis un avis, une base CVE ou un dépôt tiers pour vérifier une vulnérabilité. Confirmer l'état par les versions, configurations, journaux et outils défensifs autorisés; reproduire uniquement dans un lab isolé explicitement prévu à cet effet.

## Sources méthodologiques

- [FIRST — CVSS v4.0](https://www.first.org/cvss/v4.0/)
- [FIRST — FAQ EPSS](https://www.first.org/epss/faq.html), [données et API](https://www.first.org/epss/data.html)
- [CISA — Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) et [copie CSV/JSON CISA](https://github.com/cisagov/kev-data)
- [CVE Program — archives et format CVE v5](https://www.cve.org/Downloads)
- [OSV — schéma et base open source](https://osv.dev/)

## Voir aussi

- [Documentation officielle des logiciels](/06-documentation-ext/02-documentation-officielle/liens-docs-logicielles)
- [Sites et communautés de référence](/06-documentation-ext/03-sites-communautes/sites-web)
- [Fiches d'aide informatique](/06-documentation-ext/01-aide-memoire/fiches-aide-informatique)