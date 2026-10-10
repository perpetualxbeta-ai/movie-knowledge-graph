"""Load the movie knowledge graph from data/*.json into Neo4j.

The graph model (the "schema" of our knowledge graph):

    (:Person)-[:ACTED_IN {roles}]->(:Movie)
    (:Person)-[:DIRECTED]->(:Movie)
    (:Person)-[:WROTE]->(:Movie)
    (:Movie)-[:IN_GENRE]->(:Genre)
    (:User)-[:RATED {stars}]->(:Movie)

Every statement uses MERGE (= "find it, or create it if missing"), so running
the loader twice does not create duplicates. That property is called idempotence.
"""

from __future__ import annotations

import json
from pathlib import Path

from kg.db import run, run_with_summary

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

CONSTRAINTS = [
    # A uniqueness constraint also creates an index, so lookups by title/name are fast.
    "CREATE CONSTRAINT movie_title IF NOT EXISTS FOR (m:Movie) REQUIRE m.title IS UNIQUE",
    "CREATE CONSTRAINT person_name IF NOT EXISTS FOR (p:Person) REQUIRE p.name IS UNIQUE",
    "CREATE CONSTRAINT genre_name IF NOT EXISTS FOR (g:Genre) REQUIRE g.name IS UNIQUE",
    "CREATE CONSTRAINT user_name IF NOT EXISTS FOR (u:User) REQUIRE u.name IS UNIQUE",
]

LOAD_MOVIES = """
UNWIND $movies AS m
MERGE (movie:Movie {title: m.title})
SET movie.released = m.released
"""

LOAD_GENRES = """
UNWIND $movies AS m
MATCH (movie:Movie {title: m.title})
UNWIND m.genres AS genreName
MERGE (g:Genre {name: genreName})
MERGE (movie)-[:IN_GENRE]->(g)
"""

LOAD_CAST = """
UNWIND $movies AS m
MATCH (movie:Movie {title: m.title})
UNWIND m.cast AS c
MERGE (p:Person {name: c.name})
MERGE (p)-[r:ACTED_IN]->(movie)
SET r.roles = [c.role]
"""

LOAD_DIRECTORS = """
UNWIND $movies AS m
MATCH (movie:Movie {title: m.title})
UNWIND m.directors AS name
MERGE (p:Person {name: name})
MERGE (p)-[:DIRECTED]->(movie)
"""

LOAD_WRITERS = """
UNWIND $movies AS m
MATCH (movie:Movie {title: m.title})
UNWIND m.writers AS name
MERGE (p:Person {name: name})
MERGE (p)-[:WROTE]->(movie)
"""

LOAD_RATINGS = """
UNWIND $ratings AS r
MATCH (movie:Movie {title: r.movie})
MERGE (u:User {name: r.user})
MERGE (u)-[rated:RATED]->(movie)
SET rated.stars = r.stars
"""


def read_data() -> tuple[list[dict], list[dict]]:
    movies = json.loads((DATA_DIR / "movies.json").read_text(encoding="utf-8"))
    ratings = json.loads((DATA_DIR / "ratings.json").read_text(encoding="utf-8"))
    return movies, ratings


def reset() -> None:
    """Delete every node and relationship. Handy when experimenting."""
    run("MATCH (n) DETACH DELETE n")


def load_all(verbose: bool = True) -> None:
    movies, ratings = read_data()

    for c in CONSTRAINTS:
        run(c)

    steps = [
        ("movies", LOAD_MOVIES, {"movies": movies}),
        ("genres", LOAD_GENRES, {"movies": movies}),
        ("cast", LOAD_CAST, {"movies": movies}),
        ("directors", LOAD_DIRECTORS, {"movies": movies}),
        ("writers", LOAD_WRITERS, {"movies": movies}),
        ("ratings", LOAD_RATINGS, {"ratings": ratings}),
    ]
    for name, query, params in steps:
        _, summary = run_with_summary(query, **params)
        c = summary.counters
        if verbose:
            print(f"  {name:<10} +{c.nodes_created} nodes, +{c.relationships_created} relationships")


if __name__ == "__main__":
    load_all()
