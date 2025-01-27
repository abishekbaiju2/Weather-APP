from django.shortcuts import render
import requests
from django.views.generic import View

class WeatherView(View):
    def get(self, request):
        return render(request,'weather.html',{'weather': None})

    def post(self, request):
        city = request.POST.get('city')
        weather = None

        if city:
            api_key ='3dec5d887068297677545f485d50d6cb' 
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            try:
                response = requests.get(url)
                data = response.json()
                if data['cod'] == 200:
                    weather = {
                        'city': data['name'],
                        'temperature': data['main']['temp'],
                        'description': data['weather'][0]['description'],
                        'icon': data['weather'][0]['icon'],
                        'humidity': data['main']['humidity'],
                        'pressure': data['main']['pressure'],
                        'wind': data['wind']['speed'],

                    }
                else:
                    weather = {'error': data.get('message', 'City not found!')}
            except Exception:
                weather = {'error': 'An error occurred. Please try again.'}

        return render(request,'weather.html',{'weather': weather})
