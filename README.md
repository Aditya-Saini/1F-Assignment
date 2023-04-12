# 1F-Assignment


## Tools:

python

django

djangorestframework

auth(JWT)

database(SQLite)

postman


## Installation:

Clone the repository: git clone https://github.com/Aditya-Saini/1F-Assignment.git

Create a virtual environment: python3 -m venv env

Activate the virtual environment: source env/bin/activate

Install the requirements: pip install -r requirements.txt

Create the database tables: python manage.py migrate

Create env file for env variables in core folder

Variables required->

SECRET_KEY(Django Secret key)

ROOT_URL(Host URL)

THIRD_PARTY_API(3rd party api URL for integration)

USERNAME(3rd party api auth)

PASSWORD(3rd party api auth)

Run the development server: python manage.py runserver


## Screeshoots

3rd party api Integration

![image](https://user-images.githubusercontent.com/67433169/231564468-18da26a1-d53a-4474-9e68-89706fc3a449.png)

Collections list

![image](https://user-images.githubusercontent.com/67433169/231565167-89f48f37-5367-47c6-85e3-9b9bac28cabf.png)

List Movies from collection:

![image](https://user-images.githubusercontent.com/67433169/231566455-aef8304d-8956-4038-8b20-47d7410e4712.png)


## Usage:

Check out movies under movies endpoint

Create different collections of movies

Get your favourite Genre

API provides real-time request count


## Endpoints:


register/ : To register new users

login/ : Get access token

request-count/ : Number of requests made to API

request-count/reset/ : Resets request count

movies/ : List of movies(3rd party api integration)

collections/ : Creates a collection of movies(POST)

collections/ : get list of your collection and favourite genre(GET)

collections/uuid/ : Retrieve/Delete/Update your collection


## Testing:

Unit Testing done using Django Built-in module [File](https://github.com/Aditya-Saini/1F-Assignment/blob/master/movie/test_api.py)


