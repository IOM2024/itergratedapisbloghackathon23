from django.shortcuts import render
import requests

def index(request):
    # GitHub events
    r1 = requests.get('https://api.github.com/events')
    data = r1.json()
    events = data[0]['repo'] if data else "No events found" 

    # Bored API activity
    r2 = requests.get('https://boredapi.com/api/activity')
    data = r2.json()
    activity = data['activity']

    # Dog API image
    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog = res3['message']

    # Random Quote
    r4 = requests.get('https://api.quotable.io/random')
    quote_data = r4.json()
    quote = f'"{quote_data["content"]}" - {quote_data["author"]}' if quote_data else "No quote found"

    # Random fact
    r5 = requests.get('http://numbersapi.com/random/trivia')
    fact = r5.text if r5.status_code == 200 else "No fact available"

    return render(request, 'index.html', {'event': events, 'activity': activity, 'dog': dog, 'quote': quote, 'fact': fact})
