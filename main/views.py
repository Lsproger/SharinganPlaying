from django.shortcuts import render
from django.http import HttpResponse
from splaying.settings import BASE_DIR
from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(request, "hello.html")