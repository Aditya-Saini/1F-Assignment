from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Collection, Movie
import datetime

import logging

logger = logging.getLogger(__name__)


class CollectionViewTest(APITestCase):
    def create_token(self):
        url = 'http://localhost:8000/register/'
        data = {
            'username' : 'aditya',
            'password'  : 'abcd@123'
        }

        logger.debug('Sending TEST data to url: %s, data: %s'%(url, data))
        response = self.client.post(url, data, format='json')
        return response.data["access"]

    def test_create_user(self):
        """
        Tests creating a new User object
        """
        logger.debug('Starting test create User')
        url = 'http://localhost:8000/register/'
        data = {
            'username' : 'aditya',
            'password'  : 'abcd@123'
        }

        logger.debug('Sending TEST data to url: %s, data: %s'%(url, data))
        response = self.client.post(url, data, format='json')
        logger.debug('Testing status code response: %s, code: %d'%(response.json(), response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_count(self):
        token = self.create_token()
        logger.debug('Starting test request counter')
        url = 'http://localhost:8000/request-count/'
        logger.debug('Sending TEST to url: %s'%url)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(url, format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_request_count(self):
        token = self.create_token()
        logger.debug('Starting test request counter')
        url = 'http://localhost:8000/request-count/reset/'

        logger.debug('Sending TEST to url: %s'%url)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.post(url, format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_movie_list_api(self):
        token = self.create_token()
        logger.debug('Starting test 3rd party API integration endpoint')
        url = 'http://localhost:8000/movies/'

        logger.debug('Sending TEST to url: %s'%url)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(url, format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_collection_api(self):
        token = self.create_token()
        logger.debug('Starting test Create collection endpoint')
        url = 'http://localhost:8000/collections/'

        logger.debug('Sending TEST to url: %s'%url)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            "title": "Collection 1",
            "description": "Desc 2 list",
            "movie": [
                {
                    "title":"Queerama",
                    "description":"50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
                    "genres":"",
                    "uuid":"57baf4f4-c9ef-4197-9e4f-acf04eae5b4d"
                },
                {
                    "title":"Satana likuyushchiy",
                    "description":"In a small town live two brothers, one a minister and the other one a hunchback painter of the chapel who lives with his wife. One dreadful and stormy night, a stranger knocks at the door asking for shelter. The stranger talks about all the good things of the earthly life the minister is missing because of his puritanical faith. The minister comes to accept the stranger's viewpoint but it is others who will pay the consequences because the minister will discover the human pleasures thanks to, ehem, his sister- in -law… The tormented minister and his cuckolded brother will die in a strange accident in the chapel and later an infant will be born from the minister's adulterous relationship.",
                    "genres":"",
                    "uuid":"163ce013-03e2-47e9-8afd-e7de7688c151"
                }
            ]
        }
        response = client.post(url, data,format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        collection_uuid = response.data["collection_uuid"]
        
        logger.debug('Starting test Retrieve collection')
        response = client.get(url+str(collection_uuid)+"/",format='json')
        
        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)



        logger.debug('Starting test Update collection')
        data["title"] = "Update Collection 1"
        data["movie"].append({
            "title":"Siglo ng Pagluluwal",
            "description":"An artist struggles to finish his work while a storyline about a cult plays in his head.",
            "genres":"Drama",
            "uuid":"e9548ee7-6a95-4917-893e-1fa1d3a6de40"})
        response = client.put(url+str(collection_uuid)+"/", data,format='json')
        
        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Update Collection 1")
        self.assertEqual(len(response.data["movie"]), 3)


        logger.debug('Starting test Delete collection')
        response = client.delete(url+str(collection_uuid)+"/", data,format='json')
        
        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_collection_list_api(self):
        token = self.create_token()
        logger.debug('Starting test GET collection List')
        url = 'http://localhost:8000/collections/'

        logger.debug('Sending TEST to url: %s'%url)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(url, format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)