# Help you to make the requests for POST, GET, PATCH, PUT and DELETE

import json
import requests

def get_requests(url, auth):
    response = requests.get(url= url, auth=auth)
    return response.json()

def post_request(url,auth,headers,paylaod,in_json):
    post_response = requests.post(url=url,headers=headers, auth=auth, data=json.dumps(paylaod))
    if in_json is True:
        return post_response.json()
    return post_response



