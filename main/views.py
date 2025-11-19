import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect,  JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import requests
import json

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    owner_filter = request.GET.get('owner')
    category_filter = request.GET.get('category')
    product_list = Product.objects.all()

    if owner_filter == 'my' and request.user.is_authenticated:
        product_list = product_list.filter(user=request.user)

    if category_filter:
        match category_filter:
            case "all":
                pass 
            case "featured":
                product_list = product_list.filter(is_featured=True)
            case "hot":
                product_list = product_list.filter(views__gt=20)
            case "shoes" | "clothes" | "equipment" | "accessories" | "misc":
                product_list = product_list.filter(category=category_filter)

    context = {
        'npm': '2406496416',
        'name': request.user.username,
        'class': 'PBP E',
        'product_list': product_list.order_by('-id'),
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {
        'form': form
    }
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()  # Increment the view count
    context = {
        'product': product
    }
    return render(request, "show_product.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all().order_by('-id')
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'brand': product.brand,
            'price': product.price,
            'description': product.description,
            'rating': float(product.rating),
            'views': product.views,
            'thumbnail': product.thumbnail,
            'thumbnail_alt': product.thumbnail_alt,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'brand': product.brand,
            'price': product.price,
            'description': product.description,
            'rating': float(product.rating),
            'views': product.views,
            'thumbnail': product.thumbnail,
            'thumbnail_alt': product.thumbnail_alt,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    brand = strip_tags(request.POST.get("brand"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    rating = strip_tags(request.POST.get("rating"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    thumbnail_alt = strip_tags(request.POST.get("thumbnail_alt"))
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_product = Product(
        name=name,
        brand=brand,
        price=price,
        description=description,
        category=category,
        rating=rating,
        thumbnail=thumbnail,
        thumbnail_alt=thumbnail_alt if thumbnail_alt else None,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def add_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        brand = strip_tags(data.get("brand", ""))  # Strip HTML tags
        price = strip_tags(data.get("price", ""))  # Strip HTML tags
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        rating = strip_tags(data.get("rating", "0"))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name, 
            brand=brand,
            price=price,
            description=description,
            rating=rating,
            thumbnail=thumbnail,
            category=category,            
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@login_required
def show_json_my_products(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")