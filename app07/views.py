from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sam(request):
    return HttpResponse("<h1>hello world</h1>")
def rend(request):
    return render(request,"sample.html")
def view2(request):
    return render(request,"sec.html",context={'email':"prasanthh879@gmail.com",'name':"hariprasanth"})