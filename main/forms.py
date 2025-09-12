from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "price", "description", "rating", "thumbnail", "category", "is_featured"]