"""
LESSON 2 — Build the knowledge graph
====================================
Run:  python lessons/02_load_movies.py          (add --reset to wipe the database first)

Read kg/load.py alongside this lesson. The key ideas:

  * MODEL FIRST. Decide your node labels and relationship types before loading:
        (:Person)-[:ACTED_IN {roles}]->(:Movie)-[:IN_GENRE]->(:Genre)
        (:Person)-[:DIRECTED|WROTE]->(:Movie)
        (:User)-[:RATED {stars}]->(:Movie)
    Rule of thumb: nouns become nodes, verbs become relationships.
    A genre is a node (not a text property) because we want to *traverse* through it.

  * CONSTRAINTS. "Every Movie title is unique" stops duplicates and adds an index.

  * UNWIND + MERGE. Send a whole list as one parameter, UNWIND turns it into rows,
    MERGE makes each node/relationship exactly once. Fast and idempotent.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from kg import run, show
from kg.load import load_all, reset

if "--reset" in sys.argv:
    print("Wiping database…")
    reset()

print("Loading movie graph:")
load_all()

show(
    run("MATCH (n) RETURN labels(n)[0] AS label, count(*) AS count ORDER BY count DESC"),
    "Nodes by label",
)
show(
    run("MATCH ()-[r]->() RETURN type(r) AS relationship, count(*) AS count ORDER BY count DESC"),
    "Relationships by type",
)

print("\nNow look at it! In the Aura console → Query, run:")
print("  CALL db.schema.visualization()")
print("  MATCH p=(:Person {name:'Keanu Reeves'})-[]->(:Movie) RETURN p")
print("\nNext: python lessons/03_query_basics.py")
