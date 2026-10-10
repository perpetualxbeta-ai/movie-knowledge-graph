// Step 2 (optional, for recommendations): user ratings
UNWIND [["Aisha", "The Matrix", 5], ["Aisha", "Inception", 5], ["Aisha", "Interstellar", 4], ["Aisha", "Edge of Tomorrow", 4], ["Aisha", "Titanic", 2], ["Ben", "The Matrix", 5], ["Ben", "Inception", 4], ["Ben", "The Martian", 5], ["Ben", "Gravity", 4], ["Ben", "John Wick", 5], ["Chloe", "Forrest Gump", 5], ["Chloe", "Titanic", 5], ["Chloe", "The Lake House", 4], ["Chloe", "Cast Away", 4], ["Chloe", "The Green Mile", 5], ["Daniel", "Se7en", 5], ["Daniel", "The Departed", 5], ["Daniel", "Mystic River", 4], ["Daniel", "Fight Club", 4], ["Daniel", "Ocean's Eleven", 3], ["Elena", "Interstellar", 5], ["Elena", "The Prestige", 5], ["Elena", "Oppenheimer", 4], ["Elena", "Batman Begins", 4], ["Elena", "Inception", 5], ["Farhan", "The Shawshank Redemption", 5], ["Farhan", "The Green Mile", 4], ["Farhan", "Forrest Gump", 4], ["Farhan", "Apollo 13", 5], ["Farhan", "Saving Private Ryan", 5]] AS r
MATCH (m:Movie {title: r[1]})
MERGE (u:User {name: r[0]})
MERGE (u)-[x:RATED]->(m) SET x.stars = r[2]
RETURN count(x) AS ratingsLoaded
