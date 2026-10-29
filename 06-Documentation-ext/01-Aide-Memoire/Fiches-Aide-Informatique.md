# Fiches d'aide informatique — références rapides

Sélection de ressources pour retrouver une commande ou une syntaxe. Les exemples sont des aide-mémoire communautaires : ils ne remplacent ni le manuel officiel ni une procédure validée pour le système et la version concernés.

- **Tags** : `documentation-externe`, `aide-informatique`, `cheat-sheet`, `linux`, `windows`, `sysadmin`
- **Vérification des liens** : 27 octobre 2026

## Commandes et pages de manuel

| Ressource | À quoi elle sert | Limites à garder en tête |
|---|---|---|
| [tldr pages](https://tldr.sh/) | Exemples courts pour les commandes usuelles Linux, macOS, Windows et autres plateformes | Contenu communautaire simplifié. Vérifier les options dans le manuel de la version installée avant une action destructive. |
| [Linux man-pages](https://man7.org/linux/man-pages/) | Référence Web des pages de manuel Linux, classées par section et projet | Le site complète `man` sur la machine; la page locale correspond mieux aux binaires installés et à leurs versions. |
| [Debian Manpages](https://manpages.debian.org/) | Pages de manuel associées aux paquets Debian | Choisir la suite Debian et la version du paquet adaptées; ne pas mélanger Debian stable et unstable par défaut. |
| [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) | Référence du shell Bash : syntaxe, expansions, commandes intégrées et scripts | À distinguer de POSIX `sh`, de Dash et des autres shells; vérifier le shebang et le shell cible. |
| [ExplainShell](https://explainshell.com/) | Décomposer visuellement les éléments d'une commande shell | Service tiers et explication syntaxique seulement; il ne certifie ni la sûreté, ni l'effet exact selon le système. Ne pas y soumettre de commande contenant des secrets ou données internes. |
| [cheat.sh](https://cheat.sh/) | Recherche de réponses concises par outil depuis le Web ou le terminal | Agrège des sources communautaires; éviter d'envoyer des commandes ou questions sensibles à un service externe et relire la commande avant tout lancement. |

## Fiches éditables et clients de fiches

- [cheat — application](https://github.com/cheat/cheat) : afficher et gérer des fiches locales dans le terminal.
- [cheat — fiches communautaires](https://github.com/cheat/cheatsheets) : fichiers texte importables par l'application; plusieurs exemples anciens peuvent ne plus correspondre aux versions actuelles.
- [navi](https://github.com/denisidoro/navi) : interface interactive de fiches. Le projet annonce un mode maintenance; une fiche peut proposer une commande exécutable. Inspecter et adapter la commande avant validation.
- [The Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) : index large de ressources système, réseau, exploitation et sécurité. C'est un répertoire de liens et d'exemples, pas un corpus homogène ni certifié.
- [Devhints](https://devhints.io/) : aide-mémoire compact orienté développement et outils.
- [Awesome Cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) : collection communautaire de fiches de langages, outils et bases de données.

## Windows et PowerShell

- [Microsoft Learn — documentation PowerShell](https://learn.microsoft.com/en-us/powershell/)
- [Microsoft Learn — documentation Windows pour les professionnels IT](https://learn.microsoft.com/en-us/windows/)
- [Microsoft Learn — Windows Server](https://learn.microsoft.com/en-us/windows-server/)
- [Christian Lempa — cheat sheets](https://github.com/ChristianLempa/cheat-sheets) : notes personnelles sur divers outils et systèmes; vérifier leur fraîcheur.

## Sécurité d'utilisation

1. Confirmer l'OS, la version de l'outil, le shell et le compte utilisés.
2. Lire l'aide locale (`man`, `--help`, `Get-Help`) et consulter la documentation officielle.
3. Repérer les effets de bord : suppression, écriture, redémarrage, exposition réseau, élévation de privilèges, transfert de données ou appel externe.
4. Tester les commandes modificatrices sur un lab avec des données fictives, sauvegarde vérifiée et retour arrière.
5. Ne pas copier aveuglément une commande, surtout si elle utilise `sudo`, des privilèges administrateur, un pipeline réseau vers un shell, des chemins larges ou des variables non contrôlées.

## Voir aussi

- [Documentation officielle des logiciels](../02-Documentation-Officielle/Liens-Docs-Logicielles.md)
- [Sites et communautés de référence](../03-Sites-Communautes/Sites-Web.md)
- [Hub de veille CVE](../04-Veille-CVE/Hub-CVE.md)
- [Référentiel GitHub Sysadmin/TSSR](../05-Referentiel-GitHub/Github-TSSR.md)
