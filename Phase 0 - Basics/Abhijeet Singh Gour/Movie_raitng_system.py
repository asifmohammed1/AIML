# Empty list to store data
Movies = []

# Add movies
def add_movie(movie_list, title, director, year, rating):
    movie_list.append({
        "title": title,
        "director": director,
        "year": year,
        "rating": rating
    })

add_movie(Movies, "Sinners", "Ryan Coogler", 2025, 4.6)
add_movie(Movies, "Forrest Gump", "Robert Zemeckis", 1994, 4.9)
add_movie(Movies, "Saving Private Ryan", "Steven Spielberg", 1998, 4.8)
add_movie(Movies, "Fury", "David Ayer", 2014, 4.7)

print("\nMovies list:")
for m in Movies:
    print(m["title"], "-", m["rating"])


# Update rating
def update_rating(movie_list, title, new_rating):
    for movie in movie_list:
        if movie["title"].lower() == title.lower():
            movie["rating"] = new_rating
            return "Rating updated"
    return "Movie not found"

print("\nUpdate rating result:")
print(update_rating(Movies, "Sinners", 4.7))


print("\nMovies after rating update:")
for m in Movies:
    print(m["title"], "-", m["rating"])


# Average rating
def average_rating(movie_list):
    if len(movie_list) == 0:
        return 0

    total = 0
    for movie in movie_list:
        total += movie["rating"]

    return total / len(movie_list)

print("\nAverage rating of all movies:", average_rating(Movies))


# Highest rated movie
def highest_rated_movie(movie_list):
    highest = movie_list[0]

    for movie in movie_list:
        if movie["rating"] > highest["rating"]:
            highest = movie

    return highest["title"], highest["rating"]

title, rating = highest_rated_movie(Movies)
print("\nHighest rated movie:")
print(title, "-", rating)


# Sort movies by rating (descending)
def sort_movies_by_rating(movie_list):
    return sorted(movie_list, key=lambda m: m["rating"], reverse=True)

print("\nMovies sorted by rating:")
for m in sort_movies_by_rating(Movies):
    print(m["title"], "-", m["rating"])


# Filter movies by year
def filter_movies_by_year(movie_list, year):
    result = []
    for movie in movie_list:
        if movie["year"] == year:
            result.append(movie)
    return result

print("\nMovies released in 2014:")
for m in filter_movies_by_year(Movies, 2014):
    print(m["title"])


# Outputs:

# Movies list:
# Sinners - 4.6
# Forrest Gump - 4.9
# Saving Private Ryan - 4.8
# Fury - 4.7

# Update rating result:
# Rating updated

# Movies after rating update:
# Sinners - 4.7
# Forrest Gump - 4.9
# Saving Private Ryan - 4.8
# Fury - 4.7

# Average rating of all movies: 4.775

# Highest rated movie:
# Forrest Gump - 4.9

# Movies sorted by rating:
# Forrest Gump - 4.9
# Saving Private Ryan - 4.8
# Sinners - 4.7
# Fury - 4.7

# Movies released in 2014:
# Fury
