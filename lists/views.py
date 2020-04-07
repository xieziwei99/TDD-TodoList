from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home_page(request: HttpRequest):
    return HttpResponse(
        '''<html>
            <head>
            <title>To-Do lists</title>
            </head>    
            <body>
            <h1>Hello TDD Django</h1>
            </body>
            </html>''')