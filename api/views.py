from django.shortcuts import render
from rest_framework import views,status
from rest_framework.response import Response
from api.serializers import CodeExplainSerializer,UserSerializer
from api.models import CodeExplainer
from django.contrib.auth.models import User
# Create your views here.
class CodeExplainView(views.APIView):
    serializer_class=CodeExplainSerializer

    def get(self,request,format=None):
        qs=CodeExplainer.objects.all()
        serializer=self.serializer_class(qs,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserView(views.APIView):
    serializer_class=UserSerializer
    def get(self,request,format=None):
        qs=User.objects.all()
        serializer=self.serializer_class(qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,staus=status.HTTP_400_BAD_REQUEST)
class TokenView:
    pass

