from django.urls import path
from .views import *


urlpatterns = [
path('register/', RegisterView.as_view(), name='register'),
path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),


path('', CarListViewSet.as_view({'get': 'list', }), name='car_list'),
path('<int:pk>/', CarDetailViewSet.as_view({'get': 'retrieve',
                                              'delete': 'destroy'}), name='car_detail'),


path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                          'delete': 'destroy'}), name='user_detail'),


path('category/', MakeViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
path('category/<int:pk>/', MakeViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                          'delete': 'destroy'}), name='category_detail'),



path('photos/', CarPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='photos_list'),
path('photos/<int:pk>/', CarPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                          'delete': 'destroy'}), name='photos_detail'),


path('favorite/', FavoritesViewSet.as_view({'get': 'retrieve'}), name='favorite_detail'),
path('favorite_car/', FavoritesCarViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_car_list'),
]