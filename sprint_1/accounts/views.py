from django.shortcuts import render, HttpResponse
from .models import Post
from django.shortcuts import redirect

def homepage(request):
    return HttpResponse("Welcome to home page.")

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
