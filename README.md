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
THIRD_PARTY_API(3rd party api for integration)
USERNAME(3rd party api auth)
PASSWORD(3rd party api auth)
Run the development server: python manage.py runserver

## Usage:
Check out movies under movies endpoint
Create different collections of movies
Get your favourite Genre
API provides real-time request count

### Endpoints:

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


