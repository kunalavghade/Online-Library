from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return HttpResponse("login page")
def logout(request):
    return HttpResponse("login page")
