from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def homepage(request: HttpRequest) -> HttpResponse:
    print('render')
    return render(request, 'index.html')
