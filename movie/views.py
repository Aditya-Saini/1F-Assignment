from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Collection
from .serializer import CollectionSerializer
from .internal.services import third_party_api
from .utils import favourite_genre

# Create your views here.
class MovieListAPIView(GenericAPIView):
    """
    An endpoint to get Movie List from 3rd party API.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, req):
        response_data = third_party_api(req)
        return Response(response_data, status=status.HTTP_200_OK)

class CollectionView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CollectionSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        collection = serializer.save()
        return Response({"collection_uuid": collection.uuid}, status=status.HTTP_201_CREATED)

    def get(self, request):
        try:
            collection_list = Collection.objects.filter(user = request.user).values("title", "uuid", "description")
            fav_genre = favourite_genre(collection_list)
            response = {
                "is_success": True,
                "data":{
                    "collections":collection_list
                },
                "favourite_genres": fav_genre
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"Cannot fetch collection"}, status=status.HTTP_400_BAD_REQUEST)

class CollectionRUDAView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CollectionSerializer
    def get_queryset(self):
        try:
            return Collection.objects.all()
        except Exception as e:
            return Response({"message":"Cannot fetch collection"}, status=status.HTTP_400_BAD_REQUEST)