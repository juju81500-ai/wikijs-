# Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Securiser

- **Environnement** : VM EVE-NG (appliance basée sur Ubuntu Server 24.04 LTS) hébergée sur un poste ou serveur de virtualisation
- **OS / Version** : EVE-NG 7.x (7.2.0-18 au contrôle du 29/10/2026), Ubuntu 24.04 LTS embarqué; Community 6.2.0-4 (Ubuntu 22.04) en fin de support juin 2026
- **Catégorie** : simulation réseau / sécurité
- **Tags** : `ubuntu24.04`, `eve-ng`, `securite`, `durcissement`, `authentification`, `reseau`

---

## Problème précis à résoudre

Réduire l'exposition d'une VM EVE-NG et remplacer les identifiants par défaut.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'interface web : **Management > User management**, éditer le compte `admin` et définir un mot de passe fort `MOT_DE_PASSE_ADMIN_EVE`, puis enregistrer. Ne pas supprimer le compte `admin`.
   👉 Explication : le compte par défaut documenté est connu publiquement; la doc demande de le changer sans le supprimer. La valeur en majuscules est à remplacer.

2. Créer un compte nominatif par utilisateur : **Management > User management > Add user**, renseigner `NOM_UTILISATEUR` et le rôle adapté.
   👉 Explication : évite le partage du compte administrateur; les rôles disponibles dépendent de la licence.

3. Vérifier les services en écoute depuis la CLI :
   ```bash
   ss -tlnp | grep -E ':(22|443)\b'
   ```
   👉 Explication : EVE-NG est géré en HTTPS (443) et SSH (22); tout autre port exposé doit être justifié.

4. Contrôler la mise à jour et la version :
   ```bash
   dpkg -l eve-ng-pro
   ```
   👉 Explication : une version ancienne ou en fin de support expose à des failles non corrigées.

5. Pour l'authentification centralisée, consulter les sections Radius et Active Directory du cookbook et configurer **System > System Settings**.
   👉 Explication : fonction documentée; ⚠️ les paramètres (serveur, secret partagé) doivent venir de votre administrateur et ne sont pas détaillés ici.

6. Pour un certificat HTTPS d'entreprise, suivre la page officielle « SSL how to make EVE with custom https ».
   👉 Explication : ⚠️ procédure longue, non reproduite ici car non vérifiée en détail.

## 2. Production — Contrôles

- Filtrer l'accès à EVE-NG par pare-feu réseau (poste d'administration seulement) plutôt que de modifier les règles internes de l'appliance.
- Vérifier l'absence de conflit avec `172.29.129.0/24`, `172.29.130.0/24` et `172.17.0.0/16`.
- Revoir périodiquement les comptes et leurs rôles.

## 3. Production — Sécurité

- Ne pas exposer EVE-NG sur Internet; l'isoler dans un VLAN de lab.
- Ne pas faire de mise à niveau de la version d'Ubuntu : la doc EVE-NG l'interdit explicitement.
- Ne pas ajouter de dépôts APT tiers sur l'appliance.
- Ne pas relier de nœuds de lab au réseau de production sans accord.

## Validation et retour arrière

- **Validation** : la connexion avec l'ancien mot de passe par défaut échoue et `ss` ne montre que les ports attendus.
- **Retour arrière** : rétablir l'accès par un autre compte administrateur ou restaurer l'instantané de la VM; ne jamais revenir au mot de passe par défaut.

## Si le problème n'est pas résolu

- [EVE-NG — SSL / HTTPS personnalisé](https://www.eve-ng.net/index.php/documentation/ssl-how-to-make-eve-with-custom-https/)
- [EVE-NG — Professional Cookbook (PDF, chapitres 7 et 17)](https://www.eve-ng.net/wp-content/uploads/2026/09/EVE-PE-BOOK-7.9-2026.pdf)
[EVE-NG — documentation officielle](https://www.eve-ng.net/index.php/documentation/)
- [Fiche logiciel EVE-NG](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_EVE-NG.md)
- [Mettre à jour avec retour arrière](./Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Mettre_A_Jour_Retour.md)
