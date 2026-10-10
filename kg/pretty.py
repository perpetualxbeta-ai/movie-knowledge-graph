"""Print query results as a readable table in the terminal."""

from __future__ import annotations

from neo4j.graph import Node, Path, Relationship


def _fmt(value) -> str:
    if isinstance(value, Node):
        label = ":".join(sorted(value.labels))
        name = value.get("title") or value.get("name") or value.element_id
        return f"({label} {name})"
    if isinstance(value, Relationship):
        return f"-[:{value.type}]->"
    if isinstance(value, Path):
        parts = []
        for i, node in enumerate(value.nodes):
            parts.append(_fmt(node))
            if i < len(value.relationships):
                rel = value.relationships[i]
                arrow = f"-[:{rel.type}]->" if rel.start_node == node else f"<-[:{rel.type}]-"
                parts.append(arrow)
        return " ".join(parts)
    if isinstance(value, list):
        return ", ".join(_fmt(v) for v in value)
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def show(records, title: str | None = None, max_width: int = 60) -> None:
    """Print a list of records (from kg.db.run) as a simple table."""
    if title:
        print(f"\n=== {title} ===")
    if not records:
        print("(no rows)")
        return
    keys = list(records[0].keys())
    rows = [[_fmt(r[k])[:max_width] for k in keys] for r in records]
    widths = [max(len(k), *(len(row[i]) for row in rows)) for i, k in enumerate(keys)]
    print("  ".join(k.ljust(w) for k, w in zip(keys, widths)))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print("  ".join(c.ljust(w) for c, w in zip(row, widths)))
    print(f"({len(rows)} row{'s' if len(rows) != 1 else ''})")
