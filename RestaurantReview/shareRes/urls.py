#shareRes > urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name = 'resDetailPage'),
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name = 'resUpdate'), # ~<str:res_id>로 끝나는 코드보다 위에 있어야 함
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name = 'resUpdatePage'),
    path('restaurantDetail/delete', views.Delete_restaurant, name = 'resDelete'),
    path('restaurantCreate/', views.restaurantCreate, name= 'resCreatePage'),
    path('restaurantCreate/create', views.Create_restaurant, name= 'resCreate'),
    path('categoryCreate/', views.categoryCreate, name = 'cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name = 'cateCreate'),    
    path('categoryCreate/delete', views.Delete_category, name = 'cateDelete'),
    
    
]

# Create your views here.
