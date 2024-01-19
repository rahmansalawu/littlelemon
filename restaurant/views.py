from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view , permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from .models import Menu, Booking
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 



class UserView(APIView):
    def get(self, request):
        items = User.objects.all()
        serializer = UserSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)






class userview(APIView):
    #def userview(APIView):
    def get(self,request):
        items = User.objects.all()
        serializer = UserSerializer(items, many=True, context={'request':request})
        return Response(serializer.data)

class bookingview(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
        return Response(serializer.data) #retunr JSON
    
    def post(self,request):
        #item = request.data
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':'serializer.data'})

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class Goons(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

