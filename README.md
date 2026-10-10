# Neo4j Knowledge Graph Playground

Learn knowledge graphs by building one: a small graph of movies, actors, directors,
genres and user ratings in **Neo4j Aura Free**, explored with **Python** and **Cypher**.

```
(:Person)-[:ACTED_IN {roles}]->(:Movie)-[:IN_GENRE]->(:Genre)
(:Person)-[:DIRECTED]->(:Movie)        (:Person)-[:WROTE]->(:Movie)
(:User)-[:RATED {stars}]->(:Movie)
```

30 movies · ~70 people · 6 users · built so that interesting paths exist
(yes, you can compute Keanu Reeves' Kevin Bacon number).

---

## 1. Get a free Neo4j database (5 min)

1. Go to **https://console.neo4j.io** and sign up.
2. Create an instance → choose **AuraDB Free**.
3. A password is shown **once** — click **Download** to save the credentials `.txt` file.
4. Wait until the instance status says **Running**.

> Aura Free pauses instances that sit unused for a while. If yours is paused, open the
> console and click **Resume**.

## 2. Set up this project

Needs Python 3.10+.

```bash
git clone https://github.com/perpetualxbeta-ai/neo4j-kg-playground.git
cd neo4j-kg-playground
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # Windows: copy .env.example .env
```

Open `.env` and paste in `NEO4J_URI` and `NEO4J_PASSWORD` from the file you downloaded.
(`.env` is git-ignored, so your password never gets committed.)

## 3. Do the lessons, in order

| # | Run | You learn |
|---|-----|-----------|
| 1 | `python lessons/01_hello_graph.py` | Nodes, relationships, labels, properties, `MERGE` |
| 2 | `python lessons/02_load_movies.py` | Modelling a domain, constraints, bulk loading with `UNWIND` |
| 3 | `python lessons/03_query_basics.py` | `MATCH`, `WHERE`, aggregation, `OPTIONAL MATCH` |
| 4 | `python lessons/04_paths.py` | Variable-length paths, `shortestPath` — where graphs beat SQL |
| 5 | `python lessons/05_recommendations.py Aisha` | Content-based & collaborative recommendations, with explanations |
| 6 | `python lessons/06_your_turn.py` | Exercises with auto-checks (solutions in `solutions/`) |

Each lesson file is mostly comments: read it top to bottom, run it, then change a query and run it again.

**See the graph, don't just print it.** In the Aura console, open **Query** and paste queries
from [`cypher/cheatsheet.cypher`](cypher/cheatsheet.cypher). Results that return nodes or paths
are drawn as an interactive picture you can drag around.

## 4. Vibe code your way further

Open the repo in Claude Code (or any AI coding tool). [`CLAUDE.md`](CLAUDE.md) gives it the context
about this project, and [`docs/VIBE_PROMPTS.md`](docs/VIBE_PROMPTS.md) has prompts for next steps,
from "add a new relationship type" up to "build GraphRAG over my own notes".

## Project layout

```
kg/            db.py (connection + run()), load.py (graph model + loader), pretty.py (tables)
data/          movies.json, ratings.json  ← edit these to grow the graph
lessons/       01–06, run in order
solutions/     answers for lesson 6
cypher/        cheatsheet to paste into the Aura console
tests/         data checks that run without a database: python -m pytest -q
```

## Troubleshooting

- **`Missing Neo4j connection details`** → you haven't created `.env`, or it's in the wrong folder (it belongs next to this README).
- **`ServiceUnavailable` / can't connect** → instance is paused or still starting; check the Aura console. The URI must start with `neo4j+s://`.
- **`AuthError`** → wrong password. If you lost it, reset it from the instance's menu in the Aura console.
- **Start over** → `python lessons/02_load_movies.py --reset` wipes and reloads the graph.
