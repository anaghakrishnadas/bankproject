from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

# Create your views here.
# @login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def branch(request, district):
    district_wikipedia_urls ={
      "Kozhikode": "https://en.wikipedia.org/wiki/Kozhikode",
      "Kochi": "https://en.wikipedia.org/wiki/Kochi",
      "Trivandrum": "https://en.wikipedia.org/wiki/Thiruvananthapuram",
       "Thrissur": "https://en.wikipedia.org/wiki/Thrissur",
       "Kannur": "https://en.wikipedia.org/wiki/Kannur"  
    }
    
    # Check if the selected district exists in the dictionary
    if district in district_wikipedia_urls:
        # Redirect to the Wikipedia page of the selected district
        return redirect(district_wikipedia_urls[district])
    else:
        # If district not found, redirect to home
        return redirect('home')
    


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        fname=request.POST.get('firstname')
        lname=request.POST.get('Lastname')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('bank:login')

    return render (request,'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')

        print(f"Username: {username}, Password: {pass1}")

        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('bank:new')
        else:
            messages.error(request, "Username or Password is incorrect!!!")
            return redirect('bank:login')
    return render (request,'login.html')


def NewPage(request):
    return render(request, 'new.html')


def FormPage(request):
    if request.method == 'POST':
        return render(request, 'msg.html')
    return render(request, 'form.html')


def about(request):
    return render(request, 'about.html')


def LogoutPage(request):
    logout(request)
    return redirect('bank:login')