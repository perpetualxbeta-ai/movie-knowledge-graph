"""
LESSON 4 — Paths: where graphs beat tables
==========================================
Run:  python lessons/04_paths.py

In SQL, "friends of friends of friends" means stacking JOINs. In Cypher you
write the length of the walk directly:

    -[:ACTED_IN*2]-       exactly 2 hops
    -[:ACTED_IN*1..4]-    between 1 and 4 hops
    shortestPath(...)     the fewest hops between two nodes

Leaving out the arrow head (-[]- instead of -[]->) means "either direction".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from kg import run, show

# 1. Six Degrees of Kevin Bacon: the shortest chain of shared movies.
show(run("""
    MATCH (a:Person {name: $start}), (b:Person {name: 'Kevin Bacon'})
    MATCH p = shortestPath((a)-[:ACTED_IN*..12]-(b))
    RETURN length(p) / 2 AS baconNumber, p AS path
""", start="Keanu Reeves"), "Keanu Reeves → Kevin Bacon", max_width=400)
# Each "step" is actor → movie → actor, i.e. 2 relationships, hence length(p) / 2.

# 2. Everyone's Bacon number
show(run("""
    MATCH (bacon:Person {name: 'Kevin Bacon'}), (p:Person)
    WHERE p <> bacon AND (p)-[:ACTED_IN]->()
    MATCH path = shortestPath((p)-[:ACTED_IN*..20]-(bacon))
    RETURN length(path) / 2 AS baconNumber, collect(p.name) AS actors
    ORDER BY baconNumber
"""), "Bacon numbers", max_width=200)

# 3. Variable-length: everyone within 2 co-star steps of Leonardo DiCaprio
show(run("""
    MATCH (:Person {name: 'Leonardo DiCaprio'})-[:ACTED_IN*1..4]-(p:Person)
    WHERE p.name <> 'Leonardo DiCaprio'
    RETURN DISTINCT p.name AS reachable
    ORDER BY reachable
"""), "Within 2 co-star steps of DiCaprio")

# 4. Any relationship type: how are Christopher Nolan and Steven Spielberg connected?
show(run("""
    MATCH (a:Person {name: 'Christopher Nolan'}), (b:Person {name: 'Steven Spielberg'})
    MATCH p = allShortestPaths((a)-[:ACTED_IN|DIRECTED|WROTE*..10]-(b))
    RETURN p AS path
    LIMIT 5
"""), "Nolan ↔ Spielberg", max_width=400)

print("\nIn the Aura console, paths look great drawn as pictures. Try:")
print("  MATCH p = shortestPath((:Person {name:'Keanu Reeves'})-[*..12]-(:Person {name:'Kevin Bacon'})) RETURN p")
print("\nNext: python lessons/05_recommendations.py")
