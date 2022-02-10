#shareRes > urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name = 'resDetailPage'),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name = 'resUpdatePage'),
    path('restaurantCreate/', views.restaurantCreate, name= 'resCreatePage'),
    path('categoryCreate/', views.categoryCreate, name = 'cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name = 'cateCreate'),    
    path('categoryCreate/delete', views.Delete_category, name = 'cateDelete'),
    path('restaurantCreate/create', views.Create_restaurant, name= 'resCreate'),
    
]

# Create your views here.
