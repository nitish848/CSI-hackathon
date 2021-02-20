from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from Home.models import FIR
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,"Home/index.html")

def structure(request):
    return render(request,"Home/structure.html")

def contact(request):
    return render(request,"Home/contact.html")

def FIR(request):
    return render(request,"Home/FIR.html")

def signuperror(request):
    return render(request,"Home/signuperror.html")

def loginerror(request):
    return render(request,"Home/loginerror.html")

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']


        # check for errorneous input
    
        if len(username)>10:
            err=" Your user name must be under 10 characters "   
            return redirect('/signuperror')
    
        if not username.isalnum():
            err="User name should only contain letters and numbers"
            return redirect('/signuperror')
        if (pass1!= pass2):
            err="Passwords did not match"
            return redirect('/signuperror')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")




def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/Home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/loginerror")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/Home')

def FIRcont(request):
    FIR = FIR(content='new cat')
    FIR.save()
    return redirect('/signuperror')