from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("hello World");
    return render(request,'home.html',{'name':'Rohit'})