import requests,json
from django.http import JsonResponse
from .models import Url
from .service import *

def clearDB():
    Url.objects.all().delete()
    resp_json={
        "status":"clearDB Success!"
    }
    # --debug--Url.objects.create(url="asd")
    return(resp_json)

def getAll():
    last_url=Url.objects.latest('url_no').url
    resp=requests.get(last_url)
    resp_text=resp.text
    resp_json=json.loads(resp_text)
    return(resp_json)

def addNew(jsondata):
    objs = Url.objects
    if objs.first():
        resp_json = updateData(jsondata)
    else:
        resp_json = createNew(jsondata)
    return(resp_json)

def createNew(jsondata):
    jsonarr=[]
    jsonarr.append(jsondata)
    resp=requests.post("https://api.myjson.com/bins",json=jsonarr)
    resp_text=resp.text
    resp_json=json.loads(resp_text)
    url_link=resp_json['uri']
    Url.objects.create(url=url_link)
    return getAll()

def updateData(jsondata):
    jsonarr=getAll()
    jsonarr.append(jsondata)
    lasut_url=Url.objects.latest('url_no').url
    resp=requests.put(lasut_url,json=jsonarr)
    resp_text=resp.text
    resp_json=json.loads(resp_text)
    print(resp_json)
    return resp_json

def queryData(city,country):
    jsonarr=getAll()
    jsonarr2=[]
    for item in jsonarr:
        if city and country:
            if item['city_name']==city and item['country_name']==country:
                jsonarr2.append(item)
        elif city:
            if item['city_name']==city:
                jsonarr2.append(item)
        elif country:
            if item['country_name']==country:
                jsonarr2.append(item)
    if len(jsonarr2)>0:
        return(jsonarr2)
    else :
        resp_json={"status":"No Result!"}
        return(resp_json)
