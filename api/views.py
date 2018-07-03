from django.shortcuts import get_object_or_404, render, redirect
import requests,json
from django.http import JsonResponse
from . import service
from .models import Url

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import forms

def get(request):
    return JsonResponse(service.get(),safe=False)







def post (request):


            # return JsonResponse(request.POST.get('name_of_var'),safe=False)
    if request.method=='GET':
            form=forms.postForm()
            return render(request,'post.html',{'form':form})
    elif request.method=='POST':
        formy=forms.postForm(request.POST)
        if formy.is_valid():
            payload={
                "id":formy.cleaned_data['id'],
                "person_name": formy.cleaned_data['name'],
                "city_name": formy.cleaned_data['city'],
                "country_name": formy.cleaned_data['country'],
            }
            url_json=service.post(payload)
            url_link=url_json['uri']
            Url.objects.create(url=url_link)
            return JsonResponse(url_json,safe=False)




    # data=service.get()
    # r=requests.post("https://api.myjson.com/bins",json=data)
    # print(r.text)
    # return render(request,'post.html')

def put(request,id,name,city,country):
        if request.method=='GET':
                # form=forms.postForm()
                # print(id+name+city+country)
                data=[]
                del data[:]
                payload={
                            "id":id,
                            "person_name": name,
                            "city_name": city,
                            "country_name": country
                            }

                data=service.get()
                # a.extend([a,payload])
                # x=service.put(a)
                data.append(payload)
                x=service.put(data)
                print(x)
                return JsonResponse(x,safe=False)
    
