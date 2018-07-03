import requests,json
from django.http import JsonResponse
from .models import Url
from .service import *



def get():
    b=Url.objects.latest('url_no').url
    r=requests.get(b)
    x=r.text
    d=json.loads(x)
    return(d)

def post(jsondata):
    r=requests.post("https://api.myjson.com/bins",json=jsondata)
    x=r.text
    d=json.loads(x)
    return d

def put(jsonarr):
    b=Url.objects.latest('url_no').url
    # data=[]
    # jsonarr.append(payload)
    # jsonarr.append(get())

    r=requests.put(b,json=jsonarr)
    x=r.text
    d=json.loads(x)
    print(d)
    return d



# olddata=service.get()
# olddata.append(jsondata)
# r=requests.put(b,json=olddata)
# x=r.text
# d=json.loads(x)
