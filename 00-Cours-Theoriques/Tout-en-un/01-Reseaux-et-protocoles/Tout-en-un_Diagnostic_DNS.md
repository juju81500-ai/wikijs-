# Fiche_Simple_-_Tout-en-un_Diagnostic_DNS

- **Environnement** : postes et serveurs Linux ou Windows
- **OS / Version** : multi-OS ; les commandes doivent être adaptées à l'environnement
- **Catégorie** : Tout-en-un / Réseaux et protocoles
- **Tags** : `transverse`, `tout-en-un`, `dns`, `diagnostic`

---

## Problème précis à résoudre

Déterminer si un échec d'accès par nom vient de la résolution DNS, du résolveur configuré ou d'une donnée DNS incorrecte, sans modifier la configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'accès par nom sur Linux :
   ```bash
   getent ahosts example.org
   ```
   👉 Explication : interroge la chaîne de résolution système et affiche les adresses obtenues, sans changer l'état du serveur.

2. Contrôler le résolveur et les domaines de recherche sur Linux :
   ```bash
   resolvectl status
   ```
   👉 Explication : montre les DNS et domaines configurés par interface. Si `resolvectl` n'existe pas, utiliser la fiche propre à l'OS et à son gestionnaire réseau.

3. Vérifier le résultat d'une requête DNS sur Windows :
   ```powershell
   Resolve-DnsName -Name example.org -Type A
   Get-DnsClientServerAddress
   ```
   👉 Explication : la première commande demande un enregistrement A ; la seconde affiche les serveurs DNS configurés. Ces commandes sont en lecture seule.

4. Comparer les résultats sans forcer une modification :
   ```bash
   getent hosts example.org
   ```
   ```powershell
   Resolve-DnsName -Name example.org
   ```
   👉 Explication : comparer avec les résultats attendus et les journaux côté résolveur autorisé. Une réponse différente peut être normale selon split-DNS, VPN, cache ou politique de filtrage.

## 2. Production — Contrôles

Consigner l'heure, l'hôte, le nom interrogé, le résolveur utilisé et le résultat. Tester d'abord un nom approuvé par le propriétaire du service ; ne pas vider le cache ou changer le DNS comme première action.

## 3. Production — Sécurité

Ne pas envoyer des noms internes ou des données client à un résolveur public. Les commandes de cette fiche n'effectuent aucune modification.

## Validation et retour arrière

- **Validation** : la résolution système retourne le résultat attendu pour le nom approuvé et le serveur DNS configuré est documenté.
- **Retour arrière** : aucune modification n'est faite. Si une correction est nécessaire, utiliser la fiche réseau de l'OS concerné et créer un snapshot avant changement.

## Si le problème n'est pas résolu

- [Fiches réseau Debian](../../../01-Fiches-Simples/Debian/13/Vie-du-systeme/Fiches-par-theme/Reseau/)
- [Fiches réseau Ubuntu 24.04](../../../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiches-par-theme/Reseau/)
- [Fiches réseau Windows Server 2022](../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-systeme/Fiches-par-theme/Reseau/)
- [Sources publiques et règle de classement](../../../06-Documentation-ext/Sources_Publiques_TSSR_Pour_Fiches_Tout-en-un.md)
- [Documentation Microsoft — Resolve-DnsName](https://learn.microsoft.com/powershell/module/dnsclient/resolve-dnsname)
- [Documentation systemd — resolvectl](https://www.freedesktop.org/software/systemd/man/latest/resolvectl.html)
