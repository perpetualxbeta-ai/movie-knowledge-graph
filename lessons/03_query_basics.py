"""
LESSON 3 — Asking questions with Cypher
=======================================
Run:  python lessons/03_query_basics.py

The shape of almost every read query:
    MATCH  <pattern>          find subgraphs that look like this
    WHERE  <filter>           keep only some of them
    RETURN <what>             pick columns (aggregations like count() group automatically)
    ORDER BY … LIMIT …
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from kg import run, show

# 1. One hop: what did Keanu act in?
show(run("""
    MATCH (p:Person {name: $name})-[r:ACTED_IN]->(m:Movie)
    RETURN m.title AS movie, m.released AS year, r.roles AS roles
    ORDER BY year
""", name="Keanu Reeves"), "Keanu Reeves' movies")

# 2. Filtering with WHERE
show(run("""
    MATCH (m:Movie)
    WHERE m.released >= 2010
    RETURN m.title AS movie, m.released AS year
    ORDER BY year
"""), "Movies from 2010 onwards")

# 3. Aggregation: count() groups by the other returned columns (no GROUP BY needed)
show(run("""
    MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
    RETURN p.name AS actor, count(m) AS movies
    ORDER BY movies DESC, actor
    LIMIT 5
"""), "Busiest actors")

# 4. Two hops through a shared node: who has Tom Hanks acted with?
#    (tom)-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActor)   ← arrows can point either way
show(run("""
    MATCH (:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(co:Person)
    RETURN co.name AS coActor, collect(m.title) AS together
    ORDER BY size(together) DESC, coActor
"""), "Tom Hanks' co-stars")

# 5. Several relationship types at once, and the same person in two roles
show(run("""
    MATCH (p:Person)-[:DIRECTED]->(m:Movie)<-[:WROTE]-(p)
    RETURN p.name AS writerDirector, collect(m.title) AS movies
"""), "People who wrote AND directed the same movie")

# 6. Going through Genre nodes
show(run("""
    MATCH (d:Person)-[:DIRECTED]->(m:Movie)-[:IN_GENRE]->(g:Genre {name: 'Sci-Fi'})
    RETURN d.name AS director, count(m) AS sciFiMovies
    ORDER BY sciFiMovies DESC
"""), "Sci-Fi directors")

# 7. OPTIONAL MATCH: like a LEFT JOIN — keep the movie even if nobody rated it
show(run("""
    MATCH (m:Movie)
    OPTIONAL MATCH (u:User)-[r:RATED]->(m)
    RETURN m.title AS movie, count(r) AS ratings, round(avg(r.stars), 1) AS avgStars
    ORDER BY ratings ASC, movie
    LIMIT 8
"""), "Least-rated movies")

print("\nNext: python lessons/04_paths.py")
