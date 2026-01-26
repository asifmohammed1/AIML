'''You need to build a Movie Rating System that allows users to add movies and rate them, calculate the average rating of all movies, and find the highest-rated movie.
Part 1: Data Structure Setup (Lists & Dictionaries)
Movie List:
Create a list of dictionaries where each dictionary represents a movie. Each movie should have:
title (string)
director (string)
year (integer)
rating (float)
Add a Movie:
Implement a function to add a new movie to the list. The function should accept the movie's details (title, director, year, rating) and return the updated list.
Part 2: Movie Rating and Average Calculation (Lists & Functions)
Add a Rating to a Movie:
Write a function that allows the user to add a rating to an existing movie. The function should take the movie title and the new rating as inputs.
Calculate Average Rating:
Write a function that calculates the average rating of all the movies in the list.
Find Highest-Rated Movie:
Implement a function that finds the movie with the highest rating and returns its title and rating.
Part 3: Sorting and Filtering (For Loops & If Conditions)
List Movies by Rating:
Write a function that lists all movies in the database, sorted by rating in descending order.
Filter Movies by Year:
Implement a function that filters and returns all movies released in a given year.
Bonus (Optional):
Check if Movie Title is Palindrome:
Implement a function that checks if a given movie title is a palindrome (the title reads the same forward and backward).
Submission:
Provide the Python code for the Movie Rating System.
Include sample input and output for each of the implemented functionalities.
Ensure the code is clean and properly documented.'''
#source code
movie_db = []

class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = float(rating)

    def display_info(self):
        print(f"Title: {self.title:20}  Director: {self.director:15}  Year: {self.year}  Rating: {self.rating}")

# Add a Movie 
def add_movie(movie_list, title, director, year, rating):
    new_movie = Movie(title, director, year, rating)
    movie_list.append(new_movie)
    return movie_list

# Rating and Average Calculation 
def update_rating(movie_list, title, new_rating):
    for movie in movie_list:
        if movie.title.lower() == title.lower():
            movie.rating = float(new_rating)
            return f"Rating for '{movie.title}' updated to {new_rating}."
    return "Movie not found."
#average Rating
def calculate_average_rating(movie_list):
    if not movie_list:
        return 0.0
    total = sum(movie.rating for movie in movie_list)
    return total / len(movie_list)
#highest rating
def find_highest_rated(movie_list):
    if not movie_list:
        return None
    highest_movie = movie_list[0]
    for movie in movie_list:
        if movie.rating > highest_movie.rating:
            highest_movie = movie
    return highest_movie.title, highest_movie.rating
# Sorting and Filtering 
def list_movies_by_rating(movie_list):
    return sorted(movie_list, key=lambda m: m.rating, reverse=True)
#Filter
def filter_movies_by_year(movie_list, year):
    filtered = []
    for movie in movie_list:
        if movie.year == year:
            filtered.append(movie)
    return filtered
# Palindrome Check 
def is_title_palindrome(title):
    clean_title = title.lower().replace(" ", "")
    return clean_title == clean_title[::-1]

if __name__ == "__main__":
    # 1. Setup Data 
    print(" 1. Testing Add Movie ")
    add_movie(movie_db, "Inception", "Christopher Nolan", 2010, 8.8)
    add_movie(movie_db, "Tenet", "Christopher Nolan", 2020, 7.4)
    add_movie(movie_db, "Memento", "Christopher Nolan", 2000, 8.4)
    print(f"Movies added: {len(movie_db)}\n")

    # 2. Update Rating 
    print("Testing Add Rating to Movie ")
    print(update_rating(movie_db, "Tenet", 7.8))
    
    # 3. Average and Highest 
    avg = calculate_average_rating(movie_db)
    title, score = find_highest_rated(movie_db)
    print(f"\nRating Analytics")
    print(f"Average System Rating: {avg:.2f}")
    print(f"Highest Rated Movie: {title} ({score})")

    # 4. Sorting 
    print(f"\nMovies Sorted by Rating ")
    for m in list_movies_by_rating(movie_db):
        m.display_info()

    # 5. Filtering 
    print(f"\nFiltering Movies by Year (2010)")
    results = filter_movies_by_year(movie_db, 2010)
    for r in results:
        print(f"Found: {r.title}")

    # 6. Bonus Palindrome
    print(f"\nBonus Palindrome Check")
    test_title = "Tenet"
    print(f"Is '{test_title}' a palindrome? {is_title_palindrome(test_title)}")
'''output:
1. Testing Add Movie 
Movies added: 3

Testing Add Rating to Movie
Rating for 'Tenet' updated to 7.8.

Rating Analytics
Average System Rating: 8.33
Highest Rated Movie: Inception (8.8)

Movies Sorted by Rating
Title: Inception             Director: Christopher Nolan  Year: 2010  Rating: 8.8
Title: Memento               Director: Christopher Nolan  Year: 2000  Rating: 8.4
Title: Tenet                 Director: Christopher Nolan  Year: 2020  Rating: 7.8

Filtering Movies by Year (2010)
Found: Inception

Bonus Palindrome Check

Is 'Tenet' a palindrome? True    '''