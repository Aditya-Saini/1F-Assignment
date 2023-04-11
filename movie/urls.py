from django.urls import path
from movie.views import MovieListAPIView

urlpatterns = [
    path("movies/", MovieListAPIView.as_view(), name="movie")
]