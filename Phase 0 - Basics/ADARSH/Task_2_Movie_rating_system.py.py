# Movie Rating System

# Movie list (list of dictionaries)
movies = []

# PART 1: Add a Movie

def add_movie(title, year, rating):
    movie = {
        "title": title,
        "year": year,
        "rating": rating
    }
    movies.append(movie)
    return movies


# PART 2: Add Rating to a Movie

def add_rating(title, new_rating):
    for movie in movies:
        if movie["title"] == title:
            movie["rating"] = new_rating
            return "Rating updated"
    return "Movie not found"


# Calculate Average Rating

def average_rating():
    total = 0
    for movie in movies:
        total += movie["rating"]
    return total / len(movies)



# Find Highest Rated Movie

def highest_rated_movie():
    highest = movies[0]
    for movie in movies:
        if movie["rating"] > highest["rating"]:
            highest = movie
    return highest["title"], highest["rating"]



# PART 3: Sort Movies by Rating

def list_movies_by_rating():
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return sorted_movies



# Filter Movies by Year

def filter_by_year(year):
    result = []
    for movie in movies:
        if movie["year"] == year:
            result.append(movie)
    return result



# BONUS: Palindrome Check

def is_palindrome(title):
    title = title.lower().replace(" ", "")
    return title == title[::-1]


# SAMPLE INPUT

add_movie("Uri",  2019, 8.2)
add_movie("Article 370",  2024, 7.8)
add_movie("Madam",  2020, 7.5)


# SAMPLE OUTPUT

print("All Movies:", movies)

print("Average Rating:", average_rating())

print("Highest Rated Movie:", highest_rated_movie())

print("Movies Sorted by Rating:", list_movies_by_rating())

print("Movies Released in 2020:", filter_by_year(2020))

print("Is 'Madam' Palindrome?:", is_palindrome("Madam"))
