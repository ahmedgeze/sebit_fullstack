from django.shortcuts import get_object_or_404, render, redirect
import json
import requests, json
from django.http import JsonResponse



# test1 = {'id':20,'name':"ahmet",'city':"ankara",'country':"tr"}
# test2 = {'id':10,'name':"ado",'city':"ankara",'country':"fr"}
#
#
# x[0]=test1
# x[1]=test2



def HomePage (request):
    # test1 = {'id':20,'name':"ahmet",'city':"ankara",'country':"tr"}
    # test2 = {'id':10,'name':"ado",'city':"ankara",'country':"fr"}
    # tests = [(test1, test2),]
    # # tests.append(test1)
    # # tests.append(test2)
    # print(createarr())
    # return render(request,'home.html',{'mydict': tests})
    
    return render(request,'home.html')

def createarr():
    data={}
    jsonarr=[]
    for i in range(0,10):
        data['id']=i
        data['name']=i
        data['city']=i
        data['country']=i
        jsonarr.append(data)
    return json.dumps(jsonarr)
