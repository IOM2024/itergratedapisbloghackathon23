from django.shortcuts import render
import requests

def index(request):
    r1 = requests.get('https://api.github.com/events')
    data = r1.json()
    events = data[0]['repo'] if data else "No events found" 
    r2= requests.get('https://boredapi.com/api/activity')
    data= r2.json()
    activity = data['activity']
    r3= requests.get('https://dog.ceo/api/breeds/image/random')
    res3= r3.json()
    dog= res3['message']
    return render(request, 'index.html', {'event': events, 'activity' : activity,'dog':dog})