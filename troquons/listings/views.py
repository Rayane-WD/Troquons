from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django its me!</h1>')

def listings(request):
    return HttpResponse('<h1>Listing</h1> <p>List of products</p>')

def contact_us(request):
    return HttpResponse('<h1>Contact me!</h1> <p>My e-mail is : rayane.waidi@esme.fr</p>')

def about_us(request):
    return HttpResponse('<h1>About me</h1> <p>I am an engineer student</p>')