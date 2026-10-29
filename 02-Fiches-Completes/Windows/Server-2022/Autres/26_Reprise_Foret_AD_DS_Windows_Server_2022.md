# Reprise d'une forêt Active Directory Domain Services

- **Type de fiche** : Autres — sauvegarde / reprise après sinistre
- **Environnement** : Forêt AD DS d'entreprise; laboratoire isolé recommandé
- **OS / Version** : Windows Server 2022 pour les contrôleurs de domaine concernés
- **Rôle** : Préparer et encadrer la restauration d'une forêt AD DS après perte majeure ou compromission
- **Tags** : `windows-server-2022`, `active-directory`, `ad-ds`, `forest-recovery`, `backup`, `disaster-recovery`

## 1. Déterminer si la reprise de forêt est nécessaire

Fiche simple : [déterminer si la reprise de forêt est nécessaire](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Determiner_Necessite.md).

Une panne isolée d'un contrôleur de domaine ne justifie pas automatiquement une restauration de forêt. Évaluer d'abord l'état des réplications, des autres DC, du DNS et des sauvegardes avec l'équipe AD et sécurité. En cas d'incident de sécurité, isoler les systèmes suspectés et conserver les preuves selon le plan de réponse.

Ce guide est un cadre de préparation, pas un substitut à la procédure Microsoft et au runbook propre à la forêt. Ne jamais improviser une reprise sur la production.

## 2. Préparer et qualifier les sauvegardes

Fiche simple : [préparer et qualifier les sauvegardes AD DS](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Preparer_Sauvegardes.md).

- Maintenir des sauvegardes AD DS compatibles, protégées contre l'altération et testées régulièrement.
- Documenter par domaine le DC retenu, la date de sauvegarde, la méthode de restauration, les rôles FSMO et les dépendances DNS/SYSVOL.
- Conserver les supports, comptes de secours, clés et procédures hors ligne ou dans un coffre distinct du domaine.
- Vérifier que la sauvegarde est antérieure à la compromission présumée et que sa restauration a déjà été testée en laboratoire.

Sans sauvegarde saine et procédure vérifiée, arrêter et escalader au responsable AD/éditeur. Un snapshot VM ne remplace pas une sauvegarde AD-aware, sauf scénario explicitement pris en charge par Microsoft avec un hyperviseur compatible VM-Generation ID et le runbook correspondant.

## 3. Restaurer les premiers contrôleurs en isolation

Fiche simple : [restaurer les premiers contrôleurs en isolation](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Restaurer_Premiers_DC.md).

Suivre le runbook Microsoft officiel pour chaque domaine. En règle générale, restaurer d'abord un DC inscriptible du domaine racine de forêt, isolé du réseau de production; procéder ensuite aux domaines parents avant les domaines enfants. Utiliser une sauvegarde AD-aware et appliquer les consignes précises relatives à AD DS et SYSVOL.

La restauration initiale de SYSVOL est particulièrement sensible : la procédure autoritative ne s'applique qu'au DC désigné selon le guide Microsoft. Une mauvaise restauration peut introduire des conflits de réplication. Ne pas exécuter de séquences `ntdsutil`, `wbadmin` ou de modification de registre copiées sans confirmer qu'elles correspondent au scénario et au DC concernés.

## 4. Traiter les risques d'identité et de sécurité

Fiche simple : [traiter les risques d'identité et de sécurité](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Risques_Identite_Securite.md).

Avant reconnexion, effectuer selon le scénario les opérations documentées par Microsoft : rôles FSMO, nettoyage des métadonnées des DC perdus, DNS, invalidation/réattribution des pools RID, réinitialisation des secrets krbtgt et comptes privilégiés, puis mots de passe de comptes de service gérés si une compromission est suspectée.

Ces actions peuvent affecter l'authentification de toute la forêt. Les exécuter avec un responsable AD, en suivant les étapes exactes du guide officiel et dans l'ordre prévu; ne pas lancer de réinitialisation globale sans coordination applicative.

## 5. Valider avant retour en production

Fiche simple : [valider avant retour en production](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Valider_Avant_Production.md).

Dans un réseau de reprise isolé, vérifier DNS, SYSVOL/NETLOGON, état des DC, événements Directory Service, authentification de comptes de test et réplication. Employer les outils et critères de la procédure de reprise, notamment `dcdiag` et `repadmin` lorsque le guide l'indique.

Reconnecter à la production uniquement après validation formelle du responsable AD/sécurité et application des recommandations Microsoft pour les autres contrôleurs de domaine. Recréer ou redéployer les DC restants selon le plan, puis effectuer une nouvelle sauvegarde saine.

## 6. Clôture et amélioration

Fiche simple : [clôture et amélioration de la reprise de forêt](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Cloture_Amelioration.md).

Consigner chronologie, sauvegardes utilisées, étapes et résultats, secrets renouvelés, exceptions et date de prochain exercice. Réaliser un exercice périodique de reprise en environnement isolé et corriger le runbook à partir des écarts.

## Sources

- [Microsoft Learn — Étapes de reprise d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest)
- [Microsoft Learn — Reprise initiale d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery)
- [Microsoft Learn — Redéployer les autres contrôleurs de domaine](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-restore-additional-dcs)