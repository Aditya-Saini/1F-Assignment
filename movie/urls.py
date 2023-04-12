from django.urls import path
from movie.views import MovieListAPIView, CollectionView

urlpatterns = [
    path("movies/", MovieListAPIView.as_view(), name="movie"),
    path("collections/", CollectionView.as_view(), name="collections")

]