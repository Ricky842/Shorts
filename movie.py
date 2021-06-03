def calculate_highest_rating():
    movies = []
    highest_rating = {'movie': '', 'rating': 0}
    while len(movies) < 5:
        movie, rating = input(
            'Enter movie and rating separated by comma(,):').split(',')
        movie_obj = {'movie': movie, 'rating': int(rating)}
        if (int(rating) > 10):
            print('movie rating should within a range of (1 - 10)')
        movies.append(movie_obj)
    for movie in movies:
        if (movie['rating'] > highest_rating['rating']):
            highest_rating = movie
            most_rated_movie = highest_rating['movie']
            movie_ratings = highest_rating['rating']
            print("Highest rated movie is {} with a rating of {}".format(most_rated_movie, movie_ratings))

calculate_highest_rating()
