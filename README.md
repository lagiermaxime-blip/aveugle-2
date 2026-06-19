# Blind Toast — Restaurant · Jeu de dégustation

Site vitrine d'un restaurant expérientiel basé sur un dîner mystère en 6 manches,
où les convives devinent goûts, saveurs et ingrédients à l'aveugle.

## Stack

Site **100 % statique** — aucune dépendance, aucun build.

- HTML5 (5 pages)
- CSS3 (`css/styles.css`)
- JavaScript vanilla (`js/main.js`)
- Illustrations dans `assets/`

## Pages

| Fichier | Page |
|---|---|
| `index.html` | Accueil |
| `concept.html` | Concept (les 6 manches) |
| `evenement.html` | Événements & privatisation |
| `tarif.html` | Tarifs & formules |
| `contact.html` | Contact & réservation |

## Lancer en local

```bash
python3 serve.py
# puis http://127.0.0.1:4173
```

Ou ouvrir directement `index.html` dans un navigateur.

## Déploiement

Hébergé sur Vercel (déploiement automatique à chaque push sur `main`).
