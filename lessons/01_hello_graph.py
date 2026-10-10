"""
LESSON 1 — Hello, graph
=======================
Run:  python lessons/01_hello_graph.py

A knowledge graph stores facts as:
  * NODES          things   e.g. (:Person {name: "Keanu Reeves"})
  * RELATIONSHIPS  how things connect, always with a type and a direction
                            e.g. (keanu)-[:ACTED_IN]->(matrix)
  * PROPERTIES     key/value details on either one, e.g. {released: 1999}
  * LABELS         a node's category, e.g. :Person, :Movie

Cypher, Neo4j's query language, draws those shapes with ASCII art:
  ()          a node            (p:Person)          a node labelled Person, named p in the query
  -[]->       a relationship    -[:ACTED_IN]->      of type ACTED_IN
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from kg import get_driver, run, run_with_summary, show

# 1. Can we reach the database at all?
get_driver().verify_connectivity()
print("Connected to Neo4j ✔")

# 2. Write: create two nodes and one relationship.
#    MERGE = "match it if it exists, otherwise create it", so re-running is safe.
_, summary = run_with_summary(
    """
    MERGE (me:Learner {name: $name})
    MERGE (topic:Topic {name: 'Knowledge Graphs'})
    MERGE (me)-[r:IS_LEARNING]->(topic)
    ON CREATE SET r.since = date()      // only set the first time it's created
    """,
    name="perpetualxbeta",
)
c = summary.counters
print(f"Created {c.nodes_created} nodes and {c.relationships_created} relationships "
      "(0 if you've run this before — that's MERGE at work)")

# 3. Read it back with a pattern match.
rows = run(
    """
    MATCH (l:Learner)-[r:IS_LEARNING]->(t:Topic)
    RETURN l.name AS learner, type(r) AS relationship, t.name AS topic, r.since AS since
    """
)
show(rows, "What's in the graph")

# 4. Tidy up so the next lessons start with only movie data.
run("MATCH (n) WHERE n:Learner OR n:Topic DETACH DELETE n")
print("\nCleaned up. Next: python lessons/02_load_movies.py")

# TRY IT: open your Aura console → Query, and run:
#   MERGE (a:Learner {name:'you'})-[:LIKES]->(:Topic {name:'Graphs'}) RETURN *
# You'll see the result drawn as a picture. Then delete it with:
#   MATCH (n) WHERE n:Learner OR n:Topic DETACH DELETE n
