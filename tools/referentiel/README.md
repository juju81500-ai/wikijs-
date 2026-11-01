# Outils du référentiel et des leçons « tout-en-un »

Scripts en bibliothèque standard Python, sans dépendance tierce.

| Script | Rôle |
|---|---|
| `build_referentiel.py` | Relit les sitemaps publics (Stéphane Robert, Root & Code) et l'arborescence GitHub nivvlem-TSSR, récupère uniquement les titres de page (débit limité, User-Agent déclaré) et écrit `Tout-en-un/00-Referentiel-Sites/`. Aucun contenu pédagogique n'est copié. |
| `build_lecons_index.py` | Génère `Lecons_Index.md`, les `Lecons/README.md` de chaque catégorie et `Credits_Images.md` à partir des leçons. |

```bash
python3 tools/referentiel/build_referentiel.py --cache /tmp/referentiel-cache.json
python3 tools/referentiel/build_lecons_index.py
python3 tools/pack_master/pack_master.py check
```

Le référentiel ZenTSSR est rédigé à partir du sitemap et des titres publics du site ; il se met à jour à la main.

## Règles pour les images des leçons

- Images tierces : uniquement Wikimedia Commons sous CC0, domaine public, CC BY ou CC BY-SA, avec licence vérifiée par l'API et crédit dans la leçon.
- Sinon, schéma SVG original dédié au domaine public (CC0), avec `<title>` et `<desc>`.
- Interdits : licences NC/ND, logos et marques, captures d'interfaces propriétaires, licence incertaine.
