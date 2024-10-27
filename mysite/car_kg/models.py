# from django.contrib.postgres.fields import CITextField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(max_length=32, null=True, blank=True,
                                           validators=[MinValueValidator(14), MaxValueValidator(110)])
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')


    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

class Make(models.Model):
    make_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.make_name

class Car(models.Model):
    car_name = models.CharField(max_length=32)
    make = models.ForeignKey(Make, related_name='car', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    year = models.DateField()
    mileage = models.PositiveIntegerField()
    description = models.TextField()
    date = models.DateField(auto_now=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    BODY_CHOICES = (
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Station wagon', 'Station wagon'),
        ('Coupe', 'Coupe'),
        ('Cabriolet', 'Cabriolet'),
        ('Minivan', 'Minivan'),
        ('Off-roader', 'Off-roader'),
        ('Crossover', 'Crossover'),
        ('Pickup', 'Pickup'),
        ('Special vehicle', 'Special vehicle'),
        ('Van', 'Van'),
    )

    body = models.CharField(max_length=15, choices=BODY_CHOICES)
    COLOR_CHOICES = (
        ('White', 'White'),
        ('Black', 'Black'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Other_colors', 'Other_colors'),
    )
    color = models.CharField(max_length=15, choices=COLOR_CHOICES)
    engine_capacity = models.DecimalField(max_digits = 2, decimal_places = 1)
    FUEL_CHOICES = (
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
        ('Gas', 'Gas'),
        ('Electric car', 'Electric car'),
    )
    fuel = models.CharField(max_length=15, choices=FUEL_CHOICES)
    TRANSMISSION_BOX_CHOICES = (
        ('Mechanics', 'Mechanics'),
        ('Automatic', 'Automatic'),
    )
    transmission_box = models.CharField(max_length=15, choices=TRANSMISSION_BOX_CHOICES)
    DRIVE_CHOICES = (
        ('Передний привод', 'Передний привод'),
        ('Задний привод', 'Задний привод'),
        ('4WD', '4WD'),
        ('AWD', 'AWD'),
    )
    drive = models.CharField(max_length=15, choices=DRIVE_CHOICES)
    STEERING_WHEEL_CHOICES = (
        ('Right', 'Right'),
        ('Left', 'Left'),
    )
    steering_wheel = models.CharField(max_length=15, choices=STEERING_WHEEL_CHOICES )
    STATE_CHOICES = (
        ('Новый', 'Новый'),
        ('Б/у', 'Б/у'),
    )
    state = models.CharField(max_length=15, choices=STATE_CHOICES)
    CUSTOMS_CHOICES = (
        ('Растаможен', 'Растаможен'),
        ('Не растаможен', 'Не растаможен'),
    )
    customs = models.CharField(max_length=15, choices=CUSTOMS_CHOICES)
    CHANGE_CHOICES = (
        ('Возможен обмен', 'Возможен обмен'),
        ('Обмена нету', 'Обмена нету'),
    )
    change = models.CharField(max_length=15, choices=CHANGE_CHOICES)
    region_or_city = models.CharField(max_length=20)
    other = models.CharField(max_length=100)

    def __str__(self):
        return self.car_name

class CarPhotos(models.Model):
    car = models.ForeignKey(Car, related_name='car', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')

class Favorites(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='favorites')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

class FavoritesCar(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='favorites_car')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'