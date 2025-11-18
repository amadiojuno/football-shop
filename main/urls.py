from django.urls import path
from main.views import * 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add_product/', add_product, name='add_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit_product/<str:id>/', edit_product, name='edit_product'),
    path('delete_product/<str:id>/', delete_product, name='delete_product'),
    path('create-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('add-product-flutter/', add_product_flutter, name='add_product_flutter'),
]