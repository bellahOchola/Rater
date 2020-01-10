from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Profile
from .serializer import ProjectSerializer, ProfileSerializer
from rest_framework import status   # handles all status code responses

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
