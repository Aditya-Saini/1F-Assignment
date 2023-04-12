import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

def nav_helper(req, api_data):
    page = req.GET.get("page","")
    host = os.getenv("ROOT_URL")+"movies/?page="
    if page!="":
        api_data["next"] = host+str(int(page)+1)
        if int(page)>1:
            api_data["previous"] = host+str(int(page)-1)
    else:
        api_data["next"] = host+"2"
    return api_data

def third_party_api(request):
    partner_api_req = requests.get(os.getenv("THIRD_PARTY_API"), auth = HTTPBasicAuth(os.getenv("USERNAME"), os.getenv("PASSWORD")))
    if(partner_api_req.status_code!=200):
        while partner_api_req.status_code==200:
            partner_api_req = requests.get(os.getenv("THIRD_PARTY_API"), auth = HTTPBasicAuth(os.getenv("USERNAME"), os.getenv("PASSWORD")))
    return nav_helper(request, partner_api_req.json())
    

