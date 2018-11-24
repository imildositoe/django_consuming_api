from posts.forms import Login
from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):
    return render(request, 'posts/index.html', {
        'title': 'Lista de Usuarios'
    })


def load_users_from_api(request):
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {'usuario': 'grupo', 'senha': 'primeiro'}
    r = requests.post('http://localhost:8080/dawapi/usuario/login', data=json.dumps(data), headers=header)

    header1 = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJub21lIjoiR3J1cG8gUHJpbWVpcm8iLCJpZCI6IjEiLCJleHAiOjE1NDMxNTA4NzR9.eXxUfuvgsXOMDJONJl9djJKVR326Zl6Hmh8E3fca7PQfDTqkG0Ol1zlNTWRutzq9Ob_MLVnDgbEXB6KE4cbQEg"
    }
    r1 = requests.get('http://localhost:8080/dawapi/usuario', headers=header1)
    data2 = r1.json()
    return render(request, 'posts/index.html', {'data': data2})


def login(request):
    form = Login(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        header = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {'usuario': username, 'senha': password}
        r = requests.post('http://localhost:8080/dawapi/usuario/login', data=json.dumps(data), headers=header)
        if r.status_code == 200:
            header1 = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJub21lIjoiR3J1cG8gUHJpbWVpcm8iLCJpZCI6IjEiLCJleHAiOjE1NDMxNTA4NzR9.eXxUfuvgsXOMDJONJl9djJKVR326Zl6Hmh8E3fca7PQfDTqkG0Ol1zlNTWRutzq9Ob_MLVnDgbEXB6KE4cbQEg"
            }
            r1 = requests.get('http://localhost:8080/dawapi/usuario', headers=header1)
            data2 = r1.json()
            return render(request, 'posts/index.html', {'data': data2})

    return render(request, 'posts/login.html')
