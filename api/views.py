from django.shortcuts import get_object_or_404, render, redirect
import requests,json
from django.http import JsonResponse
from . import service
from .models import Url

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import forms

def clearDB(request):
    return JsonResponse(service.clearDB(),safe=False)

def getAll(request):
    return JsonResponse(service.getAll(),safe=False)

def addNew(request):
    form=forms.personForm(request.GET)
    if form.is_valid():
            payload={
                "person_name": form.cleaned_data['name'],
                "city_name": form.cleaned_data['city'],
                "country_name": form.cleaned_data['country'],
            }
    return JsonResponse(service.addNew(payload),safe=False)

def queryData(request):
    form=forms.queryForm(request.GET)
    if form.is_valid():
        city = form.cleaned_data['city']
        country = form.cleaned_data['country']
        if city or country:
            resp_json = service.queryData(city,country)
        else:
            resp_json = service.getAll()
    else:
        resp_json={"status":"Bad Request!"}

    return JsonResponse(resp_json,safe=False)
