from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home_page(request):
    search_query = request.GET.get('search')
    if search_query:
        contents=BlogPosts.objects.filter(heading__icontains=search_query) | BlogPosts.objects.filter(
            blog_contents__icontains=search_query
        )
    else:
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

def index(request):
    posts=BlogPosts.objects.all()
    return render(request,"myblog/index.html",{"post":posts})

def delete(request,id):
    post = BlogPosts.objects.get(id=id)
    post.delete()
    return redirect('/home')
def edit(request,id):
    post = BlogPosts.objects.get(id=id)
    if request.method == "POST":
        post.heading = request.POST['heading']
        post.blog_contents = request.POST['blog_contents']
        post.save()
        return redirect('/home')

    return render(request, 'myblog/edit.html', {'post': post})

def comment(request, post_id):
    post = BlogPosts.objects.get(id=post_id)

    # if request.method == "POST":
    #     comment_text = request.POST.get("comment")
    #     if request.user.is_authenticated:  # Check if user is logged in
    #         Comment.objects.create(blog=post, user=request.user, text=comment_text)
    #     else:
    #         return redirect('/login/')  # Redirect if not logged in

    # comments = Comment.objects.filter(blog=post)

    # return render(request, "myblog/comment.html", {"post": post, "comments": comments})
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        Comment.objects.create(blog=post, text=comment_text)

    comments = Comment.objects.filter(blog=post)
    for comment in comments:
        print(f"blog is {comment.blog}")

    return render(request, "myblog/comment.html", {"post": post, "comments": comments})