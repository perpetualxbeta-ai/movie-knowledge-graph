"""Sanity checks on data/*.json that need no database.  Run: python -m pytest -q"""
import sys, pathlib
from collections import Counter
from itertools import combinations

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from kg.load import read_data  # noqa: E402

movies, ratings = read_data()
titles = {m["title"] for m in movies}


def test_titles_unique():
    assert len(titles) == len(movies)


def test_every_movie_is_complete():
    for m in movies:
        assert isinstance(m["released"], int), m["title"]
        assert m["genres"] and m["directors"] and m["cast"], m["title"]
        for c in m["cast"]:
            assert c["name"] and c["role"], m["title"]


def test_ratings_point_at_real_movies():
    for r in ratings:
        assert r["movie"] in titles, r
        assert 1 <= r["stars"] <= 5, r


def test_exercise_answers_match_data():
    nolan = sorted((m for m in movies if "Christopher Nolan" in m["directors"]), key=lambda m: m["released"])
    assert [m["title"] for m in nolan][:2] == ["Batman Begins", "The Prestige"]

    genre_counts = Counter(g for m in movies for g in m["genres"])
    assert genre_counts.most_common(1)[0][0] == "Drama"

    pairs = Counter()
    for m in movies:
        for a, b in combinations(sorted(c["name"] for c in m["cast"]), 2):
            pairs[(a, b)] += 1
    assert max(pairs.values()) == 2


def test_kevin_bacon_reachable_from_keanu():
    graph = {}
    for m in movies:
        for c in m["cast"]:
            graph.setdefault(c["name"], set()).add(m["title"])
            graph.setdefault(m["title"], set()).add(c["name"])
    seen, frontier, hops = {"Keanu Reeves"}, {"Keanu Reeves"}, 0
    while "Kevin Bacon" not in frontier and frontier:
        frontier = {n for f in frontier for n in graph[f]} - seen
        seen |= frontier
        hops += 1
    assert "Kevin Bacon" in frontier
    print("Keanu's Bacon number:", hops // 2)
