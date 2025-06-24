from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home_page(request):
    for data in BlogPosts.objects.all():
        print(data.blog_contents)
    contents=BlogPosts.objects.all()
        
    return render(request,"myblog/home.html",{"content":contents})

def Blog(request):
    if request.method == "POST":
        heading = request.POST.get("title")
        Blog_contents=request.POST.get("blog")
        images=request.POST.get("file")
        data = BlogPosts(heading=heading,blog_contents=Blog_contents,image = images)
        data.save()
        return redirect("/home")

    return render(request,"myblog/blog.html")

def preview(request,post_id):
    contents=BlogPosts.objects.get(id=post_id)
    return render(request,"myblog/all.html",{"content":contents})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username)
        # print(Users.objects.all())
        for user in Users.objects.all():
            print(user.Fullname)
            if username == user.Fullname and password == user.Password: 
                return redirect("/home")
    return render(request,"myblog/login.html",{})

def signup(request):
    if request.method == "POST": 
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        user1 = Users(Fullname=username,Email=email,Password=password,confirm_password=confirm_password)
        user1.save()
        return redirect("/login")
    return render(request,"myblog/sign.html",{})