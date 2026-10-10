"""
LESSON 6 — Your turn
====================
Run:  python lessons/06_your_turn.py

Fill in each TODO query, then run the file. Each exercise prints a ✔ or ✘.
Stuck? Peek at solutions/06_solutions.py — or ask Claude to give you a hint
(not the answer!). Try writing queries in the Aura console first; it's faster to iterate.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from kg import run, show

# Exercise 1 — Which movies did Christopher Nolan direct? Return `title`, sorted by release year.
EX1 = """
// TODO
"""

# Exercise 2 — Which actors have worked with BOTH Christopher Nolan (as director) and Matt Damon (as co-star)?
# Return `actor`. Hint: two MATCH clauses about the same person.
EX2 = """
// TODO
"""

# Exercise 3 — For each genre, how many movies? Return `genre` and `movies`, most first.
EX3 = """
// TODO
"""

# Exercise 4 — WRITE to the graph: add a movie you like, with at least one actor and one genre,
# using MERGE so it's safe to re-run. Then return the new movie's `title`.
# (e.g. "Dune" (2021), Timothée Chalamet as Paul Atreides, genre Sci-Fi)
EX4 = """
// TODO
"""

# Exercise 5 — Which pair of actors appears together in the most movies?
# Return `actor1`, `actor2`, `together`. Avoid listing each pair twice (hint: a.name < b.name).
EX5 = """
// TODO
"""


def check(n, query, test, **params):
    if "TODO" in query:
        print(f"Exercise {n}: not attempted yet")
        return
    try:
        rows = run(query, **params)
    except Exception as e:  # show Cypher errors without a giant traceback
        print(f"Exercise {n}: ✘ Cypher error → {e}")
        return
    show(rows, f"Exercise {n}")
    print("✔ looks right!" if test(rows) else "✘ not quite — compare with what you expected")


check(1, EX1, lambda r: [x["title"] for x in r][:2] == ["Batman Begins", "The Prestige"])
check(2, EX2, lambda r: {x["actor"] for x in r} >= {"Jessica Chastain", "Cillian Murphy"})
check(3, EX3, lambda r: r[0]["genre"] == "Drama")
check(4, EX4, lambda r: len(r) == 1 and "title" in r[0].keys())
check(5, EX5, lambda r: r[0]["together"] == 2)
