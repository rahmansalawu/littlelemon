from rest_framework import serializers
from . models import Booking, Menu
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        fields = [ 'username', 'email', 'groups']