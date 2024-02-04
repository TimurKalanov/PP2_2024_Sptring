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
def movie_above_5_5(movie):
    return movie["imdb"] > 5.5
def movies_5_5(movies):
    return [movie for movie in movies if movie_above_5_5(movie)]
def category_name(movies_category):
    return [movie for movie in movies if movie["category"] == movies_category ]
def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)
def average_imdb_category(name):
    category_namess1 = category_name(name)
    return average_imdb(category_namess1)


print(movie_above_5_5({"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"}))  # Output: True
print(movies_5_5(movies))  # List of movies with IMDB score above 5.5
print(category_name("Romance"))  # List of movies under the category "Romance"
print(average_imdb(movies))  # Average IMDB score of all movies
print(average_imdb_category("Suspense"))  # Average IMDB score of movies under the category "Suspense"