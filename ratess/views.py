from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Profile
from .serializer import ProjectSerializer, ProfileSerializer
from rest_framework import status   # handles all status code responses
from .forms import SignUpForm, UploadForm, UploadProfile 
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User


#........
# Create your views here.
class ProjectList(APIView):

    # handling a retrieval request
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    # handling a post request
    def post(self,request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):

    # handling a retrieval request
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@csrf_exempt
def index(request):
    all_posts = Project.objects.all()
    return render(request, 'index.html', {'all_posts': all_posts})

def posts(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = UploadForm()

    return render(request, 'post.html', {'form': form})

def profile(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = UploadProfile(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('index')
    else:
        form = UploadProfile()

    return render(request, 'profile.html', {'form': form})


