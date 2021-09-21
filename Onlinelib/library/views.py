from django.shortcuts import render,HttpResponse
from library.models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        date = request.POST.get('date')
        data = Student(date=date,name=username,email=email,phone=phone,address=address,password=password)
        data.save()
        print(username,email,phone,address,password,date)
    return render(request,"signup.html")    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            data=Student.objects.get(name=username,password=password)
            print(data.name, data.password)
            return render(request,'index.html')
        except:
            return render(request,'login.html')
    return render(request,'login.html')        


def logout(request):
    return HttpResponse("login page")
