movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_above_5_5(movie):
    return movie["imdb"] > 5.5

def above_5_5_movies(movies):
    return [movie for movie in movies if is_above_5_5(movie)]

def movies_by_category(category_name):
    return [movie for movie in movies if movie["category"] == category_name]

def average_imdb_score(movie_list):
    if not movie_list:
        return 0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)

def average_imdb_score_by_category(category_name):
    category_movies = movies_by_category(category_name)
    return average_imdb_score(category_movies)

# Testing the functions
print(is_above_5_5({"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"}))  # Output: True
print(above_5_5_movies(movies))  # List of movies with IMDB score above 5.5
print(movies_by_category("Romance"))  # List of movies under the category "Romance"
print(average_imdb_score(movies))  # Average IMDB score of all movies
print(average_imdb_score_by_category("Suspense"))  # Average IMDB score of movies under the category "Suspense"
