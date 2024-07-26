from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SuperUserRegistrationForm

def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Enquiry.objects.create(name=name, email=email,phone=phone, message=message)  
        messages.success(request, "Thank you for contacting us !!!")
        return redirect("home")
    return render(request,'contact.html')


def project(request):
    projects = Projects.objects.all()
    context = {"projects":projects}
    return render(request,'project.html',context)



def service(request):
    services = Services.objects.all()
    context = {"services":services}
    return render(request,'service.html',context)



def team(request):
    return render(request,'team.html')



def testimonials(request):
    return render(request,'testimonials.html')



def faq(request):
    return render(request,'faq.html')



def features(request):
    return render(request,'features.html')




def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscription.objects.create(email=email)
        messages.success(request, "Thank you for subscribing !!!")
        return redirect('/')
    




######################### LOGIN / LOGOUT ########################


def register(request):
    if request.method == 'POST':
        form = SuperUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['is_superuser']:
                user.is_superuser = True
                user.is_staff = True
                user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SuperUserRegistrationForm()
    return render(request, 'register.html', {'form': form})

#RegisterPage
def RegisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect("login")
        else:
            return render(request, "registerpage.html", {'form':form})
    return render(request, "registerpage.html", {'form':form})


#loginpage
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "welcome " + str(request.user.username))
            return redirect('home')
        else:
            messages.info(request, "Invalid Login Credentials")
            return redirect("login")
    return render(request, "loginpage.html")


#Logout
def UserLogout(request):
    logout(request)
    messages.success(request,"Logged out Successfully !!")
    return redirect('home')

def Career(request):
    return render(request,'careers.html')

def webdetail(request):
    return render(request,'web-detail.html')

def erpdetail(request):
    return render(request,'erp-details.html')

def Annotdetail(request):
    return render(request,'annot-details.html')

def mldetail(request):
    return render(request,'ml-detail.html')
def Gallery(request):
    return render(request,"gallery.html")
