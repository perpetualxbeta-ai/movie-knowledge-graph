"""Tiny wrapper around the official Neo4j Python driver.

Usage:
    from kg.db import run
    rows = run("MATCH (m:Movie) RETURN m.title AS title LIMIT $n", n=5)
    for row in rows:
        print(row["title"])

Connection details come from a `.env` file (see `.env.example`).
"""

from __future__ import annotations

import atexit
import os
import sys

from dotenv import load_dotenv
from neo4j import GraphDatabase, Driver

load_dotenv()

_driver: Driver | None = None


def _settings() -> tuple[str, str, str, str]:
    uri = os.getenv("NEO4J_URI")
    user = os.getenv("NEO4J_USERNAME", "neo4j")
    password = os.getenv("NEO4J_PASSWORD")
    database = os.getenv("NEO4J_DATABASE", "neo4j")
    if not uri or not password:
        sys.exit(
            "Missing Neo4j connection details.\n"
            "  1. Copy .env.example to .env\n"
            "  2. Paste in NEO4J_URI and NEO4J_PASSWORD from your Aura instance\n"
            "See README.md, step 1."
        )
    return uri, user, password, database


def get_driver() -> Driver:
    """Return one shared driver for the whole program (drivers are expensive to create)."""
    global _driver
    if _driver is None:
        uri, user, password, _ = _settings()
        _driver = GraphDatabase.driver(uri, auth=(user, password))
        atexit.register(_driver.close)
    return _driver


def run(query: str, **params):
    """Run one Cypher query and return a list of records.

    Each record behaves like a dict: row["title"], row.data(), etc.
    Always pass values as parameters ($name) instead of pasting them into the string —
    it is safer (no injection) and lets Neo4j cache the query plan.
    """
    _, _, _, database = _settings()
    records, _summary, _keys = get_driver().execute_query(query, params, database_=database)
    return records


def run_with_summary(query: str, **params):
    """Same as run(), but also returns the summary (counters: nodes created, etc.)."""
    _, _, _, database = _settings()
    records, summary, _keys = get_driver().execute_query(query, params, database_=database)
    return records, summary
