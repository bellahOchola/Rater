from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import ProjectSerializer
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

