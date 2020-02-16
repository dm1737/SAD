from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .forms import NewUserForm, EmailForm
from django.contrib.auth.models import User

def homepage(request):
    return render(request = request,
                template_name="accounts/home.html")
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("accounts:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "accounts/register.html",
                          context={"form":form})
    form = NewUserForm
    return render(request = request,
                template_name = "accounts/register.html",
                context={"form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("accounts:homepage")

def fgtpassword(request):
    if request.method == 'GET':
        form = EmailForm()
        return render(request = request,
                template_name = "accounts/forgot_password.html",
                context={"form":form})
    if request.method == 'POST':    
        form = EmailForm(data=request.POST)
        if form.is_valid():            
            email = form.cleaned_data.get('email')            
            #user = authenticate(email=email)
            #print(user)
            if email is not None:                
                messages.info(request, f"Email sent to {email}")
               # return redirect('/')
            else:
                messages.error(request, "Invalid email.")
        else:
            messages.error(request, "Invalid email.")
        return render(request = request,
                template_name = "accounts/forgot_password.html",
                context={"form":form})
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})

def view_account(request):
    args = {'user': request.user}
    return render(request, 'accounts/accountinfo.html', args)

def profile(request):
    return render(request = request, template_name = "accounts/profile.html")  

def help(request):
    return render(request = request, template_name = "accounts/help.html")   

"""if request.method == 'POST':
        print('here')
        if request.POST.get('username') and request.POST.get('password'):
            print('here')
            post=Post()
            post.username= request.POST.get('username')
            post.password= request.POST.get('password')
            post.save()
                
            return render(request, 'posts/home.html')  
     else:
            return render(request, 'accounts/login.html') """