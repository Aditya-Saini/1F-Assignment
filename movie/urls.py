from django.urls import path
from movie.views import MovieListAPIView, CollectionView, CollectionRUDAView

urlpatterns = [
    path("movies/", MovieListAPIView.as_view(), name="movie"),
    path("collections/", CollectionView.as_view(), name="collections"),
    path("collections/<uuid:pk>", CollectionRUDAView.as_view(), name="single_collections")

]