import spacy

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")

# Read text file with movies and add them to a dictionary
with open("movies.txt", "r") as f:
    movies = {}
    for line in f:
        parts = line.strip().split(":")
        movies[parts[0]] = parts[1]

# Defines the function that takes in a description and returns the most similar movie title
def find_similar_movie(description):
    description_doc = nlp(description)
    # Variables to keep track of values while running the for loop
    max_similarity = 0
    most_similar_movie = ""
    # For loop that goes through each movie on the list
    # compares it to the description of another movie
    # and return the most similar one as a result
    for movie, plot in movies.items():
        plot_doc = nlp(plot)
        similarity = description_doc.similarity(plot_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie
    return most_similar_movie

# Description of movie and print out result
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(f"Most similar movie to watch is {find_similar_movie(description)}")
