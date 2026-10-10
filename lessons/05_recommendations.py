"""
LESSON 5 — Recommendations with explanations
============================================
Run:  python lessons/05_recommendations.py [UserName]      (default: Aisha)

Two classic approaches, both just graph patterns:

  CONTENT-BASED   "You liked X; Y shares a director / actor / genre with X."
                  (user)-[:RATED]->(liked)-[]-(thing)-[]-(rec)

  COLLABORATIVE   "People who liked what you liked also liked Y."
                  (user)-[:RATED]->(m)<-[:RATED]-(peer)-[:RATED]->(rec)

A big advantage of knowledge graphs: the path that produced a recommendation
*is* the explanation, so we can return it alongside the score.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from kg import run, show

user = sys.argv[1] if len(sys.argv) > 1 else "Aisha"

show(run("""
    MATCH (:User {name: $user})-[r:RATED]->(m:Movie)
    RETURN m.title AS movie, r.stars AS stars ORDER BY stars DESC
""", user=user), f"What {user} rated")

# 1. Content-based: score unseen movies by how much they share with movies the user liked (4+ stars).
#    People connections count more than genres, because they're more specific.
show(run("""
    MATCH (u:User {name: $user})-[r:RATED]->(liked:Movie) WHERE r.stars >= 4
    MATCH (liked)-[:ACTED_IN|DIRECTED|WROTE|IN_GENRE]-(thing)-[:ACTED_IN|DIRECTED|WROTE|IN_GENRE]-(rec:Movie)
    WHERE NOT (u)-[:RATED]->(rec) AND rec <> liked
    WITH rec,
         sum(CASE WHEN thing:Genre THEN 1 ELSE 3 END) AS score,
         collect(DISTINCT coalesce(thing.name, thing.title)) AS because
    RETURN rec.title AS recommendation, score, because[0..4] AS sharedWith
    ORDER BY score DESC, recommendation
    LIMIT 5
""", user=user), f"Content-based picks for {user}", max_width=80)

# 2. Collaborative: find peers who rated the same movies similarly, then borrow their favourites.
show(run("""
    MATCH (u:User {name: $user})-[r1:RATED]->(m:Movie)<-[r2:RATED]-(peer:User)
    WHERE abs(r1.stars - r2.stars) <= 1
    WITH u, peer, count(m) AS overlap
    MATCH (peer)-[r:RATED]->(rec:Movie)
    WHERE r.stars >= 4 AND NOT (u)-[:RATED]->(rec)
    RETURN rec.title AS recommendation,
           sum(overlap * r.stars) AS score,
           collect(peer.name) AS likedBy
    ORDER BY score DESC, recommendation
    LIMIT 5
""", user=user), f"Collaborative picks for {user}")

print("\nTry other users: Ben, Chloe, Daniel, Elena, Farhan")
print("Next: python lessons/06_your_turn.py")
