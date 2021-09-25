from django.shortcuts import render,HttpResponse,redirect
from library.models import Student,books
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def main(request):
    if request.method == 'POST':
        search = request.POST['search']
        Books = books.objects.filter(book_name__icontains=search)
    else:
        Books = books.objects
    return render(request,'main.html', { 'Books' : Books} )    

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date = request.POST.get('date')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request,'signup.html')            
        else:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            data = Student(date=date,name=username,email=email,phone=phone,address=address,password=password)
            data.save()
            return redirect('./main')
    return render(request,"signup.html")    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('./main')
        except:
            return render(request,'login.html')        
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('./login')
