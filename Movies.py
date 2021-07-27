#Empty list and dictionaries to store data for the movies and their ratings
movies = []
movie_dict = {'movie': '', 'rating': 0}

#Check validity of movie rating
def check_entry(rating):
    while rating.isnumeric() is True:
        movie_rating = int(rating)
        if(movie_rating > 10 or movie_rating < 1):
            rating = input("Please enter a rating between 1 and 10: ")
            movie_rating = rating
        else:
            return movie_rating
    movie_rating = input("Please enter an Integer between 1 and 10: ")
    movie_rating = check_entry(movie_rating)
    return movie_rating

#Calculates the highest rated movie
def rating():
    numMovies = int(input("How many movies have you watched this year? "))
    while len(movies) < numMovies:
        movie_name = input("Please enter the name of the movie: ")
        movie_rating = input(f"Please enter the rating of {movie_name} between 1 and 10: ")
        movie_rating = check_entry(movie_rating)
        movie_rating = int(movie_rating)
        movie_dict = {'movie': movie_name, 'rating':movie_rating}
        movies.append(movie_dict)
    highest_rating = 0
    for movie in movies:
        if movie['rating'] > highest_rating:
            highest_rating = movie['rating']
            favMovie = movie['movie']

    print(f"Your favorite movie was {favMovie} with a rating of {highest_rating}")

rating()

#Initial commit to Git