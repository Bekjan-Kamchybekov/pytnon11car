from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['make_name']

class CarListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')

    class Meta:
        model = Car
        fields = ['id','car_name', 'make', 'year', 'price', 'region_or_city']

class CarDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    class Meta:
        model = Car
        fields = ['id', 'car_name', 'year', 'price', 'mileage', 'description', 'date', 'body', 'color',
                  'engine_capacity', 'fuel', 'transmission_box', 'drive',
                  'steering_wheel', 'state', 'customs', 'change', 'region_or_city', 'other', 'make', 'owner']

class CarPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotos
        fields = ['image']

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'

class FavoritesCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritesCar
        fields = '__all__'