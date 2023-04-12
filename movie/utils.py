from .models import Movie
from collections import Counter

def favourite_genre(collection):
    fav_genre = ""
    movie_list = []
    for i in collection.values("movie"):
        temp_list = list(Movie.objects.filter(id = i["movie"]).values_list("genres", flat=True))
        if temp_list and temp_list[0]!="":
            movie_list+=temp_list[0].split(",")
    count = Counter(movie_list)
    for i,j in count.most_common(3):
        fav_genre+=i+","
    return fav_genre[:-1]