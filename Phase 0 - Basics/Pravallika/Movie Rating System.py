Problem Statement:
You need to build a Movie Rating System that allows users to add movies and rate them, calculate the average rating of all movies, and find the highest-rated movie.

movies = [
    {"title": "Mayabazar",              "director": "K. V. Reddy",          "year": 1957, "rating": 9.2},
    {"title": "Sita Ramam",             "director": "Hanu Raghavapudi",    "year": 2022, "rating": 8.8},
    {"title": "Baahubali 2: The Conclusion", "director": "S. S. Rajamouli", "year": 2017, "rating": 8.2},
    {"title": "Kalki 2898 AD",          "director": "Nag Ashwin",          "year": 2024, "rating": 7.0},
    {"title": "Lucky Baskhar",          "director": "Venky Atluri",        "year": 2024, "rating": 8.0},
    {"title": "Hanu-Man",               "director": "Prasanth Varma",      "year": 2024, "rating": 7.7},
]
# Part 1 – Add Movie
def add_movie(title, director, year, rating):
    """Add a new Telugu movie to the list."""
    movie = {
        "title": title,
        "director": director,
        "year": year,
        "rating": float(rating)
    }
    movies.append(movie)
    print(f"Added: {title} ({year}) by {director}")
    return movies
# Part 2 – Rating operations# 
def add_rating(title, new_rating):
    """Update rating for a Telugu movie by title (case-insensitive)."""
    for movie in movies:
        if movie["title"].lower() == title.lower():
            movie["rating"] = float(new_rating)
            print(f"Rating updated → '{movie['title']}' : {new_rating}")
            return True
    print(f"Movie '{title}' not found in Telugu database.")
    return False
def calculate_average_rating():
    """Average rating of all Telugu movies."""
    if not movies:
        return 0.0
    total = sum(m["rating"] for m in movies)
    return total / len(movies)
def find_highest_rated_movie():
    """Highest-rated Telugu movie title & rating."""
    if not movies:
        return None, None
    best = max(movies, key=lambda m: m["rating"])
    return best["title"], best["rating"]
# Part 3 – Sorting & Filtering
def list_movies_by_rating():
    """Show all Telugu movies sorted by rating (descending)."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    print("\nTelugu Movies Sorted by Rating (Highest to Lowest):")
    for m in sorted_movies:
        print(f"  {m['rating']:.1f} ★  |  {m['title']} ({m['year']})  - {m['director']}")
def filter_movies_by_year(year):
    """Filter Telugu movies by release year."""
    matches = [m for m in movies if m["year"] == year]
    if not matches:
        print(f"No Telugu movies found from {year}")
        return []
    print(f"\nTelugu Movies from {year}:")
    for m in matches:
        print(f"  {m['rating']:.1f} ★  |  {m['title']}  - {m['director']}")
    return matches
# Bonus – Palindrome check for title
def is_palindrome_title(title):
    """Check if Telugu movie title is palindrome (ignore spaces, case, punctuation)."""
    cleaned = ''.join(c.lower() for c in title if c.isalnum())
    is_pal = cleaned == cleaned[::-1]
    return is_pal
# Demo with Telugu Movies
print("Telugu Movie Database - Initial count:", len(movies))
print(f"Average rating: {calculate_average_rating():.2f} ★\n")
# Add a new recent Telugu movie
add_movie("Game Changer", "Shankar", 2025, 7.5)
# Update an existing rating (example)
add_rating("RRR", 8.0)
add_rating("Pushpa 2", 8.9)  # not present → shows message
# Find top movie
top_title, top_rating = find_highest_rated_movie()
print(f"\nHighest rated Telugu movie: {top_title} → {top_rating} ★")
# Sorted list
list_movies_by_rating()
# Filter examples
filter_movies_by_year(2024)
filter_movies_by_year(1957)
# Bonus: palindrome check on some Telugu titles
for title in ["RRR", "Tenet", "Mayabazar", "Radar", "Sita Ramam"]:
    status = "Yes" if is_palindrome_title(title) else "No"
    print(f"Is '{title}' a palindrome title? {status}")

#output:
Telugu Movie Database - Initial count: 6
Average rating: 8.15 ★

Added: Game Changer (2025) by Shankar
Movie 'RRR' not found in Telugu database.
Movie 'Pushpa 2' not found in Telugu database.

Highest rated Telugu movie: Mayabazar → 9.2 ★
Telugu Movies Sorted by Rating (Highest to Lowest):
  9.2 ★  |  Mayabazar (1957)  - K. V. Reddy
  8.8 ★  |  Sita Ramam (2022)  - Hanu Raghavapudi
  8.2 ★  |  Baahubali 2: The Conclusion (2017)  - S. S. Rajamouli
  8.0 ★  |  Lucky Baskhar (2024)  - Venky Atluri
  7.7 ★  |  Hanu-Man (2024)  - Prasanth Varma
  7.5 ★  |  Game Changer (2025)  - Shankar
  7.0 ★  |  Kalki 2898 AD (2024)  - Nag Ashwin

Telugu Movies from 2024:
  7.0 ★  |  Kalki 2898 AD  - Nag Ashwin
  8.0 ★  |  Lucky Baskhar  - Venky Atluri
  7.7 ★  |  Hanu-Man  - Prasanth Varma

Telugu Movies from 1957:
  9.2 ★  |  Mayabazar  - K. V. Reddy
Is 'RRR' a palindrome title? Yes
Is 'Tenet' a palindrome title? Yes
Is 'Mayabazar' a palindrome title? No
Is 'Radar' a palindrome title? Yes
Is 'Sita Ramam' a palindrome title? No
