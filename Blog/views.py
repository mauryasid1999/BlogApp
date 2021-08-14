from django import forms
from django.db.models import query
from Blog.models import BlogPost
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Blog.forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

 
def search(request):
    
    query=request.GET['search']
    posts=BlogPost.objects.filter(title__icontains=query)

    context={
        "posts":posts
    }    
        

    return render(request,'search.html',context)   

# Create your views here.
class BlogDetailView(DetailView):
    model = BlogPost
    template_name='blog_detail.html'


def blogs(request):
    posts=BlogPost.objects.all()
    posts=BlogPost.objects.filter().order_by('-datetime')

    context={
        "posts":posts
    }

    return render (request,'home.html',context)



def Register(request):
    if  request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1!=password2:
            messages.error(request,"password does not match")
            return redirect('/register')

        user=User.objects.create_user(username,email,password1)
        user.first_name=first_name
        user.last_name= last_name
        user.save()

        return render(request,'login.html')

    return render(request,"register.html")


def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username , password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')

        else:
            messages.error(request,'INVALID CRUDENTIALS')

                
    return render(request,"login.html")


def Logout(request):
    logout(request)
    return redirect('/')



@login_required(login_url='login/')
def Add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            #return render(request, "home.html",{'obj':obj, 'alert':alert})
            return redirect('/')
    else:
        form=BlogPostForm()
    return render(request, "addblogs.html", {'form':form})

def blogs_delete(request):
    pass





            
            


