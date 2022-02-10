from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories' : categories, 'restaurants': restaurants}
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html', content)

def restaurantDetail(request, res_id):
    # return HttpResponse("restaurantDetail")
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant' : restaurant}
    return render(request, 'shareRes/restaurantDetail.html', content)
    
def restaurantUpdate(request, res_id):
    return HttpResponse('restaurant을 수정할 페이지')

def restaurantCreate(request):
    # return HttpResponse("restaurantCreate")
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request, 'shareRes/restaurantCreate.html', content)

def categoryCreate(request):
    # return HttpResponse("categoryCreate")
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/categoryCreate.html', content)
    
def Create_category(request):
    # return HttpResponse("여기서 category Create 기능을 구현할 거야.")
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category, restaurant_name = name, restaurant_link = link, restaurant_content = content, restaurant_keyword = keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))
    
