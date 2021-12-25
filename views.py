from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.views import APIView
from .models import Task
from django.http import Http404
# Create your views here.
from .models import About
from .serializers import AboutSerializer
# from .models import Comment
# from .serializers import CommentSerializer
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class SnippetList(APIView):
    
    def get(self, request, format=None):
        snippets =  Task.objects.all()
        serializer = TaskSerializer(snippets,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return  Task.objects.get(pk=pk)
        except  Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(instance= snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







class  AboutList(APIView):
    
    def get(self, request, format=None):
        snippets =   About.objects.all()
        serializer =  AboutSerializer(snippets,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =  AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class  AboutDetail(APIView):
    def get_object(self, pk):
        try:
            return   About.objects.get(pk=pk)
        except   About.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =  AboutSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =  AboutSerializer(instance= snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
   
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











