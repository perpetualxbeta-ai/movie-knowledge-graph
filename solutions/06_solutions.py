"""Solutions for lessons/06_your_turn.py — try first, peek second!"""

EX1 = """
MATCH (:Person {name: 'Christopher Nolan'})-[:DIRECTED]->(m:Movie)
RETURN m.title AS title
ORDER BY m.released
"""

EX2 = """
MATCH (:Person {name: 'Christopher Nolan'})-[:DIRECTED]->(:Movie)<-[:ACTED_IN]-(a:Person)
MATCH (a)-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(:Person {name: 'Matt Damon'})
RETURN DISTINCT a.name AS actor
ORDER BY actor
"""

EX3 = """
MATCH (m:Movie)-[:IN_GENRE]->(g:Genre)
RETURN g.name AS genre, count(m) AS movies
ORDER BY movies DESC, genre
"""

EX4 = """
MERGE (m:Movie {title: 'Dune'})
SET m.released = 2021
MERGE (p:Person {name: 'Timothée Chalamet'})
MERGE (p)-[r:ACTED_IN]->(m)
SET r.roles = ['Paul Atreides']
MERGE (g:Genre {name: 'Sci-Fi'})
MERGE (m)-[:IN_GENRE]->(g)
RETURN m.title AS title
"""

EX5 = """
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(b:Person)
WHERE a.name < b.name
RETURN a.name AS actor1, b.name AS actor2, count(m) AS together
ORDER BY together DESC, actor1, actor2
LIMIT 5
"""
