from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from .userSerializer import UserSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def login(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        realUserData=serializer.data
        print(realUserData)
        return Response(realUserData)
    return Response(serializer.errors,status=400)