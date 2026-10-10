# Project context for AI coding assistants

This is a **learning project**: the owner is learning knowledge graphs and Neo4j by vibe coding.
Favour clarity over cleverness, and explain new Cypher or graph concepts in comments when you introduce them.

## Stack
- Neo4j **AuraDB Free** (cloud). Connection details in `.env` (never commit it; `.env.example` is the template).
- Python 3.10+, official `neo4j` driver, `python-dotenv`.
- Aura Free has no Graph Data Science (GDS) or APOC Extended plugins — stick to plain Cypher
  (APOC Core functions are available).

## Code conventions
- Run queries with `from kg import run, show`: `run(query, **params)` returns records; `show(records, "title")` prints a table.
- Always pass values as `$parameters`; never format them into the query string.
- Writes use `MERGE` so scripts stay idempotent (safe to re-run).
- Lessons live in `lessons/NN_name.py`, start with a docstring explaining the concept, and add the
  repo root to `sys.path` (copy the two lines from an existing lesson) so they run as `python lessons/NN_name.py`.

## Graph model
```
(:Person {name})-[:ACTED_IN {roles}]->(:Movie {title, released})
(:Person)-[:DIRECTED]->(:Movie)
(:Person)-[:WROTE]->(:Movie)
(:Movie)-[:IN_GENRE]->(:Genre {name})
(:User {name})-[:RATED {stars}]->(:Movie)
```
Uniqueness constraints on Movie.title, Person.name, Genre.name, User.name (see `kg/load.py`).
Source data is `data/movies.json` and `data/ratings.json`; when changing the model, update
`kg/load.py`, this file, and the README diagram together.

## Checks
- `python -m pytest -q` validates the JSON data (no database needed). Add tests when adding data rules.
- If you can, run the lesson you changed against the real database before calling it done.
