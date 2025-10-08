#peticiones a apis con python

#sin dependencias (forma nativa)

import urllib.error
import urllib.request 
import json #para transformar la peticion a json

api_post="https://jsonplaceholder.typicode.com/posts"

try :

    response=urllib.request.urlopen(api_post) #llamando a la api
    data=response.read() 
    json_date=json.loads(data.decode("utf-8"))
    print(json_date)
    response.close()

except urllib.error.URLError as e:
    print(e)


#con dependencia (requests)

import requests

print("get")
api_post="https://jsonplaceholder.typicode.com/posts"
response=requests.get(api_post)
json=response.json()
print(json[0])


# Post
input={
    "title":"python",
    "body":"hola"
}
try:

    response= requests.post(
        api_post,json=input
    )
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(e)

#Put

input={
    "title":"python nahuel",
    "body":"hola 2",
    "userId":1
}
try:

    response= requests.put(
        "https://jsonplaceholder.typicode.com/posts/1"
        ,json=input
    )
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(e)


