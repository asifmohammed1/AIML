# Empty list to store data

Movies = []

# To add movies title,director,year and rating to the list 

def add_movie(movie_list ,title ,director ,year ,rating):
    movie ={
        "title": title,
        "director": director,
        "year": year,
        "rating": rating
    }

    movie_list.append(movie)
    return movie_list

add_movie(Movies , "Sinners", "Ryan coogler", 2025, 4.6)
add_movie(Movies , "Forrest Gump", "Robert Zemeckis", 1994, 4.9)
add_movie(Movies , "Saving Privat Ryan", "Steven Spielberg", 1998, 4.8)
add_movie(Movies , "Fury", "David Ayer", 2014, 4.7)

print(Movies)

# To update the rating of existing movie 

def update_rating(movie_list , title , new_rating):
    for movie in movie_list:
        if movie["title"].lower() == title.lower():
            movie["rating"] = new_rating
            return "rating Updated"
    return "Movie Not Found"

print(update_rating(Movies, "Sinners", 4.7))
 
print(Movies)

# To find the average rating of all movies 

def average_rating(movie_list):
    if len(movie_list) == 0 :
        return 0
   
    total = 0    
    for movie in movie_list:
        total += movie["rating"]
   
    return total/len(movie_list)

print("Average Rating:",average_rating(Movies))

# To find the highest rated movies

def highest_rated_movie(movie_list):
    highest = movie_list[0]

    for movie in movie_list:
        if movie["rating"] > highest["rating"]:
            highest = movie

    return highest["title"], highest["rating"]

print("Highest Rating Movie:", highest_rated_movie(Movies))

# To sort the list of movies according to their rating in descending order

def sort_movies_by_rating(movie_list):
    return sorted(movie_list , key = lambda m:m["rating"], reverse= True)

print(sort_movies_by_rating(Movies))

# To filter movies by year

def filter_movies_by_year(movie_list, year):
    result = []
    for movie in movie_list:
        if movie["year"] == year:
            result.append(movie)
    return result

print(filter_movies_by_year(Movies,2014))
