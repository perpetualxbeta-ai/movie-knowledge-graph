// Paste these into the Aura console → Query, one at a time.
// Queries that RETURN nodes or paths are drawn as a graph you can drag around.

// --- Look around -------------------------------------------------------------
CALL db.schema.visualization();                          // the model itself, as a picture
MATCH (n) RETURN labels(n) AS label, count(*) AS count;  // what's in here?
MATCH (n) RETURN n LIMIT 50;                             // a peek at everything

// --- One person's neighbourhood ----------------------------------------------
MATCH p = (:Person {name: 'Keanu Reeves'})-[]-() RETURN p;

// --- Two hops: co-stars ------------------------------------------------------
MATCH p = (:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(:Person)
RETURN p;

// --- A whole director's world ------------------------------------------------
MATCH p = (:Person {name: 'Christopher Nolan'})-[:DIRECTED]->(:Movie)<-[:ACTED_IN]-(:Person)
RETURN p;

// --- Six degrees of Kevin Bacon ----------------------------------------------
MATCH p = shortestPath(
  (:Person {name: 'Keanu Reeves'})-[:ACTED_IN*..12]-(:Person {name: 'Kevin Bacon'})
)
RETURN p;

// Newer Cypher syntax for the same thing (Neo4j 5.21+):
MATCH p = SHORTEST 1 (:Person {name: 'Keanu Reeves'})-[:ACTED_IN]-+(:Person {name: 'Kevin Bacon'})
RETURN p;

// --- Genres as hubs ----------------------------------------------------------
MATCH p = (:Movie)-[:IN_GENRE]->(:Genre {name: 'Sci-Fi'}) RETURN p;

// --- Users and what they rated -----------------------------------------------
MATCH p = (:User)-[:RATED]->(:Movie) RETURN p;

// --- Modify the graph --------------------------------------------------------
MERGE (m:Movie {title: 'Dune'}) SET m.released = 2021
MERGE (p:Person {name: 'Timothée Chalamet'})
MERGE (p)-[:ACTED_IN {roles: ['Paul Atreides']}]->(m)
RETURN p, m;

// Delete one thing (DETACH removes its relationships too)
MATCH (m:Movie {title: 'Dune'}) DETACH DELETE m;

// Nuke everything (then reload with: python lessons/02_load_movies.py)
// MATCH (n) DETACH DELETE n;
