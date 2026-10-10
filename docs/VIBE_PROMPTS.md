# Prompts for vibe coding your next steps

Paste these into Claude Code (or your AI tool of choice) from the repo folder. They go roughly
from easy to ambitious. A good habit: after each one, ask *"explain the Cypher you wrote, line by line."*

## Grow the graph
- "Add 10 more movies to `data/movies.json` that connect to existing actors, keep the tests passing, and reload."
- "Add a `born` year to Person nodes for the actors, then write a lesson query for the oldest director of each genre."
- "Add a new relationship `(:Person)-[:PRODUCED]->(:Movie)` end to end: data, loader, CLAUDE.md, README diagram."
- "Model awards: `(:Movie)-[:WON]->(:Award {name, year})`. Which actors have been in the most award-winning films?"

## Ask better questions
- "Write a lesson on `WITH` — chaining query steps — using our movie data, with 4 examples that build on each other."
- "Find 'bridge' actors whose removal would disconnect parts of the co-star graph. Explain the idea first."
- "Show me the difference between `MATCH` and `OPTIONAL MATCH` with a query where it changes the answer."
- "Profile my slowest query with `PROFILE` and explain what the plan means."

## See it
- "Build a small Streamlit app: pick an actor, show their neighbourhood as an interactive graph (pyvis)."
- "Make a CLI: `python cli.py bacon 'Tom Cruise'` prints the shortest path to Kevin Bacon."

## Turn text into a knowledge graph
- "Write a script that takes a paragraph of text, uses an LLM to extract (entity, relation, entity) triples as JSON,
   and MERGEs them into Neo4j. Start with 3 Wikipedia-style paragraphs about films."
- "Add entity resolution: before creating a Person, check for near-duplicate names ('Leo DiCaprio' vs 'Leonardo DiCaprio')."

## GraphRAG (knowledge graph + LLM)
- "Build a question-answering script: an LLM writes Cypher from a natural-language question using our schema,
   we run it, and the LLM answers from the results. Add guardrails so it can only read, never write."
- "Add vector embeddings to Movie nodes (a short plot summary each), create a Neo4j vector index,
   and combine similarity search with graph traversal for recommendations."

## Bring your own domain
- "Help me design a graph model for <my topic>. Ask me questions first, then propose labels and relationships,
   then create `data/<topic>.json` and a loader like `kg/load.py`."
