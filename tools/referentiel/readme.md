# Outils du référentiel et des leçons « tout-en-un »

Scripts en bibliothèque standard Python, sans dépendance tierce.

| Script | Rôle |
|---|---|
| `build-referentiel.py` | Relit les sitemaps publics (Stéphane Robert, Root & Code) et l'arborescence GitHub nivvlem-tssr, récupère uniquement les titres de page (débit limité, User-Agent déclaré) et écrit `Tout-en-un/00-referentiel-sites/`. Aucun contenu pédagogique n'est copié. |
| `build-lecons-index.py` | Génère `lecons-index.md`, les `Lecons/readme.md` de chaque catégorie et `credits-images.md` à partir des leçons. |

```bash
python3 tools/referentiel/build-referentiel.py --cache /tmp/referentiel-cache.json
python3 tools/referentiel/build-lecons-index.py
python3 tools/pack-master/pack-master.py check
```

Le référentiel ZenTSSR est rédigé à partir du sitemap et des titres publics du site ; il se met à jour à la main.

## Règles pour les images des leçons

- Images tierces : uniquement Wikimedia Commons sous CC0, domaine public, CC BY ou CC BY-SA, avec licence vérifiée par l'API et crédit dans la leçon.
- Sinon, schéma SVG original dédié au domaine public (CC0), avec `<title>` et `<desc>`.
- Interdits : licences NC/ND, logos et marques, captures d'interfaces propriétaires, licence incertaine.
