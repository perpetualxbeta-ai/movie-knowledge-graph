// Paste into Aura console → Query and click Run. Safe to run twice (MERGE).
WITH [
  {t: "The Matrix", y: 1999, g: ["Sci-Fi", "Action"], d: ["Lana Wachowski", "Lilly Wachowski"], w: ["Lana Wachowski", "Lilly Wachowski"], c: [["Keanu Reeves", "Neo"], ["Carrie-Anne Moss", "Trinity"], ["Laurence Fishburne", "Morpheus"], ["Hugo Weaving", "Agent Smith"]]},
  {t: "The Matrix Reloaded", y: 2003, g: ["Sci-Fi", "Action"], d: ["Lana Wachowski", "Lilly Wachowski"], w: ["Lana Wachowski", "Lilly Wachowski"], c: [["Keanu Reeves", "Neo"], ["Carrie-Anne Moss", "Trinity"], ["Laurence Fishburne", "Morpheus"], ["Hugo Weaving", "Agent Smith"]]},
  {t: "John Wick", y: 2014, g: ["Action", "Thriller"], d: ["Chad Stahelski"], w: [], c: [["Keanu Reeves", "John Wick"], ["Willem Dafoe", "Marcus"]]},
  {t: "Speed", y: 1994, g: ["Action", "Thriller"], d: ["Jan de Bont"], w: [], c: [["Keanu Reeves", "Jack Traven"], ["Sandra Bullock", "Annie Porter"], ["Dennis Hopper", "Howard Payne"]]},
  {t: "The Lake House", y: 2006, g: ["Romance", "Drama"], d: ["Alejandro Agresti"], w: [], c: [["Keanu Reeves", "Alex Wyler"], ["Sandra Bullock", "Kate Forster"]]},
  {t: "Gravity", y: 2013, g: ["Sci-Fi", "Thriller"], d: ["Alfonso Cuarón"], w: ["Alfonso Cuarón"], c: [["Sandra Bullock", "Ryan Stone"], ["George Clooney", "Matt Kowalski"]]},
  {t: "Ocean's Eleven", y: 2001, g: ["Crime", "Thriller"], d: ["Steven Soderbergh"], w: [], c: [["George Clooney", "Danny Ocean"], ["Brad Pitt", "Rusty Ryan"], ["Julia Roberts", "Tess Ocean"], ["Matt Damon", "Linus Caldwell"]]},
  {t: "Fight Club", y: 1999, g: ["Drama"], d: ["David Fincher"], w: [], c: [["Brad Pitt", "Tyler Durden"], ["Edward Norton", "The Narrator"], ["Helena Bonham Carter", "Marla Singer"]]},
  {t: "Se7en", y: 1995, g: ["Crime", "Thriller"], d: ["David Fincher"], w: [], c: [["Brad Pitt", "David Mills"], ["Morgan Freeman", "William Somerset"]]},
  {t: "The Shawshank Redemption", y: 1994, g: ["Drama"], d: ["Frank Darabont"], w: ["Frank Darabont"], c: [["Tim Robbins", "Andy Dufresne"], ["Morgan Freeman", "Red"]]},
  {t: "The Green Mile", y: 1999, g: ["Drama", "Fantasy"], d: ["Frank Darabont"], w: ["Frank Darabont"], c: [["Tom Hanks", "Paul Edgecomb"], ["Michael Clarke Duncan", "John Coffey"]]},
  {t: "Forrest Gump", y: 1994, g: ["Drama", "Romance"], d: ["Robert Zemeckis"], w: [], c: [["Tom Hanks", "Forrest Gump"], ["Robin Wright", "Jenny Curran"], ["Gary Sinise", "Lt. Dan Taylor"]]},
  {t: "Cast Away", y: 2000, g: ["Drama", "Adventure"], d: ["Robert Zemeckis"], w: [], c: [["Tom Hanks", "Chuck Noland"], ["Helen Hunt", "Kelly Frears"]]},
  {t: "Apollo 13", y: 1995, g: ["Drama", "History"], d: ["Ron Howard"], w: [], c: [["Tom Hanks", "Jim Lovell"], ["Kevin Bacon", "Jack Swigert"], ["Bill Paxton", "Fred Haise"], ["Gary Sinise", "Ken Mattingly"], ["Ed Harris", "Gene Kranz"]]},
  {t: "Saving Private Ryan", y: 1998, g: ["War", "Drama"], d: ["Steven Spielberg"], w: [], c: [["Tom Hanks", "Captain John Miller"], ["Matt Damon", "Private James Ryan"]]},
  {t: "Good Will Hunting", y: 1997, g: ["Drama"], d: ["Gus Van Sant"], w: ["Matt Damon", "Ben Affleck"], c: [["Matt Damon", "Will Hunting"], ["Robin Williams", "Sean Maguire"], ["Ben Affleck", "Chuckie Sullivan"]]},
  {t: "The Martian", y: 2015, g: ["Sci-Fi", "Adventure"], d: ["Ridley Scott"], w: [], c: [["Matt Damon", "Mark Watney"], ["Jessica Chastain", "Melissa Lewis"]]},
  {t: "Interstellar", y: 2014, g: ["Sci-Fi", "Drama"], d: ["Christopher Nolan"], w: ["Christopher Nolan", "Jonathan Nolan"], c: [["Matthew McConaughey", "Cooper"], ["Anne Hathaway", "Brand"], ["Jessica Chastain", "Murph"], ["Matt Damon", "Dr. Mann"]]},
  {t: "Inception", y: 2010, g: ["Sci-Fi", "Action"], d: ["Christopher Nolan"], w: ["Christopher Nolan"], c: [["Leonardo DiCaprio", "Cobb"], ["Joseph Gordon-Levitt", "Arthur"], ["Elliot Page", "Ariadne"], ["Tom Hardy", "Eames"], ["Cillian Murphy", "Robert Fischer"], ["Michael Caine", "Miles"]]},
  {t: "The Departed", y: 2006, g: ["Crime", "Thriller"], d: ["Martin Scorsese"], w: [], c: [["Leonardo DiCaprio", "Billy Costigan"], ["Matt Damon", "Colin Sullivan"], ["Jack Nicholson", "Frank Costello"]]},
  {t: "Catch Me If You Can", y: 2002, g: ["Crime", "Drama"], d: ["Steven Spielberg"], w: [], c: [["Leonardo DiCaprio", "Frank Abagnale Jr."], ["Tom Hanks", "Carl Hanratty"]]},
  {t: "Titanic", y: 1997, g: ["Romance", "Drama"], d: ["James Cameron"], w: ["James Cameron"], c: [["Leonardo DiCaprio", "Jack Dawson"], ["Kate Winslet", "Rose DeWitt Bukater"]]},
  {t: "Footloose", y: 1984, g: ["Drama", "Music"], d: ["Herbert Ross"], w: [], c: [["Kevin Bacon", "Ren McCormack"], ["John Lithgow", "Rev. Shaw Moore"]]},
  {t: "A Few Good Men", y: 1992, g: ["Drama"], d: ["Rob Reiner"], w: ["Aaron Sorkin"], c: [["Tom Cruise", "Lt. Daniel Kaffee"], ["Jack Nicholson", "Col. Nathan R. Jessup"], ["Demi Moore", "Lt. Cdr. JoAnne Galloway"], ["Kevin Bacon", "Capt. Jack Ross"]]},
  {t: "Top Gun", y: 1986, g: ["Action"], d: ["Tony Scott"], w: [], c: [["Tom Cruise", "Maverick"], ["Val Kilmer", "Iceman"]]},
  {t: "Mystic River", y: 2003, g: ["Crime", "Drama"], d: ["Clint Eastwood"], w: [], c: [["Sean Penn", "Jimmy Markum"], ["Tim Robbins", "Dave Boyle"], ["Kevin Bacon", "Sean Devine"]]},
  {t: "Edge of Tomorrow", y: 2014, g: ["Sci-Fi", "Action"], d: ["Doug Liman"], w: [], c: [["Tom Cruise", "Cage"], ["Emily Blunt", "Rita Vrataski"]]},
  {t: "Oppenheimer", y: 2023, g: ["Drama", "History"], d: ["Christopher Nolan"], w: ["Christopher Nolan"], c: [["Cillian Murphy", "J. Robert Oppenheimer"], ["Emily Blunt", "Kitty Oppenheimer"], ["Matt Damon", "Leslie Groves"], ["Robert Downey Jr.", "Lewis Strauss"]]},
  {t: "Batman Begins", y: 2005, g: ["Action", "Crime"], d: ["Christopher Nolan"], w: ["Christopher Nolan"], c: [["Christian Bale", "Bruce Wayne"], ["Michael Caine", "Alfred"], ["Cillian Murphy", "Jonathan Crane"], ["Morgan Freeman", "Lucius Fox"]]},
  {t: "The Prestige", y: 2006, g: ["Drama", "Mystery"], d: ["Christopher Nolan"], w: ["Christopher Nolan", "Jonathan Nolan"], c: [["Christian Bale", "Alfred Borden"], ["Hugh Jackman", "Robert Angier"], ["Michael Caine", "Cutter"]]}
] AS movies
UNWIND movies AS m
MERGE (mv:Movie {title: m.t}) SET mv.released = m.y
FOREACH (g IN m.g | MERGE (gn:Genre {name: g}) MERGE (mv)-[:IN_GENRE]->(gn))
FOREACH (n IN m.d | MERGE (p:Person {name: n}) MERGE (p)-[:DIRECTED]->(mv))
FOREACH (n IN m.w | MERGE (p:Person {name: n}) MERGE (p)-[:WROTE]->(mv))
FOREACH (c IN m.c | MERGE (p:Person {name: c[0]}) MERGE (p)-[r:ACTED_IN]->(mv) SET r.roles = [c[1]])
RETURN count(mv) AS moviesLoaded
