from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post,Draft
from .serializers import PostSerializer,DraftSerializer,AccountSerializer
from django.contrib.auth import authenticate, login,logout




@api_view(['GET', 'POST'])
def log(request):
    print("in log")
    dict = {
        "username": "",
        "password": ""
    }
    if request.method=='POST':
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"Message": "LOgIn done"})
        else:
            return Response({"Message":"Try Again"})
    else:
        return Response(dict)


# Create your views here.
@api_view(['GET', 'POST'])
def post(request,pk=None):
    if pk:
        post = Post.objects.get(pk=pk)
        if post is None:
            return Response({"Message":"That blog is not exist"})
        else:
            dr=Draft.objects.get(author=post.post.author,title=post.post.title,body=post.post.body,id=post.post.id)
            srlzr=DraftSerializer(data=dr)
            srlzr.is_valid()
            print(srlzr['id'])
            return Response(srlzr.data)
    else:
        posts = Post.objects.all()
        srlzr = PostSerializer(data=posts,many=True)
        srlzr.is_valid()
        return Response(srlzr.data)



@api_view(['GET', 'POST'])
def create_post(request):
    print("in create")
    print(type(request.data))
    print("print")
    if request.method == 'POST':
        body = request.data['body']
        author = request.user
        title = request.data['title']
        if request.user.is_superuser:
            draft = Draft.objects.create(title=title, author=author, body=body)
            post=Post.objects.create(post=draft)
            post.save()
            return Response({"message": "Post Created","data":request.data})
        elif request.user.is_staff:
            draft=Draft.objects.create(title=title,author=author,body=body)
            draft.save()
            return Response({"message": "Add in Draft"})
        else:
            return Response({"message": "You are not an admin"})
    else:
        dict={
            "title":"",
            "body":""
        }
        return Response(dict)


@api_view(['GET', 'POST'])
def add(request,pk):
    if request.user.is_superuser:
        draft = Draft.objects.get(id=pk)
        post=Post(post=draft)
        post.save()
        return Response({"Message":"Now it is a post"})
    else:
        return Response({"Message":"You are not Authorised"})