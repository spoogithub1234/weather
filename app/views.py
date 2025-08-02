from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
def index(request):
    city=request.GET.get('city','bangalore')
    api_key='56b258dea9bbcfa0e61c45a5387fab6b'
    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    print(api_url)
    api=requests.get(api_url).json()
    temparature=api['main']['temp']
    country=api['sys']['country']
    city=api['name']
    return render(request,'index.html',{'temperature':temparature,'country':country,'city':city})


# Create your views here.
