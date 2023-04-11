from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests

# Create your views here.
class MovieListAPIView(GenericAPIView):
    """
    An endpoint to get Movie List.
    """
    permission_classes = (IsAuthenticated,)
    def get(self, req):
        page = req.GET.get("page","")
        host = "http://localhost:8000/movie/?page="
        partner_api_req = requests.get("https://demo.credy.in/api/v1/maya/movies/")
        if(partner_api_req.status_code!=200):
            while partner_api_req.status_code==200:
                partner_api_req = requests.get("https://demo.credy.in/api/v1/maya/movies/")
        response_data = partner_api_req.json()
        if page!="":
            response_data["next"] = host+str(int(page)+1)
            if int(page)>1:
                response_data["previous"] = host+str(int(page)-1)
        else:
            response_data["next"] = host+"2"
            
        return Response(response_data, status=status.HTTP_200_OK)