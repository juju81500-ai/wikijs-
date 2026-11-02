# Référentiel des sites TSSR — cours et catégories

- **Tags** : `transverse`, `tout-en-un`, `referentiel`, `tssr`

Carte des quatre sources publiques suivies par le pack : catégories, cours et liens vers les sites d'origine.

Ce référentiel ne reproduit **aucun contenu pédagogique** : il liste uniquement les titres publics, les catégories et les liens, à des fins de navigation. Les droits sur les cours restent à leurs auteurs ; pour les lire, utiliser le lien vers le site d'origine. Les titres sont relevés le 2026-11-01 ; ils peuvent évoluer côté éditeur.

| Source | Pages du référentiel | Volume relevé |
|---|---|---|
| Stéphane Robert — documentation, compétences, labs, articles | [Index](Stephane-Robert/README.md) | 1172 pages |
| Root & Code (jousseaume.online) | [Référentiel](Jousseaume/Referentiel_Root_and_Code.md) | 98 cours, 10 catégories |
| nivvlem-TSSR (GitHub) | [Référentiel](Nivvlem/Referentiel_nivvlem-TSSR.md) | 22 modules, 331 documents |
| ZenTSSR | [Référentiel](ZenTSSR/Referentiel_ZenTSSR.md) | voir la page |

## Comment s'en servir

1. Choisir la catégorie dans l'index de la source.
2. Ouvrir le cours sur le site d'origine, pour lire son contenu à jour.
3. Suivre les leçons originales du pack dans les huit catégories « tout-en-un » pour une version illustrée et structurée.

## Régénérer le référentiel

```bash
python3 tools/referentiel/build_referentiel.py --cache /tmp/referentiel-cache.json
```
👉 Explication : relit les sitemaps publics à débit limité, récupère uniquement les titres de page et réécrit ces fichiers.
